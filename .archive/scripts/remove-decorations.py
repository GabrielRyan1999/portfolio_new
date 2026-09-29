import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Revert Barcode back to EST 2026
old_barcode = r'<div className="flex gap-1 h-6 mb-2">[\s\S]*?<\/div>\s*<div className="text-\[10px\] font-mono tracking-widest uppercase">ARCHIVE_2026<\/div>'
new_est = '''<div className="w-12 h-[1px] bg-[#F5F2EB]/50 mb-3"></div>
          <div className="text-xs font-semibold tracking-widest uppercase">EST. 2026</div>'''
content = re.sub(old_barcode, new_est, content)

# 2. Revert Japanese text back to INNOVATE and remove crosshairs + grid dots
old_decorations = r'\{\/\* Rotated Innovate Text \*\/\}[\s\S]*?\{\/\* Minimalist Grid Dots \*\/\}[\s\S]*?<\/div>\s*<\/div>'
new_innovate = '''{/* Rotated Innovate Text */}
        <div className="absolute bottom-[25%] right-[10vw] md:right-[15vw] z-40 bg-[#D4C5B3] px-2 py-4 pointer-events-none mix-blend-multiply origin-center translate-x-1/2">
           <div className="[writing-mode:vertical-lr] text-[#1A365D] text-xs tracking-widest font-semibold uppercase rotate-180">
              INNOVATE.
           </div>
        </div>'''
content = re.sub(old_decorations, new_innovate, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Removed decorative elements.')
