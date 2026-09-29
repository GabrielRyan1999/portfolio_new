import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the favicon from Top Right Meta
old_top_right = r'\{\/\* Top Right Meta with Favicon \*\/\}[\s\S]*?<\/div>\s*<\/div>'
new_top_right = '''{/* Top Right Meta */}
        <div className="absolute top-8 right-8 md:top-12 md:right-12 z-40 flex flex-col items-end pointer-events-none">
          <div className="text-[#1A365D] text-xs font-semibold tracking-widest uppercase text-right leading-relaxed mb-4">
            VISUAL STUDY <br/> BY GABRIEL RYAN
          </div>
        </div>'''
content = re.sub(old_top_right, new_top_right, content)

# 2. Add the Favicon as a mid-right Inset Polaroid
# I will inject it right before the "Giant Typography" section.
injection_point = r'\{\/\* 4\. Giant Typography \(Strictly BEHIND subject for 3D Magazine effect\) \*\/\}'
new_inset = '''{/* Mid Right Inset Photo (Favicon) */}
        <div className="absolute top-[45%] md:top-[50%] right-[8vw] md:right-[12vw] z-40 pointer-events-none">
           {/* Decorative Navy Block Behind */}
           <div className="absolute -top-6 -left-6 w-full h-full bg-[#1A365D] opacity-10"></div>
           
           {/* The Photo Polaroid */}
           <div className="relative p-2 bg-[#F5F2EB] border border-[#1A365D]/30 shadow-xl">
             <img src="/favicon.jpg" alt="Gabriel Ryan Thumbnail" className="w-24 h-24 md:w-32 md:h-32 object-cover grayscale contrast-125 mix-blend-multiply" />
           </div>
           
           {/* Small caption */}
           <div className="absolute -right-8 top-1/2 -translate-y-1/2 [writing-mode:vertical-rl] text-[#1A365D] text-[9px] tracking-[0.2em] uppercase">
              FIG. 01 — AUTHOR
           </div>
        </div>

        {/* 4. Giant Typography (Strictly BEHIND subject for 3D Magazine effect) */}'''
content = content.replace(injection_point, new_inset)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Relocated favicon to mid-right inset.')
