# Editorial Theme Project Notes

## Design Direction
- **Theme**: Minimalist Editorial / Editorial Brutalism (Magazine style).
- **Vibe**: Clean, typography-heavy, high contrast, elegant but structural.
- **Color Palette**:
  - `cream`: `#F5F2EB` (Warm, off-white paper background)
  - `navy`: `#1A365D` (Deep blue ink, used instead of pure black for softer contrast)
- **Typography**:
  - **Primary**: Standard Sans-Serif (`font-sans`) for body and structural text.
  - **Headlines**: Serif (`font-serif`) for massive, bold, structural text (e.g., "GABRIEL", "SERVICES").
  - **Signature/Accent**: `font-mayonice` (custom `Mayonice.ttf` loaded via `@font-face`), used for the cursive "Ryan" text.

## Architecture & Layout
- **Single Page Scroll**: The site has been refactored in `App.jsx` into a true one-pager. The `<Routes>` now renders an `<IndexPage />` that stacks all sections (`Home`, `About`, `Work`, `Service`, `Experience`, `Contact`) vertically.
- **Navigation**: The `FloatingDock` (bottom navigation) has been deliberately **removed** to maintain a clean, immersive editorial reading experience.
- **Scroll Progress**: A thin blue line (`#213555`) exists at the top of the screen to indicate scroll progress.

## Accomplished Work
- **Hero Section (`Home`)**:
  - Fully complete and pixel-perfect across Desktop and Mobile.
  - Background split (Cream right, Navy left) using `clip-path`.
  - Portrait image is cleanly isolated with background removed.
  - **Z-Index Fix**: The "SCROLL TO EXPLORE" hint is placed in Layer 4 (`z-30`) to ensure it renders *above* the user's portrait (`z-20`). It uses a dual-color split effect matching the background.

## Next Steps for the New Agent
1. **Redesign the `About` Section**:
   - This is the immediate next priority.
   - **User Request / Idea**: Format the typography like a Vogue magazine article (e.g., 2-column text layout, elegant drop caps, strong typographic hierarchy) to seamlessly continue the editorial vibe from the Hero section.
2. **Continue Section-by-Section Polish**:
   - Apply the same editorial treatment to `Work`, `Service`, `Experience`, and `Contact`.
   - Ensure the `bg-cream` and `bg-navy` classes are used effectively to create alternating blocks of content.
3. **Impeccable Skill**:
   - The user relies on the `impeccable` design critique skill to audit and refine the UI. Run it on the remaining sections as needed.

## Technical Quirks to Remember
- **Tailwind v4 Configuration**: Custom colors (`--color-cream`, `--color-navy`) and custom fonts (`--font-mayonice`) are defined in the `@theme` block inside `src/index.css`. DO NOT overwrite or remove this block.
- **Mayonice Font**: The `@font-face` declaration is manually injected at the top of `src/index.css`.
- **Python Regex**: When modifying React components using Python scripts, always remember to use `re.DOTALL` to match multiline JSX tags.
