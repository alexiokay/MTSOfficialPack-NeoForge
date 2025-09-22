# Content Pack Cleanup Recommendations

## Files That Can Be Safely Removed

### 1. Legacy Java Files
These files are no longer needed in NeoForge 1.21.1:

```
✗ PackCompiler.java                              - Legacy auto-generator, causes issues
✗ PackCompiler_updated.java                      - Modified version, still problematic
✗ src/main/java/mtsofficialpack/ForgePackLoader.java - Not needed, NeoForge handles loading
```

### 2. Legacy Build Scripts
```
✗ compile.bat                                    - Uses problematic PackCompiler
✗ compile.sh                                     - Unix version of compile.bat
✗ copy_3d_models.bat                            - Workaround script, not needed with proper workflow
```

### 3. Test and Backup Models
In `assets/mtsofficialpack/models/item/`:
```
✗ wheellarge_test1_direct_mtl.json              - Test file
✗ wheellarge_test2_minimal.json                 - Test file
✗ wheellarge_test3_flipv.json                   - Test file
✗ wheellarge_test4_bigtrans.json                - Test file
✗ wheellarge_3d_backup.json                     - Backup
✗ wheelmedium_3d_backup.json                    - Backup
✗ wheellargee.json                              - Typo/duplicate of wheellarge.json
✗ wheellarge_nolegacy.json                      - Testing file
```

### 4. Generated Documentation (Optional)
These were created for debugging and can be removed once stable:
```
? contentpack-missing-textures-gui.md           - Debug documentation
? texture-rendering-analysis.md                 - Debug analysis
? model-loading-solution-analysis.md            - Debug analysis
? temp-in-car-fixes-learned.md                 - Temporary notes
? proper-player-model-behaviour-in-car.txt      - Temporary notes
? compatible-mods.txt                           - May want to keep for reference
```

## Files That MUST Be Kept

### 1. Core Build Files
```
✓ build.gradle                                  - Gradle build configuration
✓ gradlew / gradlew.bat                        - Gradle wrapper scripts
✓ settings.gradle                               - Gradle settings
✓ gradle.properties                             - Build properties
```

### 2. Mod Metadata
```
✓ src/main/resources/META-INF/mods.toml        - Mod information for NeoForge
✓ src/main/resources/META-INF/accesstransformer.cfg - If using access transformers
✓ src/main/resources/pack.mcmeta               - Resource pack metadata
```

### 3. Content Pack Resources
```
✓ src/main/resources/assets/mtsofficialpack/   - All pack content
  ├── textures/                                - All textures
  ├── objmodels/                               - 3D OBJ models for vehicles/parts
  ├── models/item/                             - Keep clean 3D JSON models only
  ├── jsondefs/                                - Item/vehicle definitions
  └── sounds/                                   - Sound files

✓ src/main/resources/assets/mts/
  └── models/item/                             - Properly named item models
      └── mtsofficialpack.*.json               - Keep all working 3D models
```

## Recommended Cleanup Commands

```bash
# Remove legacy files
rm PackCompiler.java
rm PackCompiler_updated.java
rm compile.bat
rm compile.sh
rm copy_3d_models.bat
rm -rf src/main/java/mtsofficialpack

# Remove test models
cd src/main/resources/assets/mtsofficialpack/models/item
rm wheellarge_test*.json
rm wheellarge_3d_backup.json
rm wheelmedium_3d_backup.json
rm wheellargee.json
rm wheellarge_nolegacy.json

# Clean build artifacts
./gradlew clean
```

## Why These Files Exist (Historical Context)

1. **PackCompiler.java**: Created for older Forge versions that required Java mod loader classes. Would scan PNGs and auto-generate item models.

2. **ForgePackLoader.java**: A simple Java class with @Mod annotation that Forge required to recognize the pack as a mod.

3. **Test models**: Created during debugging to figure out why OBJ models weren't loading (texture path issues, MTL references, etc.)

4. **compile.bat**: Wrapper around PackCompiler to make building "easier" but actually made it more complex.

## Modern Clean Structure

After cleanup, your pack should look like:
```
MTSOfficialPack-1.21.1/
├── build.gradle
├── gradle.properties
├── settings.gradle
├── gradlew / gradlew.bat
├── MODERN_DEVELOPMENT_GUIDE.md
└── src/main/
    └── resources/
        ├── META-INF/
        │   └── mods.toml
        ├── pack.mcmeta
        └── assets/
            ├── mts/models/item/        ← 3D item models
            └── mtsofficialpack/        ← Everything else
```

## Summary

Removing these legacy files will:
- Eliminate confusion about which build system to use
- Prevent accidental overwriting of 3D models
- Simplify the development workflow
- Reduce repository size
- Make the codebase cleaner for other developers

The modern approach is simpler: just place your Blockbench models in the right folder and use `./gradlew build`.