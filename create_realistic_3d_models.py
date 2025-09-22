#!/usr/bin/env python3

import os
import json

def create_wheel_model(texture_path):
    """Create a wheel-like cylindrical model"""
    return {
        "textures": {
            "side": texture_path,
            "front": texture_path,
            "particle": texture_path
        },
        "elements": [
            # Main wheel cylinder (thicker)
            {
                "from": [4, 6, 4],
                "to": [12, 10, 12],
                "faces": {
                    "down":  {"texture": "#front", "cullface": "down"},
                    "up":    {"texture": "#front", "cullface": "up"},
                    "north": {"texture": "#side"},
                    "south": {"texture": "#side"},
                    "west":  {"texture": "#side"},
                    "east":  {"texture": "#side"}
                }
            },
            # Inner rim detail
            {
                "from": [5, 5, 5],
                "to": [11, 11, 11],
                "faces": {
                    "down":  {"texture": "#front"},
                    "up":    {"texture": "#front"},
                    "north": {"texture": "#side"},
                    "south": {"texture": "#side"},
                    "west":  {"texture": "#side"},
                    "east":  {"texture": "#side"}
                }
            }
        ],
        "display": {
            "ground": {
                "rotation": [0, 0, 90],  # Lay wheel flat on ground
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
                "scale": [0.5, 0.5, 0.5]
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
                "scale": [0.5, 0.5, 0.5]
            },
            "firstperson_lefthand": {
                "rotation": [0, 225, 0],
                "translation": [0, 0, 0],
                "scale": [0.5, 0.5, 0.5]
            }
        }
    }

def create_engine_model(texture_path):
    """Create an engine-like rectangular model"""
    return {
        "textures": {
            "texture": texture_path,
            "particle": texture_path
        },
        "elements": [
            # Main engine block
            {
                "from": [3, 5, 5],
                "to": [13, 11, 11],
                "faces": {
                    "down":  {"texture": "#texture"},
                    "up":    {"texture": "#texture"},
                    "north": {"texture": "#texture"},
                    "south": {"texture": "#texture"},
                    "west":  {"texture": "#texture"},
                    "east":  {"texture": "#texture"}
                }
            },
            # Engine detail/exhaust
            {
                "from": [2, 7, 7],
                "to": [4, 9, 9],
                "faces": {
                    "down":  {"texture": "#texture"},
                    "up":    {"texture": "#texture"},
                    "north": {"texture": "#texture"},
                    "south": {"texture": "#texture"},
                    "west":  {"texture": "#texture"},
                    "east":  {"texture": "#texture"}
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
                "rotation": [30, 45, 0],
                "translation": [0, 0, 0],
                "scale": [0.6, 0.6, 0.6]
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
                "scale": [0.4, 0.4, 0.4]
            },
            "firstperson_lefthand": {
                "rotation": [0, 225, 0],
                "translation": [0, 0, 0],
                "scale": [0.4, 0.4, 0.4]
            }
        }
    }

def create_barrel_model(texture_path):
    """Create a barrel/crate-like cylindrical model"""
    return {
        "textures": {
            "texture": texture_path,
            "particle": texture_path
        },
        "elements": [
            # Main barrel body
            {
                "from": [5, 4, 5],
                "to": [11, 12, 11],
                "faces": {
                    "down":  {"texture": "#texture"},
                    "up":    {"texture": "#texture"},
                    "north": {"texture": "#texture"},
                    "south": {"texture": "#texture"},
                    "west":  {"texture": "#texture"},
                    "east":  {"texture": "#texture"}
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
                "rotation": [30, 45, 0],
                "translation": [0, 0, 0],
                "scale": [0.6, 0.6, 0.6]
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
                "scale": [0.4, 0.4, 0.4]
            },
            "firstperson_lefthand": {
                "rotation": [0, 225, 0],
                "translation": [0, 0, 0],
                "scale": [0.4, 0.4, 0.4]
            }
        }
    }

def create_turret_model(texture_path):
    """Create a turret-like model with base and barrel"""
    return {
        "textures": {
            "texture": texture_path,
            "particle": texture_path
        },
        "elements": [
            # Turret base
            {
                "from": [4, 4, 4],
                "to": [12, 8, 12],
                "faces": {
                    "down":  {"texture": "#texture"},
                    "up":    {"texture": "#texture"},
                    "north": {"texture": "#texture"},
                    "south": {"texture": "#texture"},
                    "west":  {"texture": "#texture"},
                    "east":  {"texture": "#texture"}
                }
            },
            # Turret barrel
            {
                "from": [7, 6, 2],
                "to": [9, 8, 14],
                "faces": {
                    "down":  {"texture": "#texture"},
                    "up":    {"texture": "#texture"},
                    "north": {"texture": "#texture"},
                    "south": {"texture": "#texture"},
                    "west":  {"texture": "#texture"},
                    "east":  {"texture": "#texture"}
                }
            }
        ],
        "display": {
            "ground": {
                "rotation": [0, 45, 0],
                "translation": [0, 2, 0],
                "scale": [0.5, 0.5, 0.5]
            },
            "gui": {
                "rotation": [30, 45, 0],
                "translation": [0, 0, 0],
                "scale": [0.6, 0.6, 0.6]
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
                "scale": [0.4, 0.4, 0.4]
            },
            "firstperson_lefthand": {
                "rotation": [0, 225, 0],
                "translation": [0, 0, 0],
                "scale": [0.4, 0.4, 0.4]
            }
        }
    }

def main():
    """Create realistic 3D models that actually look like the items they represent"""

    models_dir = "src/main/resources/assets/mtsofficialpack/models/item"

    # Define item categories with their appropriate models
    item_categories = {
        "wheel": [
            "wheellarge", "wheellarge_gold", "wheellarge_goth", "wheellarge_holering",
            "wheellarge_holes", "wheellarge_legacy", "wheellarge_rusty", "wheellarge_spokes",
            "wheellarge_spokes2", "wheelmedium", "wheelsmall"
        ],
        "engine": [
            "engineallison250", "engineamci4", "enginebristolmercury", "enginedetroitdiesel",
            "enginefordfe428", "enginefranklin0335", "enginelycomingo360", "enginemercedesm102",
            "enginepw610f"
        ],
        "barrel": [
            "crate", "barrel", "barrel_black", "auxiliary_tank",
            "ammocrate_bomb_250", "ammocrate_rocket", "ammocrate_shell37_ap",
            "ammocrate_shell37_he", "ammocrate_shell37_prox"
        ],
        "turret": [
            "aa_turret_37", "aa_turret_762", "aa_base", "barrelbell47g",
            "barrel_blank", "barrel_blank_s"
        ],
        "engine": [  # Add bulldozers to engine category for now
            "bulldozer_green", "bulldozer_blue", "bulldozer_sand", "dozerblade"
        ]
    }

    fixed_count = 0

    print("=== CREATING REALISTIC 3D MODELS ===")

    for category, items in item_categories.items():
        print(f"\nProcessing {category} items...")

        for item_name in items:
            model_path = os.path.join(models_dir, f"{item_name}.json")

            if os.path.exists(model_path):
                try:
                    with open(model_path, 'r') as f:
                        model_data = json.load(f)

                    # Get the texture path
                    if "textures" in model_data and "texture" in model_data["textures"]:
                        texture_path = model_data["textures"]["texture"]
                    elif "textures" in model_data and "layer0" in model_data["textures"]:
                        texture_path = model_data["textures"]["layer0"]
                    else:
                        print(f"Could not find texture for {item_name}, skipping")
                        continue

                    print(f"Creating {category} model for {item_name}")

                    # Create appropriate model based on category
                    if category == "wheel":
                        new_model = create_wheel_model(texture_path)
                    elif category == "engine":
                        new_model = create_engine_model(texture_path)
                    elif category == "barrel":
                        new_model = create_barrel_model(texture_path)
                    elif category == "turret":
                        new_model = create_turret_model(texture_path)
                    else:
                        continue

                    with open(model_path, 'w') as f:
                        json.dump(new_model, f, indent=2)

                    fixed_count += 1

                except Exception as e:
                    print(f"Error processing {item_name}: {e}")

    print(f"\n=== RESULTS ===")
    print(f"Created {fixed_count} realistic 3D models")
    print(f"- Wheels: Cylindrical shape that lays flat when dropped")
    print(f"- Engines: Rectangular blocks with details")
    print(f"- Barrels/Crates: Tall cylindrical containers")
    print(f"- Turrets: Base with protruding barrel")
    print(f"\nNow items should look like actual wheels, engines, etc. when dropped!")

if __name__ == "__main__":
    main()