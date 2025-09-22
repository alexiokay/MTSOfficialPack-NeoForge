#!/usr/bin/env python3

import os
import json
import shutil

def main():
    """Fix remaining items that have 3D models available but aren't using them"""

    models_dir = "src/main/resources/assets/mtsofficialpack/models/item"
    parts_dir = os.path.join(models_dir, "parts")

    # Find all existing 3D models in parts directory
    available_3d_models = {}
    if os.path.exists(parts_dir):
        for filename in os.listdir(parts_dir):
            if filename.endswith('.json'):
                item_name = filename[:-5]  # Remove .json
                available_3d_models[item_name] = os.path.join(parts_dir, filename)

    print(f"Found {len(available_3d_models)} available 3D models in parts/")

    # Check which items still need to be upgraded to 3D
    fixed_count = 0

    for item_name, parts_path in available_3d_models.items():
        root_model_path = os.path.join(models_dir, f"{item_name}.json")

        if os.path.exists(root_model_path):
            # Read the root model to see if it's still a simple generated one
            try:
                with open(root_model_path, 'r') as f:
                    model_data = json.load(f)

                # Check if it's a simple generated model (not already 3D)
                if (model_data.get("parent") == "item/generated" and
                    "elements" not in model_data):

                    print(f"Upgrading {item_name} from 2D to 3D")

                    # Delete the 2D model
                    os.remove(root_model_path)

                    # Copy the 3D model to root location
                    shutil.copy2(parts_path, root_model_path)

                    fixed_count += 1
                else:
                    print(f"Skipping {item_name} - already has 3D model")

            except Exception as e:
                print(f"Error processing {item_name}: {e}")
        else:
            # Item doesn't exist at root level - create it from parts
            print(f"Creating missing {item_name} from parts/")
            shutil.copy2(parts_path, root_model_path)
            fixed_count += 1

    print(f"\nUpgraded {fixed_count} more models to 3D")

    # Also check for items that might be missing textures entirely
    # Create very basic models for items that might exist but have no model at all
    potential_missing = [
        "confetti", "confettigun", "flaregun", "drill_bit", "tank_track",
        "vehicle_mirror", "vehicle_light", "horn", "siren"
    ]

    created_count = 0
    for item_name in potential_missing:
        model_path = os.path.join(models_dir, f"{item_name}.json")
        if not os.path.exists(model_path):
            # Create basic model
            basic_model = {
                "parent": "item/generated",
                "textures": {
                    "layer0": f"mtsofficialpack:item/{item_name}"
                }
            }

            with open(model_path, 'w') as f:
                json.dump(basic_model, f, indent=2)

            print(f"Created basic model for: {item_name}")
            created_count += 1

    print(f"\nCreated {created_count} new basic models")
    print(f"Total improvements: {fixed_count + created_count}")

if __name__ == "__main__":
    main()