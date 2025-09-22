#!/usr/bin/env python3

import os
import json
import shutil
from pathlib import Path

def find_texture_files(pack_dir):
    """Find all available texture files in the pack"""
    textures = {}
    texture_dirs = [
        "src/main/resources/assets/*/textures/item",
        "src/main/resources/assets/*/textures/items",
        "src/main/resources/assets/*/textures/parts",
        "src/main/resources/assets/*/textures/decors",
        "src/main/resources/assets/*/textures/vehicles"
    ]

    for pattern in texture_dirs:
        for texture_dir in Path(pack_dir).glob(pattern):
            if texture_dir.is_dir():
                namespace = texture_dir.parts[-4]  # Extract namespace from path
                for texture_file in texture_dir.glob("**/*.png"):
                    # Get relative path from textures directory
                    rel_path = texture_file.relative_to(texture_dir.parent)
                    item_name = texture_file.stem
                    texture_path = f"{namespace}:{rel_path.as_posix()[:-4]}"  # Remove .png
                    textures[item_name] = texture_path
                    print(f"Found texture: {item_name} -> {texture_path}")

    return textures

def find_existing_3d_models(models_dir):
    """Find all existing 3D models in various subdirectories"""
    models_3d = {}

    # Check common subdirectories for 3D models
    subdirs = ["parts", "items", "vehicles", "decors", "weapons", "tools"]

    for subdir in subdirs:
        subdir_path = os.path.join(models_dir, subdir)
        if os.path.exists(subdir_path):
            for filename in os.listdir(subdir_path):
                if filename.endswith('.json'):
                    item_name = filename[:-5]
                    model_path = os.path.join(subdir_path, filename)

                    # Check if it's actually a 3D model
                    try:
                        with open(model_path, 'r') as f:
                            model_data = json.load(f)

                        if "elements" in model_data:  # Has 3D geometry
                            models_3d[item_name] = model_path
                            print(f"Found 3D model: {item_name} in {subdir}/")
                    except:
                        pass

    return models_3d

def create_basic_model(item_name, texture_path):
    """Create a basic 2D model with proper texture reference"""
    return {
        "parent": "item/generated",
        "textures": {
            "layer0": texture_path
        }
    }

def create_fallback_model():
    """Create a fallback model for items with no texture"""
    return {
        "parent": "item/generated",
        "textures": {
            "layer0": "minecraft:item/barrier"
        }
    }

def main():
    pack_dir = "."
    namespace = "mtsofficialpack"  # Can be changed for other packs
    models_dir = f"src/main/resources/assets/{namespace}/models/item"

    print("=== UNIVERSAL MODEL FIXER ===")
    print(f"Processing pack: {namespace}")

    # Create models directory if it doesn't exist
    os.makedirs(models_dir, exist_ok=True)

    # Step 1: Find all available textures
    print("\n1. Scanning for textures...")
    available_textures = find_texture_files(pack_dir)
    print(f"Found {len(available_textures)} textures")

    # Step 2: Find all existing 3D models
    print("\n2. Scanning for 3D models...")
    available_3d_models = find_existing_3d_models(models_dir)
    print(f"Found {len(available_3d_models)} 3D models")

    # Step 3: Process all items that need models
    print("\n3. Processing items...")

    total_created = 0
    total_upgraded = 0

    # First, upgrade any items that have 3D models available
    for item_name, model_3d_path in available_3d_models.items():
        root_model_path = os.path.join(models_dir, f"{item_name}.json")

        if os.path.exists(root_model_path):
            # Check if current model is 2D
            try:
                with open(root_model_path, 'r') as f:
                    current_model = json.load(f)

                if current_model.get("parent") == "item/generated" and "elements" not in current_model:
                    print(f"Upgrading {item_name} to 3D")
                    os.remove(root_model_path)
                    shutil.copy2(model_3d_path, root_model_path)
                    total_upgraded += 1
            except:
                pass
        else:
            # Create 3D model at root level
            print(f"Creating 3D model for {item_name}")
            shutil.copy2(model_3d_path, root_model_path)
            total_created += 1

    # Second, create models for items that have textures but no models
    for item_name, texture_path in available_textures.items():
        root_model_path = os.path.join(models_dir, f"{item_name}.json")

        if not os.path.exists(root_model_path):
            print(f"Creating model for {item_name} with texture {texture_path}")
            model_data = create_basic_model(item_name, texture_path)

            with open(root_model_path, 'w') as f:
                json.dump(model_data, f, indent=2)

            total_created += 1

    # Step 4: Handle items from logs that might still be missing
    print("\n4. Checking for items from error logs...")

    # Read all possible item names from previous logs/scripts
    known_items = set()

    # Add items from your original list
    log_items = """
    mirrorornament_rubix fuzeproxy spraycan_black instrument_car_fuelqty merc230_salmon
    fordmustang69_bluestripe brigbedbox fordmustang69_white crashbarrier grilleornament_horns
    merc230_extravagant skyhawk_red vulcanair_orange instrument_car_electric sign_cow
    mc172_oak instrument_car_oilpressure_p brigbedtanker_greenred instrument_car_oilpressure_b
    brigbeddump_dirt merc230_brown repairkit enginequad brigbeddump_coal mirrorornament_blockacacia
    ocpbutter mirrorornament_pine comanche_blackred spotlight carseat_brown mirrorornament_1911gray
    dump_storage seatyellow spotlight_bell206 fluidunloader wheelsmall_legacy enginedetroitdiesel
    gunflaregun merc230_olive e500_blue hydraulics sign_noparking comanche_yellow dump_dropper
    pzl37los_brown skidhelicopter comanche_blackredstripe bullet3700proxy pole_crossingsignal
    paint_black bullet3700solid_mag vulcanair_cow beacon_tower_inverted crate_green watercannon
    barrel scout_red aa_turret_37 fordmustang69_lime carseat_black drill mirrorornament_saturn
    propellerrotor mirrorornament_blockgrass wheellarge_spokes2 gmcbrig_tan bell47g_blue
    extinguisherfoam carseat_red wheelsmall brigbedtanker_blank bullet3700he_mag spring
    pole_flashingsignal_red nuts skyhawk_blackred fordmustang69_seagreen fordmustang69_police
    merc230_blue fordmustang69_yellow grilleornament_snail enginemercedesm102 brigbeddump_moss
    mirrorornament_anvil crate_blue brigbeddump_copper vulcanair_green instrument_aircraft_flaps
    wheelmedium_legacy wheellarge_holering sign_turn_right pontoon bulletflare_red heavy_bomb
    wheellarge_whiterim comanche_orangebrown sign_priority mirrorornament_steak brigbeddump_nether
    fordmustang69_orange plating e500_green signalcontroller propellersmall2blade skyhawk_coffee
    bulletflare_white aa_base merc230_yellow fordmustang69_red sign_route sign_speedlimit
    vulcanair_yellow glovebox_skyhawk instrument_car_spedometer_kph trimotor_blue vulcanair_redsnail
    smallarmscartridge bulletrocket bulldozer_green bulldozer_blue bulldozer_sand dozerblade
    truck_yellow truck_silver truck_blue truck_red
    """.split()

    for item in log_items:
        if item.strip():
            known_items.add(item.strip())

    # Add items you specifically mentioned
    specific_items = [
        "ocpbutter", "stop", "sign_stop", "turn_left", "sign_turn_left",
        "confetti", "confettigun", "sign_turn_right"
    ]
    known_items.update(specific_items)

    missing_created = 0
    for item_name in known_items:
        root_model_path = os.path.join(models_dir, f"{item_name}.json")

        if not os.path.exists(root_model_path):
            # Try to find a matching texture
            best_texture = None

            # Direct match
            if item_name in available_textures:
                best_texture = available_textures[item_name]
            else:
                # Fuzzy match
                for texture_name, texture_path in available_textures.items():
                    if item_name in texture_name or texture_name in item_name:
                        best_texture = texture_path
                        break

            # Create model
            if best_texture:
                model_data = create_basic_model(item_name, best_texture)
                print(f"Creating model for {item_name} with texture {best_texture}")
            else:
                model_data = create_basic_model(item_name, f"{namespace}:item/{item_name}")
                print(f"Creating model for {item_name} with default texture path")

            with open(root_model_path, 'w') as f:
                json.dump(model_data, f, indent=2)

            missing_created += 1

    print(f"\n=== SUMMARY ===")
    print(f"Upgraded to 3D: {total_upgraded}")
    print(f"Created from textures: {total_created}")
    print(f"Created from missing list: {missing_created}")
    print(f"Total improvements: {total_upgraded + total_created + missing_created}")
    print(f"\nThis script can be used for any content pack by changing the 'namespace' variable.")

if __name__ == "__main__":
    main()