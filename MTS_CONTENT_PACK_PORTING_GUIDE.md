# MTS Content Pack Porting Guide: Forge to NeoForge 1.21.1

This guide explains how to port an MTS/Immersive Vehicles content pack from older Forge versions to NeoForge 1.21.1.

## Overview of Changes

| Component | Old (Forge) | New (NeoForge 1.21.1) |
|-----------|-------------|----------------------|
| Mod descriptor | `META-INF/mods.toml` | `META-INF/neoforge.mods.toml` |
| Java loader class | `ForgePackLoader.class` | Not needed (delete) |
| Item models | Not needed | Required in `assets/mts/models/item/` |
| Item textures | `textures/items/` (nested) | Also need `textures/item/` (flat) |
| Language files | `assets/{packid}/language/` | `assets/{packid}/lang/` |
| Recipe folder | `data/{packid}/recipes/` | `data/{packid}/recipe/` |
| Recipe tags | `forge:ingots/gold` | `c:ingots/gold` |
| MTL files | Used by some packs | Delete (cause rendering issues) |

---

## Step 1: Create NeoForge Mod Descriptor

Delete `META-INF/mods.toml` and any `.class` files (like `ForgePackLoader.class`).

Create `META-INF/neoforge.mods.toml`:

```toml
modLoader="javafml"
loaderVersion="[4,)"
license="All rights reserved"

[[mods]]
modId="yourpackid"
version="1.0.0"
displayName="Your Pack Name"
logoFile="logo.png"
description='''
Your pack description here.
'''

[[dependencies.yourpackid]]
    modId="minecraft"
    type="required"
    versionRange="[1.21.1,1.22)"
    ordering="NONE"
    side="BOTH"

[[dependencies.yourpackid]]
    modId="neoforge"
    type="required"
    versionRange="[21.1.0,)"
    ordering="NONE"
    side="BOTH"

[[dependencies.yourpackid]]
    modId="mts"
    type="required"
    versionRange="[22.18.0,)"
    ordering="NONE"
    side="BOTH"
```

Replace `yourpackid` with your pack's ID (must match `packdefinition.json`).

---

## Step 2: Remove MTL Files

Delete all `.mtl` files from `objmodels/` folders. They cause rendering issues in NeoForge 1.21.1.

```bash
find assets/yourpackid/objmodels -name "*.mtl" -delete
```

---

## Step 3: Create Item Model JSON Files

NeoForge 1.21.1 requires explicit item model files for inventory rendering.

Create folder: `assets/mts/models/item/`

For each item in your pack, create a JSON file:

**Filename:** `{packid}.{itemname}.json`

**Content:**
```json
{"parent":"mts:item/basic","textures":{"layer0": "{packid}:item/{itemname}"}}
```

### Examples:

`ivairlinerpack.707-120.json`:
```json
{"parent":"mts:item/basic","textures":{"layer0": "ivairlinerpack:item/707-120"}}
```

`ivairlinerpack.cfm56-3.json`:
```json
{"parent":"mts:item/basic","textures":{"layer0": "ivairlinerpack:item/cfm56-3"}}
```

### Batch Generation Script (Bash):

```bash
cd assets/mts/models/item
for f in ../../yourpackid/textures/item/*.png; do
    name=$(basename "$f" .png)
    echo "{\"parent\":\"mts:item/basic\",\"textures\":{\"layer0\": \"yourpackid:item/$name\"}}" > "yourpackid.$name.json"
done
```

---

## Step 4: Create Flat Item Textures Folder

Minecraft's item model system requires textures in a flat `textures/item/` folder.

MTS still uses the nested `textures/items/` folder internally, so **keep both**.

### Copy all item textures to flat folder:

```bash
mkdir -p assets/yourpackid/textures/item

find assets/yourpackid/textures/items -name "*.png" -exec cp {} assets/yourpackid/textures/item/ \;
```

### Before:
```
textures/items/
├── items/
│   └── crafting_part/
│       └── iron_plate.png
├── parts/
│   └── engine/
│       └── cfm56-3.png
└── vehicles/
    └── plane/
        └── 707-120/
            └── 707-120.png
```

### After (keep old + add new):
```
textures/items/           <- KEEP (MTS uses this)
├── items/
├── parts/
└── vehicles/

textures/item/            <- NEW (Minecraft item models use this)
├── iron_plate.png
├── cfm56-3.png
└── 707-120.png
```

---

## Step 5: Migrate Language Files (if applicable)

If your pack has language/translation files:

**Old path:** `assets/{packid}/language/{subfolder}/en_us.json`

**New path:** `assets/{packid}/lang/en_us.json`

```bash
mkdir -p assets/yourpackid/lang
mv assets/yourpackid/language/*/*.json assets/yourpackid/lang/
rm -rf assets/yourpackid/language
```

---

## Step 6: Migrate Vanilla Crafting Recipes (if applicable)

If your pack has vanilla Minecraft crafting recipes:

### 6a. Rename folder (plural to singular):

**Old:** `data/{packid}/recipes/`

**New:** `data/{packid}/recipe/`

### 6b. Update recipe JSON format:

**Old format (Forge):**
```json
{
    "type": "minecraft:crafting_shaped",
    "pattern": [" a ", " a ", " b "],
    "key": {
        "a": {"tag": "forge:ingots/gold"},
        "b": {"tag": "forge:nuggets/iron"}
    },
    "result": {
        "item": "mts:yourpackid.itemname",
        "count": 8
    }
}
```

**New format (NeoForge 1.21.1):**
```json
{
    "type": "minecraft:crafting_shaped",
    "category": "misc",
    "pattern": [" a ", " a ", " b "],
    "key": {
        "a": {"tag": "c:ingots/gold"},
        "b": {"tag": "c:nuggets/iron"}
    },
    "result": {
        "id": "mts:yourpackid.itemname",
        "count": 8
    }
}
```

### Changes:
- Add `"category": "misc"`
- Change `forge:` tags to `c:` (common tags)
- Change `"item":` to `"id":` in result

---

## Final Pack Structure

```
yourpackid-1.21.1.jar
├── META-INF/
│   └── neoforge.mods.toml        <- NeoForge mod descriptor
├── assets/
│   ├── mts/
│   │   └── models/
│   │       └── item/             <- Item model JSONs
│   │           ├── yourpackid.item1.json
│   │           ├── yourpackid.item2.json
│   │           └── ...
│   └── yourpackid/
│       ├── jsondefs/             <- Unchanged
│       │   ├── items/
│       │   ├── parts/
│       │   └── vehicles/
│       ├── objmodels/            <- Remove .mtl files
│       │   ├── parts/
│       │   └── vehicles/
│       ├── textures/
│       │   ├── item/             <- NEW: Flat folder (for Minecraft)
│       │   │   ├── item1.png
│       │   │   └── item2.png
│       │   ├── items/            <- KEEP: Nested folders (for MTS)
│       │   │   ├── items/
│       │   │   ├── parts/
│       │   │   └── vehicles/
│       │   ├── parts/            <- 3D model textures
│       │   └── vehicles/         <- 3D model textures
│       ├── sounds/               <- Unchanged
│       ├── lang/                 <- Renamed from language/
│       │   └── en_us.json
│       └── packdefinition.json   <- Unchanged
├── data/
│   └── yourpackid/
│       └── recipe/               <- Renamed from recipes/
│           └── *.json            <- Updated format
├── pack.mcmeta
└── logo.png
```

---

## Building the JAR

From the `src/main/resources` folder (or your pack root):

```bash
jar -cvf yourpackid-1.21.1.jar .
```

Or simply zip all files and rename `.zip` to `.jar`.

---

## Checklist

- [ ] Created `META-INF/neoforge.mods.toml`
- [ ] Deleted `META-INF/mods.toml` (old Forge)
- [ ] Deleted `ForgePackLoader.class` and any `.class` files
- [ ] Deleted all `.mtl` files from `objmodels/`
- [ ] Created `assets/mts/models/item/` with model JSONs
- [ ] Created `assets/{packid}/textures/item/` with flat textures
- [ ] Kept `assets/{packid}/textures/items/` (MTS still needs it)
- [ ] Renamed `language/` to `lang/` (if applicable)
- [ ] Renamed `recipes/` to `recipe/` (if applicable)
- [ ] Updated recipe JSON format (if applicable)
- [ ] Built JAR file

---

## Troubleshooting

### "Mod is for Forge" error
- Make sure you have `neoforge.mods.toml`, not `mods.toml`
- Delete any `.class` files

### Missing item icons
- Check `assets/mts/models/item/` has JSON files for each item
- Check `assets/{packid}/textures/item/` has PNG files
- Filenames must match exactly (case-sensitive)

### 3D models not rendering
- Delete `.mtl` files from `objmodels/`
- Keep `.obj` files

### Recipes not working
- Folder must be `recipe/` (singular), not `recipes/`
- Use `c:` tags instead of `forge:`
- Use `"id":` instead of `"item":` in result
- Add `"category": "misc"`
