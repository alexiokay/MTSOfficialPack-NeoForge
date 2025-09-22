#!/usr/bin/env python3

import os
import json

def main():
    """Fix NeoForge item definitions to reference JSON models instead of OBJ"""

    items_dir = "src/main/resources/assets/mtsofficialpack/items"

    if not os.path.exists(items_dir):
        print("No items directory found!")
        return

    print("=== FIXING NEOFORGE ITEM DEFINITIONS ===")

    fixed_count = 0
    for filename in os.listdir(items_dir):
        if filename.endswith('.json'):
            item_name = filename[:-5]  # Remove .json
            item_path = os.path.join(items_dir, filename)

            try:
                # Read current item definition
                with open(item_path, 'r') as f:
                    item_def = json.load(f)

                # Check if it has OBJ model reference
                if 'model' in item_def and isinstance(item_def['model'], dict):
                    if 'loader' in item_def['model'] and item_def['model']['loader'] == 'neoforge:obj':
                        print(f"Fixing {item_name} - switching from OBJ to JSON model reference")

                        # Replace with simple JSON model reference
                        new_item_def = {
                            "__comment": "NeoForge item definition - references JSON model",
                            "model": f"mtsofficialpack:item/{item_name}"
                        }

                        # Write updated definition
                        with open(item_path, 'w') as f:
                            json.dump(new_item_def, f, indent=2)

                        fixed_count += 1

            except Exception as e:
                print(f"Error processing {filename}: {e}")

    print(f"\n=== RESULTS ===")
    print(f"Fixed {fixed_count} NeoForge item definitions")
    print(f"Items now reference JSON models in /models/item/ instead of direct OBJ")
    print(f"This should fix purple cube texture issues!")

if __name__ == "__main__":
    main()