#!/usr/bin/env python3

import os
import json

def main():
    """Switch all complex OBJ items to simple 2D models for better GUI display"""

    models_dir = "src/main/resources/assets/mtsofficialpack/models/item"
    obj_dir = "src/main/resources/assets/mtsofficialpack/objmodels/parts"

    # Find all OBJ models (excluding handheld items and wheels)
    obj_models = []
    handheld_items = [
        "gunfireextinguisher", "gunflaregun", "gunconfetti", "gunm1919",
        "gunobserver", "gunrocketlauncher", "gunrocketpod", "gunft17turret"
    ]

    # Keep wheels as OBJ since they work well
    wheel_items = [
        "wheellarge", "wheellarge_nolegacy", "wheelmedium", "wheelsmall"
    ]

    if os.path.exists(obj_dir):
        for filename in os.listdir(obj_dir):
            if filename.endswith('.obj'):
                item_name = filename[:-4]
                if item_name not in handheld_items and item_name not in wheel_items:
                    obj_models.append(item_name)

    print(f"=== SWITCHING {len(obj_models)} COMPLEX ITEMS TO 2D MODELS ===")
    print("Keeping wheels as OBJ models since they work well")

    fixed_count = 0

    for item_name in obj_models:
        try:
            print(f"Converting {item_name} to 2D model")

            # Create clean 2D model with proper transforms
            simple_model = {
                "__comment": f"Clean 2D model for {item_name} - better GUI display",
                "parent": "item/generated",
                "textures": {
                    "layer0": f"mtsofficialpack:item/{item_name}"
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
                    },
                    "fixed": {
                        "rotation": [0, 0, 0],
                        "translation": [0, 0, 0],
                        "scale": [0.5, 0.5, 0.5]
                    }
                }
            }

            model_path = os.path.join(models_dir, f"{item_name}.json")
            with open(model_path, 'w') as f:
                json.dump(simple_model, f, indent=2)

            fixed_count += 1

        except Exception as e:
            print(f"Error converting {item_name}: {e}")

    print(f"\n=== RESULTS ===")
    print(f"Converted {fixed_count} complex items to 2D models")
    print(f"Benefits:")
    print(f"  - Clean, readable inventory icons")
    print(f"  - No weird 3D model artifacts in GUI")
    print(f"  - Consistent with Minecraft item display standards")
    print(f"  - Much better performance")
    print(f"\nItems still using OBJ models:")
    for wheel in wheel_items:
        print(f"  - {wheel} (wheels work well with OBJ)")

if __name__ == "__main__":
    main()