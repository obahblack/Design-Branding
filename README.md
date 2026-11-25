# DesignOS brand website

Static HTML/CSS/JS. Run `python3 -m http.server 4173 --directory dist` from this directory. No build dependencies.

Routes use hashes so each guideline page can be linked directly on static hosting. Theme preference persists locally. Fonts are fetched from Google Fonts with system fallbacks. Product actions are clearly illustrative.

The editable identity and downloads live in identity/ and dist/assets/. Name and mark remain placeholders.

## Architectural heroes and usage reference

`dist/architecture.js` and `dist/architecture.css` define measured 12-column hero compositions, sequential title/line/example entry, icon usage scrollers and visible product specification tables. The imagery page uses a generated unpopulated landscape and an original gradient field. Image-generation provenance and the exact built-in prompt are in `identity/imagery-generation.txt`.
