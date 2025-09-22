#!/usr/bin/env python3

import os
import json

def main():
    """Setup proper NeoForge 1.21.1 OBJ model references for items"""

    models_dir = "src/main/resources/assets/mtsofficialpack/models/item"
    items_dir = "src/main/resources/assets/mtsofficialpack/items"
    obj_models_dir = "src/main/resources/assets/mtsofficialpack/objmodels/parts"

    # Create items directory if it doesn't exist (NeoForge 21.4+ requirement)
    os.makedirs(items_dir, exist_ok=True)

    # Find all available OBJ models
    obj_models = {}
    if os.path.exists(obj_models_dir):
        for filename in os.listdir(obj_models_dir):
            if filename.endswith('.obj'):
                item_name = filename[:-4]  # Remove .obj extension
                obj_models[item_name] = f"mtsofficialpack:objmodels/parts/{filename}"

    print(f"Found {len(obj_models)} OBJ models")

    if not obj_models:
        print("No OBJ models found! Check the objmodels directory.")
        return

    fixed_count = 0

    print(f"\n=== SETTING UP NEOFORGE OBJ MODEL REFERENCES ===")

    for item_name, obj_path in obj_models.items():
        # 1. Create NeoForge item definition (new system)
        item_def_path = os.path.join(items_dir, f"{item_name}.json")

        # 2. Create/update item model that references OBJ
        model_path = os.path.join(models_dir, f"{item_name}.json")

        try:
            print(f"Setting up NeoForge OBJ reference for {item_name}")

            # Create NeoForge item definition
            item_definition = {
                "__comment": "NeoForge 1.21.1 item definition - references OBJ model",
                "model": {
                    "type": "obj",
                    "loader": "neoforge:obj",
                    "model": obj_path,
                    "automatic_culling": True,
                    "flip_v": False
                },
                "textures": {
                    "texture": f"mtsofficialpack:item/{item_name}",
                    "particle": f"mtsofficialpack:item/{item_name}"
                }
            }

            with open(item_def_path, 'w') as f:
                json.dump(item_definition, f, indent=2)

            # Create item model that references the item definition
            item_model = {
                "__comment": "References NeoForge item definition for OBJ rendering",
                "parent": "item/generated",
                "loader": "neoforge:obj",
                "model": obj_path,
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
                    "fixed": {
                        "rotation": [0, 0, 0],
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
                json.dump(item_model, f, indent=2)

            fixed_count += 1

        except Exception as e:
            print(f"Error processing {item_name}: {e}")

    print(f"\n=== RESULTS ===")
    print(f"Setup {fixed_count} NeoForge OBJ model references")
    print(f"Created files in:")
    print(f"  - {items_dir}/ (NeoForge item definitions)")
    print(f"  - {models_dir}/ (Item models with OBJ loader)")

    print(f"\nNow items should render as proper 3D OBJ models when dropped!")
    print(f"\nNOTE: If models don't load immediately, try F3+T to reload resources.")

    # Create info file about the setup
    info_content = """# NeoForge 1.21.1 OBJ Model Setup

This content pack has been configured for NeoForge 1.21.1 OBJ model rendering:

## Files Created:
- `/items/*.json` - NeoForge item definitions (new system)
- `/models/item/*.json` - Item models with OBJ loader references

## How It Works:
1. NeoForge 1.21.1 uses a new "Client Items" system
2. Items reference OBJ models using `"loader": "neoforge:obj"`
3. The OBJ models in `/objmodels/parts/` are now properly linked

## Troubleshooting:
- If models don't appear, press F3+T to reload resources
- Check that OBJ files exist in `/objmodels/parts/`
- Verify textures exist in `/textures/item/`

## Migration from Forge:
- Forge 1.20.1 had automatic OBJ rendering
- NeoForge 1.21.1 requires explicit OBJ loader configuration
- This setup restores the 3D model functionality
"""

    with open("NEOFORGE_OBJ_SETUP.md", 'w') as f:
        f.write(info_content)

    print(f"Created NEOFORGE_OBJ_SETUP.md with setup information")

if __name__ == "__main__":
    main()