# DesignOS brand direction · Draft v0.1

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

Canonical tokens: ../dist/assets/tokens.json
