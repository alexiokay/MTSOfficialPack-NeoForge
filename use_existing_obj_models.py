#!/usr/bin/env python3

import os
import json

def main():
    """Use existing OBJ models by creating proper references in item JSON models"""

    models_dir = "src/main/resources/assets/mtsofficialpack/models/item"
    obj_models_dir = "src/main/resources/assets/mtsofficialpack/objmodels/parts"

    # Find all available OBJ models
    obj_models = {}
    if os.path.exists(obj_models_dir):
        for filename in os.listdir(obj_models_dir):
            if filename.endswith('.obj'):
                item_name = filename[:-4]  # Remove .obj extension
                obj_models[item_name] = f"mtsofficialpack:parts/{item_name}"

    print(f"Found {len(obj_models)} OBJ models:")
    for item in sorted(obj_models.keys())[:10]:
        print(f"  - {item}")
    if len(obj_models) > 10:
        print(f"  ... and {len(obj_models) - 10} more")

    # For dropped items, we need to create simple models that at least show the texture properly
    # since Minecraft's item rendering doesn't directly support OBJ models for dropped items

    fixed_count = 0

    print(f"\n=== CREATING PROPER ITEM MODELS ===")

    for item_name in obj_models.keys():
        model_path = os.path.join(models_dir, f"{item_name}.json")

        if os.path.exists(model_path):
            try:
                with open(model_path, 'r') as f:
                    model_data = json.load(f)

                # Get the texture path
                texture_path = None
                if "textures" in model_data:
                    if "texture" in model_data["textures"]:
                        texture_path = model_data["textures"]["texture"]
                    elif "side" in model_data["textures"]:
                        texture_path = model_data["textures"]["side"]
                    elif "layer0" in model_data["textures"]:
                        texture_path = model_data["textures"]["layer0"]

                if not texture_path:
                    print(f"Could not find texture for {item_name}, skipping")
                    continue

                print(f"Fixing model for {item_name}")

                # Create a better 3D-looking model that references the OBJ model concept
                # Use a simple approach that will work for dropped items
                new_model = {
                    "parent": "item/generated",
                    "textures": {
                        "layer0": texture_path
                    },
                    "display": {
                        "ground": {
                            "rotation": [0, 0, 0],
                            "translation": [0, 3, 0],
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

                # Add a comment about the OBJ model
                new_model["__comment"] = f"3D model: {obj_models[item_name]}.obj"

                with open(model_path, 'w') as f:
                    json.dump(new_model, f, indent=2)

                fixed_count += 1

            except Exception as e:
                print(f"Error processing {item_name}: {e}")

    print(f"\n=== RESULTS ===")
    print(f"Fixed {fixed_count} item models")
    print(f"Items now use proper display settings")
    print(f"The actual 3D OBJ models will be used when items are placed as parts")
    print(f"Dropped items will show with proper scaling and positioning")

    # Additional note about MTS rendering
    print(f"\nNote: MTS uses OBJ models for:")
    print(f"- Parts placed on vehicles/entities (uses OBJ)")
    print(f"- Items in inventory/dropped (uses JSON with textures)")
    print(f"This is the correct behavior for MTS content packs.")

if __name__ == "__main__":
    main()