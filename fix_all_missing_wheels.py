#!/usr/bin/env python3

import os
import json

def main():
    """Fix all wheel variants that weren't properly set up with OBJ models"""

    models_dir = "src/main/resources/assets/mtsofficialpack/models/item"
    obj_dir = "src/main/resources/assets/mtsofficialpack/objmodels/parts"

    # Find all wheel models in models/item directory
    all_wheel_models = []
    if os.path.exists(models_dir):
        for filename in os.listdir(models_dir):
            if filename.startswith('wheel') and filename.endswith('.json'):
                item_name = filename[:-5]  # Remove .json
                all_wheel_models.append(item_name)

    # Find which ones have OBJ models
    obj_wheels = []
    if os.path.exists(obj_dir):
        for filename in os.listdir(obj_dir):
            if filename.startswith('wheel') and filename.endswith('.obj'):
                item_name = filename[:-4]  # Remove .obj
                obj_wheels.append(item_name)

    print(f"Found {len(all_wheel_models)} wheel model files")
    print(f"Found {len(obj_wheels)} wheel OBJ files")

    # Check which wheels don't have OBJ models and need simple 2D fallback
    wheels_without_obj = []
    wheels_with_obj = []

    for wheel in all_wheel_models:
        if wheel in obj_wheels:
            wheels_with_obj.append(wheel)
        else:
            wheels_without_obj.append(wheel)

    print(f"\nWheels WITH OBJ models: {len(wheels_with_obj)}")
    for wheel in wheels_with_obj:
        print(f"  - {wheel}")

    print(f"\nWheels WITHOUT OBJ models: {len(wheels_without_obj)}")
    for wheel in wheels_without_obj:
        print(f"  - {wheel}")

    # Fix wheels with OBJ models
    print(f"\n=== FIXING WHEELS WITH OBJ MODELS ===")
    for wheel in wheels_with_obj:
        try:
            print(f"Setting up OBJ model for {wheel}")

            # Create proper wheel OBJ model with scaling
            wheel_model = {
                "__comment": f"Properly scaled NeoForge OBJ model for {wheel}",
                "loader": "neoforge:obj",
                "model": f"mtsofficialpack:objmodels/parts/{wheel}.obj",
                "textures": {
                    "particle": f"mtsofficialpack:item/{wheel}"
                },
                "display": {
                    "gui": {
                        "rotation": [30, 45, 0],
                        "translation": [0, 0, 0],
                        "scale": [0.5, 0.5, 0.5]  # Good size for GUI
                    },
                    "ground": {
                        "rotation": [0, 0, 90],  # Lay flat like a real wheel
                        "translation": [0, 1, 0],
                        "scale": [0.3, 0.3, 0.3]  # Reasonable size when dropped
                    },
                    "fixed": {
                        "rotation": [0, 0, 0],
                        "translation": [0, 0, 0],
                        "scale": [0.25, 0.25, 0.25]
                    },
                    "thirdperson_righthand": {
                        "rotation": [75, 45, 0],
                        "translation": [0, 2.5, 0],
                        "scale": [0.25, 0.25, 0.25]
                    },
                    "thirdperson_lefthand": {
                        "rotation": [75, 225, 0],
                        "translation": [0, 2.5, 0],
                        "scale": [0.25, 0.25, 0.25]
                    },
                    "firstperson_righthand": {
                        "rotation": [0, 45, 0],
                        "translation": [0, 0, 0],
                        "scale": [0.3, 0.3, 0.3]
                    },
                    "firstperson_lefthand": {
                        "rotation": [0, 225, 0],
                        "translation": [0, 0, 0],
                        "scale": [0.3, 0.3, 0.3]
                    }
                }
            }

            model_path = os.path.join(models_dir, f"{wheel}.json")
            with open(model_path, 'w') as f:
                json.dump(wheel_model, f, indent=2)

            print(f"  Fixed: {wheel}.json")

        except Exception as e:
            print(f"Error fixing {wheel}: {e}")

    # Fix wheels without OBJ models (use 2D)
    print(f"\n=== FIXING WHEELS WITHOUT OBJ MODELS (2D) ===")
    for wheel in wheels_without_obj:
        try:
            print(f"Setting up 2D model for {wheel}")

            # Create simple 2D model
            simple_model = {
                "__comment": f"2D model for {wheel} - no OBJ model available",
                "parent": "item/generated",
                "textures": {
                    "layer0": f"mtsofficialpack:item/{wheel}"
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
                    "thirdperson_righthand": {
                        "rotation": [75, 45, 0],
                        "translation": [0, 2.5, 0],
                        "scale": [0.375, 0.375, 0.375]
                    },
                    "thirdperson_lefthand": {
                        "rotation": [75, 225, 0],
                        "translation": [0, 2.5, 0],
                        "scale": [0.375, 0.375, 0.375]
                    }
                }
            }

            model_path = os.path.join(models_dir, f"{wheel}.json")
            with open(model_path, 'w') as f:
                json.dump(simple_model, f, indent=2)

            print(f"  Fixed: {wheel}.json (2D)")

        except Exception as e:
            print(f"Error fixing {wheel}: {e}")

    print(f"\n=== RESULTS ===")
    print(f"Fixed {len(wheels_with_obj)} wheels with OBJ models (3D)")
    print(f"Fixed {len(wheels_without_obj)} wheels without OBJ models (2D)")
    print(f"All wheels should now be properly sized!")

if __name__ == "__main__":
    main()