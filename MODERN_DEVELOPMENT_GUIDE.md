# Modern MTS Content Pack Development Guide

## Overview
This guide outlines the current best practices for developing MTS content packs for NeoForge 1.21.1, avoiding legacy tools that cause issues.

## ✅ Modern Development Workflow

### 1. Creating 3D Item Models
- **Tool**: Blockbench (recommended)
- **Export Format**: JSON model format
- **Texture Size**: 64x64 or 128x128 pixels
- **Output**: Complex 3D geometry with proper UV mapping

### 2. File Placement Structure
```
MTSOfficialPack-1.21.1/
└── src/main/resources/assets/
    ├── mts/
    │   └── models/
    │       └── item/
    │           └── mtsofficialpack.{itemname}.json  ← 3D models go here
    └── mtsofficialpack/
        ├── textures/
        │   └── item/
        │       └── {itemname}.png  ← Item textures
        └── objmodels/
            └── parts/
                └── {partname}.obj  ← Vehicle/part models for world rendering
```

### 3. Model Naming Convention
- **MTS namespace models**: `mtsofficialpack.{itemname}.json`
- **Textures**: `{itemname}.png` (without pack prefix)
- **Example**:
  - Model: `mtsofficialpack.wheelsmall.json`
  - Texture: `wheelsmall.png`

### 4. Building the Pack
```bash
# Use Gradle directly, NOT compile.bat
./gradlew build

# Output location
build/libs/MTS Official Pack-V{version}.jar
```

## ❌ Legacy Tools to Avoid

### PackCompiler.java / compile.bat
**Why to avoid:**
- Auto-generates flat 2D models, overwriting 3D models
- Designed for older Forge versions
- Creates unnecessary Java loader classes
- Doesn't understand Blockbench 3D JSON models
- Causes texture loading issues

### What PackCompiler does (and why it's problematic):
1. Scans for PNG textures
2. Auto-generates basic 2D item models
3. Overwrites existing 3D models
4. Creates legacy namespace bridges

## 📁 Files That Can Be Removed

### 1. Auto-generated Java Files
```
src/main/java/mtsofficialpack/ForgePackLoader.java  ← Not needed in NeoForge 1.21.1
```

### 2. Legacy Compiler Files
```
PackCompiler.java     ← Legacy tool, causes issues
compile.bat          ← Uses PackCompiler, problematic
compile.sh           ← Unix version of compile.bat
```

### 3. Duplicate/Test Models
```
assets/mtsofficialpack/models/item/
├── wheellarge_test1_direct_mtl.json   ← Test file
├── wheellarge_test2_minimal.json      ← Test file
├── wheellarge_test3_flipv.json        ← Test file
├── wheellarge_test4_bigtrans.json     ← Test file
├── wheellarge_3d_backup.json          ← Backup, not needed
├── wheelmedium_3d_backup.json         ← Backup, not needed
└── wheellargee.json                   ← Typo/duplicate
```

### 4. Auto-generated Bridge Files
```
assets/mts/models/item/
└── [Any flat 2D models that were auto-generated]
    Example: {"parent":"mts:item/basic","textures":{"layer0": "..."}}
```

## 🔧 Proper Development Process

### Step 1: Create Model in Blockbench
1. Design your 3D item model
2. Apply textures with proper UV mapping
3. Export as JSON (File → Export → Minecraft Java Block/Item Model)

### Step 2: Place Files
1. Copy JSON model to `assets/mts/models/item/mtsofficialpack.{itemname}.json`
2. Copy texture PNG to `assets/mtsofficialpack/textures/item/{itemname}.png`

### Step 3: Verify Model Structure
Your JSON should have complex 3D elements, not just:
```json
// ❌ BAD - Flat 2D auto-generated
{"parent":"mts:item/basic","textures":{"layer0": "..."}}

// ✅ GOOD - Proper 3D model
{
    "credit": "Made with Blockbench",
    "texture_size": [64, 64],
    "textures": {...},
    "elements": [
        {
            "from": [...],
            "to": [...],
            "faces": {...}
        }
    ],
    "display": {...}
}
```

### Step 4: Build and Test
```bash
# Build the pack
./gradlew build

# Copy to mods folder for testing
cp "build/libs/MTS Official Pack-V*.jar" "../MinecraftTransportSimulator-1.21.1/run/mods/"

# Run client to test
cd ../MinecraftTransportSimulator-1.21.1
./gradlew runClient
```

## 🎯 Key Differences: Legacy vs Modern

| Aspect | Legacy (with PackCompiler) | Modern (Direct Placement) |
|--------|---------------------------|---------------------------|
| Model Creation | Auto-generated from PNGs | Created in Blockbench |
| Model Quality | Flat 2D items | Full 3D items |
| Build Command | compile.bat | ./gradlew build |
| Java Loader | Required ForgePackLoader.java | Not needed |
| Namespace | Complex dual namespace | Simple MTS namespace |
| Texture Loading | Often broken | Reliable |

## 📝 Summary

The modern development experience is much simpler:
1. **Create** 3D models in Blockbench
2. **Place** files in correct folders
3. **Build** with gradlew
4. **Skip** PackCompiler entirely

This approach avoids all the legacy complications and produces better-looking items with proper 3D models that work reliably in NeoForge 1.21.1.