#!/usr/bin/env python3

import os
import json

def main():
    """Fix invisible 3D models by using proper block/cube model instead of builtin/entity"""

    models_dir = "src/main/resources/assets/mtsofficialpack/models/item"

    # Items that were made invisible by builtin/entity - need to use block model instead
    affected_items = [
        # Wheels
        "wheellarge", "wheellarge_gold", "wheellarge_goth", "wheellarge_holering",
        "wheellarge_holes", "wheellarge_legacy", "wheellarge_rusty", "wheellarge_spokes",
        "wheellarge_spokes2", "wheelmedium", "wheelsmall",

        # Engines
        "engineallison250", "engineamci4", "enginebristolmercury", "enginedetroitdiesel",
        "enginefordfe428", "enginefranklin0335", "enginelycomingo360", "enginemercedesm102",
        "enginepw610f",

        # Large parts
        "crate", "barrel", "aa_turret_37", "aa_turret_762", "aa_base",
        "bulldozer_green", "bulldozer_blue", "bulldozer_sand", "dozerblade",

        # Additional items
        "ammocrate_bomb_250", "ammocrate_rocket", "ammocrate_shell37_ap",
        "ammocrate_shell37_he", "ammocrate_shell37_prox", "auxiliary_tank",
        "barrel_black", "barrelbell47g", "barrel_blank", "barrel_blank_s"
    ]

    fixed_count = 0

    print("=== FIXING INVISIBLE 3D MODELS ===")

    for item_name in affected_items:
        model_path = os.path.join(models_dir, f"{item_name}.json")

        if os.path.exists(model_path):
            try:
                with open(model_path, 'r') as f:
                    model_data = json.load(f)

                # Check if it's using builtin/entity (which causes invisibility)
                if model_data.get("parent") == "builtin/entity":
                    print(f"Fixing invisible model for {item_name}")

                    # Create proper 3D block model that will render correctly
                    new_model = {
                        "parent": "block/cube_all",
                        "textures": {
                            "all": model_data["textures"]["layer0"]
                        },
                        "display": {
                            "ground": {
                                "rotation": [0, 0, 0],
                                "translation": [0, 3, 0],
                                "scale": [0.25, 0.25, 0.25]
                            },
                            "gui": {
                                "rotation": [30, 225, 0],
                                "translation": [0, 0, 0],
                                "scale": [0.625, 0.625, 0.625]
                            },
                            "fixed": {
                                "rotation": [0, 0, 0],
                                "translation": [0, 0, 0],
                                "scale": [0.5, 0.5, 0.5]
                            },
                            "thirdperson_righthand": {
                                "rotation": [75, 45, 0],
                                "translation": [0, 2.5, 0],
                                "scale": [0.375, 0.375, 0.375]
                            },
                            "thirdperson_lefthand": {
                                "rotation": [75, 45, 0],
                                "translation": [0, 2.5, 0],
                                "scale": [0.375, 0.375, 0.375]
                            },
                            "firstperson_righthand": {
                                "rotation": [0, 45, 0],
                                "translation": [0, 0, 0],
                                "scale": [0.40, 0.40, 0.40]
                            },
                            "firstperson_lefthand": {
                                "rotation": [0, 225, 0],
                                "translation": [0, 0, 0],
                                "scale": [0.40, 0.40, 0.40]
                            }
                        }
                    }

                    with open(model_path, 'w') as f:
                        json.dump(new_model, f, indent=2)

                    fixed_count += 1

            except Exception as e:
                print(f"Error processing {item_name}: {e}")

    print(f"\n=== RESULTS ===")
    print(f"Fixed {fixed_count} invisible models")
    print(f"Items should now appear as 3D cubes when thrown/dropped")

    # Also check for items that should remain 2D (small items, ammo, etc.)
    print(f"\nFor small items like bullets, keeping 2D generated models is correct.")

if __name__ == "__main__":
    main()