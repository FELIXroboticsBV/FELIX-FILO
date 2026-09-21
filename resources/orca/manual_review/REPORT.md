# Cura -> OrcaSlicer conversion report

This file accumulates across every run of cura_to_orca.py against this output directory (e.g. every printer in convert_all.sh). Newest run is at the bottom.


---

## Run: FELIX Printers FELIX Food Single

Materials processed this run: **10**


### PRINTER

- [FELIX Printers FELIX Food Single] printable_area built from machine_width/machine_depth assuming machine_center_is_zero=False (this key was NOT found in the def and defaulted to False). Double check bed origin in Orca matches your real machine.
- Nozzle diameter guessed as 2.0mm from preferred_variant_name='Steel syringe 2.0 mm nozzle'. Cura keeps real nozzle size in a separate 'variant' file that was not provided to this script -- CONFIRM this, or pass --nozzle-diameter explicitly next time.

### MATERIALS

- [Molten Chocolate] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Molten Chocolate] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Molten Chocolate] filament_retraction_length set as a per-filament OVERRIDE (0.1mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Molten Chocolate] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Molten Chocolate] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Molten Chocolate] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Molten Chocolate] filament_retraction_length set as a per-filament OVERRIDE (0.5mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Molten Chocolate] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Molten Chocolate] filament/Molten_Chocolate.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Yogurt] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Yogurt] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Yogurt] filament_retraction_length set as a per-filament OVERRIDE (0.2mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Yogurt] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Yogurt] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Yogurt] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Yogurt] filament_retraction_length set as a per-filament OVERRIDE (0.75mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Yogurt] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Yogurt] filament/Yogurt.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Hummus] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Hummus] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Hummus] filament_retraction_length set as a per-filament OVERRIDE (1mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Hummus] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Hummus] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Hummus] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Hummus] filament_retraction_length set as a per-filament OVERRIDE (3mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Hummus] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Hummus] filament/Hummus.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Mashed potatoes] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Mashed potatoes] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Mashed potatoes] filament_retraction_length set as a per-filament OVERRIDE (2mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Mashed potatoes] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Mashed potatoes] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Mashed potatoes] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Mashed potatoes] filament_retraction_length set as a per-filament OVERRIDE (2mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Mashed potatoes] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Mashed potatoes] filament/Mashed_potatoes.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Marzipan] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Marzipan] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Marzipan] filament_retraction_length set as a per-filament OVERRIDE (2mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Marzipan] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Marzipan] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Marzipan] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Marzipan] filament_retraction_length set as a per-filament OVERRIDE (2mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Marzipan] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Marzipan] filament/Marzipan.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.

Quality/process presets: skipped, as requested. `process/` was created empty. OrcaSlicer's stock process presets are used until you build your own. Most Cura settings that look like 'quality' settings (walls, infill, speeds, cooling curve, coasting, bridging, supports) were on the PRINTER def and MATERIAL file respectively, not in a separate quality file -- see manual_review/*unmapped* files for all of them.

---

## Run: FELIX Printers FELIX Food Switch

Materials processed this run: **10**


### PRINTER

- [FELIX Printers FELIX Food Switch] printable_area built from machine_width/machine_depth assuming machine_center_is_zero=False (this key was NOT found in the def and defaulted to False). Double check bed origin in Orca matches your real machine.
- Nozzle diameter guessed as 2.0mm from preferred_variant_name='Steel syringe 2.0 mm nozzle'. Cura keeps real nozzle size in a separate 'variant' file that was not provided to this script -- CONFIRM this, or pass --nozzle-diameter explicitly next time.

### MATERIALS

- [Molten Chocolate] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Molten Chocolate] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Molten Chocolate] filament_retraction_length set as a per-filament OVERRIDE (0.1mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Molten Chocolate] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Molten Chocolate] filament/Molten_Chocolate.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Molten Chocolate] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Molten Chocolate] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Molten Chocolate] filament_retraction_length set as a per-filament OVERRIDE (0.5mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Molten Chocolate] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Molten Chocolate] filament/Molten_Chocolate.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Yogurt] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Yogurt] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Yogurt] filament_retraction_length set as a per-filament OVERRIDE (0.2mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Yogurt] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Yogurt] filament/Yogurt.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Yogurt] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Yogurt] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Yogurt] filament_retraction_length set as a per-filament OVERRIDE (0.75mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Yogurt] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Yogurt] filament/Yogurt.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Hummus] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Hummus] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Hummus] filament_retraction_length set as a per-filament OVERRIDE (1mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Hummus] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Hummus] filament/Hummus.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Hummus] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Hummus] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Hummus] filament_retraction_length set as a per-filament OVERRIDE (3mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Hummus] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Hummus] filament/Hummus.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Mashed potatoes] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Mashed potatoes] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Mashed potatoes] filament_retraction_length set as a per-filament OVERRIDE (2mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Mashed potatoes] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Mashed potatoes] filament/Mashed_potatoes.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Mashed potatoes] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Mashed potatoes] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Mashed potatoes] filament_retraction_length set as a per-filament OVERRIDE (2mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Mashed potatoes] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Mashed potatoes] filament/Mashed_potatoes.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Marzipan] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Marzipan] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Marzipan] filament_retraction_length set as a per-filament OVERRIDE (2mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Marzipan] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Marzipan] filament/Marzipan.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Marzipan] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Marzipan] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Marzipan] filament_retraction_length set as a per-filament OVERRIDE (2mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Marzipan] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Marzipan] filament/Marzipan.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.

Quality/process presets: skipped, as requested. `process/` was created empty. OrcaSlicer's stock process presets are used until you build your own. Most Cura settings that look like 'quality' settings (walls, infill, speeds, cooling curve, coasting, bridging, supports) were on the PRINTER def and MATERIAL file respectively, not in a separate quality file -- see manual_review/*unmapped* files for all of them.

---

## Run: FELIX Printers FELIX Food Twin

Materials processed this run: **10**


### PRINTER

- [FELIX Printers FELIX Food Twin] printable_area built from machine_width/machine_depth assuming machine_center_is_zero=False (this key was NOT found in the def and defaulted to False). Double check bed origin in Orca matches your real machine.
- Nozzle diameter guessed as 2.0mm from preferred_variant_name='Steel syringe 2.0 mm nozzle'. Cura keeps real nozzle size in a separate 'variant' file that was not provided to this script -- CONFIRM this, or pass --nozzle-diameter explicitly next time.

### MATERIALS

- [Molten Chocolate] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Molten Chocolate] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Molten Chocolate] filament_retraction_length set as a per-filament OVERRIDE (0.1mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Molten Chocolate] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Molten Chocolate] filament/Molten_Chocolate.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Molten Chocolate] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Molten Chocolate] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Molten Chocolate] filament_retraction_length set as a per-filament OVERRIDE (0.5mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Molten Chocolate] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Molten Chocolate] filament/Molten_Chocolate.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Yogurt] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Yogurt] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Yogurt] filament_retraction_length set as a per-filament OVERRIDE (0.2mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Yogurt] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Yogurt] filament/Yogurt.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Yogurt] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Yogurt] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Yogurt] filament_retraction_length set as a per-filament OVERRIDE (0.75mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Yogurt] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Yogurt] filament/Yogurt.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Hummus] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Hummus] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Hummus] filament_retraction_length set as a per-filament OVERRIDE (1mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Hummus] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Hummus] filament/Hummus.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Hummus] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Hummus] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Hummus] filament_retraction_length set as a per-filament OVERRIDE (3mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Hummus] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Hummus] filament/Hummus.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Mashed potatoes] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Mashed potatoes] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Mashed potatoes] filament_retraction_length set as a per-filament OVERRIDE (2mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Mashed potatoes] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Mashed potatoes] filament/Mashed_potatoes.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Mashed potatoes] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Mashed potatoes] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Mashed potatoes] filament_retraction_length set as a per-filament OVERRIDE (2mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Mashed potatoes] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Mashed potatoes] filament/Mashed_potatoes.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Marzipan] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Marzipan] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Marzipan] filament_retraction_length set as a per-filament OVERRIDE (2mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Marzipan] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Marzipan] filament/Marzipan.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Marzipan] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Marzipan] This material had 5 hotend/nozzle variants (0.5 mm, 1.0 mm, 2.0 mm, 3.0 mm, 4.0 mm). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.5 mm' for temperature/retraction. The other 4 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Marzipan] filament_retraction_length set as a per-filament OVERRIDE (2mm from hotend '0.5 mm'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Marzipan] material_identifier product(s) ['felixfoodsingle', 'felixfoodswitch', 'felixfoodtwin'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Marzipan] filament/Marzipan.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.

Quality/process presets: skipped, as requested. `process/` was created empty. OrcaSlicer's stock process presets are used until you build your own. Most Cura settings that look like 'quality' settings (walls, infill, speeds, cooling curve, coasting, bridging, supports) were on the PRINTER def and MATERIAL file respectively, not in a separate quality file -- see manual_review/*unmapped* files for all of them.

---

## Run: FELIX Printers FELIX Pro 3

Materials processed this run: **4**


### PRINTER

- [FELIX Printers FELIX Pro 3] printable_area built from machine_width/machine_depth assuming machine_center_is_zero=False (this key was NOT found in the def and defaulted to False). Double check bed origin in Orca matches your real machine.
- Nozzle diameter guessed as 0.35mm from preferred_variant_name='0.35 mm brass'. Cura keeps real nozzle size in a separate 'variant' file that was not provided to this script -- CONFIRM this, or pass --nozzle-diameter explicitly next time.

### MATERIALS

- [FLEX] filament_type guessed as 'TPU' (inherits 'fdm_filament_tpu') from the material name/label. CONFIRM this matches the real polymer.
- [FLEX] This material had 6 hotend/nozzle variants (0.35 mm brass, 0.50 mm brass, 0.25 mm hardend steel, 0.35 mm hardend steel, 0.50 mm hardend steel, 0.70 mm hardend steel). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.35 mm brass' for temperature/retraction. The other 5 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [FLEX] filament_retraction_length set as a per-filament OVERRIDE (2.2mm from hotend '0.35 mm brass'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [FLEX] material_identifier product(s) ['felixproxl', 'felixprol', 'felixpro3', 'felixtec4'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [PETG] filament_type guessed as 'PETG' (inherits 'fdm_filament_pet') from the material name/label. CONFIRM this matches the real polymer.
- [PETG] This material had 6 hotend/nozzle variants (0.35 mm brass, 0.50 mm brass, 0.25 mm hardend steel, 0.35 mm hardend steel, 0.50 mm hardend steel, 0.70 mm hardend steel). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.35 mm brass' for temperature/retraction. The other 5 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [PETG] filament_retraction_length set as a per-filament OVERRIDE (1.2mm from hotend '0.35 mm brass'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [PETG] material_identifier product(s) ['felixproxl', 'felixprol', 'felixpro3', 'felixtec4'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Premium PLA] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Premium PLA] This material had 6 hotend/nozzle variants (0.35 mm brass, 0.50 mm brass, 0.25 mm hardend steel, 0.35 mm hardend steel, 0.50 mm hardend steel, 0.70 mm hardend steel). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.35 mm brass' for temperature/retraction. The other 5 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Premium PLA] filament_retraction_length set as a per-filament OVERRIDE (1.4mm from hotend '0.35 mm brass'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Premium PLA] material_identifier product(s) ['felixproxl', 'felixprol', 'felixpro3', 'felixtec4'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Wood] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Wood] This material had 6 hotend/nozzle variants (0.35 mm brass, 0.50 mm brass, 0.25 mm hardend steel, 0.35 mm hardend steel, 0.50 mm hardend steel, 0.70 mm hardend steel). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.35 mm brass' for temperature/retraction. The other 5 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Wood] filament_retraction_length set as a per-filament OVERRIDE (2.5mm from hotend '0.35 mm brass'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Wood] material_identifier product(s) ['felixproxl', 'felixprol', 'felixpro3', 'felixtec4'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.

Quality/process presets: skipped, as requested. `process/` was created empty. OrcaSlicer's stock process presets are used until you build your own. Most Cura settings that look like 'quality' settings (walls, infill, speeds, cooling curve, coasting, bridging, supports) were on the PRINTER def and MATERIAL file respectively, not in a separate quality file -- see manual_review/*unmapped* files for all of them.

---

## Run: FELIX Printers FELIX Pro XL

Materials processed this run: **4**


### PRINTER

- [FELIX Printers FELIX Pro XL] printable_area built from machine_width/machine_depth assuming machine_center_is_zero=False (this key was NOT found in the def and defaulted to False). Double check bed origin in Orca matches your real machine.
- Nozzle diameter guessed as 0.50mm from preferred_variant_name='0.50 mm brass'. Cura keeps real nozzle size in a separate 'variant' file that was not provided to this script -- CONFIRM this, or pass --nozzle-diameter explicitly next time.

### MATERIALS

- [FLEX] filament_type guessed as 'TPU' (inherits 'fdm_filament_tpu') from the material name/label. CONFIRM this matches the real polymer.
- [FLEX] This material had 6 hotend/nozzle variants (0.35 mm brass, 0.50 mm brass, 0.25 mm hardend steel, 0.35 mm hardend steel, 0.50 mm hardend steel, 0.70 mm hardend steel). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.35 mm brass' for temperature/retraction. The other 5 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [FLEX] filament_retraction_length set as a per-filament OVERRIDE (2.2mm from hotend '0.35 mm brass'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [FLEX] material_identifier product(s) ['felixproxl', 'felixprol', 'felixpro3', 'felixtec4'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [FLEX] filament/FLEX.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [PETG] filament_type guessed as 'PETG' (inherits 'fdm_filament_pet') from the material name/label. CONFIRM this matches the real polymer.
- [PETG] This material had 6 hotend/nozzle variants (0.35 mm brass, 0.50 mm brass, 0.25 mm hardend steel, 0.35 mm hardend steel, 0.50 mm hardend steel, 0.70 mm hardend steel). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.35 mm brass' for temperature/retraction. The other 5 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [PETG] filament_retraction_length set as a per-filament OVERRIDE (1.2mm from hotend '0.35 mm brass'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [PETG] material_identifier product(s) ['felixproxl', 'felixprol', 'felixpro3', 'felixtec4'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [PETG] filament/PETG.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Premium PLA] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Premium PLA] This material had 6 hotend/nozzle variants (0.35 mm brass, 0.50 mm brass, 0.25 mm hardend steel, 0.35 mm hardend steel, 0.50 mm hardend steel, 0.70 mm hardend steel). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.35 mm brass' for temperature/retraction. The other 5 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Premium PLA] filament_retraction_length set as a per-filament OVERRIDE (1.4mm from hotend '0.35 mm brass'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Premium PLA] material_identifier product(s) ['felixproxl', 'felixprol', 'felixpro3', 'felixtec4'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Premium PLA] filament/Premium_PLA.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Wood] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Wood] This material had 6 hotend/nozzle variants (0.35 mm brass, 0.50 mm brass, 0.25 mm hardend steel, 0.35 mm hardend steel, 0.50 mm hardend steel, 0.70 mm hardend steel). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.35 mm brass' for temperature/retraction. The other 5 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Wood] filament_retraction_length set as a per-filament OVERRIDE (2.5mm from hotend '0.35 mm brass'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Wood] material_identifier product(s) ['felixproxl', 'felixprol', 'felixpro3', 'felixtec4'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Wood] filament/Wood.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.

Quality/process presets: skipped, as requested. `process/` was created empty. OrcaSlicer's stock process presets are used until you build your own. Most Cura settings that look like 'quality' settings (walls, infill, speeds, cooling curve, coasting, bridging, supports) were on the PRINTER def and MATERIAL file respectively, not in a separate quality file -- see manual_review/*unmapped* files for all of them.

---

## Run: FELIX Printers FELIX Tec 4

Materials processed this run: **4**


### PRINTER

- [FELIX Printers FELIX Tec 4] printable_area built from machine_width/machine_depth assuming machine_center_is_zero=False (this key was NOT found in the def and defaulted to False). Double check bed origin in Orca matches your real machine.
- Nozzle diameter guessed as 0.35mm from preferred_variant_name='0.35 mm brass'. Cura keeps real nozzle size in a separate 'variant' file that was not provided to this script -- CONFIRM this, or pass --nozzle-diameter explicitly next time.

### MATERIALS

- [FLEX] filament_type guessed as 'TPU' (inherits 'fdm_filament_tpu') from the material name/label. CONFIRM this matches the real polymer.
- [FLEX] This material had 6 hotend/nozzle variants (0.35 mm brass, 0.50 mm brass, 0.25 mm hardend steel, 0.35 mm hardend steel, 0.50 mm hardend steel, 0.70 mm hardend steel). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.35 mm brass' for temperature/retraction. The other 5 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [FLEX] filament_retraction_length set as a per-filament OVERRIDE (2.2mm from hotend '0.35 mm brass'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [FLEX] material_identifier product(s) ['felixproxl', 'felixprol', 'felixpro3', 'felixtec4'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [FLEX] filament/FLEX.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [PETG] filament_type guessed as 'PETG' (inherits 'fdm_filament_pet') from the material name/label. CONFIRM this matches the real polymer.
- [PETG] This material had 6 hotend/nozzle variants (0.35 mm brass, 0.50 mm brass, 0.25 mm hardend steel, 0.35 mm hardend steel, 0.50 mm hardend steel, 0.70 mm hardend steel). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.35 mm brass' for temperature/retraction. The other 5 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [PETG] filament_retraction_length set as a per-filament OVERRIDE (1.2mm from hotend '0.35 mm brass'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [PETG] material_identifier product(s) ['felixproxl', 'felixprol', 'felixpro3', 'felixtec4'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [PETG] filament/PETG.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Premium PLA] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Premium PLA] This material had 6 hotend/nozzle variants (0.35 mm brass, 0.50 mm brass, 0.25 mm hardend steel, 0.35 mm hardend steel, 0.50 mm hardend steel, 0.70 mm hardend steel). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.35 mm brass' for temperature/retraction. The other 5 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Premium PLA] filament_retraction_length set as a per-filament OVERRIDE (1.4mm from hotend '0.35 mm brass'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Premium PLA] material_identifier product(s) ['felixproxl', 'felixprol', 'felixpro3', 'felixtec4'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Premium PLA] filament/Premium_PLA.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.
- [Wood] filament_type guessed as 'PLA' (inherits 'fdm_filament_pla') from the material name/label. CONFIRM this matches the real polymer.
- [Wood] This material had 6 hotend/nozzle variants (0.35 mm brass, 0.50 mm brass, 0.25 mm hardend steel, 0.35 mm hardend steel, 0.50 mm hardend steel, 0.70 mm hardend steel). Per your instruction (option B) only ONE filament preset is generated per material, using hotend '0.35 mm brass' for temperature/retraction. The other 5 variant(s) are saved in manual_review in case you want to build extra nozzle-specific filament presets later.
- [Wood] filament_retraction_length set as a per-filament OVERRIDE (2.5mm from hotend '0.35 mm brass'). In OrcaSlicer retraction normally lives on the PRINTER/extruder profile, with this kind of per-filament override being the exception, not the rule -- consider moving this to the printer's extruder settings instead if it's the same for every filament on that printer.
- [Wood] material_identifier product(s) ['felixproxl', 'felixprol', 'felixpro3', 'felixtec4'] did not match any printer processed in this run, so compatible_printers could not be filled for them. Re-run including those printers, or add them to compatible_printers by hand.
- [Wood] filament/Wood.json already existed from an earlier printer in this batch -- merged compatible_printers (now: []) rather than overwriting it.

Quality/process presets: skipped, as requested. `process/` was created empty. OrcaSlicer's stock process presets are used until you build your own. Most Cura settings that look like 'quality' settings (walls, infill, speeds, cooling curve, coasting, bridging, supports) were on the PRINTER def and MATERIAL file respectively, not in a separate quality file -- see manual_review/*unmapped* files for all of them.
