# NeoForge 1.21.1 OBJ Model Setup

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
