#!/usr/bin/env python3

import os
import json

def main():
    """Fix the multi-texture cube issue by using proper item/generated with 3D transforms"""

    models_dir = "src/main/resources/assets/mtsofficialpack/models/item"

    # Items that are showing multiple textures due to block/cube_all
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

    print("=== FIXING MULTI-TEXTURE CUBE ISSUE ===")

    for item_name in affected_items:
        model_path = os.path.join(models_dir, f"{item_name}.json")

        if os.path.exists(model_path):
            try:
                with open(model_path, 'r') as f:
                    model_data = json.load(f)

                # Check if it's using block/cube_all (which causes multi-texture issue)
                if model_data.get("parent") == "block/cube_all":
                    print(f"Fixing multi-texture issue for {item_name}")

                    # Get the texture path from the current model
                    texture_path = model_data["textures"]["all"]

                    # Create proper item model with enhanced 3D display settings
                    new_model = {
                        "parent": "item/generated",
                        "textures": {
                            "layer0": texture_path
                        },
                        "display": {
                            "ground": {
                                "rotation": [0, 0, 0],
                                "translation": [0, 2, 0],
                                "scale": [0.5, 0.5, 0.5]
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
                                "rotation": [75, 225, 0],
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
    print(f"Fixed {fixed_count} models with multi-texture issues")
    print(f"Items now use single texture with enhanced 3D display transforms")
    print(f"This creates 3D appearance without the confusing multiple textures")

    # Create a summary of what this approach does
    print(f"\nHow this works:")
    print(f"- Uses 'item/generated' parent (single texture)")
    print(f"- Enhanced display transforms make items appear more 3D")
    print(f"- Larger scale and better positioning when dropped")
    print(f"- Proper rotations for different view modes")

if __name__ == "__main__":
    main()