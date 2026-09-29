import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the typography block
old_typography = r'\{\/\* 4\. Giant Typography[\s\S]*?<\/div>\s*<\/div>\s*<\/div>'

new_typography = '''{/* 4. Giant Typography (Moved ABOVE head, Split GABRIEL + Difference RYAN) */}
        <div className="absolute top-[8%] md:top-[10%] left-0 w-full h-[40vh] z-20 pointer-events-none">
           
           {/* GABRIEL - Explicitly Split Colors with Pixel-Perfect Alignment */}
           {/* Left Side (Cream Text over Navy BG) */}
           <div className="absolute top-0 left-0 w-[45vw] h-full overflow-hidden">
               <div className="absolute top-0 left-0 w-[100vw] h-full flex justify-center">
                   <h1 className="font-serif text-[16vw] md:text-[18vw] leading-none tracking-tighter font-black text-[#F5F2EB] uppercase whitespace-nowrap">
                      GABRIEL
                   </h1>
               </div>
           </div>

           {/* Right Side (Navy Text over Cream BG) */}
           <div className="absolute top-0 left-[45vw] w-[55vw] h-full overflow-hidden">
               <div className="absolute top-0 left-[-45vw] w-[100vw] h-full flex justify-center">
                   <h1 className="font-serif text-[16vw] md:text-[18vw] leading-none tracking-tighter font-black text-[#1A365D] uppercase whitespace-nowrap">
                      GABRIEL
                   </h1>
               </div>
           </div>
           
           {/* RYAN - Cursive Typography (Single element, mix-blend-difference) */}
           <div className="absolute top-[30%] md:top-[25%] left-1/2 -translate-x-1/2 w-full flex justify-center z-30 mix-blend-difference">
               <h2 
                 className="text-[14vw] md:text-[16vw] leading-none text-white -rotate-[10deg] ml-[20vw] drop-shadow-xl whitespace-nowrap" 
                 style={{ fontFamily: "'Mayonice', 'Brush Script MT', 'Bradley Hand', cursive" }}
               >
                  Ryan
               </h2>
           </div>
           
        </div>'''

content = re.sub(old_typography, new_typography, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed text alignment.')
