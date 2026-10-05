# Task Prompt: Blender to Roblox Material Pack

You have Blender MCP access. Build a set of production-quality, Roblox-ready assets and tiling material sets in Blender, bake them to PBR texture maps, and deliver everything with an import checklist and a Studio setup script.

You cannot upload to Roblox yourself. Your deliverable is files on disk plus the instructions and Luau script needed to wire them up in Studio.

---

## 1. Non-negotiable Roblox target specs

Verify these against current Roblox Creator Hub docs before you start, but treat them as the working baseline:

**Two texture systems. Choosing the wrong one is the most common failure.**

| System | Applies to | Tiles on resize? | Use it for |
|---|---|---|---|
| `SurfaceAppearance` | MeshPart only, follows the mesh UVs | No, locked to UV layout | Unique props: boxes, net panels, glass panes with baked detail |
| `MaterialVariant` | Regular Parts, MeshParts, Terrain | Yes, via `StudsPerTile` | Tileable surfaces: diamond plate, any material that must survive arbitrary part scaling |
| `Texture` object | BasePart face | Yes, via `StudsPerTileU/V` | Color-only fallback, no PBR. Avoid unless a PBR path is impossible |

- `MaterialVariant` also carries physical properties (friction, density) inherited from a chosen base material. `SurfaceAppearance` does not.
- `MaterialVariant` tiles outward from the **center** of a face, not a corner. Sizing a part to a non-odd multiple of `StudsPerTile` shifts the pattern. Note this in the docs you write.
- `SurfaceAppearance` maps: `ColorMap`, `NormalMap`, `RoughnessMap`, `MetalnessMap`, and an emissive control. Roughness is grayscale, white is rough. Metalness is grayscale, white is metal.
- Roblox uses the **metalness workflow only**. No specular/gloss.
- Normal maps must be **tangent-space, OpenGL convention (green channel up)**. Blender's default Cycles normal bake is already OpenGL. Do not flip green.
- Texture resolution: up to 4096x4096 is supported, 1024x1024 is the practical target for most surfaces. Use 512 for small props. Always square, always power of two.
- Mesh budget: hard cap 20,000 triangles per MeshPart, target under 10,000. Aim far lower for these assets.
- Scale: 1 Roblox stud = 0.28 metres. Model at 1 Blender unit = 1 stud so importer scaling is predictable, and state the intended stud dimensions for every asset.
- Apply all transforms before export (`Ctrl+A > All Transforms`, or `bpy.ops.object.transform_apply`). Unapplied scale is the top cause of broken imports.
- Export `.fbx` with Path Mode `Copy`, Embed Textures on, Apply Scalings `FBX Unit Scale`. Also emit a `.glb` alongside each asset as a fallback. Export maps as separate PNGs regardless, since they get uploaded individually.

**Alpha behaviour, this matters for nets and glass:**

- `AlphaMode = Overlay` (default): the ColorMap composites over the MeshPart's own `Color` wherever alpha is present.
- `AlphaMode = Transparency`: alpha genuinely cuts through the mesh, the base color is not revealed.
- For **hard-edged cutouts** (netting, mesh, chain-link, lace): `AlphaMode = Transparency` and `MeshPart.Transparency = 0`. Fully opaque pixels then get proper depth occlusion, which keeps depth of field, glass, and water reflection behaving correctly.
- For **soft or semi-transparent gradients** (dirty windows, grime, smudges): `AlphaMode = Transparency` and `MeshPart.Transparency` set to at least 0.02. This improves blending but breaks some depth effects.
- Never pre-multiply alpha. Preserve RGB color inside fully transparent pixels or you get dark fringing on filtered edges.

---

## 2. Global Blender working rules

1. **Everything is scripted.** Write each asset as a standalone, re-runnable Python file under `output/scripts/`. No manual clicking that you cannot reproduce. The user must be able to change a parameter and rebuild.
2. **Parameterise.** Tread spacing, box dimensions, wire gauge, mesh aperture, rib pitch, and so on go at the top of each script as named constants with comments.
3. **Bake settings:** Cycles, GPU if available, 128 to 512 samples depending on map, bake margin 16px, "Extend" margin type.
   - Color: bake type `Diffuse`, Direct and Indirect **off**, Color only. No lighting baked in.
   - Normal: bake type `Normal`, space Tangent, R+ G+ Z+.
   - Roughness: bake type `Roughness`.
   - Metalness: Cycles has no metalness bake pass. Route the metallic value into an Emission shader and bake `Emit`, or write a flat constant map when the surface is uniformly metal or non-metal.
   - AO and curvature: bake separately and use them to drive edge wear and dirt in the ColorMap. Do not ship AO as its own map, Roblox has no AO slot.
4. **Color spaces on save:** ColorMap as sRGB. Normal, Roughness, Metalness as Non-Color. Getting this wrong is silent and ruins the result.
5. **Seamless tiling method:** model one tile, array it 3x3, then bake **only the centre tile** with the neighbours present. This guarantees edges match. Verify by tiling the baked result 4x4 in a test render and looking for visible seams or an obvious repeating hero feature.
6. **Naming convention**, exact, because it makes the Studio wiring unambiguous:
   `AssetName_ColorMap.png`, `AssetName_NormalMap.png`, `AssetName_RoughnessMap.png`, `AssetName_MetalnessMap.png`
7. **Self-review loop.** After each asset: render a turntable or a flat-lit preview to `output/previews/`, look at it with the screenshot tool, and fix what is wrong before moving on. Specifically check for stretched UVs, seams, normal map inversion (lit from above, raised features must read as raised), and texel density consistency.
8. Keep a running `output/NOTES.md` recording decisions, real-world dimensions each tile represents, and recommended `StudsPerTile` values.

---

## 3. The assets

### 3.1 Cardboard boxes (storage room)

Route: **MeshPart + SurfaceAppearance.** Unique UVs, not tiling.

Build **four variants**, each under 1,500 triangles:

- **A**: sealed box, taped seam across the top, slight bulge, small corner dents.
- **B**: open box, four flaps folded outward at slightly uneven angles, corrugation visible on the flap cut edges.
- **C**: crushed or sagging box, one corner collapsed, top bowed inward as if something heavy sat on it.
- **D**: long flat box, different proportions so a stack does not look cloned.

Requirements:

- Bevel every edge slightly. Perfectly sharp cardboard edges are the single clearest tell of a low-effort asset. Soft, slightly rounded, slightly frayed.
- Give the flap cut edges actual visible corrugation, either as geometry on the exposed edge or baked into the normal map.
- Suggested sizes in studs: roughly 4x4x4, 6x4x4, 5x5x3, 8x4x2. State the exact values.
- ColorMap: base kraft brown with per-variant hue and value shift so a stack reads as varied. Add subtle fibre grain, a slightly darker tone along fold lines, AO in the creases, edge wear where the bevels catch light (drive this with a baked curvature map), scuffs on the lower faces, and packing tape as a distinct semi-gloss strip.
- Do **not** put readable brand logos, real company marks, or text you did not invent. Generic printed markings only: fragile arrows, handling symbols, a plain rectangle shipping label, a barcode-like block. Keep them plausible and generic.
- Roughness: cardboard is uniformly rough, roughly 0.75 to 0.9. Tape is much smoother, roughly 0.25 to 0.4. This contrast is what sells the material. Vary roughness slightly with the fibre noise.
- Metalness: flat black, cardboard is fully dielectric. You may ship a constant value instead of a map to save an upload.
- 1024x1024 per variant. If a shared trim-sheet layout is feasible across all four, do that instead and note it, since one texture set for four boxes is a real memory win.

### 3.2 Diamond plate (checker plate / tread plate / durabar)

Route: **MaterialVariant.** This is the one that must survive arbitrary resizing, so it is a tiling material, not a mesh.

- Build the classic pattern: raised elongated lozenge treads in pairs, each pair rotated roughly 90 degrees from its neighbours, arranged in a staggered grid. Get the real proportions right, the treads are long, low, with sloped ends and a flat top, not pyramids.
- Authoring approach: high-poly tile with real tread geometry on a flat base plane, arrayed 3x3, baked down to a flat plane. Never model treads as a texture-only guess, bake from real geometry so the normal map is correct.
- Decide the real-world footprint of one tile and record it. A tile representing 2m x 2m is a sensible default. At 0.28m per stud that is roughly 7 studs, so recommend `StudsPerTile = 7` and note that parts sized to odd multiples of that value keep the pattern centred cleanly.
- Ship **three finish variants** sharing the same normal map, differing in color and roughness:
  - **Polished aluminium**: bright, low roughness (0.2 to 0.35), high metalness.
  - **Painted industrial**: safety grey or yellow paint, roughness 0.5 to 0.65, low metalness, chipped paint on the tread tops exposing metal beneath.
  - **Worn steel**: darker, rust bloom in the recesses, scuffed and burnished tread tops where feet land, roughness varying strongly across the surface (0.3 on worn tops, 0.8 on rusted recesses).
- Roughness variation is what makes metal read as real. Uniform roughness always looks like plastic. Make sure the recesses between treads are dirtier and rougher than the tread tops.
- Metalness: near 1.0 on bare metal, drop toward 0 wherever paint or heavy rust covers it.
- 1024x1024. Include a 2048 version of the color and normal maps for close-up hero use, noted as optional.
- Also export a **single tile mesh with real geometry** (low poly, under 600 tris) for close-up or edge use where a normal map alone would break silhouette.

### 3.3 Glass varieties

Glass on Roblox is a decision tree, not one material. Deliver all of the following and document when to use each.

Known engine constraints to write into the docs:
- The built-in `Glass` material gives Fresnel reflection and multiplicative tint, but it **will not render particles, terrain water, or other transparent parts behind it**. This is a hard engine limitation, not a bug you can texture around.
- A common workaround for that case is `Plastic` with high `Reflectance` and tuned `Transparency`, which loses Fresnel but composites normally.

Produce:

1. **Clear float glass** (no mesh needed). Just a documented Part recipe: `Material = Glass`, `Transparency` 0.7 to 0.85, `Reflectance` 0.05 to 0.15, thin part depth. Provide two or three tuned presets.
2. **Frosted / sandblasted glass.** MeshPart + SurfaceAppearance. ColorMap near-white with alpha around 0.35 to 0.5, high roughness (0.6 to 0.8), fine irregular surface noise in the normal map. `AlphaMode = Transparency`, `MeshPart.Transparency = 0.05`.
3. **Reeded / ribbed / fluted glass.** Build the ribs as **real geometry**, a plane with vertical half-cylinder ribs, under 800 tris. Real ribs catch light far better than a normal map here because the silhouette matters. Ship both a geometry version and a normal-mapped flat version, and say in the notes that the geometry version is worth the tris.
4. **Wired safety glass.** Flat pane, embedded square wire grid. The grid goes in the ColorMap with alpha and in the normal map. Slight green tint. This is the warehouse and stairwell look.
5. **Dirty / grimy warehouse glass.** Tileable, so ship it as a **MaterialVariant** as well as a SurfaceAppearance version. Dust accumulation heavier at the edges and bottom, streaks, water spots, fingerprints, a few small chips. Alpha varying from about 0.15 in clean centres to 0.6 in the grimiest corners. Roughness varying with the grime.
6. **Tinted / tempered glass.** Green-edge tempered look and a smoked grey variant. Mostly a tint and reflectance recipe rather than a texture, document it as presets.

For every textured glass entry, state the exact `AlphaMode` and `MeshPart.Transparency` pairing, since that combination is what determines whether it renders correctly.

### 3.4 Mesh nets

Route: **alpha cutout on low-poly geometry.** `AlphaMode = Transparency`, `MeshPart.Transparency = 0`.

Build **four types**, each as a flat tileable panel plus a baked texture set:

- **Chain-link fence**: interwoven diamond wire pattern. Bake from real high-poly interwoven wire geometry so the over-under weave and the wire's cylindrical shading are correct. A hand-drawn chain-link texture always looks flat.
- **Industrial mesh grate / expanded metal**: flattened diamond apertures with the characteristic angled cut edges.
- **Cargo / rope net**: thicker knotted rope, visible fibre twist, larger apertures.
- **Fine window screen / insect mesh**: tight square weave, very fine, mostly used at a distance.

Requirements:

- The geometry the texture sits on is a **single flat plane or a simple frame**, a handful of triangles. All the detail lives in the alpha and normal maps.
- Alpha must be **hard-edged**, near-binary, not a soft gradient. Soft alpha on a net reads as fog. Keep a one-pixel transition at most.
- RGB must be filled in behind the transparent regions, do not leave black there, or filtering will pull dark halos into the wire edges.
- Normal map must carry the wire's round cross-section so raking light picks out individual strands.
- Double-sided consideration: Roblox does not render backfaces on a single plane. Either build the panel as two back-to-back planes with flipped normals, or document that the net must be viewed from one side. Recommend the two-plane approach and note the tris cost.
- Also provide **real-geometry versions** of chain-link and cargo net for close-up use, under 3,000 tris each, since alpha cards break down when the player is right against them.
- Tileable in both axes. Verify with a 4x4 tile test render.
- Note recommended `StudsPerTile` if a MaterialVariant version is also shipped.

---

## 4. Deliverables

```
output/
  scripts/          one re-runnable .py per asset
  meshes/           .fbx and .glb per asset
  textures/         AssetName_ColorMap.png etc, PNG, correct color spaces
  previews/         render per asset, plus tiling verification renders
  studio_setup.lua  see below
  IMPORT_GUIDE.md
  NOTES.md
```

**`studio_setup.lua`**: a Studio script the user runs once after uploading the images. It should have a clearly marked table at the top where asset IDs get pasted, then programmatically create every `MaterialVariant` inside `MaterialService` with the correct base material, `StudsPerTile`, and physical properties, and create template Parts and MeshParts with correctly configured `SurfaceAppearance` children for the mesh assets. Comment it properly.

**`IMPORT_GUIDE.md`**: step by step. Uploading images and getting asset IDs, the 3D Importer settings to use, where to check the Output window for the "Successfully uploaded compressed SurfaceAppearance" confirmation, how to verify the result at multiple graphics quality levels, and the `AlphaMode` / `Transparency` pairing table. Include the gotchas: MaterialVariant centre-tiling, SurfaceAppearance properties being mostly non-scriptable at runtime, and unapplied transforms breaking scale.

---

## 5. Order of work and check-ins

Work in this order, and **stop and show the user a preview render after each one** before continuing:

1. Diamond plate. It is the highest-value asset and it validates the whole tiling and baking pipeline. Get this right first.
2. Cardboard boxes.
3. Mesh nets.
4. Glass varieties.
5. Studio script and documentation.

At each check-in, state briefly what you built, show the preview, and flag anything you had to compromise on. Do not batch all four and present at the end.

---

## 6. Standing instructions

- If a Blender API call fails or a bake produces something wrong, diagnose it rather than working around it with a lower-quality substitute. Say what broke.
- Verify Roblox specs against current documentation rather than trusting this brief blindly. If something here has changed, say so and follow the current docs.
- Prefer real baked geometry over hand-authored or procedurally guessed normal maps everywhere. This is the difference between the assets looking real and looking like a texture pack.
- Keep triangle counts honest and report them per asset.
- No em dashes in any documentation you write.
