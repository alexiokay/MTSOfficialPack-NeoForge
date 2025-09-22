#!/usr/bin/env python3

import os
import json

def main():
    """Fix wheel OBJ models with proper NeoForge 1.21.1 implementation"""

    models_dir = "src/main/resources/assets/mtsofficialpack/models/item"
    obj_dir = "src/main/resources/assets/mtsofficialpack/objmodels/parts"

    # Find wheels with OBJ models
    wheel_models = ["wheellarge", "wheellarge_nolegacy", "wheelmedium", "wheelsmall"]

    print(f"=== FIXING {len(wheel_models)} WHEEL OBJ MODELS WITH PROPER NEOFORGE IMPLEMENTATION ===")

    for wheel in wheel_models:
        try:
            print(f"Fixing {wheel} with proper NeoForge implementation")

            # Create proper NeoForge OBJ model according to documentation
            wheel_model = {
                "__comment": f"Proper NeoForge 1.21.1 OBJ model for {wheel}",
                "loader": "neoforge:obj",
                "model": f"mtsofficialpack:objmodels/parts/{wheel}.obj",
                "textures": {
                    "texture0": f"mtsofficialpack:item/{wheel}",
                    "particle": f"mtsofficialpack:item/{wheel}"
                },
                "display": {
                    "gui": {
                        "rotation": [30, 45, 0],
                        "translation": [0, 0, 0],
                        "scale": [0.6, 0.6, 0.6]  # Larger for GUI
                    },
                    "ground": {
                        "rotation": [0, 0, 90],  # Lay flat like real wheel
                        "translation": [0, 1, 0],
                        "scale": [0.75, 0.75, 0.75]  # Closer to original size
                    },
                    "fixed": {
                        "rotation": [0, 0, 0],
                        "translation": [0, 0, 0],
                        "scale": [0.5, 0.5, 0.5]  # Item frames
                    },
                    "thirdperson_righthand": {
                        "rotation": [75, 45, 0],
                        "translation": [0, 2.5, 0],
                        "scale": [0.4, 0.4, 0.4]  # Hand holding
                    },
                    "thirdperson_lefthand": {
                        "rotation": [75, 225, 0],
                        "translation": [0, 2.5, 0],
                        "scale": [0.4, 0.4, 0.4]  # Hand holding
                    },
                    "firstperson_righthand": {
                        "rotation": [0, 45, 0],
                        "translation": [0, 0, 0],
                        "scale": [0.5, 0.5, 0.5]  # First person
                    },
                    "firstperson_lefthand": {
                        "rotation": [0, 225, 0],
                        "translation": [0, 0, 0],
                        "scale": [0.5, 0.5, 0.5]  # First person
                    }
                }
            }

            # Write updated model
            model_path = os.path.join(models_dir, f"{wheel}.json")
            with open(model_path, 'w') as f:
                json.dump(wheel_model, f, indent=2)

            # Create proper MTL file with texture references
            mtl_content = f"""# MTL file for {wheel}
# Proper NeoForge 1.21.1 texture mapping

newmtl none
Ka 1.000000 1.000000 1.000000
Kd 1.000000 1.000000 1.000000
Ks 0.000000 0.000000 0.000000
Ns 0.000000
map_Kd #texture0

newmtl material0
Ka 1.000000 1.000000 1.000000
Kd 1.000000 1.000000 1.000000
Ks 0.000000 0.000000 0.000000
Ns 0.000000
map_Kd #texture0
"""

            mtl_path = os.path.join(obj_dir, f"{wheel}.mtl")
            with open(mtl_path, 'w') as f:
                f.write(mtl_content)

            print(f"  ✅ Fixed {wheel}.json and {wheel}.mtl")

        except Exception as e:
            print(f"  ❌ Error fixing {wheel}: {e}")

    print(f"\n=== RESULTS ===")
    print(f"✅ Applied proper NeoForge 1.21.1 OBJ implementation to all wheels")
    print(f"Changes made:")
    print(f"  - Added 'texture0' definition in JSON models")
    print(f"  - Updated MTL files to use #texture0 references")
    print(f"  - Increased ground scale to 0.75 (closer to original size)")
    print(f"  - Improved scaling for all display contexts")
    print(f"")
    print(f"This should fix:")
    print(f"  ✅ Broken textures (proper MTL mapping)")
    print(f"  ✅ Small wheel size (increased to 0.75 scale)")
    print(f"  ✅ Proper rotation when dropped")

if __name__ == "__main__":
    main()