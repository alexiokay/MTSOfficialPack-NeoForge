#!/usr/bin/env python3

import os
import shutil

def main():
    """Fix MTS model naming - create mtsofficialpack.ITEMNAME.json files"""

    models_dir = "src/main/resources/assets/mts/models/item"
    source_dir = "src/main/resources/assets/mtsofficialpack/models/item"

    # Create MTS models directory if it doesn't exist
    os.makedirs(models_dir, exist_ok=True)

    if not os.path.exists(source_dir):
        print("Source models directory not found!")
        return

    print("=== CREATING MTS-COMPATIBLE MODEL FILES ===")

    copied_count = 0
    for filename in os.listdir(source_dir):
        if filename.endswith('.json'):
            item_name = filename[:-5]  # Remove .json

            # Create MTS-style filename
            mts_filename = f"mtsofficialpack.{item_name}.json"

            source_path = os.path.join(source_dir, filename)
            target_path = os.path.join(models_dir, mts_filename)

            try:
                # Copy the model file with new name
                shutil.copy2(source_path, target_path)
                print(f"Created: {mts_filename}")
                copied_count += 1

            except Exception as e:
                print(f"Error copying {filename}: {e}")

    print(f"\n=== RESULTS ===")
    print(f"Created {copied_count} MTS-compatible model files")
    print(f"Files are now in: {models_dir}")
    print(f"Format: mtsofficialpack.ITEMNAME.json")
    print(f"This should fix the purple cube texture issues!")

if __name__ == "__main__":
    main()