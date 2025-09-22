#!/usr/bin/env python3

import os
import json

def create_wheel_3d_model(texture_path):
    """Create a better wheel model with multiple elements to simulate 3D shape"""
    return {
        "textures": {
            "texture": texture_path,
            "particle": texture_path
        },
        "elements": [
            # Outer rim
            {
                "from": [4, 6, 4],
                "to": [12, 10, 12],
                "faces": {
                    "down":  {"texture": "#texture", "tintindex": 0},
                    "up":    {"texture": "#texture", "tintindex": 0},
                    "north": {"texture": "#texture", "tintindex": 0},
                    "south": {"texture": "#texture", "tintindex": 0},
                    "west":  {"texture": "#texture", "tintindex": 0},
                    "east":  {"texture": "#texture", "tintindex": 0}
                }
            },
            # Inner wheel
            {
                "from": [5, 7, 5],
                "to": [11, 9, 11],
                "faces": {
                    "down":  {"texture": "#texture", "tintindex": 0},
                    "up":    {"texture": "#texture", "tintindex": 0},
                    "north": {"texture": "#texture", "tintindex": 0},
                    "south": {"texture": "#texture", "tintindex": 0},
                    "west":  {"texture": "#texture", "tintindex": 0},
                    "east":  {"texture": "#texture", "tintindex": 0}
                }
            }
        ],
        "display": {
            "ground": {
                "rotation": [0, 0, 90],  # Lay wheel flat
                "translation": [0, 2, 0],
                "scale": [0.75, 0.75, 0.75]
            },
            "gui": {
                "rotation": [30, 45, 0],
                "translation": [0, 0, 0],
                "scale": [0.75, 0.75, 0.75]
            },
            "fixed": {
                "rotation": [0, 0, 0],
                "translation": [0, 0, 0],
                "scale": [0.75, 0.75, 0.75]
            },
            "thirdperson_righthand": {
                "rotation": [75, 45, 0],
                "translation": [0, 2.5, 0],
                "scale": [0.5, 0.5, 0.5]
            },
            "thirdperson_lefthand": {
                "rotation": [75, 225, 0],
                "translation": [0, 2.5, 0],
                "scale": [0.5, 0.5, 0.5]
            },
            "firstperson_righthand": {
                "rotation": [0, 45, 0],
                "translation": [0, 0, 0],
                "scale": [0.5, 0.5, 0.5]
            },
            "firstperson_lefthand": {
                "rotation": [0, 225, 0],
                "translation": [0, 0, 0],
                "scale": [0.5, 0.5, 0.5]
            }
        }
    }

def create_engine_3d_model(texture_path):
    """Create a better engine model with multiple elements"""
    return {
        "textures": {
            "texture": texture_path,
            "particle": texture_path
        },
        "elements": [
            # Main engine block
            {
                "from": [2, 5, 5],
                "to": [14, 11, 11],
                "faces": {
                    "down":  {"texture": "#texture", "tintindex": 0},
                    "up":    {"texture": "#texture", "tintindex": 0},
                    "north": {"texture": "#texture", "tintindex": 0},
                    "south": {"texture": "#texture", "tintindex": 0},
                    "west":  {"texture": "#texture", "tintindex": 0},
                    "east":  {"texture": "#texture", "tintindex": 0}
                }
            },
            # Engine attachment point
            {
                "from": [1, 7, 7],
                "to": [3, 9, 9],
                "faces": {
                    "down":  {"texture": "#texture", "tintindex": 0},
                    "up":    {"texture": "#texture", "tintindex": 0},
                    "north": {"texture": "#texture", "tintindex": 0},
                    "south": {"texture": "#texture", "tintindex": 0},
                    "west":  {"texture": "#texture", "tintindex": 0},
                    "east":  {"texture": "#texture", "tintindex": 0}
                }
            },
            # Engine detail
            {
                "from": [6, 4, 6],
                "to": [10, 6, 10],
                "faces": {
                    "down":  {"texture": "#texture", "tintindex": 0},
                    "up":    {"texture": "#texture", "tintindex": 0},
                    "north": {"texture": "#texture", "tintindex": 0},
                    "south": {"texture": "#texture", "tintindex": 0},
                    "west":  {"texture": "#texture", "tintindex": 0},
                    "east":  {"texture": "#texture", "tintindex": 0}
                }
            }
        ],
        "display": {
            "ground": {
                "rotation": [0, 0, 0],
                "translation": [0, 2, 0],
                "scale": [0.6, 0.6, 0.6]
            },
            "gui": {
                "rotation": [30, 45, 0],
                "translation": [0, 0, 0],
                "scale": [0.7, 0.7, 0.7]
            },
            "fixed": {
                "rotation": [0, 0, 0],
                "translation": [0, 0, 0],
                "scale": [0.6, 0.6, 0.6]
            },
            "thirdperson_righthand": {
                "rotation": [75, 45, 0],
                "translation": [0, 2.5, 0],
                "scale": [0.4, 0.4, 0.4]
            },
            "thirdperson_lefthand": {
                "rotation": [75, 225, 0],
                "translation": [0, 2.5, 0],
                "scale": [0.4, 0.4, 0.4]
            },
            "firstperson_righthand": {
                "rotation": [0, 45, 0],
                "translation": [0, 0, 0],
                "scale": [0.45, 0.45, 0.45]
            },
            "firstperson_lefthand": {
                "rotation": [0, 225, 0],
                "translation": [0, 0, 0],
                "scale": [0.45, 0.45, 0.45]
            }
        }
    }

def create_barrel_3d_model(texture_path):
    """Create a better barrel/crate model"""
    return {
        "textures": {
            "texture": texture_path,
            "particle": texture_path
        },
        "elements": [
            # Main barrel
            {
                "from": [5, 3, 5],
                "to": [11, 13, 11],
                "faces": {
                    "down":  {"texture": "#texture", "tintindex": 0},
                    "up":    {"texture": "#texture", "tintindex": 0},
                    "north": {"texture": "#texture", "tintindex": 0},
                    "south": {"texture": "#texture", "tintindex": 0},
                    "west":  {"texture": "#texture", "tintindex": 0},
                    "east":  {"texture": "#texture", "tintindex": 0}
                }
            }
        ],
        "display": {
            "ground": {
                "rotation": [0, 0, 0],
                "translation": [0, 2, 0],
                "scale": [0.6, 0.6, 0.6]
            },
            "gui": {
                "rotation": [30, 45, 0],
                "translation": [0, 0, 0],
                "scale": [0.7, 0.7, 0.7]
            },
            "fixed": {
                "rotation": [0, 0, 0],
                "translation": [0, 0, 0],
                "scale": [0.6, 0.6, 0.6]
            },
            "thirdperson_righthand": {
                "rotation": [75, 45, 0],
                "translation": [0, 2.5, 0],
                "scale": [0.4, 0.4, 0.4]
            },
            "thirdperson_lefthand": {
                "rotation": [75, 225, 0],
                "translation": [0, 2.5, 0],
                "scale": [0.4, 0.4, 0.4]
            },
            "firstperson_righthand": {
                "rotation": [0, 45, 0],
                "translation": [0, 0, 0],
                "scale": [0.45, 0.45, 0.45]
            },
            "firstperson_lefthand": {
                "rotation": [0, 225, 0],
                "translation": [0, 0, 0],
                "scale": [0.45, 0.45, 0.45]
            }
        }
    }

def main():
    """Create better 3D models with multiple elements for more realistic shapes"""

    models_dir = "src/main/resources/assets/mtsofficialpack/models/item"

    # Item categories
    wheels = [
        "wheellarge", "wheellarge_gold", "wheellarge_goth", "wheellarge_holering",
        "wheellarge_holes", "wheellarge_legacy", "wheellarge_rusty", "wheellarge_spokes",
        "wheellarge_spokes2", "wheelmedium", "wheelsmall"
    ]

    engines = [
        "engineallison250", "engineamci4", "enginebristolmercury", "enginedetroitdiesel",
        "enginefordfe428", "enginefranklin0335", "enginelycomingo360", "enginemercedesm102",
        "enginepw610f"
    ]

    barrels = [
        "crate", "barrel", "barrel_black", "auxiliary_tank",
        "ammocrate_bomb_250", "ammocrate_rocket", "ammocrate_shell37_ap",
        "ammocrate_shell37_he", "ammocrate_shell37_prox", "aa_turret_37", "aa_turret_762"
    ]

    fixed_count = 0

    print("=== CREATING BETTER 3D MODELS ===")

    # Process wheels
    for item_name in wheels:
        model_path = os.path.join(models_dir, f"{item_name}.json")
        if os.path.exists(model_path):
            try:
                with open(model_path, 'r') as f:
                    model_data = json.load(f)

                texture_path = model_data["textures"]["layer0"]
                print(f"Creating better wheel model for {item_name}")

                new_model = create_wheel_3d_model(texture_path)

                with open(model_path, 'w') as f:
                    json.dump(new_model, f, indent=2)

                fixed_count += 1
            except Exception as e:
                print(f"Error processing {item_name}: {e}")

    # Process engines
    for item_name in engines:
        model_path = os.path.join(models_dir, f"{item_name}.json")
        if os.path.exists(model_path):
            try:
                with open(model_path, 'r') as f:
                    model_data = json.load(f)

                texture_path = model_data["textures"]["layer0"]
                print(f"Creating better engine model for {item_name}")

                new_model = create_engine_3d_model(texture_path)

                with open(model_path, 'w') as f:
                    json.dump(new_model, f, indent=2)

                fixed_count += 1
            except Exception as e:
                print(f"Error processing {item_name}: {e}")

    # Process barrels/crates
    for item_name in barrels:
        model_path = os.path.join(models_dir, f"{item_name}.json")
        if os.path.exists(model_path):
            try:
                with open(model_path, 'r') as f:
                    model_data = json.load(f)

                texture_path = model_data["textures"]["layer0"]
                print(f"Creating better barrel/crate model for {item_name}")

                new_model = create_barrel_3d_model(texture_path)

                with open(model_path, 'w') as f:
                    json.dump(new_model, f, indent=2)

                fixed_count += 1
            except Exception as e:
                print(f"Error processing {item_name}: {e}")

    print(f"\n=== RESULTS ===")
    print(f"Created {fixed_count} better 3D models")
    print(f"- Wheels: Multiple elements with flat orientation when dropped")
    print(f"- Engines: Complex rectangular shape with details")
    print(f"- Barrels/Crates: Tall container shapes")
    print(f"\nThese should look more 3D when dropped!")
    print(f"\nNOTE: Minecraft has fundamental limitations for dropped item rendering.")
    print(f"For true 3D models, items need to be placed as entities/blocks, not dropped as items.")

if __name__ == "__main__":
    main()