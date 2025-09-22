#!/usr/bin/env python3

import os
import json
from pathlib import Path

def find_actual_textures(pack_dir):
    """Find all actual texture files and their correct paths"""
    textures = {}

    # Search all possible texture directories
    for texture_path in Path(pack_dir).rglob("**/textures/**/*.png"):
        # Get the namespace from the path
        path_parts = texture_path.parts
        assets_index = None
        for i, part in enumerate(path_parts):
            if part == "assets":
                assets_index = i
                break

        if assets_index is not None and len(path_parts) > assets_index + 3:
            namespace = path_parts[assets_index + 1]
            relative_path = "/".join(path_parts[assets_index + 3:-1])  # Remove extension and textures folder
            item_name = texture_path.stem

            # Create correct texture reference
            if relative_path:
                texture_ref = f"{namespace}:{relative_path}/{item_name}"
            else:
                texture_ref = f"{namespace}:{item_name}"

            textures[item_name] = texture_ref
            print(f"Found: {item_name} -> {texture_ref}")

    return textures

def fix_model_texture_paths(model_file, actual_textures):
    """Fix texture paths in a model file"""
    try:
        with open(model_file, 'r') as f:
            model_data = json.load(f)

        changed = False

        # Fix textures in the model
        if "textures" in model_data:
            for key, texture_path in model_data["textures"].items():
                # Extract item name from current path
                if ":" in texture_path:
                    current_item = texture_path.split("/")[-1]
                else:
                    current_item = texture_path

                # Check if we have the correct path for this item
                if current_item in actual_textures:
                    correct_path = actual_textures[current_item]
                    if texture_path != correct_path:
                        print(f"  Fixing {model_file.name}: {texture_path} -> {correct_path}")
                        model_data["textures"][key] = correct_path
                        changed = True

        # Save if changed
        if changed:
            with open(model_file, 'w') as f:
                json.dump(model_data, f, indent=2)
            return True

    except Exception as e:
        print(f"Error processing {model_file}: {e}")

    return False

def main():
    """Universal texture path fixer for any content pack"""

    pack_dir = "."
    namespace = "mtsofficialpack"  # Change this for other packs
    models_dir = Path(f"src/main/resources/assets/{namespace}/models/item")

    print("=== UNIVERSAL TEXTURE PATH FIXER ===")
    print(f"Processing pack: {namespace}")

    # Step 1: Find all actual textures
    print("\n1. Scanning for actual texture files...")
    actual_textures = find_actual_textures(pack_dir)
    print(f"Found {len(actual_textures)} textures")

    # Step 2: Fix all model files
    print("\n2. Fixing model texture paths...")
    fixed_count = 0

    if models_dir.exists():
        for model_file in models_dir.rglob("*.json"):
            if fix_model_texture_paths(model_file, actual_textures):
                fixed_count += 1

    print(f"\n=== SUMMARY ===")
    print(f"Fixed {fixed_count} model files")
    print(f"This script automatically finds correct texture paths for any pack!")

if __name__ == "__main__":
    main()