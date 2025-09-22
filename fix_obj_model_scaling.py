#!/usr/bin/env python3

import os
import json

def main():
    """Fix massive OBJ model scaling by adding proper display transforms"""

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

    print(f"=== FIXING OBJ MODEL SCALING FOR {len(obj_models)} ITEMS ===")

    fixed_count = 0

    for item_name in obj_models:
        try:
            print(f"Fixing scaling for {item_name}")

            # Create properly scaled OBJ model
            scaled_model = {
                "__comment": f"Properly scaled NeoForge OBJ model for {item_name}",
                "loader": "neoforge:obj",
                "model": f"mtsofficialpack:objmodels/parts/{item_name}.obj",
                "textures": {
                    "particle": f"mtsofficialpack:item/{item_name}"
                },
                "display": {
                    "gui": {
                        "rotation": [30, 45, 0],
                        "translation": [0, 0, 0],
                        "scale": [0.4, 0.4, 0.4]  # Much smaller for GUI
                    },
                    "ground": {
                        "rotation": [0, 0, 0],
                        "translation": [0, 1, 0],
                        "scale": [0.25, 0.25, 0.25]  # Small when dropped
                    },
                    "fixed": {
                        "rotation": [0, 0, 0],
                        "translation": [0, 0, 0],
                        "scale": [0.25, 0.25, 0.25]  # Small for item frames
                    },
                    "thirdperson_righthand": {
                        "rotation": [75, 45, 0],
                        "translation": [0, 2.5, 0],
                        "scale": [0.25, 0.25, 0.25]  # Small in hand
                    },
                    "thirdperson_lefthand": {
                        "rotation": [75, 225, 0],
                        "translation": [0, 2.5, 0],
                        "scale": [0.25, 0.25, 0.25]  # Small in hand
                    },
                    "firstperson_righthand": {
                        "rotation": [0, 45, 0],
                        "translation": [0, 0, 0],
                        "scale": [0.3, 0.3, 0.3]  # Small first person
                    },
                    "firstperson_lefthand": {
                        "rotation": [0, 225, 0],
                        "translation": [0, 0, 0],
                        "scale": [0.3, 0.3, 0.3]  # Small first person
                    }
                }
            }

            # Special scaling for different item types
            if "wheel" in item_name:
                # Wheels should lay flat when dropped
                scaled_model["display"]["ground"]["rotation"] = [0, 0, 90]
                scaled_model["display"]["ground"]["scale"] = [0.3, 0.3, 0.3]
                scaled_model["display"]["gui"]["scale"] = [0.5, 0.5, 0.5]

            elif "engine" in item_name:
                # Engines are bigger items
                scaled_model["display"]["ground"]["scale"] = [0.35, 0.35, 0.35]
                scaled_model["display"]["gui"]["scale"] = [0.5, 0.5, 0.5]

            elif any(x in item_name for x in ["crate", "barrel", "tank"]):
                # Containers are medium sized
                scaled_model["display"]["ground"]["scale"] = [0.3, 0.3, 0.3]
                scaled_model["display"]["gui"]["scale"] = [0.45, 0.45, 0.45]

            model_path = os.path.join(models_dir, f"{item_name}.json")
            with open(model_path, 'w') as f:
                json.dump(scaled_model, f, indent=2)

            fixed_count += 1

        except Exception as e:
            print(f"Error fixing {item_name}: {e}")

    print(f"\n=== RESULTS ===")
    print(f"Fixed scaling for {fixed_count} OBJ models")
    print(f"Items should now be properly sized:")
    print(f"  - GUI: Small enough to fit in inventory slots")
    print(f"  - Ground: Reasonable size when dropped")
    print(f"  - Hand: Appropriate size when held")
    print(f"  - Wheels: Lay flat when dropped")

    # Create summary of scaling values
    print(f"\nScaling summary:")
    print(f"  - GUI: 0.4-0.5 scale (inventory display)")
    print(f"  - Ground: 0.25-0.35 scale (dropped items)")
    print(f"  - Hand: 0.25-0.3 scale (when held)")
    print(f"  - Wheels get special flat rotation when dropped")

if __name__ == "__main__":
    main()