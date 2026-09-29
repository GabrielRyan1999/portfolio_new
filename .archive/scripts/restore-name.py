import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

giant_text = '''{/* 4. Giant Typography (Strictly BEHIND subject for 3D Magazine effect) */}
        <div className="absolute inset-0 z-20 pointer-events-none">
           {/* Left Side (Cream Text on Blue BG) */}
           <div className="absolute top-0 left-0 w-[45vw] h-full overflow-hidden">
               <div className="absolute top-0 left-0 w-[100vw] h-full flex flex-col items-center justify-center">
                   <h1 className="font-serif text-[13vw] md:text-[15vw] leading-[0.85] tracking-tighter font-black text-center whitespace-nowrap text-[#F5F2EB]">
                      <span className="block">GABRIEL</span>
                      <span className="block">RYAN</span>
                   </h1>
               </div>
           </div>
           {/* Right Side (Blue Text on Cream BG) */}
           <div className="absolute top-0 right-0 w-[55vw] h-full overflow-hidden">
               <div className="absolute top-0 right-0 w-[100vw] h-full flex flex-col items-center justify-center">
                   <h1 className="font-serif text-[13vw] md:text-[15vw] leading-[0.85] tracking-tighter font-black text-center whitespace-nowrap text-[#1A365D]">
                      <span className="block">GABRIEL</span>
                      <span className="block">RYAN</span>
                   </h1>
               </div>
           </div>
        </div>

        {/* 5. The Subject'''

content = content.replace('{/* 5. The Subject', giant_text)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Restored Giant Typography.')
