#!/usr/bin/env python3

import os
import json

def fix_mtl_files():
    """Fix MTL files to work with NeoForge OBJ loader"""

    obj_dir = "src/main/resources/assets/mtsofficialpack/objmodels/parts"

    # Find all MTL files
    mtl_files = []
    if os.path.exists(obj_dir):
        for filename in os.listdir(obj_dir):
            if filename.endswith('.mtl'):
                mtl_files.append(filename[:-4])  # Remove .mtl extension

    print(f"Found {len(mtl_files)} MTL files to fix")

    for item_name in mtl_files:
        try:
            print(f"Fixing MTL for {item_name}")

            # Create proper MTL content for NeoForge
            mtl_content = f"""# MTL file for {item_name}
# Fixed for NeoForge 1.21.1

newmtl none
Ka 1.000000 1.000000 1.000000
Kd 1.000000 1.000000 1.000000
Ks 0.000000 0.000000 0.000000
Ns 0.000000
map_Kd mtsofficialpack:item/{item_name}

newmtl material0
Ka 1.000000 1.000000 1.000000
Kd 1.000000 1.000000 1.000000
Ks 0.000000 0.000000 0.000000
Ns 0.000000
map_Kd mtsofficialpack:item/{item_name}
"""

            mtl_path = os.path.join(obj_dir, f"{item_name}.mtl")
            with open(mtl_path, 'w') as f:
                f.write(mtl_content)

            print(f"  Updated MTL: {item_name}.mtl")

        except Exception as e:
            print(f"Error fixing MTL for {item_name}: {e}")

def simplify_item_models():
    """Simplify item models to basic NeoForge OBJ format"""

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

    print(f"Simplifying {len(obj_models)} item models")

    for item_name in obj_models:
        try:
            print(f"Simplifying model for {item_name}")

            # Create very simple model
            simple_model = {
                "__comment": f"Simple NeoForge OBJ model for {item_name}",
                "loader": "neoforge:obj",
                "model": f"mtsofficialpack:objmodels/parts/{item_name}.obj",
                "textures": {
                    "particle": f"mtsofficialpack:item/{item_name}"
                }
            }

            model_path = os.path.join(models_dir, f"{item_name}.json")
            with open(model_path, 'w') as f:
                json.dump(simple_model, f, indent=2)

            print(f"  Simplified: {item_name}.json")

        except Exception as e:
            print(f"Error simplifying {item_name}: {e}")

def main():
    """Fix MTL material references and simplify models"""

    print("=== FIXING MTL MATERIAL REFERENCES ===")
    fix_mtl_files()

    print(f"\n=== SIMPLIFYING ITEM MODELS ===")
    simplify_item_models()

    print(f"\n=== RESULTS ===")
    print(f"Fixed MTL files to include 'none' material that OBJ files reference")
    print(f"Simplified item models to basic NeoForge OBJ format")
    print(f"Purple/black cubes should now show proper textures!")

    print(f"\nIf textures still don't work, try:")
    print(f"1. F3+T to reload resources")
    print(f"2. Check game logs for texture loading errors")

if __name__ == "__main__":
    main()