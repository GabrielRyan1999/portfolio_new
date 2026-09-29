import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Add Sparkle component
sparkle = '''const Sparkle = ({ className }) => (
  <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" className={className}>
    <path d="M12 0L12.5 11.5L24 12L12.5 12.5L12 24L11.5 12.5L0 12L11.5 11.5L12 0Z" fill="currentColor"/>
  </svg>
);

const fadeUp = {'''
content = content.replace('const fadeUp = {', sparkle)

# Replace the text-based corners with Sparkles
old_corners = r'\{\/\* Top Left Meta \*\/\}[\s\S]*?\{\/\* Mid Left Role \*\/\}'

new_corners = '''{/* Top Left Meta */}
        <div className="absolute top-8 left-8 md:top-12 md:left-12 z-40 text-[#1a1a1a] flex items-center gap-4 pointer-events-none">
          <Sparkle className="w-6 h-6" />
          <div className="text-xs font-semibold tracking-widest uppercase leading-relaxed">
            VOL. 01 <br/> OCT / 2026
          </div>
        </div>

        {/* Top Right Meta */}
        <div className="absolute top-8 right-8 md:top-12 md:right-12 z-40 text-[#1a1a1a] flex items-center gap-4 pointer-events-none">
          <div className="text-xs font-semibold tracking-widest uppercase text-right leading-relaxed">
            VISUAL STUDY <br/> BY GABRIEL RYAN
          </div>
          <Sparkle className="w-6 h-6" />
        </div>

        {/* Bottom Right Sparkle */}
        <div className="absolute bottom-12 right-12 z-40 text-[#1a1a1a] pointer-events-none">
          <Sparkle className="w-12 h-12" />
        </div>

        {/* Mid Left Role */}'''
content = re.sub(old_corners, new_corners, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Added sparkles.')
