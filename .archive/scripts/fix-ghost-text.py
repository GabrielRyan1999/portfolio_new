import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the mix-blend Typography with robust Split Typography
old_typography = r'\{\/\* 4\. Giant Typography \(Moved ABOVE head so it\'s not blocked\) \*\/\}[\s\S]*?\{\/\* 5\. The Subject'

new_typography = '''{/* 4. Giant Typography (Moved ABOVE head, using explicit Split Colors instead of mix-blend) */}
        <div className="absolute top-[8%] md:top-[10%] left-0 w-full h-[40vh] z-20 pointer-events-none">
           
           {/* Left Side (Cream Text over Navy BG) */}
           <div className="absolute top-0 left-0 w-[45vw] h-full overflow-hidden">
               <div className="absolute top-0 left-0 w-[100vw] h-full">
                   {/* Top Typography: GABRIEL */}
                   <div className="absolute top-0 left-0 w-full flex justify-center">
                       <h1 className="font-serif text-[16vw] md:text-[18vw] leading-none tracking-tighter font-black text-[#F5F2EB] uppercase">
                          GABRIEL
                       </h1>
                   </div>
                   {/* Cursive Typography: Ryan */}
                   <div className="absolute top-[55%] md:top-[45%] left-1/2 -translate-x-1/2 w-full text-center">
                       <h2 className="font-cursive text-[12vw] md:text-[15vw] leading-none text-[#F5F2EB] -rotate-6 drop-shadow-2xl ml-[10vw]">
                          Ryan
                       </h2>
                   </div>
               </div>
           </div>

           {/* Right Side (Navy Text over Cream BG) */}
           <div className="absolute top-0 right-0 w-[55vw] h-full overflow-hidden">
               <div className="absolute top-0 right-0 w-[100vw] h-full">
                   {/* Top Typography: GABRIEL */}
                   <div className="absolute top-0 left-0 w-full flex justify-center">
                       <h1 className="font-serif text-[16vw] md:text-[18vw] leading-none tracking-tighter font-black text-[#1A365D] uppercase">
                          GABRIEL
                       </h1>
                   </div>
                   {/* Cursive Typography: Ryan */}
                   <div className="absolute top-[55%] md:top-[45%] left-1/2 -translate-x-1/2 w-full text-center">
                       <h2 className="font-cursive text-[12vw] md:text-[15vw] leading-none text-[#1A365D] -rotate-6 drop-shadow-2xl ml-[10vw]">
                          Ryan
                       </h2>
                   </div>
               </div>
           </div>
           
        </div>

        {/* 5. The Subject'''

content = re.sub(old_typography, new_typography, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Applied explicit split colors for typography.')
