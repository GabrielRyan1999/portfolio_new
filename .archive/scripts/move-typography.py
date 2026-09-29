import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the Giant Typography section with the new Top-Aligned layout
old_typography = r'\{\/\* 4\. Giant Typography \(Strictly BEHIND subject for 3D Magazine effect\) \*\/\}[\s\S]*?\{\/\* 5\. The Subject'

new_typography = '''{/* Inject Google Font for Cursive */}
        <style dangerouslySetInnerHTML={{__html: `
          @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@700&display=swap');
          .font-cursive { font-family: 'Caveat', cursive; }
        `}} />

        {/* 4. Giant Typography (Moved ABOVE head so it's not blocked) */}
        <div className="absolute top-[8%] md:top-[10%] left-0 w-full z-20 pointer-events-none mix-blend-difference">
           
           {/* Top Typography: GABRIEL */}
           <div className="absolute top-0 left-0 w-full flex justify-center">
               <h1 className="font-serif text-[16vw] md:text-[18vw] leading-none tracking-tighter font-black text-white uppercase">
                  GABRIEL
               </h1>
           </div>

           {/* Cursive Typography: Ryan */}
           <div className="absolute top-[60%] md:top-[50%] left-1/2 -translate-x-1/2 w-full text-center z-30">
               <h2 className="font-cursive text-[12vw] md:text-[15vw] leading-none text-white -rotate-6 drop-shadow-lg ml-[10vw]">
                  Ryan
               </h2>
           </div>
        </div>

        {/* 5. The Subject'''

content = re.sub(old_typography, new_typography, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Moved typography above head.')
