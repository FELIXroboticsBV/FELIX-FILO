#!/usr/bin/env bash
set -euo pipefail

SCRIPT="./cura_to_orca.py"
VENDOR="FELIX Printers"
OUTDIR="./orca"

# --- material sets, reused across all printers of the same class ---------
FOOD_MATERIALS="materials/felix_scale1_254.xml.fdm_material,materials/felix_scale1_312.xml.fdm_material,materials/felix_scale2_254.xml.fdm_material,materials/felix_scale2_312.xml.fdm_material,materials/felix_scale3_254.xml.fdm_material,materials/felix_scale3_312.xml.fdm_material,materials/felix_scale4_254.xml.fdm_material,materials/felix_scale4_312.xml.fdm_material,materials/felix_scale5_254.xml.fdm_material,materials/felix_scale5_312.xml.fdm_material"

PLASTIC_MATERIALS="materials/felix_flex_175.xml.fdm_material,materials/felix_petg_175.xml.fdm_material,materials/felix_ppla_175.xml.fdm_material,materials/felix_wood_175.xml.fdm_material"

# --- printers --------------------------------------------------------------
# format: def_json|nozzle|extruders|materials|name_override
#
# TODO: fill in the `extruders` column (3rd field) for Food Switch and Food
# Twin -- both are multi-extruder machines (your "Right Syringe" sample was
# position 1 of felixfoodswitch, so a position-0 extruder file must also
# exist). Comma-separate multiple extruder .def.json paths in that field,
# e.g.:  extruders/felixfoodswitch_left.def.json,extruders/felixfoodswitch_right.def.json
# Left empty here on purpose rather than guessed -- guessing filenames that
# might not exist on your disk would just produce a confusing "file not
# found" skip instead of a useful error.
PRINTERS=(
  "definitions/felixfoodsingle.def.json|||${FOOD_MATERIALS}|"
  "definitions/felixfoodswitch.def.json|||${FOOD_MATERIALS}|"
  "definitions/felixfoodtwin.def.json|||${FOOD_MATERIALS}|"

  "definitions/felixpro3.def.json|||${PLASTIC_MATERIALS}|"
  "definitions/felixprol.def.json|||${PLASTIC_MATERIALS}|"
  "definitions/felixproxl.def.json|||${PLASTIC_MATERIALS}|"
  "definitions/felixtec4.def.json|||${PLASTIC_MATERIALS}|"
)

# ---------------------------------------------------------------------------

if [ ! -f "$SCRIPT" ]; then
  echo "Can't find $SCRIPT -- edit the SCRIPT variable at the top of this file." >&2
  exit 1
fi

total=${#PRINTERS[@]}
count=0
failures=0

for entry in "${PRINTERS[@]}"; do
  count=$((count + 1))
  IFS='|' read -r def_json nozzle extruders materials printer_name <<< "$entry"

  echo "============================================================"
  echo "[$count/$total] $def_json${nozzle:+ (nozzle $nozzle)}"
  echo "============================================================"

  if [ ! -f "$def_json" ]; then
    echo "  SKIPPED -- definition file not found: $def_json" >&2
    failures=$((failures + 1))
    continue
  fi

  cmd=(python3 "$SCRIPT" --printer "$def_json" --output "$OUTDIR")
  [ -n "$VENDOR" ] && cmd+=(--vendor "$VENDOR")
  [ -n "$nozzle" ] && cmd+=(--nozzle-diameter "$nozzle")
  [ -n "$printer_name" ] && cmd+=(--name "$printer_name")

  if [ -n "$extruders" ]; then
    IFS=',' read -ra ext_array <<< "$extruders"
    for ext in "${ext_array[@]}"; do
      if [ ! -f "$ext" ]; then
        echo "  WARNING: extruder file not found, skipping it: $ext" >&2
        continue
      fi
      cmd+=(--extruders "$ext")
    done
  fi

  if [ -n "$materials" ]; then
    IFS=',' read -ra mat_array <<< "$materials"
    valid_mats=()
    for mat in "${mat_array[@]}"; do
      if [ ! -f "$mat" ]; then
        echo "  WARNING: material file not found, skipping it: $mat" >&2
        continue
      fi
      valid_mats+=("$mat")
    done
    if [ "${#valid_mats[@]}" -gt 0 ]; then
      cmd+=(--materials "${valid_mats[@]}")
    fi
  fi

  echo "  + ${cmd[*]}"
  if ! "${cmd[@]}"; then
    echo "  FAILED: $def_json" >&2
    failures=$((failures + 1))
  fi
  echo
done

echo "============================================================"
echo "Done: $((total - failures))/$total printer entries converted successfully."
echo "Read $OUTDIR/manual_review/REPORT.md -- it accumulates one section per printer"
echo "run above, so it now covers the whole batch, not just the last printer."
if [ "$failures" -gt 0 ]; then
  echo "$failures printer entrie(s) had errors -- see output above."
  exit 1
fi