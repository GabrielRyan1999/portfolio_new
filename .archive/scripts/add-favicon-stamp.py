import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate the Top Right Meta block
old_top_right = r'''      \{\/\* Top Right Meta \*\/\}
      <div className="absolute top-8 right-8 md:top-12 md:right-12 z-40 text-\[#1A365D\] text-xs font-semibold tracking-widest uppercase text-right leading-relaxed pointer-events-none">
        VISUAL STUDY <br\/> BY GABRIEL RYAN
        
      </div>'''

new_top_right = '''      {/* Top Right Meta */}
      <div className="absolute top-8 right-8 md:top-12 md:right-12 z-40 flex flex-col items-end pointer-events-none">
        <div className="text-[#1A365D] text-xs font-semibold tracking-widest uppercase text-right leading-relaxed mb-4">
          VISUAL STUDY <br/> BY GABRIEL RYAN
        </div>
        <div className="p-1 border border-[#1A365D]/20 bg-[#F5F2EB]">
          <img src="/favicon.jpg" alt="Author Thumbnail" className="w-12 h-12 md:w-14 md:h-14 object-cover grayscale contrast-125 mix-blend-multiply" />
        </div>
      </div>'''

content = re.sub(old_top_right, new_top_right, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Added favicon stamp to top right.')
