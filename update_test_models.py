#!/usr/bin/env python3

import os
import json

def main():
    """Update test model files to reference correct OBJ files"""

    models_dir = "src/main/resources/assets/mtsofficialpack/models/item"

    tests = [
        ("wheellarge_test2_minimal", "Test 2: Particle texture reference - should show wheel texture"),
        ("wheellarge_test3_flipv", "Test 3: Texture0 + FlipV - should show wheel texture"),
        ("wheellarge_test4_bigtrans", "Test 4: RED solid color - should show RED wheel")
    ]

    for test_name, comment in tests:
        model_path = os.path.join(models_dir, f"{test_name}.json")

        # Read current model
        with open(model_path, 'r') as f:
            model = json.load(f)

        # Update model reference and comment
        model["model"] = f"mtsofficialpack:objmodels/parts/{test_name}.obj"
        model["__comment"] = comment

        # Write updated model
        with open(model_path, 'w') as f:
            json.dump(model, f, indent=2)

        print(f"Updated {test_name}.json")

    print("All test models updated!")

if __name__ == "__main__":
    main()