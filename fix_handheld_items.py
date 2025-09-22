#!/usr/bin/env python3

import os
import json

def main():
    """Fix handheld items that have custom MTS rendering by reverting to 2D models"""

    models_dir = "src/main/resources/assets/mtsofficialpack/models/item"
    items_dir = "src/main/resources/assets/mtsofficialpack/items"

    # Items that have custom MTS handheld rendering and should NOT use OBJ models
    handheld_items = [
        "gunfireextinguisher",  # Fire extinguisher - has custom hand rendering
        "gunflaregun",          # Flare gun - has custom hand rendering
        "gunconfetti",          # Confetti gun - likely has custom rendering
        "gunm1919",             # Machine gun - likely has custom rendering
        "gunobserver",          # Observer gun - likely has custom rendering
        "gunrocketlauncher",    # Rocket launcher - likely has custom rendering
        "gunrocketpod",         # Rocket pod - likely has custom rendering
        "gunft17turret"         # Turret gun - likely has custom rendering
    ]

    print(f"=== FIXING HANDHELD ITEMS WITH CUSTOM MTS RENDERING ===")

    fixed_count = 0

    for item_name in handheld_items:
        try:
            print(f"Reverting {item_name} to 2D rendering")

            # Create simple 2D model for items with custom MTS rendering
            model_path = os.path.join(models_dir, f"{item_name}.json")

            simple_2d_model = {
                "__comment": f"2D model for {item_name} - has custom MTS handheld rendering",
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
                json.dump(simple_2d_model, f, indent=2)

            # Remove item definition to avoid conflicts
            items_path = os.path.join(items_dir, f"{item_name}.json")
            if os.path.exists(items_path):
                os.remove(items_path)
                print(f"  Removed conflicting item definition: {item_name}.json")

            print(f"  Reverted to 2D model: {item_name}.json")
            fixed_count += 1

        except Exception as e:
            print(f"Error fixing {item_name}: {e}")

    print(f"\n=== RESULTS ===")
    print(f"Fixed {fixed_count} handheld items")
    print(f"These items now use 2D models and won't conflict with MTS custom rendering")
    print(f"Purple/black cubes should be gone for these items!")

    # Also list other potential handheld items to check
    potential_handheld = [
        "drill",           # Tools might have custom rendering
        "watercannon",     # Water cannon might be handheld
        "spotlight"        # Spotlight might be handheld
    ]

    print(f"\nPotential other handheld items to check:")
    for item in potential_handheld:
        print(f"  - {item}")

    print(f"\nIf any other items show dual rendering, add them to the handheld_items list")

if __name__ == "__main__":
    main()