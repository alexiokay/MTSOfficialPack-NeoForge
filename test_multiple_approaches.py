#!/usr/bin/env python3

import os
import json

def main():
    """Test multiple approaches for texture mapping and centering"""

    models_dir = "src/main/resources/assets/mtsofficialpack/models/item"
    obj_dir = "src/main/resources/assets/mtsofficialpack/objmodels/parts"

    print("=== CREATING MULTIPLE TEST APPROACHES ===")

    # Approach 1: Direct texture paths in MTL + different GUI translation
    approach1 = {
        "__comment": "Test 1: Direct MTL texture paths + centered GUI",
        "loader": "neoforge:obj",
        "model": "mtsofficialpack:objmodels/parts/wheellarge.obj",
        "textures": {
            "particle": "mtsofficialpack:item/wheellarge"
        },
        "display": {
            "gui": {
                "rotation": [30, 45, 0],
                "translation": [0, 0, 0],
                "scale": [0.6, 0.6, 0.6]
            },
            "ground": {
                "rotation": [0, 0, 90],
                "translation": [0, 1, 0],
                "scale": [1.0, 1.0, 1.0]
            }
        }
    }

    # Approach 2: Only particle texture + no extra parameters
    approach2 = {
        "__comment": "Test 2: Minimal config with only particle texture",
        "loader": "neoforge:obj",
        "model": "mtsofficialpack:objmodels/parts/wheellarge.obj",
        "textures": {
            "particle": "mtsofficialpack:item/wheellarge"
        },
        "display": {
            "gui": {
                "rotation": [0, 0, 0],
                "translation": [0, 0, 0],
                "scale": [1.0, 1.0, 1.0]
            },
            "ground": {
                "rotation": [0, 0, 90],
                "translation": [0, 1, 0],
                "scale": [1.0, 1.0, 1.0]
            }
        }
    }

    # Approach 3: Try with different MTL material name
    approach3 = {
        "__comment": "Test 3: Using texture0 with flip_v and automatic_culling",
        "loader": "neoforge:obj",
        "model": "mtsofficialpack:objmodels/parts/wheellarge.obj",
        "flip_v": True,
        "automatic_culling": False,
        "textures": {
            "texture0": "mtsofficialpack:item/wheellarge",
            "particle": "mtsofficialpack:item/wheellarge"
        },
        "display": {
            "gui": {
                "rotation": [30, 45, 0],
                "translation": [0, 0, 0],
                "scale": [0.6, 0.6, 0.6]
            },
            "ground": {
                "rotation": [0, 0, 90],
                "translation": [0, 1, 0],
                "scale": [1.0, 1.0, 1.0]
            }
        }
    }

    # Approach 4: Big GUI translation to see if centering works
    approach4 = {
        "__comment": "Test 4: Large translation values to test centering",
        "loader": "neoforge:obj",
        "model": "mtsofficialpack:objmodels/parts/wheellarge.obj",
        "textures": {
            "particle": "mtsofficialpack:item/wheellarge"
        },
        "display": {
            "gui": {
                "rotation": [30, 45, 0],
                "translation": [4, 4, 0],
                "scale": [0.6, 0.6, 0.6]
            },
            "ground": {
                "rotation": [0, 0, 90],
                "translation": [0, 1, 0],
                "scale": [1.0, 1.0, 1.0]
            }
        }
    }

    approaches = [
        ("test1_direct_mtl", approach1),
        ("test2_minimal", approach2),
        ("test3_flipv", approach3),
        ("test4_bigtrans", approach4)
    ]

    for name, config in approaches:
        # Write test model
        test_path = os.path.join(models_dir, f"wheellarge_{name}.json")
        with open(test_path, 'w') as f:
            json.dump(config, f, indent=2)
        print(f"Created: wheellarge_{name}.json")

    # Create MTL files for different texture approaches
    print(f"\n=== CREATING TEST MTL FILES ===")

    # MTL 1: Direct paths (current)
    mtl1 = """# Test MTL 1: Direct texture paths
newmtl none
Ka 1.000000 1.000000 1.000000
Kd 1.000000 1.000000 1.000000
Ks 0.000000 0.000000 0.000000
Ns 0.000000
map_Kd mtsofficialpack:item/wheellarge
"""

    # MTL 2: Using #particle reference
    mtl2 = """# Test MTL 2: Particle texture reference
newmtl none
Ka 1.000000 1.000000 1.000000
Kd 1.000000 1.000000 1.000000
Ks 0.000000 0.000000 0.000000
Ns 0.000000
map_Kd #particle
"""

    # MTL 3: Using #texture0 reference
    mtl3 = """# Test MTL 3: texture0 reference
newmtl none
Ka 1.000000 1.000000 1.000000
Kd 1.000000 1.000000 1.000000
Ks 0.000000 0.000000 0.000000
Ns 0.000000
map_Kd #texture0
"""

    # MTL 4: No texture mapping (solid color)
    mtl4 = """# Test MTL 4: No texture mapping
newmtl none
Ka 1.000000 0.000000 0.000000
Kd 1.000000 0.000000 0.000000
Ks 0.000000 0.000000 0.000000
Ns 0.000000
"""

    mtl_tests = [
        ("wheellarge_test1.mtl", mtl1),
        ("wheellarge_test2.mtl", mtl2),
        ("wheellarge_test3.mtl", mtl3),
        ("wheellarge_test4.mtl", mtl4)
    ]

    for filename, content in mtl_tests:
        mtl_path = os.path.join(obj_dir, filename)
        with open(mtl_path, 'w') as f:
            f.write(content)
        print(f"Created: {filename}")

    print(f"\n=== TEST INSTRUCTIONS ===")
    print(f"1. Test each wheel variant:")
    print(f"   - wheellarge_test1_direct_mtl")
    print(f"   - wheellarge_test2_minimal")
    print(f"   - wheellarge_test3_flipv")
    print(f"   - wheellarge_test4_bigtrans")
    print(f"")
    print(f"2. Also manually copy test MTL files over wheellarge.mtl to test:")
    print(f"   - wheellarge_test1.mtl (direct paths)")
    print(f"   - wheellarge_test2.mtl (#particle)")
    print(f"   - wheellarge_test3.mtl (#texture0)")
    print(f"   - wheellarge_test4.mtl (red solid color)")
    print(f"")
    print(f"3. Look for:")
    print(f"   - Which approach shows textures correctly")
    print(f"   - Which translation values center the wheel properly")
    print(f"   - Test4 should show red color if MTL is working at all")

if __name__ == "__main__":
    main()