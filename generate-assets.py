from pathlib import Path
import json, math, re
p=Path(__file__).parent; a=p/'dist/assets'
tokens={'status':'Draft v0.1','brandName':'DesignOS (temporary)','logoStatus':'Placeholder only','color':{'light':{'background':'#F8F9F6','surface':'#FFFFFF','text':'#172724','textSecondary':'#586661','action':'#006B60','actionLabel':'#F8F9F6','divider':'#D8DFDA','inputBoundary':'#728078'},'dark':{'background':'#121B19','surface':'#1C2824','text':'#F3F6F1','textSecondary':'#B0BEB5','action':'#9DE4C3','actionLabel':'#172724','divider':'#405047','inputBoundary':'#8D9D92'},'brand':{'teal':'#006B60','mint':'#C2F4D7','ink':'#172724','canvas':'#F8F9F6'},'semantic':{'light':{'success':'#176B43','warning':'#885B00','error':'#B93239','info':'#255EB8'},'dark':{'success':'#9DE4C3','warning':'#F2CD7C','error':'#FFADB0','info':'#ABC9FF'}}},'typography':{'display':'Manrope, Arial, sans-serif','body':'DM Sans, Arial, sans-serif','mono':'IBM Plex Mono, monospace','sizes':[12,14,16,18,28,40,64,128],'bodyLineHeight':1.5},'spacing':[4,8,12,16,24,32,48,64],'radius':{'control':6,'card':10,'panel':16,'chip':999},'stroke':{'divider':1,'icon':1.75,'focus':3},'motion':{'feedbackMs':180,'transitionMs':280,'expressionMs':800,'easing':'cubic-bezier(0.22, 1, 0.36, 1)','reducedMotion':'No scroll transforms. Show resolved states. Remove spatial animation.'}}
(a/'tokens.json').write_text(json.dumps(tokens,indent=2))
guidance='''# DesignOS brand direction · Draft v0.1

DesignOS is a temporary name for an AI creative workspace for designs, images, artifacts and brand exploration. The logo is explicitly a placeholder. Do not treat the mark or name as final.

## Idea
Room for ideas. Structure for the work; space for the unexpected.
Clear by nature. Open to possibility. Made to move forward.

## Color
Monochrome surfaces dominate the product. Deep teal identifies actions in light mode; pale teal identifies actions in dark mode. Mint is an expressive background with dark Ink text. White on Mint is prohibited for text. No rainbow gradients or low-contrast pale text. Gradients are limited to teal/mint artwork, never control backgrounds or text reading surfaces.
Use tokens.json for exact semantic values. Status requires a label or icon as well as color.

## Type
Manrope: display and headings, 550–700. DM Sans: body and product UI, 400–600. IBM Plex Mono: code and secondary metadata. Fonts use the SIL Open Font License; preserve licenses when self-hosting. Fetch fonts from official distributions.
Use 16 px reading text, 14 px controls and 12 px secondary metadata only. Default body line height 1.5. Display tracking -0.05em to -0.07em; normal tracking in UI copy. Fallbacks: Arial/sans-serif; monospace for code.

## Form
4 px spacing base; preferred steps 4,8,12,16,24,32,48,64.
Radius: controls 6 px, product cards 10 px, brand panels 16 px. Full rounding for chips only. Brand-site navigation may be more expressive.
Decorative dividers 1 px; original icons 1.75 px at 24 px; focus outline 3 px.
Use sufficient boundary contrast for fields and essential controls. Subtle dividers must not be the sole interactive affordance.

## Imagery
Original rounded geometric forms, layered planes, tonal orbital textures. Matte materials and one directional light. Meaningful transformation or arrangement. No generic robot brains, unrelated planets, rainbow clouds, or stock-photo filler.
Photography, when used: real making and reviewing, directional natural light, honest color, uncluttered compositions. UI images show real workflows; label illustrative content.

## Icons
24 px base grid. 1.75 px stroke. Rounded joins/caps. 16/20/24 px output sizes checked optically. Familiar meanings and text labels for ambiguous controls. Icons never replace accessible names.

## Motion
Ease cubic-bezier(0.22,1,0.36,1). Feedback 180 ms, transitions 280 ms, expression 800 ms. Product motion explains state changes; brand motion can assemble fragments into a coherent composition. Natural scrolling. Honor prefers-reduced-motion. Never show invented progress percentages or use decorative animation as an honest generation status.

## Voice
Clear, encouraging and honest. State the useful action. Errors explain what happened and what to do next. Avoid inflated AI claims, forced humor and judgmental empty states.
Examples: Create project. Your brand kit is ready. We couldn’t save your changes. Your draft is still here; try saving again.

## Application checks
Validate dashboard, launch poster and presentation title. Check light/dark mode, 200% zoom, keyboard navigation, narrow screens, long labels, loading, empty and error states. Use normal-text contrast >=4.5:1; large text and essential graphical controls >=3:1. Do not rely on color alone.

## Open decisions
Name, final logo, brand owner and approval remain open. Digital-first RGB palette. CMYK/Pantone are not approved; convert and proof only if print enters scope. Broad rollout requires review of this proposal.
'''
(a/'brand-guidance.md').write_text(guidance)
svg=lambda body,w=800,h=800:f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{body}</svg>'
orb='<defs><radialGradient id="g" cx="35%" cy="30%"><stop stop-color="#C2F4D7"/><stop offset=".5" stop-color="#499D80"/><stop offset="1" stop-color="#004E46"/></radialGradient><clipPath id="c"><circle cx="400" cy="400" r="275"/></clipPath></defs><rect width="800" height="800" fill="#006B60"/><circle cx="400" cy="400" r="275" fill="url(#g)"/><g clip-path="url(#c)" fill="none" stroke="#C2F4D7" stroke-width="1.8" opacity=".65">'+''.join(f'<ellipse cx="{400+i*2}" cy="400" rx="{30+i*7}" ry="275" transform="rotate(-28 400 400)"/>' for i in range(1,40))+'</g>'
(a/'orbit.svg').write_text(svg(orb))
mark='<title>Temporary DesignOS construction mark — not final logo</title><rect width="128" height="128" rx="20" fill="#006B60"/><g fill="#C2F4D7"><path d="M28 28h31v31H28V43a15 15 0 0 1 15-15Z"/><path d="M69 28h31v31H69Z M28 69h31v31H28Z M69 69h31v16a15 15 0 0 1-15 15H69Z"/></g>'
(a/'placeholder-mark.svg').write_text(svg(mark,128,128))
(a/'launch-poster.svg').write_text(svg('<rect width="1080" height="1080" fill="#C2F4D7"/><g fill="#172724" font-family="Arial,sans-serif"><text x="70" y="95" font-size="24">DesignOS / A creative workspace</text><text x="70" y="280" font-size="115" font-weight="bold" letter-spacing="-7">From a thought.</text><text x="70" y="410" font-size="115" font-weight="bold" letter-spacing="-7">To a thing.</text><text x="70" y="1000" font-size="24">Make room for ideas.</text></g><circle cx="760" cy="730" r="200" fill="#006B60"/><g fill="none" stroke="#C2F4D7" opacity=".6">'+''.join(f'<ellipse cx="760" cy="730" rx="{i*9}" ry="190" transform="rotate(-25 760 730)"/>' for i in range(1,23))+'</g>',1080,1080))
(a/'presentation.svg').write_text(svg('<rect width="1600" height="900" fill="#172724"/><g fill="#C2F4D7" font-family="Arial,sans-serif"><text x="90" y="100" font-size="24">DesignOS / Brand direction</text><text x="90" y="400" font-size="120" font-weight="bold" letter-spacing="-7">A clear canvas.</text><text x="90" y="540" font-size="120" font-weight="bold" letter-spacing="-7">An open mind.</text><text x="90" y="810" font-size="22">Identity exploration · 2026</text></g>',1600,900))
(a/'product-concept.svg').write_text(svg('<rect width="1440" height="900" fill="#F8F9F6"/><path d="M230 0v900" stroke="#D8DFDA"/><g fill="#172724" font-family="Arial,sans-serif"><text x="40" y="70" font-size="28" font-weight="bold">DesignOS</text>'+''.join(f'<text x="40" y="{170+i*55}" font-size="20">{s}</text>' for i,s in enumerate(['Home','Projects','Prompts','Artifacts','Assets','Brands','Handoff']))+'<text x="290" y="140" font-size="46" font-weight="bold">Your next great idea starts here.</text><text x="290" y="190" font-size="22">A place for your projects. Space for your process.</text></g>'+''.join(f'<rect x="{290+i*355}" y="260" width="325" height="340" rx="12" fill="#FFFFFF" stroke="#D8DFDA"/><rect x="{305+i*355}" y="275" width="295" height="220" rx="8" fill="{["#006B60","#C2F4D7","#172724"][i]}"/><text x="{310+i*355}" y="545" font-family="Arial,sans-serif" font-size="23" fill="#172724">{["Brand exploration","Editorial website","Campaign assets"][i]}</text>' for i in range(3)),1440,900))
# Original outline paths are extracted from the same app source so downloads match previews.
s=(p/'dist/app.js').read_text(); obj=s[s.index('const paths={')+len('const paths={'):s.index('};\nfunction icon')]
icons=re.findall(r"(?:^|,)(\w+):'([^']*)'",obj)
(a/'icons.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg">'+''.join(f'<symbol id="{n}" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">{v}</g></symbol>' for n,v in icons)+'</svg>')
for name,section in [('colors','Color'),('typography','Type'),('imagery','Imagery'),('motion','Motion')]:
 (p/f'identity/{name}.md').write_text(guidance+'\nCanonical tokens: ../dist/assets/tokens.json\n')
(p/'identity/logo/README.md').write_text('Placeholder only. Final logo intentionally unresolved. See ../../dist/assets/placeholder-mark.svg. Do not publish as a final identity. Digital primary/wordmark/symbol/monogram and PNG exports remain deferred until naming and mark approval.')
(p/'identity/iconography/README.md').write_text('Original 24 px outline icons. 1.75 px strokes, rounded joins/caps. Downloadable individually on the iconography page and as ../../dist/assets/icons.svg.')
(p/'identity/applications/README.md').write_text('Three SVG application concepts: ../../dist/assets/product-concept.svg, ../../dist/assets/launch-poster.svg and ../../dist/assets/presentation.svg. All are illustrative draft applications.')
(p/'README.md').write_text('# DesignOS brand website\n\nStatic HTML/CSS/JS. Run `python3 -m http.server 4173 --directory dist` from this directory. No build dependencies.\n\nRoutes use hashes so each guideline page can be linked directly on static hosting. Theme preference persists locally. Fonts are fetched from Google Fonts with system fallbacks. Product actions are clearly illustrative.\n\nThe editable identity and downloads live in identity/ and dist/assets/. Name and mark remain placeholders.\n')
print('Created tokens, guidance, original SVG artwork and 3 application mockups.')
