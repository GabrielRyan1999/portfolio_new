import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change the harsh Navy (#111C2B) to an Academic/Friendly Yale Blue (#1A365D)
content = content.replace('#111C2B', '#1A365D')

# 2. Clean up intimidating gimmicks (crosshairs, barcode, dot grid)
# Remove crosshairs (lines with >+<)
content = re.sub(r'<div[^>]*>\+</div>', '', content)
# Remove CSS barcode section entirely
barcode_regex = r'\{\/\* Bottom Left Barcode \*\/\}.*?<div className="text-\[9px\] md:text-\[10px\] font-bold tracking-\[0\.2em\] uppercase">ARCHIVE_2026</div>\s*</div>'
content = re.sub(barcode_regex, '', content, flags=re.DOTALL)
# Remove Dot Grid
content = re.sub(r'\{\/\* Dot Grid \(Mid Right\) \*\/\}.*?style=\{\{ backgroundImage: \'radial-gradient.*?\s*</div>', '', content, flags=re.DOTALL)

# 3. Improve Typography Accessibility (increase 9px/10px to 12px)
# Replace text-[9px] and text-[10px] with text-xs (12px)
content = re.sub(r'text-\[9px\] md:text-\[10px\]', 'text-xs', content)
# Decrease extreme tracking from 0.2em/0.3em to tracking-widest for better legibility at larger sizes
content = re.sub(r'tracking-\[0\.[23]em\]', 'tracking-widest', content)

# 4. Add a subtle, classic editorial separator (a thin hairline) where the barcode used to be
bottom_left_meta = r'''{/* Bottom Left Meta */}
      <div className="absolute bottom-8 left-4 md:bottom-12 md:left-8 z-40 text-[#F5F2EB] pointer-events-none flex flex-col">
        <div className="w-12 h-[1px] bg-[#F5F2EB]/50 mb-3"></div>
        <div className="text-xs font-semibold tracking-widest uppercase">EST. 2026</div>
      </div>'''

content = re.sub(r'\{\/\* Bottom Right Navy Block \*\/\}', bottom_left_meta + '\n\n      {/* Bottom Right Navy Block */}', content)


with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Applied Warm Editorial Blue fixes.')
