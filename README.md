# DesignOS brand website

Static HTML/CSS/JS. Run `python3 -m http.server 4173 --directory dist` from this directory. No build dependencies.

Routes use hashes so each guideline page can be linked directly on static hosting. Theme preference persists locally. Fonts are fetched from Google Fonts with system fallbacks. Product actions are clearly illustrative.

The editable identity and downloads live in identity/ and dist/assets/. Name and mark remain placeholders.

## Violet palette revision

`dist/color-system.js` and `dist/color-system.css` replace the folding swatches with overlapping Core, Accent and Neutral rows. Pointer movement creates a distance-based wave; keyboard focus reveals each color; selection copies its value. Touch rows scroll horizontally.

Primary is Violet #6646D8. Accents include lavender, cobalt, sky, coral, peach, amber, ochre, raspberry, rose, plum and lilac. Semantic status colors remain role-based. The catalogue is exported in dist/assets/palette.json and included in theme tokens.

New imagery: dist/assets/landscape-violet.png, generated with the built-in tool. Exact prompt: identity/imagery-generation-violet.txt.
