#!/usr/bin/env python3

import os
import json

def main():
    """Fix additional items that should be 3D"""

    models_dir = "src/main/resources/assets/mtsofficialpack/models/item"

    # Additional items that should render as 3D entities
    additional_3d_items = [
        # Ammunition crates and containers
        "ammocrate_bomb_250", "ammocrate_rocket", "ammocrate_shell37_ap",
        "ammocrate_shell37_he", "ammocrate_shell37_prox",

        # Fuel tanks and barrels
        "auxiliary_tank", "barrel_black", "jerrycan", "fueltank_large",

        # Gun barrels and weapon parts
        "barrelbell47g", "barrel_blank", "barrel_blank_s", "gunmount",
        "gunturret", "gunturret_m2", "turret_main",

        # Seats and furniture
        "seat_leather", "seat_fabric", "seat_pilot", "chair_wood",

        # Large mechanical parts
        "gearbox", "differential", "axle", "transmission",

        # Propellers and rotors (if they exist)
        "propeller", "rotor", "propeller_metal", "propeller_wood"
    ]

    fixed_count = 0

    print("=== FIXING ADDITIONAL 3D ITEMS ===")

    for item_name in additional_3d_items:
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
        else:
            print(f"Model not found: {item_name}")

    print(f"\n=== RESULTS ===")
    print(f"Fixed {fixed_count} additional models for 3D rendering")

    # Show summary of all changes
    print(f"\nTo recompile the content pack:")
    print(f"1. Run: ./gradlew build")
    print(f"2. Test in-game - wheels, engines, and parts should now appear as 3D when thrown")

if __name__ == "__main__":
    main()