#!/usr/bin/env python3

import os
import json

def main():
    """Fix wheel pivot/centering issues for proper GUI and hand display"""

    models_dir = "src/main/resources/assets/mtsofficialpack/models/item"

    # Wheels with OBJ models
    wheel_models = ["wheellarge", "wheellarge_nolegacy", "wheelmedium", "wheelsmall"]

    print(f"=== FIXING WHEEL PIVOT/CENTERING ISSUES ===")

    for wheel in wheel_models:
        try:
            print(f"Fixing centering for {wheel}")

            # Create wheel model with proper centering transforms
            wheel_model = {
                "__comment": f"Centered NeoForge OBJ model for {wheel} - fixed pivot issues",
                "loader": "neoforge:obj",
                "model": f"mtsofficialpack:objmodels/parts/{wheel}.obj",
                "textures": {
                    "texture0": f"mtsofficialpack:item/{wheel}",
                    "particle": f"mtsofficialpack:item/{wheel}"
                },
                "display": {
                    "gui": {
                        "rotation": [30, 45, 0],
                        "translation": [0, 1, 0],  # Slight up translation for centering
                        "scale": [0.6, 0.6, 0.6]
                    },
                    "ground": {
                        "rotation": [0, 0, 90],  # Lay flat
                        "translation": [0, 1, 0],
                        "scale": [1.0, 1.0, 1.0]  # Larger ground size
                    },
                    "fixed": {
                        "rotation": [0, 0, 0],
                        "translation": [0, 0, 0],
                        "scale": [0.5, 0.5, 0.5]
                    },
                    "thirdperson_righthand": {
                        "rotation": [75, 45, 0],
                        "translation": [0, 3, 0],  # Better hand positioning
                        "scale": [0.4, 0.4, 0.4]
                    },
                    "thirdperson_lefthand": {
                        "rotation": [75, 225, 0],
                        "translation": [0, 3, 0],  # Better hand positioning
                        "scale": [0.4, 0.4, 0.4]
                    },
                    "firstperson_righthand": {
                        "rotation": [0, 45, 0],
                        "translation": [1, 1, 0],  # Center in first person view
                        "scale": [0.5, 0.5, 0.5]
                    },
                    "firstperson_lefthand": {
                        "rotation": [0, 225, 0],
                        "translation": [1, 1, 0],  # Center in first person view
                        "scale": [0.5, 0.5, 0.5]
                    }
                }
            }

            # Write updated model
            model_path = os.path.join(models_dir, f"{wheel}.json")
            with open(model_path, 'w') as f:
                json.dump(wheel_model, f, indent=2)

            print(f"  Fixed centering for {wheel}.json")

        except Exception as e:
            print(f"  Error fixing {wheel}: {e}")

    print(f"\n=== RESULTS ===")
    print(f"Applied centering fixes:")
    print(f"  - GUI: Added Y translation (0, 1, 0) to center in inventory")
    print(f"  - Ground: Increased scale to 1.0 (closer to original size)")
    print(f"  - Third person: Better hand positioning (Y: 3)")
    print(f"  - First person: Centered view (1, 1, 0)")
    print(f"")
    print(f"This should fix:")
    print(f"  - Wheel appearing in corner of GUI slot")
    print(f"  - Wrong rotation pivot point")
    print(f"  - Better visibility when holding in hand")

if __name__ == "__main__":
    main()