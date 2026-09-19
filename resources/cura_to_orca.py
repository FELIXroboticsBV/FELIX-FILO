#!/usr/bin/env python3
"""
cura_to_orca.py

Converts Cura profiles (.curaprofile files, which are zips of .inst.cfg
sections) into OrcaSlicer-style JSON profile skeletons (process + filament).

This is a STARTING POINT, not a finished converter. Cura and OrcaSlicer use
different slicing engines with different settings models, so:
  - Some settings map cleanly (1 Cura key -> 1 Orca key, maybe with a unit
    or value transform).
  - Some Cura settings have no Orca equivalent, or map to a *combination*
    of Orca settings (these need a human to decide).
  - Some Orca settings have no Cura equivalent and should just come from
    Orca's own defaults / inherited base profile.

The script:
  1. Extracts every key/value Cura actually overrides from a .curaprofile.
  2. Runs known keys through CURA_TO_ORCA_MAP (name + optional transform).
  3. Emits an Orca-shaped JSON skeleton (process or filament) with
     "inherits" pointing at the common base, ready to be dropped into
     resources/profiles/<Vendor>/{process,filament}/.
  4. Prints a report of any Cura keys it didn't know how to map, so you
     can extend the mapping table or handle them by hand.

USAGE
-----
    python cura_to_orca.py path/to/profile.curaprofile \
        --vendor "MyVendor" \
        --printer "MyVendor Printer 0.4 nozzle" \
        --type process \
        --outdir ./out

    python cura_to_orca.py path/to/material_profile.curaprofile \
        --vendor "MyVendor" \
        --printer "MyVendor Printer 0.4 nozzle" \
        --type filament \
        --outdir ./out

You can also point it at a raw .inst.cfg file directly (not zipped) if
that's what you're extracting from Cura's config folder.

EXTENDING THE MAPPING
----------------------
Add entries to CURA_TO_ORCA_MAP below. Each entry is:

    "cura_key": MapEntry(orca_key, transform=fn, note="...")

`transform` receives the raw Cura value dict (all extracted settings) and
the raw string value for this key, and returns the value(s) to write into
the Orca profile. Most Orca "process" fields are single-element string
lists, e.g. "layer_height": ["0.2"] -- the helper `as_list` handles that
for you.
"""

import argparse
import configparser
import json
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Optional


# ---------------------------------------------------------------------------
# 1. Extraction: read every [values] key out of a .curaprofile / .inst.cfg
# ---------------------------------------------------------------------------

def extract_cura_settings(path: Path) -> dict:
    """
    Returns {key: raw_string_value} for every setting override found.
    Handles both a zipped .curaprofile (which contains one or more
    .inst.cfg members) and a bare .inst.cfg file.
    """
    settings = {}

    def parse_cfg_text(text: str):
        cp = configparser.ConfigParser(strict=False)
        # Cura's cfg files are not always fully spec-compliant configparser
        # input (duplicate-ish sections across concatenated files), so be
        # lenient and parse section-by-section manually as a fallback.
        try:
            cp.read_string(text)
            if cp.has_section("values"):
                for k, v in cp.items("values"):
                    settings[k] = v
                return
        except configparser.Error:
            pass
        # Fallback: manual line scan for a [values] block.
        in_values = False
        for line in text.splitlines():
            line = line.strip()
            if not line or line.startswith(("#", ";")):
                continue
            if line.startswith("[") and line.endswith("]"):
                in_values = line.strip("[]").lower() == "values"
                continue
            if in_values and "=" in line:
                k, _, v = line.partition("=")
                settings[k.strip()] = v.strip()

    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as zf:
            for name in zf.namelist():
                if name.endswith(".cfg") or name.endswith(".inst.cfg"):
                    parse_cfg_text(zf.read(name).decode("utf-8", errors="replace"))
    else:
        parse_cfg_text(path.read_text(encoding="utf-8", errors="replace"))

    return settings


def extract_cura_definition_json(path: Path) -> dict:
    """
    Reads a Cura printer or extruder *.def.json file. Cura definitions store
    per-setting defaults under "overrides": {key: {"default_value": ...}},
    and top-level machine facts under "overrides" too (machine_width,
    machine_depth, machine_height, machine_nozzle_size, etc.), plus some
    info directly under "metadata".
    Handles the common case where the definition "inherits" another file
    only by extracting overrides present in THIS file -- it does not
    resolve the parent chain, since that file usually isn't available
    locally. Merge manually if you need parent defaults too.
    """
    data = json.loads(path.read_text(encoding="utf-8", errors="replace"))
    settings = {}

    overrides = data.get("overrides", {})
    for key, spec in overrides.items():
        if isinstance(spec, dict) and "default_value" in spec:
            # Normalize to string, same as the .inst.cfg parser produces,
            # so every downstream transform can assume a plain string.
            settings[key] = str(spec["default_value"])

    return settings


# Cura material XML files label settings with human-readable, space-separated
# keys rather than the snake_case keys used in .inst.cfg files. This maps the
# common ones back to their internal Cura key so they can flow through the
# same CURA_TO_ORCA_MAP used everywhere else. Extend as you encounter more.
XML_LABEL_TO_CURA_KEY = {
    "print temperature": "material_print_temperature",
    "default print temperature": "material_print_temperature",
    "heated bed temperature": "material_bed_temperature",
    "default heated bed temperature": "material_bed_temperature",
    "standby temperature": "material_standby_temperature",
    "initial print temperature": "material_print_temperature_layer_0",
    "final print temperature": "material_final_print_temperature",
    "retraction amount": "retraction_amount",
    "retraction speed": "retraction_speed",
    "flow": "material_flow",
    "build volume temperature": "build_volume_temperature",
}


def _normalize_id(text: str) -> str:
    return re.sub(r"[^a-z0-9]", "", text.lower())


def extract_cura_material_xml(path: Path, printer_id: Optional[str] = None,
                               hotend_id: Optional[str] = None) -> dict:
    """
    Reads a Cura *.xml.fdm_material file and returns internal-Cura-key
    settings, applying the base <settings> block first and then layering
    any <machine> block that matches printer_id / hotend_id on top (Cura's
    real override behaviour: base values, overridden per-printer, overridden
    further per-hotend within that printer).

    printer_id should match a Cura <machine_identifier product="..."> or
    definition id; hotend_id should match a <hotend id="...">. Matching is
    case-insensitive and ignores spaces/underscores/punctuation (so
    "my_printer" matches "My Printer"). Both are optional -- omit them to
    just get the material's global base settings.
    """
    tree = ET.parse(path)
    root = tree.getroot()
    # Strip namespace for easier tag matching.
    for elem in root.iter():
        if "}" in elem.tag:
            elem.tag = elem.tag.split("}", 1)[1]

    settings = {}

    def apply_settings_block(settings_elem):
        for setting in settings_elem.findall("setting"):
            label = setting.get("key", "").strip().lower()
            cura_key = XML_LABEL_TO_CURA_KEY.get(label)
            if cura_key and setting.text is not None:
                settings[cura_key] = setting.text.strip()

    # Base, global settings.
    base_settings = root.find("settings")
    if base_settings is not None:
        apply_settings_block(base_settings)

    # Per-printer / per-hotend overrides.
    if printer_id:
        norm_printer_id = _normalize_id(printer_id)
        for machine in root.findall("settings/machine"):
            ident = machine.find("machine_identifier")
            product = (ident.get("product") if ident is not None else None) or ""
            norm_product = _normalize_id(product)
            if norm_printer_id not in norm_product and norm_product not in norm_printer_id:
                continue
            machine_settings = machine.find("settings")
            if machine_settings is not None:
                apply_settings_block(machine_settings)
            if hotend_id:
                norm_hotend_id = _normalize_id(hotend_id)
                for hotend in machine.findall("hotend"):
                    if _normalize_id(hotend.get("id", "")) == norm_hotend_id:
                        hotend_settings = hotend.find("settings")
                        if hotend_settings is not None:
                            apply_settings_block(hotend_settings)

    return settings


# ---------------------------------------------------------------------------
# 2. Mapping table: Cura key -> Orca key (+ optional transform)
# ---------------------------------------------------------------------------

def as_list(value) -> list:
    """Orca process/filament values are almost always single-element lists
    of strings, e.g. "layer_height": ["0.2"]."""
    if isinstance(value, list):
        return [str(v) for v in value]
    return [str(value)]


def mm_thickness_to_wall_count(all_values: dict, raw: str):
    """Cura's wall_thickness (mm) -> Orca's wall_loop_count (integer),
    derived by dividing by line width. Falls back to wall_line_count if
    Cura already gives you a count directly."""
    if "wall_line_count" in all_values:
        try:
            return as_list(int(float(all_values["wall_line_count"])))
        except ValueError:
            pass
    try:
        thickness = float(raw)
        line_width = float(all_values.get("wall_line_width_0", all_values.get("line_width", 0.4)))
        count = max(1, round(thickness / line_width))
        return as_list(count)
    except (ValueError, ZeroDivisionError):
        return None


def percent_passthrough(all_values: dict, raw: str):
    # Cura infill density is already 0-100; Orca uses the same convention.
    return as_list(raw)


def bool_passthrough(all_values: dict, raw: str):
    truthy = raw.strip().lower() in ("true", "1", "yes")
    return as_list(1 if truthy else 0)


@dataclass
class MapEntry:
    orca_key: str
    transform: Optional[Callable[[dict, str], Optional[list]]] = None
    note: str = ""


CURA_TO_ORCA_MAP = {
    # --- Layer / quality ---
    "layer_height":            MapEntry("layer_height"),
    "layer_height_0":          MapEntry("initial_layer_print_height"),
    "line_width":              MapEntry("line_width"),
    "wall_line_width_0":       MapEntry("outer_wall_line_width"),
    "wall_line_width_x":       MapEntry("inner_wall_line_width"),
    "wall_thickness":          MapEntry("wall_loop_count", transform=mm_thickness_to_wall_count,
                                          note="Converted mm thickness to a wall count; verify against your line width."),
    "top_thickness":           MapEntry("top_shell_thickness"),
    "bottom_thickness":        MapEntry("bottom_shell_thickness"),
    "top_layers":              MapEntry("top_shell_layers"),
    "bottom_layers":           MapEntry("bottom_shell_layers"),

    # --- Infill ---
    "infill_sparse_density":  MapEntry("sparse_infill_density", transform=percent_passthrough),
    "infill_line_width":      MapEntry("infill_line_width"),
    "infill_pattern":         MapEntry("sparse_infill_pattern",
                                          note="Cura and Orca pattern *names* differ (e.g. 'zigzag' vs 'zig-zag', "
                                               "'cubicsubdiv' has no direct Orca equivalent) -- check manually."),

    # --- Speed ---
    "speed_print":            MapEntry("outer_wall_speed", note="Cura's speed_print is a global fallback; Orca "
                                          "has separate speeds per feature -- review each one."),
    "speed_wall_0":            MapEntry("outer_wall_speed"),
    "speed_wall_x":            MapEntry("inner_wall_speed"),
    "speed_travel":            MapEntry("travel_speed"),
    "speed_topbottom":         MapEntry("top_surface_speed"),
    "speed_infill":            MapEntry("sparse_infill_speed"),

    # --- Temperatures (usually belong on the FILAMENT profile) ---
    "material_print_temperature":       MapEntry("nozzle_temperature"),
    "material_print_temperature_layer_0": MapEntry("nozzle_temperature_initial_layer"),
    "material_bed_temperature":         MapEntry("hot_plate_temp"),
    "material_bed_temperature_layer_0": MapEntry("hot_plate_temp_initial_layer"),
    "material_flow":                    MapEntry("filament_flow_ratio", transform=percent_passthrough,
                                          note="Cura's material_flow is a percentage; Orca's filament_flow_ratio "
                                               "is a multiplier (100% -> 1.0). Divide by 100 if needed."),

    # --- Retraction ---
    "retraction_amount":       MapEntry("retraction_length"),
    "retraction_speed":        MapEntry("retraction_speed"),
    "retraction_min_travel":   MapEntry("retraction_minimum_travel"),
    "retraction_enable":       MapEntry("retract_when_changing_layer", transform=bool_passthrough,
                                          note="Not a true 1:1 concept; double check against Orca's retraction docs."),

    # --- Support ---
    "support_enable":          MapEntry("enable_support", transform=bool_passthrough),
    "support_angle":           MapEntry("support_threshold_angle"),
    "support_infill_rate":     MapEntry("support_density", transform=percent_passthrough),

    # --- Adhesion ---
    "adhesion_type":           MapEntry("skirt_type", note="Cura's adhesion_type (skirt/brim/raft/none) doesn't "
                                          "map cleanly to one Orca field; Orca splits skirt/brim/raft into separate "
                                          "enable flags. Handle manually."),
    "brim_width":              MapEntry("brim_width"),
    "skirt_line_count":        MapEntry("skirt_loops"),
}


_PRINTABLE_AREA_INPUT_KEYS = {"machine_width", "machine_depth", "machine_center_is_zero"}


def wh_to_printable_area(all_values: dict, raw: str):
    """Builds Orca's printable_area (a rectangle of corner points) from
    Cura's machine_width / machine_depth, honouring origin_at_center.
    machine_depth and machine_center_is_zero are consumed here as inputs
    rather than getting their own Orca key -- that's expected, not a
    missing mapping."""
    try:
        w = float(all_values.get("machine_width", raw))
        d = float(all_values.get("machine_depth", 0))
    except ValueError:
        return None
    if not w or not d:
        return None
    centered = all_values.get("machine_center_is_zero", "false").strip().lower() in ("true", "1")
    if centered:
        pts = [(-w / 2, -d / 2), (w / 2, -d / 2), (w / 2, d / 2), (-w / 2, d / 2)]
    else:
        pts = [(0, 0), (w, 0), (w, d), (0, d)]
    return [f"{x}x{y}" for x, y in pts]


def gcode_flavor_map(all_values: dict, raw: str):
    flavor_map = {
        "Marlin": "marlin",
        "Marlin2": "marlin2",
        "RepRap": "reprapfirmware",
        "RepRapFirmware": "reprapfirmware",
        "Repetier": "repetier",
        "Griffin": "klipper",
        "UltiGCode": "marlin",
        "Smoothie": "smoothie",
    }
    return as_list(flavor_map.get(raw, raw))


# Cura printer/extruder definition keys -> Orca "machine" (variant) keys.
CURA_TO_ORCA_MACHINE_MAP = {
    "machine_nozzle_size":         MapEntry("nozzle_diameter"),
    "machine_width":               MapEntry("printable_area", transform=wh_to_printable_area,
                                              note="Computed from machine_width/machine_depth/machine_center_is_zero -- verify."),
    "machine_height":              MapEntry("printable_height"),
    "machine_gcode_flavor":        MapEntry("gcode_flavor", transform=gcode_flavor_map),
    "machine_start_gcode":         MapEntry("machine_start_gcode"),
    "machine_end_gcode":           MapEntry("machine_end_gcode"),
    "machine_max_feedrate_x":      MapEntry("machine_max_speed_x"),
    "machine_max_feedrate_y":      MapEntry("machine_max_speed_y"),
    "machine_max_feedrate_z":      MapEntry("machine_max_speed_z"),
    "machine_max_feedrate_e":      MapEntry("machine_max_speed_e"),
    "machine_max_acceleration_x":  MapEntry("machine_max_acceleration_x"),
    "machine_max_acceleration_y":  MapEntry("machine_max_acceleration_y"),
    "machine_heated_bed":          MapEntry("has_heatbed", transform=bool_passthrough),
}


# ---------------------------------------------------------------------------
# 3. Build Orca profile JSON
# ---------------------------------------------------------------------------

def build_orca_profile(cura_values: dict, profile_type: str, name: str,
                        inherits: str, compatible_printers: list) -> tuple:
    """
    Returns (orca_profile_dict, unmapped_keys, notes)
    profile_type: "process", "filament", or "machine"
    """
    orca = {
        "type": profile_type if profile_type != "machine" else "machine",
        "name": name,
        "inherits": inherits,
        "from": "system",
        "instantiation": "true",
    }
    if profile_type in ("process", "filament"):
        orca["compatible_printers"] = compatible_printers

    mapping_table = CURA_TO_ORCA_MACHINE_MAP if profile_type == "machine" else CURA_TO_ORCA_MAP

    unmapped = []
    notes = []

    for cura_key, raw_value in cura_values.items():
        if cura_key in _PRINTABLE_AREA_INPUT_KEYS and cura_key != "machine_width":
            continue  # consumed as an input by the machine_width transform, not a missing mapping
        entry = mapping_table.get(cura_key)
        if entry is None:
            unmapped.append(cura_key)
            continue
        if entry.transform:
            value = entry.transform(cura_values, raw_value)
            if value is None:
                unmapped.append(f"{cura_key} (transform failed, needs manual review)")
                continue
        else:
            value = as_list(raw_value)
        orca[entry.orca_key] = value
        if entry.note:
            notes.append(f"{cura_key} -> {entry.orca_key}: {entry.note}")

    return orca, unmapped, notes


def get_cfg_general_field(path: Path, field_name: str) -> Optional[str]:
    """Reads a single [general] field (e.g. 'type' or 'definition') from a
    bare .inst.cfg file, or from every .cfg member if path is a zip. Used
    to tell quality/quality_changes/variant/definition_changes files apart
    since they all share the same .inst.cfg format."""
    def scan(text: str) -> Optional[str]:
        in_general = False
        for line in text.splitlines():
            line = line.strip()
            if line.startswith("[") and line.endswith("]"):
                in_general = line.strip("[]").lower() == "general"
                continue
            if in_general and "=" in line:
                k, _, v = line.partition("=")
                if k.strip().lower() == field_name.lower():
                    return v.strip()
        return None

    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as zf:
            for member in zf.namelist():
                if member.endswith(".cfg"):
                    result = scan(zf.read(member).decode("utf-8", errors="replace"))
                    if result:
                        return result
        return None
    return scan(path.read_text(encoding="utf-8", errors="replace"))


def extract_cura_material_xml_auto(path: Path) -> dict:
    """Batch-mode material extraction: if the file defines exactly one
    <machine> override block, apply it (and its single <hotend> block, if
    there's exactly one) automatically, since with only your own printer(s)
    left in the resources folder there's usually nothing else it could be.
    If there's more than one machine/hotend block, only the base settings
    are used and a note is returned so you know to re-run that file with
    explicit --printer-id/--hotend-id if you want the override applied."""
    tree = ET.parse(path)
    root = tree.getroot()
    for elem in root.iter():
        if "}" in elem.tag:
            elem.tag = elem.tag.split("}", 1)[1]

    machines = root.findall("settings/machine")
    note = None
    printer_id = hotend_id = None
    if len(machines) == 1:
        ident = machines[0].find("machine_identifier")
        printer_id = (ident.get("product") if ident is not None else None) or None
        hotends = machines[0].findall("hotend")
        if len(hotends) == 1:
            hotend_id = hotends[0].get("id")
        elif len(hotends) > 1:
            note = f"{path.name}: multiple hotend overrides found, used base settings only for the machine block."
    elif len(machines) > 1:
        note = f"{path.name}: multiple machine overrides found, used global base settings only."

    settings = extract_cura_material_xml(path, printer_id=printer_id, hotend_id=hotend_id)
    return settings, note


CLASSIFY_EXTENSIONS = {
    ".def.json": "machine",
    ".xml.fdm_material": "filament",
}


def classify_and_extract(path: Path) -> tuple:
    """
    Returns (bucket, settings_dict, note_or_None) for a single file found
    while walking a directory. bucket is "machine", "filament", "process",
    or None if the file should be skipped (not a recognized Cura profile
    format -- e.g. images, STLs, READMEs).
    """
    name = path.name.lower()

    if name.endswith(".def.json"):
        return "machine", extract_cura_definition_json(path), None

    if name.endswith(".fdm_material") or (name.endswith(".xml") and "material" in str(path).lower()):
        settings, note = extract_cura_material_xml_auto(path)
        return "filament", settings, note

    if name.endswith(".inst.cfg") or name.endswith(".curaprofile") or name.endswith(".cfg"):
        cfg_type = (get_cfg_general_field(path, "type") or "").lower()
        settings = extract_cura_settings(path)
        if cfg_type == "variant":
            return "machine", settings, f"{path.name}: Cura 'variant' file (nozzle-specific overrides) -- mapped as a machine profile."
        if cfg_type == "definition_changes":
            return "machine", settings, None
        # quality, quality_changes, user, or unknown -> treat as process
        return "process", settings, None

    return None, {}, None


def run_batch(root_dir: Path, args):
    extensions = ("*.def.json", "*.xml.fdm_material", "*.inst.cfg", "*.curaprofile", "*.cfg")
    found = []
    for pattern in extensions:
        found.extend(root_dir.rglob(pattern))
    found = sorted(set(found))

    if not found:
        sys.exit(f"No .def.json, .xml.fdm_material, .inst.cfg, .curaprofile, or .cfg files found under {root_dir}")

    compatible_printers = [p.strip() for p in args.printer.split(",")]
    default_inherits = {
        "process": "fdm_process_common",
        "filament": "fdm_filament_common",
        "machine": "fdm_machine_common",
    }

    counts = {"machine": 0, "filament": 0, "process": 0, "skipped": 0}
    all_unmapped = {"machine": set(), "filament": set(), "process": set()}
    batch_notes = []

    for path in found:
        bucket, cura_values, note = classify_and_extract(path)
        if note:
            batch_notes.append(note)
        if bucket is None or not cura_values:
            counts["skipped"] += 1
            continue

        rel = path.relative_to(root_dir)
        name = f"{args.vendor} {path.stem} @{compatible_printers[0]}"
        inherits = default_inherits[bucket]

        orca_profile, unmapped, notes = build_orca_profile(
            cura_values, bucket, name, inherits, compatible_printers
        )

        out_dir = args.outdir / bucket
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{name}.json"
        out_path.write_text(json.dumps(orca_profile, indent=4), encoding="utf-8")

        counts[bucket] += 1
        all_unmapped[bucket].update(unmapped)
        for n in notes:
            batch_notes.append(f"{rel}: {n}")

    print(f"Processed {len(found)} files under {root_dir}")
    print(f"  machine profiles written:  {counts['machine']}")
    print(f"  filament profiles written: {counts['filament']}")
    print(f"  process profiles written:  {counts['process']}")
    print(f"  skipped (unrecognized):    {counts['skipped']}")

    if batch_notes:
        print("\n--- Per-file review notes ---")
        for n in batch_notes:
            print(f"  - {n}")

    for bucket in ("machine", "filament", "process"):
        if all_unmapped[bucket]:
            print(f"\n--- UNMAPPED keys across all {bucket} files (dedup'd) ---")
            for key in sorted(all_unmapped[bucket]):
                print(f"  - {key}")

    print(f"\nAll compatible_printers were set to: {compatible_printers}")
    print("IMPORTANT: this is almost certainly wrong for some files (e.g. a quality profile "
          "that only applies to one nozzle size). Check each output's compatible_printers "
          "field against which printer/nozzle variant it actually belongs to.")


def run_printer_mode(args):
    """
    Converts everything belonging to ONE printer in a single pass: the
    printer's own definition, one or more material files you point it at,
    and every quality/quality_changes file under a directory you point it
    at -- all tagged with that printer's compatible_printers name.
    """
    def_path = args.definition
    if not def_path.exists():
        sys.exit(f"Printer definition not found: {def_path}")

    def_data = json.loads(def_path.read_text(encoding="utf-8", errors="replace"))
    default_stem = def_path.name
    for suffix in (".def.json", ".json"):
        if default_stem.lower().endswith(suffix):
            default_stem = default_stem[: -len(suffix)]
            break
    printer_name = args.printer_name or def_data.get("name") or def_data.get("id") or default_stem
    machine_settings = extract_cura_definition_json(def_path)

    if args.nozzle:
        machine_settings["machine_nozzle_size"] = str(args.nozzle)

    compatible_name = f"{args.vendor} {printer_name}"
    if args.nozzle:
        compatible_name += f" {args.nozzle} nozzle"
    compatible_printers = [compatible_name]

    args.outdir.mkdir(parents=True, exist_ok=True)
    written = {"machine": 0, "filament": 0, "process": 0}
    unmapped_all = {"machine": set(), "filament": set(), "process": set()}
    notes_all = []

    def write_profile(bucket, settings, name, inherits):
        orca_profile, unmapped, notes = build_orca_profile(settings, bucket, name, inherits, compatible_printers)
        out_dir = args.outdir / bucket
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / f"{name}.json").write_text(json.dumps(orca_profile, indent=4), encoding="utf-8")
        written[bucket] += 1
        unmapped_all[bucket].update(unmapped)
        return notes

    # 1. Machine profile from the printer definition.
    notes_all += [f"[machine:{def_path.name}] {n}" for n in write_profile(
        "machine", machine_settings, compatible_name, "fdm_machine_common")]
    if not args.nozzle:
        notes_all.append("No --nozzle given: compatible_printers has no nozzle suffix. If this printer "
                          "supports multiple nozzle sizes, run this mode once per nozzle with --nozzle set, "
                          "and give --name a distinct value each time so the outputs don't overwrite each other.")

    # 2. One filament profile per material file you specify.
    for mat_path in args.material or []:
        if not mat_path.exists():
            notes_all.append(f"Material file not found, skipped: {mat_path}")
            continue
        hotend_id = f"{args.nozzle}mm" if args.nozzle else None
        settings = extract_cura_material_xml(mat_path, printer_id=printer_name, hotend_id=hotend_id)
        if not settings:
            notes_all.append(f"[filament:{mat_path.name}] no settings extracted -- check the file is a "
                              f"real Cura material XML.")
            continue
        name = f"{args.vendor} {mat_path.stem} @{compatible_name}"
        notes_all += [f"[filament:{mat_path.name}] {n}" for n in write_profile(
            "filament", settings, name, "fdm_filament_common")]

    # 3. Every quality / quality_changes file under the directory you specify.
    if args.quality_dir:
        if not args.quality_dir.exists():
            notes_all.append(f"Quality dir not found, skipped: {args.quality_dir}")
        else:
            quality_files = sorted(set(args.quality_dir.rglob("*.inst.cfg"))
                                    | set(args.quality_dir.rglob("*.curaprofile"))
                                    | set(args.quality_dir.rglob("*.cfg")))
            for path in quality_files:
                cfg_type = (get_cfg_general_field(path, "type") or "").lower()
                settings = extract_cura_settings(path)
                if not settings:
                    continue
                bucket = "machine" if cfg_type in ("variant", "definition_changes") else "process"
                inherits = "fdm_machine_common" if bucket == "machine" else "fdm_process_common"
                name = f"{args.vendor} {path.stem} @{compatible_name}"
                rel = path.relative_to(args.quality_dir)
                notes_all += [f"[{bucket}:{rel}] {n}" for n in write_profile(bucket, settings, name, inherits)]

    print(f"Printer: {compatible_name}")
    print(f"  machine profiles written:  {written['machine']}")
    print(f"  filament profiles written: {written['filament']}")
    print(f"  process profiles written:  {written['process']}")

    if notes_all:
        print("\n--- Review notes ---")
        for n in notes_all:
            print(f"  - {n}")

    for bucket in ("machine", "filament", "process"):
        if unmapped_all[bucket]:
            print(f"\n--- UNMAPPED keys across all {bucket} files (dedup'd) ---")
            for key in sorted(unmapped_all[bucket]):
                print(f"  - {key}")


# ---------------------------------------------------------------------------
# 4. CLI
# ---------------------------------------------------------------------------

def detect_format_and_extract(path: Path, args) -> dict:
    """Picks the right extractor based on file extension / content."""
    suffixes = "".join(path.suffixes).lower()
    name = path.name.lower()

    if name.endswith(".def.json"):
        return extract_cura_definition_json(path)
    if name.endswith(".fdm_material") or suffixes.endswith(".xml"):
        return extract_cura_material_xml(path, printer_id=args.printer_id, hotend_id=args.hotend_id)
    # Otherwise assume .curaprofile (zip) or a bare .inst.cfg file.
    return extract_cura_settings(path)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="mode", required=True)

    # --- "printer" mode: one printer, explicit materials + quality dir ---
    p_printer = sub.add_parser("printer", help="Convert one printer: its definition, the material files "
                                                 "you point it at, and every quality file under a directory.")
    p_printer.add_argument("--def", dest="definition", type=Path, required=True,
                            help="The printer's *.def.json file.")
    p_printer.add_argument("--material", type=Path, action="append",
                            help="A material *.xml.fdm_material file for this printer. Repeatable: "
                                 "--material pla.xml.fdm_material --material petg.xml.fdm_material")
    p_printer.add_argument("--quality-dir", dest="quality_dir", type=Path,
                            help="Directory containing this printer's quality / quality_changes .inst.cfg "
                                 "files (searched recursively).")
    p_printer.add_argument("--nozzle", default=None,
                            help="Nozzle size, e.g. 0.4. Sets nozzle_diameter and is used to name the "
                                 "output profiles and to pick per-hotend material overrides. Run this mode "
                                 "again with a different --nozzle (and --outdir, or accept overwrites) for "
                                 "each nozzle size the printer supports.")
    p_printer.add_argument("--vendor", required=True, help="Vendor name, e.g. 'MyVendor'")
    p_printer.add_argument("--printer-name", dest="printer_name", default=None,
                            help="Display name to use. Defaults to the 'name' or 'id' field in --def.")
    p_printer.add_argument("--outdir", type=Path, default=Path("."))

    # --- "scan" mode: whole resources tree, best-effort auto classification ---
    p_scan = sub.add_parser("scan", help="Recursively convert every recognized Cura file under a directory, "
                                          "applying the same --printer name to all of them.")
    p_scan.add_argument("directory", type=Path)
    p_scan.add_argument("--vendor", required=True)
    p_scan.add_argument("--printer", required=True,
                         help="Compatible printer variant name applied to every file found, e.g. "
                              "'MyVendor Printer 0.4 nozzle'.")
    p_scan.add_argument("--outdir", type=Path, default=Path("."))

    # --- "file" mode: convert exactly one file ---
    p_file = sub.add_parser("file", help="Convert a single file.")
    p_file.add_argument("cura_file", type=Path)
    p_file.add_argument("--vendor", required=True)
    p_file.add_argument("--printer", required=True,
                         help="Compatible printer variant name(s), comma separated.")
    p_file.add_argument("--type", choices=["process", "filament", "machine"], required=True)
    p_file.add_argument("--name", default=None)
    p_file.add_argument("--inherits", default=None)
    p_file.add_argument("--outdir", type=Path, default=Path("."))
    p_file.add_argument("--printer-id", dest="printer_id", default=None,
                         help="(Material XML only) which Cura <machine_identifier product=...> to pull "
                              "per-printer overrides from.")
    p_file.add_argument("--hotend-id", dest="hotend_id", default=None,
                         help="(Material XML only) which Cura <hotend id=...> to pull per-nozzle overrides from.")

    args = ap.parse_args()

    if args.mode == "printer":
        run_printer_mode(args)
        return

    if args.mode == "scan":
        if not args.directory.exists():
            sys.exit(f"Directory not found: {args.directory}")
        run_batch(args.directory, args)
        return

    # args.mode == "file"
    if not args.cura_file.exists():
        sys.exit(f"Input file not found: {args.cura_file}")

    cura_values = detect_format_and_extract(args.cura_file, args)
    if not cura_values:
        sys.exit("No recognizable settings were extracted -- check the file is really a Cura profile/definition/material file, "
                  "or that --printer-id/--hotend-id (for material XML) match what's actually in the file.")

    compatible_printers = [p.strip() for p in args.printer.split(",")]
    default_inherits = {
        "process": "fdm_process_common",
        "filament": "fdm_filament_common",
        "machine": "fdm_machine_common",
    }[args.type]
    inherits = args.inherits or default_inherits
    name = args.name or f"{args.vendor} {args.cura_file.stem} @{compatible_printers[0]}"

    orca_profile, unmapped, notes = build_orca_profile(
        cura_values, args.type, name, inherits, compatible_printers
    )

    args.outdir.mkdir(parents=True, exist_ok=True)
    out_path = args.outdir / f"{name}.json"
    out_path.write_text(json.dumps(orca_profile, indent=4), encoding="utf-8")

    mapped_count = len(cura_values) - len(unmapped)
    print(f"Wrote {out_path}")
    print(f"Mapped {mapped_count} of {len(cura_values)} extracted Cura settings.")

    if notes:
        print("\n--- Review notes (mapped, but check the logic) ---")
        for n in notes:
            print(f"  - {n}")

    if unmapped:
        print("\n--- UNMAPPED Cura keys (add to the mapping table or handle by hand) ---")
        for key in sorted(unmapped):
            print(f"  - {key} = {cura_values.get(key, '')}")


if __name__ == "__main__":
    main()