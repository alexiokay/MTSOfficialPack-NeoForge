#!/usr/bin/env python3

import os
import json
from pathlib import Path

def fix_to_working_pattern():
    """Fix all models to use the EXACT same pattern as the working engineallison250"""

    namespace = "mtsofficialpack"
    models_dir = Path(f"src/main/resources/assets/{namespace}/models/item")
    textures_dir = Path(f"src/main/resources/assets/{namespace}/textures")

    print("=== FIXING TO WORKING PATTERN ===")
    print("Using the exact same pattern as engineallison250 (the one that works)")

    if not models_dir.exists():
        print(f"Models directory not found: {models_dir}")
        return

    # Build a simple map of textures in the item/ directory
    item_textures = {}
    item_dir = textures_dir / "item"
    if item_dir.exists():
        for png_file in item_dir.rglob("*.png"):
            # Get relative path from item directory
            rel_path = png_file.relative_to(item_dir)
            filename = png_file.stem
            # Store the path relative to textures/item/
            texture_path = str(rel_path).replace("\\", "/").replace(".png", "")
            item_textures[filename] = f"item/{texture_path}"
            print(f"Found item texture: {filename} -> {texture_path}")

    print(f"Found {len(item_textures)} textures in item/ directory")

    fixed_count = 0
    processed_count = 0

    for model_file in models_dir.rglob("*.json"):
        try:
            with open(model_file, 'r') as f:
                model_data = json.load(f)

            processed_count += 1
            changed = False
            item_name = model_file.stem

            # Fix texture paths in the model - use item/ directory like the working one
            if "textures" in model_data:
                for layer, texture_path in model_data["textures"].items():
                    # Check if this item has a texture in the item/ directory
                    if item_name in item_textures:
                        new_path = f"{namespace}:{item_textures[item_name]}"
                        if new_path != texture_path:
                            print(f"FIXING {model_file.name}: {texture_path} -> {new_path}")
                            model_data["textures"][layer] = new_path
                            changed = True

            # Save if changed
            if changed:
                with open(model_file, 'w') as f:
                    json.dump(model_data, f, indent=2)
                fixed_count += 1

        except Exception as e:
            print(f"Error processing {model_file.name}: {e}")

    print(f"\n=== WORKING PATTERN RESULTS ===")
    print(f"Processed {processed_count} model files")
    print(f"Fixed {fixed_count} models to use working item/ pattern")
    print("Now they should work exactly like engineallison250!")

if __name__ == "__main__":
    fix_to_working_pattern()