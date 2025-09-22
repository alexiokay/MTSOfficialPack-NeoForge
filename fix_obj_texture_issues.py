#!/usr/bin/env python3

import os
import json

def create_mtl_file(item_name, obj_dir):
    """Create MTL file for NeoForge OBJ model"""
    mtl_content = f"""# MTL file for {item_name}
# Generated for NeoForge 1.21.1

newmtl material0
Ka 1.000000 1.000000 1.000000
Kd 1.000000 1.000000 1.000000
Ks 0.000000 0.000000 0.000000
Ns 0.000000
map_Kd #texture
"""

    mtl_path = os.path.join(obj_dir, f"{item_name}.mtl")
    with open(mtl_path, 'w') as f:
        f.write(mtl_content)

    return mtl_path

def fix_obj_model_textures():
    """Fix NeoForge OBJ model texture issues"""

    models_dir = "src/main/resources/assets/mtsofficialpack/models/item"
    items_dir = "src/main/resources/assets/mtsofficialpack/items"
    obj_dir = "src/main/resources/assets/mtsofficialpack/objmodels/parts"

    # Find all OBJ models
    obj_models = []
    if os.path.exists(obj_dir):
        for filename in os.listdir(obj_dir):
            if filename.endswith('.obj'):
                item_name = filename[:-4]  # Remove .obj extension
                obj_models.append(item_name)

    print(f"Found {len(obj_models)} OBJ models to fix")

    fixed_count = 0

    for item_name in obj_models:
        try:
            print(f"Fixing texture issues for {item_name}")

            # 1. Create MTL file if missing
            mtl_path = os.path.join(obj_dir, f"{item_name}.mtl")
            if not os.path.exists(mtl_path):
                create_mtl_file(item_name, obj_dir)
                print(f"  Created missing MTL file: {item_name}.mtl")

            # 2. Update item model with better NeoForge OBJ configuration
            model_path = os.path.join(models_dir, f"{item_name}.json")
            if os.path.exists(model_path):

                # Create simplified model that should work with NeoForge
                fixed_model = {
                    "__comment": "NeoForge OBJ model with texture fix",
                    "loader": "neoforge:obj",
                    "model": f"mtsofficialpack:objmodels/parts/{item_name}.obj",
                    "automatic_culling": True,
                    "flip_v": False,
                    "textures": {
                        "texture": f"mtsofficialpack:item/{item_name}",
                        "particle": f"mtsofficialpack:item/{item_name}"
                    },
                    "display": {
                        "ground": {
                            "rotation": [0, 0, 0],
                            "translation": [0, 2, 0],
                            "scale": [0.75, 0.75, 0.75]
                        },
                        "gui": {
                            "rotation": [30, 45, 0],
                            "translation": [0, 0, 0],
                            "scale": [0.75, 0.75, 0.75]
                        },
                        "thirdperson_righthand": {
                            "rotation": [75, 45, 0],
                            "translation": [0, 2.5, 0],
                            "scale": [0.5, 0.5, 0.5]
                        },
                        "thirdperson_lefthand": {
                            "rotation": [75, 225, 0],
                            "translation": [0, 2.5, 0],
                            "scale": [0.5, 0.5, 0.5]
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

                with open(model_path, 'w') as f:
                    json.dump(fixed_model, f, indent=2)

                print(f"  Updated model file: {item_name}.json")

            # 3. Simplify items definition
            items_path = os.path.join(items_dir, f"{item_name}.json")
            if os.path.exists(items_path):

                # Simplified item definition
                item_def = {
                    "__comment": "NeoForge item definition - simplified for texture fix",
                    "model": {
                        "loader": "neoforge:obj",
                        "model": f"mtsofficialpack:objmodels/parts/{item_name}.obj",
                        "automatic_culling": True
                    },
                    "textures": {
                        "texture": f"mtsofficialpack:item/{item_name}"
                    }
                }

                with open(items_path, 'w') as f:
                    json.dump(item_def, f, indent=2)

                print(f"  Updated item definition: {item_name}.json")

            fixed_count += 1

        except Exception as e:
            print(f"Error fixing {item_name}: {e}")

    print(f"\n=== RESULTS ===")
    print(f"Fixed texture issues for {fixed_count} OBJ models")
    print(f"Created missing MTL files")
    print(f"Simplified model configurations for NeoForge compatibility")
    print(f"\nPurple/black cubes should now show proper textures!")
    print(f"Try F3+T to reload resources if needed.")

def main():
    fix_obj_model_textures()

if __name__ == "__main__":
    main()