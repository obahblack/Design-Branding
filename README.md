# DesignOS brand website

Static HTML/CSS/JS. Run `python3 -m http.server 4173 --directory dist` from this directory. No build dependencies.

Routes use hashes so each guideline page can be linked directly on static hosting. Theme preference persists locally. Fonts are fetched from Google Fonts with system fallbacks. Product actions are clearly illustrative.

The editable identity and downloads live in identity/ and dist/assets/. Name and mark remain placeholders.

## Visual storytelling revision

`dist/immersive.js` and `dist/immersive.css` provide individual visual detail pages, scroll scenes, named illustrative cursors, recolorable compositions and compact usage documentation. `app.js` retains shared UI helpers, theme handling, resources and downloads. All pages remain linkable via hash routes.

Scroll scenes use passive listeners and requestAnimationFrame. Reduced motion follows the OS preference and a persistent page-level toggle. Typography roles now distinguish bold product headings from body text.
