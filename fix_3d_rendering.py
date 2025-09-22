#!/usr/bin/env python3

import os
import json

def main():
    """Fix 2D models to render as 3D when thrown/dropped"""

    models_dir = "src/main/resources/assets/mtsofficialpack/models/item"

    # Items that should render as 3D blocks/entities when thrown
    items_3d_entity = [
        # Wheels
        "wheellarge", "wheellarge_gold", "wheellarge_goth", "wheellarge_holering",
        "wheellarge_holes", "wheellarge_legacy", "wheellarge_rusty", "wheellarge_spokes",
        "wheellarge_spokes2", "wheelmedium", "wheelsmall", "wheelcar", "wheeltruck",

        # Engines
        "engineallison250", "engineamci4", "enginebristolmercury", "enginedetroitdiesel",
        "enginefordfe428", "enginefranklin0335", "enginelycomingo360", "enginemercedesm102",
        "enginepw610f", "enginequad", "engineradial", "engineturbofan", "engineturbojet",

        # Engine parts
        "prop_wooden", "prop_metal", "prop_airliner", "rotor_main", "rotor_tail",

        # Crates and containers
        "crate", "crate_green", "crate_brown", "barrel", "jerrycan", "fueltank",

        # Large parts/components
        "aa_turret_37", "aa_turret_762", "aa_base", "gunturret", "seat", "chair",
        "bulldozer_green", "bulldozer_blue", "bulldozer_sand", "dozerblade"
    ]

    # Items that should use handheld model (tools, weapons, small items)
    items_handheld = [
        "gunflaregun", "drill", "wrench", "hammer", "screwdriver", "gunpistol",
        "gunrifle", "gunmachinegun", "gunshotgun", "binoculars", "radio", "compass"
    ]

    fixed_count = 0

    print("=== FIXING 3D RENDERING FOR ITEMS ===")

    # Fix items that should render as 3D entities
    for item_name in items_3d_entity:
        model_path = os.path.join(models_dir, f"{item_name}.json")

        if os.path.exists(model_path):
            try:
                with open(model_path, 'r') as f:
                    model_data = json.load(f)

                # Check if it's currently using 2D generated model
                if model_data.get("parent") == "item/generated":
                    print(f"Converting {item_name} to 3D entity rendering")

                    # Create 3D model configuration
                    new_model = {
                        "parent": "builtin/entity",
                        "display": {
                            "ground": {
                                "rotation": [0, 0, 0],
                                "translation": [0, 2, 0],
                                "scale": [0.5, 0.5, 0.5]
                            },
                            "head": {
                                "rotation": [0, 180, 0],
                                "translation": [0, 13, 7],
                                "scale": [1, 1, 1]
                            },
                            "thirdperson_righthand": {
                                "rotation": [75, 315, 0],
                                "translation": [0, 2.5, 0],
                                "scale": [0.375, 0.375, 0.375]
                            },
                            "gui": {
                                "rotation": [30, 45, 0],
                                "translation": [0, 0, 0],
                                "scale": [0.625, 0.625, 0.625]
                            }
                        },
                        "textures": model_data["textures"]
                    }

                    with open(model_path, 'w') as f:
                        json.dump(new_model, f, indent=2)

                    fixed_count += 1

            except Exception as e:
                print(f"Error processing {item_name}: {e}")

    # Fix items that should use handheld model
    for item_name in items_handheld:
        model_path = os.path.join(models_dir, f"{item_name}.json")

        if os.path.exists(model_path):
            try:
                with open(model_path, 'r') as f:
                    model_data = json.load(f)

                # Check if it's currently using 2D generated model
                if model_data.get("parent") == "item/generated":
                    print(f"Converting {item_name} to handheld 3D rendering")

                    # Update to handheld model
                    model_data["parent"] = "item/handheld"

                    with open(model_path, 'w') as f:
                        json.dump(model_data, f, indent=2)

                    fixed_count += 1

            except Exception as e:
                print(f"Error processing {item_name}: {e}")

    print(f"\n=== RESULTS ===")
    print(f"Fixed {fixed_count} models for 3D rendering")

    # Look for other potential 3D items
    print(f"\nChecking for other potential 3D items...")
    potential_3d = []

    if os.path.exists(models_dir):
        for filename in os.listdir(models_dir):
            if filename.endswith('.json'):
                item_name = filename[:-5]

                # Skip if already processed
                if item_name in items_3d_entity or item_name in items_handheld:
                    continue

                # Look for keywords that suggest 3D items
                if any(keyword in item_name.lower() for keyword in
                       ['wheel', 'engine', 'prop', 'rotor', 'turret', 'gun', 'seat',
                        'crate', 'barrel', 'tank', 'blade', 'drill']):
                    potential_3d.append(item_name)

    if potential_3d:
        print("Potential 3D items to review:")
        for item in potential_3d[:10]:  # Show first 10
            print(f"  - {item}")
        if len(potential_3d) > 10:
            print(f"  ... and {len(potential_3d) - 10} more")

if __name__ == "__main__":
    main()