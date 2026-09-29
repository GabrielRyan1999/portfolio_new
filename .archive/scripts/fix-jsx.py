import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Match from Giant Typography all the way to the end of the section
old_block = r'\{\/\* 4\. Giant Typography[\s\S]*?<\/section>'

clean_block = '''{/* 4. Giant Typography (Moved ABOVE head, Split GABRIEL + Difference RYAN) */}
        <div className="absolute top-[8%] md:top-[10%] left-0 w-full h-[40vh] z-20 pointer-events-none">
           
           {/* GABRIEL - Explicitly Split Colors */}
           {/* Left Side (Cream Text over Navy BG) */}
           <div className="absolute top-0 left-0 w-[45vw] h-full overflow-hidden">
               <div className="absolute top-0 left-0 w-[100vw] h-full flex justify-center">
                   <h1 className="font-serif text-[16vw] md:text-[18vw] leading-none tracking-tighter font-black text-[#F5F2EB] uppercase">
                      GABRIEL
                   </h1>
               </div>
           </div>

           {/* Right Side (Navy Text over Cream BG) */}
           <div className="absolute top-0 right-0 w-[55vw] h-full overflow-hidden">
               <div className="absolute top-0 right-0 w-[100vw] h-full flex justify-center">
                   <h1 className="font-serif text-[16vw] md:text-[18vw] leading-none tracking-tighter font-black text-[#1A365D] uppercase">
                      GABRIEL
                   </h1>
               </div>
           </div>
           
           {/* RYAN - Cursive Typography (Single element, mix-blend-difference) */}
           <div className="absolute top-[30%] md:top-[25%] left-1/2 -translate-x-1/2 w-full flex justify-center z-30 mix-blend-difference">
               <h2 
                 className="text-[14vw] md:text-[16vw] leading-none text-white -rotate-[10deg] ml-[20vw] drop-shadow-xl" 
                 style={{ fontFamily: "'Mayonice', 'Brush Script MT', 'Bradley Hand', cursive" }}
               >
                  Ryan
               </h2>
           </div>
           
        </div>

        {/* 5. The Subject (Portrait - Strictly IN FRONT of text) */}
        <div className="absolute bottom-0 w-full h-[85vh] md:h-[90vh] flex justify-center z-30 pointer-events-none">
           <img src="/profile-nobg.png" alt="Gabriel Ryan" className="h-full w-auto object-contain object-bottom drop-shadow-2xl grayscale contrast-125 hover:grayscale-0 transition-all duration-700" />
        </div>
        
      </section>'''

content = re.sub(old_block, clean_block, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed JSX Syntax Error.')
