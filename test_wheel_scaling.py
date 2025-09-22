#!/usr/bin/env python3

import os
import json

def main():
    """Test different wheel scaling to match original 1.20.1 size"""

    models_dir = "src/main/resources/assets/mtsofficialpack/models/item"

    print("=== TESTING DIFFERENT WHEEL SCALES ===")

    # Test different scales to find the right size
    test_scales = [
        {"name": "small", "ground": 0.75, "gui": 0.6},      # Current
        {"name": "medium", "ground": 1.0, "gui": 0.7},     # Larger
        {"name": "large", "ground": 1.25, "gui": 0.8},     # Much larger
        {"name": "xlarge", "ground": 1.5, "gui": 0.9},     # Even larger
    ]

    for scale_test in test_scales:
        scale_name = scale_test["name"]
        ground_scale = scale_test["ground"]
        gui_scale = scale_test["gui"]

        print(f"Creating {scale_name} scale test (ground: {ground_scale}, gui: {gui_scale})")

        # Create test wheel model
        wheel_model = {
            "__comment": f"Test wheel scaling - {scale_name} (ground: {ground_scale})",
            "loader": "neoforge:obj",
            "model": "mtsofficialpack:objmodels/parts/wheellarge.obj",
            "textures": {
                "texture0": "mtsofficialpack:item/wheellarge",
                "particle": "mtsofficialpack:item/wheellarge"
            },
            "display": {
                "gui": {
                    "rotation": [30, 45, 0],
                    "translation": [0, 0, 0],
                    "scale": [gui_scale, gui_scale, gui_scale]
                },
                "ground": {
                    "rotation": [0, 0, 90],
                    "translation": [0, 1, 0],
                    "scale": [ground_scale, ground_scale, ground_scale]
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

        # Write test model
        test_path = os.path.join(models_dir, f"wheellarge_test_{scale_name}.json")
        with open(test_path, 'w') as f:
            json.dump(wheel_model, f, indent=2)

        print(f"  Created: wheellarge_test_{scale_name}.json")

    print(f"\n=== TEST INSTRUCTIONS ===")
    print(f"1. Build and test the content pack")
    print(f"2. Try each test wheel in creative inventory:")
    print(f"   - wheellarge_test_small  (current size)")
    print(f"   - wheellarge_test_medium (larger)")
    print(f"   - wheellarge_test_large  (much larger)")
    print(f"   - wheellarge_test_xlarge (even larger)")
    print(f"3. Drop them on ground and compare to original 1.20.1 size")
    print(f"4. Let me know which scale looks closest to original")

    # Also create a version with alternative texture mapping approach
    print(f"\n=== CREATING ALTERNATIVE TEXTURE MAPPING TEST ===")

    alt_model = {
        "__comment": "Alternative texture mapping test - using particle texture",
        "loader": "neoforge:obj",
        "model": "mtsofficialpack:objmodels/parts/wheellarge.obj",
        "textures": {
            "particle": "mtsofficialpack:item/wheellarge"
        },
        "display": {
            "gui": {
                "rotation": [30, 45, 0],
                "translation": [0, 0, 0],
                "scale": [0.7, 0.7, 0.7]
            },
            "ground": {
                "rotation": [0, 0, 90],
                "translation": [0, 1, 0],
                "scale": [1.0, 1.0, 1.0]
            }
        }
    }

    alt_path = os.path.join(models_dir, "wheellarge_test_alt_texture.json")
    with open(alt_path, 'w') as f:
        json.dump(alt_model, f, indent=2)

    print("Created wheellarge_test_alt_texture.json (particle texture only)")

    # Create MTL using particle reference
    alt_mtl = """# Alternative MTL test - using particle texture

newmtl none
Ka 1.000000 1.000000 1.000000
Kd 1.000000 1.000000 1.000000
Ks 0.000000 0.000000 0.000000
Ns 0.000000
map_Kd #particle

newmtl material0
Ka 1.000000 1.000000 1.000000
Kd 1.000000 1.000000 1.000000
Ks 0.000000 0.000000 0.000000
Ns 0.000000
map_Kd #particle
"""

    alt_mtl_path = "src/main/resources/assets/mtsofficialpack/objmodels/parts/wheellarge_alt.mtl"
    with open(alt_mtl_path, 'w') as f:
        f.write(alt_mtl)

    print("Created wheellarge_alt.mtl (using #particle reference)")

if __name__ == "__main__":
    main()