#!/usr/bin/env python3

import os
import json

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

def main():
    """Fix the actual engine items that were missed"""

    models_dir = "src/main/resources/assets/mtsofficialpack/models/item"

    # Actual engine items
    engine_items = [
        "engineallison250", "engineamci4", "enginebristolmercury", "enginedetroitdiesel",
        "enginefordfe428", "enginefranklin0335", "enginelycomingo360", "enginemercedesm102",
        "enginepw610f"
    ]

    fixed_count = 0

    print("=== FIXING ACTUAL ENGINE MODELS ===")

    for item_name in engine_items:
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

                print(f"Creating engine model for {item_name}")

                new_model = create_engine_model(texture_path)

                with open(model_path, 'w') as f:
                    json.dump(new_model, f, indent=2)

                fixed_count += 1

            except Exception as e:
                print(f"Error processing {item_name}: {e}")

    print(f"\n=== RESULTS ===")
    print(f"Fixed {fixed_count} engine models")
    print(f"Engines now have rectangular block shape with detail piece")

if __name__ == "__main__":
    main()