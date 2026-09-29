import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

injection_point = r'\{\/\* 4\. Giant Typography \(Strictly BEHIND subject for 3D Magazine effect\) \*\/\}'
new_inset = '''{/* Mid Right Inset Photo (Favicon) */}
        <div className="absolute top-[45%] md:top-[50%] right-[8vw] md:right-[12vw] z-40 pointer-events-none">
           {/* Decorative Navy Block Behind */}
           <div className="absolute -top-4 -left-4 w-full h-full bg-[#1A365D] opacity-10"></div>
           
           {/* The Photo Polaroid */}
           <div className="relative p-2 bg-[#F5F2EB] border border-[#1A365D]/30 shadow-xl">
             <img src="/favicon.jpg" alt="Gabriel Ryan Thumbnail" className="w-24 h-24 md:w-32 md:h-32 object-cover grayscale contrast-125 mix-blend-multiply" />
           </div>
           
           {/* Small caption */}
           <div className="absolute -right-8 top-1/2 -translate-y-1/2 [writing-mode:vertical-rl] text-[#1A365D] text-[9px] tracking-[0.2em] uppercase font-semibold">
              FIG. 01 — AUTHOR
           </div>
        </div>

        {/* 4. Giant Typography (Strictly BEHIND subject for 3D Magazine effect) */}'''

# Use re.sub instead of replace
content = re.sub(injection_point, new_inset, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Injected favicon successfully this time.')
