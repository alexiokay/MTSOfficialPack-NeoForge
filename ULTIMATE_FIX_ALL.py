#!/usr/bin/env python3

import os
import json
from pathlib import Path

def fix_everything():
    """ULTIMATE ALL-IN-ONE SCRIPT - Fixes everything at once with proper OBJ vs JSON handling"""

    namespace = "mtsofficialpack"
    pack_dir = "."
    models_dir = Path(f"src/main/resources/assets/{namespace}/models/item")

    print("=== ULTIMATE SMART FIX SCRIPT ===")
    print(f"Processing namespace: {namespace}")

    if not models_dir.exists():
        print(f"Models directory not found: {models_dir}")
        return

    # Items that need OBJ models (should NOT have JSON models)
    obj_items = {
        # Bullets - these need OBJ models for 3D rendering
        "basicbomb", "bomblet", "bullet3700he", "bullet3700he_mag", "bullet3700proxy",
        "bullet3700proxy_mag", "bullet3700solid", "bullet3700solid_mag", "bullet762",
        "bulletflare_blue", "bulletflare_green", "bulletflare_rainbow", "bulletflare_red",
        "bulletflare_white", "bulletflare_yellow", "bulletrocket", "extinguisherfoam",
        "heavy_bomb", "paint_black", "paint_blue", "paint_glow", "paint_red", "paint_yellow",
        "watercannon_proj",

        # Decors - these need OBJ models
        "beacon_top", "beacon_tower_inverted", "beacon_tower_standard", "crashbarrier",
        "fluidloader", "fluidunloader", "fuelpump", "itemloader", "itemunloader",
        "prop1", "prop2", "prop3", "prop4", "prop5", "signalcontroller", "telephonebooth",
        "trafficcone",

        # Most parts need OBJ models
        # Most vehicles need OBJ models
    }

    # Items that should have simple JSON models (2D textures only)
    simple_items = {
        # Instruments are usually just 2D textures
        "instrument_aircraft_adf", "instrument_aircraft_airspeed", "instrument_aircraft_altimeter",
        "instrument_aircraft_attitude", "instrument_aircraft_beacon_distance", "instrument_aircraft_clock",
        "instrument_aircraft_coordinate", "instrument_aircraft_electric", "instrument_aircraft_enginetemp",
        "instrument_aircraft_flaps", "instrument_aircraft_fuelflow", "instrument_aircraft_fuelqty",
        "instrument_aircraft_heading", "instrument_aircraft_ils", "instrument_aircraft_liftreserve",
        "instrument_aircraft_oilpressure", "instrument_aircraft_tachometer", "instrument_aircraft_trim",
        "instrument_aircraft_turncoord", "instrument_aircraft_turnslip", "instrument_aircraft_verticalspeed",
        "instrument_car_clock", "instrument_car_electric", "instrument_car_enginetemp_c",
        "instrument_car_enginetemp_f", "instrument_car_fuelqty", "instrument_car_gear",
        "instrument_car_oilpressure_b", "instrument_car_oilpressure_p", "instrument_car_spedometer_blk",
        "instrument_car_spedometer_kph", "instrument_car_spedometer_mph", "instrument_car_tachometer",
        "instrument_car_tachometer_amc", "instrument_car_tachometer_det",

        # Signs/poles might work as simple items
        "pole_core", "pole_crossingsignal", "pole_flashingsignal_red", "pole_flashingsignal_yellow",
        "pole_streetlight", "pole_trafficsignal", "sign_bump", "sign_cow", "sign_crosswalk",
        "sign_deadend", "sign_donotenter", "sign_entryforbidden", "sign_highway", "sign_highwayend",
        "sign_left_direction", "sign_mts", "sign_noparking", "sign_oneway_left", "sign_oneway_right",
        "sign_priority", "sign_priorityend", "sign_restrictionsend", "sign_right_direction",
        "sign_route", "sign_speedlimit", "sign_stop", "sign_turn_left", "sign_turn_right",
        "sign_wrongway", "sign_yield"
    }

    # STEP 1: Find ALL actual texture files
    print("\n1. Scanning for actual texture files...")
    texture_dir = Path(f"src/main/resources/assets/{namespace}/textures")
    actual_textures = {}

    if texture_dir.exists():
        for png_file in texture_dir.rglob("*.png"):
            relative_path = png_file.relative_to(texture_dir)
            item_name = png_file.stem
            texture_ref = f"{namespace}:{relative_path.as_posix()[:-4]}"

            # Store all possible locations for each item
            if item_name not in actual_textures:
                actual_textures[item_name] = []
            actual_textures[item_name].append(texture_ref)

    print(f"Found {len(actual_textures)} unique texture names")

    # STEP 2: Clean up bad models
    print("\n2. Cleaning up bad models...")
    deleted_count = 0
    for item_name in obj_items:
        model_file = models_dir / f"{item_name}.json"
        if model_file.exists():
            try:
                model_file.unlink()
                print(f"DELETED: {item_name}.json (needs OBJ model)")
                deleted_count += 1
            except Exception as e:
                print(f"Failed to delete {item_name}.json: {e}")

    # STEP 3: Fix existing models for simple items only
    print("\n3. Fixing simple item models...")
    fixed_count = 0
    created_count = 0

    for item_name in simple_items:
        if item_name not in actual_textures:
            continue

        model_file = models_dir / f"{item_name}.json"
        texture_options = actual_textures[item_name]

        # Find best texture path
        best_texture = None
        priorities = [
            f"{namespace}:items/instruments/",
            f"{namespace}:items/poles/",
            f"{namespace}:items/",
            f"{namespace}:item/",
            f"{namespace}:"
        ]

        for priority in priorities:
            for texture in texture_options:
                if texture.startswith(priority):
                    best_texture = texture
                    break
            if best_texture:
                break

        if not best_texture:
            best_texture = texture_options[0]

        # Create simple model
        model_data = {
            "parent": "item/generated",
            "textures": {
                "layer0": best_texture
            }
        }

        try:
            if model_file.exists():
                # Fix existing model
                with open(model_file, 'r') as f:
                    existing_data = json.load(f)

                if "textures" in existing_data and "layer0" in existing_data["textures"]:
                    old_texture = existing_data["textures"]["layer0"]
                    if old_texture != best_texture:
                        print(f"FIXING: {item_name}.json: {old_texture} -> {best_texture}")
                        existing_data["textures"]["layer0"] = best_texture
                        with open(model_file, 'w') as f:
                            json.dump(existing_data, f, indent=2)
                        fixed_count += 1
                else:
                    existing_data["textures"] = {"layer0": best_texture}
                    with open(model_file, 'w') as f:
                        json.dump(existing_data, f, indent=2)
                    fixed_count += 1
            else:
                # Create new simple model
                print(f"CREATING: {item_name}.json -> {best_texture}")
                with open(model_file, 'w') as f:
                    json.dump(model_data, f, indent=2)
                created_count += 1

        except Exception as e:
            print(f"Error processing {item_name}: {e}")

    print(f"\n=== SMART FIX RESULTS ===")
    print(f"Deleted bad OBJ-item models: {deleted_count}")
    print(f"Fixed simple item models: {fixed_count}")
    print(f"Created simple item models: {created_count}")
    print(f"Total textures found: {len(actual_textures)}")
    print("\nSMART BEHAVIOR:")
    print("- OBJ items (bullets, decors, parts) will use MTS's built-in system")
    print("- Simple items (instruments, signs) will use JSON models")
    print("- No more black/purple textures for wrong model types!")

if __name__ == "__main__":
    fix_everything()