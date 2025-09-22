#!/usr/bin/env python3

import os
import json
import shutil

def main():
    """Fix items that have 3D models but are using 2D generated models"""

    models_dir = "src/main/resources/assets/mtsofficialpack/models/item"
    parts_dir = os.path.join(models_dir, "parts")

    # Find all existing 3D models in parts directory
    existing_3d_models = {}
    if os.path.exists(parts_dir):
        for filename in os.listdir(parts_dir):
            if filename.endswith('.json'):
                item_name = filename[:-5]  # Remove .json
                existing_3d_models[item_name] = os.path.join(parts_dir, filename)
                print(f"Found 3D model: {item_name}")

    print(f"Found {len(existing_3d_models)} existing 3D models")

    # Find generated 2D models that should use 3D instead
    fixed_count = 0

    for item_name, parts_path in existing_3d_models.items():
        # Check if there's a 2D model in root that should be replaced
        root_model_path = os.path.join(models_dir, f"{item_name}.json")

        if os.path.exists(root_model_path):
            # Read the root model to see if it's a simple generated one
            try:
                with open(root_model_path, 'r') as f:
                    model_data = json.load(f)

                # Check if it's a simple generated model
                if (model_data.get("parent") == "item/generated" and
                    "elements" not in model_data):

                    print(f"Replacing 2D model for {item_name} with 3D redirect")

                    # Delete the 2D model
                    os.remove(root_model_path)

                    # Copy the 3D model to root location
                    shutil.copy2(parts_path, root_model_path)

                    fixed_count += 1

            except Exception as e:
                print(f"Error processing {item_name}: {e}")

    print(f"\nFixed {fixed_count} models to use 3D instead of 2D")

    # Also check for items that might need models but don't have them
    missing_items = [
        "gunflaregun", "drill", "bulldozer_green", "bulldozer_blue", "bulldozer_sand",
        "dozerblade", "truck_yellow", "truck_silver", "truck_blue", "truck_red"
    ]

    print(f"\nChecking for missing models...")
    for item_name in missing_items:
        root_model_path = os.path.join(models_dir, f"{item_name}.json")
        parts_model_path = os.path.join(parts_dir, f"{item_name}.json")

        if not os.path.exists(root_model_path):
            if os.path.exists(parts_model_path):
                print(f"Copying 3D model for {item_name} from parts/")
                shutil.copy2(parts_model_path, root_model_path)
                fixed_count += 1
            else:
                print(f"Need to create model for: {item_name}")

    print(f"\nTotal models fixed: {fixed_count}")

if __name__ == "__main__":
    main()