#!/usr/bin/env python3

import os
import json

def main():
    """Create hybrid models: 2D for GUI, 3D OBJ for world rendering"""

    models_dir = "src/main/resources/assets/mtsofficialpack/models/item"
    obj_dir = "src/main/resources/assets/mtsofficialpack/objmodels/parts"

    # Find all OBJ models (excluding handheld items)
    obj_models = []
    handheld_items = [
        "gunfireextinguisher", "gunflaregun", "gunconfetti", "gunm1919",
        "gunobserver", "gunrocketlauncher", "gunrocketpod", "gunft17turret"
    ]

    if os.path.exists(obj_dir):
        for filename in os.listdir(obj_dir):
            if filename.endswith('.obj'):
                item_name = filename[:-4]
                if item_name not in handheld_items:
                    obj_models.append(item_name)

    print(f"=== CREATING HYBRID GUI/WORLD MODELS FOR {len(obj_models)} ITEMS ===")

    fixed_count = 0

    for item_name in obj_models:
        try:
            print(f"Creating hybrid model for {item_name}")

            # Create hybrid model that uses:
            # - 2D texture for GUI (inventory) display
            # - 3D OBJ model for ground and hand display
            hybrid_model = {
                "__comment": f"Hybrid model for {item_name}: 2D in GUI, 3D in world",
                "parent": "item/generated",
                "textures": {
                    "layer0": f"mtsofficialpack:item/{item_name}"
                },
                "overrides": [
                    {
                        "predicate": {"custom_model_data": 1},
                        "model": f"mtsofficialpack:item/{item_name}_3d"
                    }
                ]
            }

            # Create separate 3D model file for world rendering
            obj_model = {
                "__comment": f"3D OBJ model for {item_name} - used in world",
                "loader": "neoforge:obj",
                "model": f"mtsofficialpack:objmodels/parts/{item_name}.obj",
                "textures": {
                    "particle": f"mtsofficialpack:item/{item_name}"
                },
                "display": {
                    "ground": {
                        "rotation": [0, 0, 0],
                        "translation": [0, 1, 0],
                        "scale": [0.25, 0.25, 0.25]
                    },
                    "fixed": {
                        "rotation": [0, 0, 0],
                        "translation": [0, 0, 0],
                        "scale": [0.25, 0.25, 0.25]
                    },
                    "thirdperson_righthand": {
                        "rotation": [75, 45, 0],
                        "translation": [0, 2.5, 0],
                        "scale": [0.25, 0.25, 0.25]
                    },
                    "thirdperson_lefthand": {
                        "rotation": [75, 225, 0],
                        "translation": [0, 2.5, 0],
                        "scale": [0.25, 0.25, 0.25]
                    },
                    "firstperson_righthand": {
                        "rotation": [0, 45, 0],
                        "translation": [0, 0, 0],
                        "scale": [0.3, 0.3, 0.3]
                    },
                    "firstperson_lefthand": {
                        "rotation": [0, 225, 0],
                        "translation": [0, 0, 0],
                        "scale": [0.3, 0.3, 0.3]
                    }
                }
            }

            # Special handling for wheels
            if "wheel" in item_name:
                obj_model["display"]["ground"]["rotation"] = [0, 0, 90]
                obj_model["display"]["ground"]["scale"] = [0.3, 0.3, 0.3]

            elif "engine" in item_name:
                obj_model["display"]["ground"]["scale"] = [0.35, 0.35, 0.35]

            elif any(x in item_name for x in ["crate", "barrel", "tank"]):
                obj_model["display"]["ground"]["scale"] = [0.3, 0.3, 0.3]

            # Write main hybrid model
            model_path = os.path.join(models_dir, f"{item_name}.json")
            with open(model_path, 'w') as f:
                json.dump(hybrid_model, f, indent=2)

            # Write 3D model variant
            obj_model_path = os.path.join(models_dir, f"{item_name}_3d.json")
            with open(obj_model_path, 'w') as f:
                json.dump(obj_model, f, indent=2)

            fixed_count += 1

        except Exception as e:
            print(f"Error creating hybrid model for {item_name}: {e}")

    print(f"\n=== RESULTS ===")
    print(f"Created hybrid models for {fixed_count} items")
    print(f"Benefits:")
    print(f"  - GUI: Clean 2D textures in inventory")
    print(f"  - World: Proper 3D models when dropped/held")
    print(f"  - No more broken 3D models in GUI")
    print(f"  - Best of both worlds!")

    # Create alternative: Simple 2D only models
    print(f"\n=== CREATING SIMPLE 2D FALLBACK MODELS ===")

    simple_count = 0
    for item_name in obj_models:
        try:
            print(f"Creating simple 2D model for {item_name}")

            # Simple 2D model with proper display transforms
            simple_model = {
                "__comment": f"Simple 2D model for {item_name} - no OBJ complexity",
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
                    }
                }
            }

            # Write simple 2D fallback
            simple_model_path = os.path.join(models_dir, f"{item_name}_2d.json")
            with open(simple_model_path, 'w') as f:
                json.dump(simple_model, f, indent=2)

            simple_count += 1

        except Exception as e:
            print(f"Error creating simple model for {item_name}: {e}")

    print(f"Created {simple_count} simple 2D fallback models")
    print(f"\nTo use simple 2D models instead:")
    print(f"  - Rename {item_name}_2d.json to {item_name}.json")
    print(f"  - Delete the _3d.json files")

if __name__ == "__main__":
    main()