#!/usr/bin/env python3

import os
import json

def main():
    """Create proper 3D models using custom elements instead of flat textures"""

    models_dir = "src/main/resources/assets/mtsofficialpack/models/item"

    # Items that should be 3D
    items_3d = [
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

    print("=== CREATING PROPER 3D MODELS WITH CUSTOM ELEMENTS ===")

    for item_name in items_3d:
        model_path = os.path.join(models_dir, f"{item_name}.json")

        if os.path.exists(model_path):
            try:
                with open(model_path, 'r') as f:
                    model_data = json.load(f)

                # Get the texture path
                texture_path = model_data["textures"]["layer0"]

                print(f"Creating 3D model for {item_name}")

                # Create a proper 3D model with elements that form a small cube/box
                new_model = {
                    "textures": {
                        "texture": texture_path,
                        "particle": texture_path
                    },
                    "elements": [
                        {
                            "from": [6, 6, 6],
                            "to": [10, 10, 10],
                            "faces": {
                                "down":  {"texture": "#texture", "cullface": "down"},
                                "up":    {"texture": "#texture", "cullface": "up"},
                                "north": {"texture": "#texture", "cullface": "north"},
                                "south": {"texture": "#texture", "cullface": "south"},
                                "west":  {"texture": "#texture", "cullface": "west"},
                                "east":  {"texture": "#texture", "cullface": "east"}
                            }
                        }
                    ],
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
    print(f"Created {fixed_count} proper 3D models with custom elements")
    print(f"Items now have actual 3D geometry (small cubes) with texture on all faces")
    print(f"This should provide true 3D appearance when dropped!")

    # Create specialized models for different item types
    print(f"\nNext improvements could include:")
    print(f"- Different cube sizes for different item types")
    print(f"- Wheel-specific geometry (torus/cylinder)")
    print(f"- Engine-specific geometry (rectangular prism)")
    print(f"- Custom shapes for each category")

if __name__ == "__main__":
    main()