import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the entire Home section with the new Arch Layout
old_home = r'<section id="home" className="relative min-h-screen w-full bg-\[#F5F2EB\] text-\[#1A365D\] overflow-hidden">[\s\S]*?<\/section>'

new_home = '''<section id="home" className="relative min-h-screen w-full bg-[#F5F2EB] text-[#1A365D] overflow-hidden">
        
        {/* Inject Google Font for Cursive */}
        <style dangerouslySetInnerHTML={{__html: `
          @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@700&display=swap');
          .font-cursive { font-family: 'Caveat', cursive; }
        `}} />

        {/* 1. Base Cream Background is already applied on section */}

        {/* 2. The Horizon Line (Torn Paper fake effect) */}
        <div className="absolute top-[50%] left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-[#1A365D]/20 to-transparent z-0"></div>

        {/* 3. The Massive Navy Arch */}
        <div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-[90vw] md:w-[60vw] h-[45vw] md:h-[30vw] bg-[#1A365D] rounded-t-full z-10 pointer-events-none transition-all duration-700"></div>
  
        {/* 4. Top Typography: GABRIEL */}
        <div className="absolute top-[10%] left-0 w-full flex justify-center z-20 pointer-events-none">
           <h1 className="font-serif text-[18vw] leading-none tracking-tight font-black text-[#1A1A1A] uppercase">
              GABRIEL
           </h1>
        </div>

        {/* 5. Cursive Typography: Ryan */}
        <div className="absolute top-[22%] left-1/2 -translate-x-1/2 z-30 pointer-events-none">
           <h2 className="font-cursive text-[15vw] leading-none text-[#4A72A5] -rotate-6 scale-110 drop-shadow-lg">
              Ryan
           </h2>
        </div>
  
        {/* 6. The Subject (Portrait) */}
        <div className="absolute bottom-0 w-full h-[85vh] md:h-[90vh] flex justify-center z-40 pointer-events-none">
           <img src="/profile-nobg.png" alt="Gabriel Ryan" className="h-full w-auto object-contain object-bottom drop-shadow-2xl grayscale contrast-125 hover:grayscale-0 transition-all duration-700" />
        </div>

        {/* 7. Bottom Left Text Block */}
        <div className="absolute bottom-[10%] left-[5%] md:left-[10%] z-50 pointer-events-none w-[200px] md:w-[250px]">
           <p className="text-xs md:text-sm font-semibold leading-relaxed mb-4 text-[#1A1A1A]">
             Shaping digital learning through engineered platforms—
           </p>
           <div className="flex gap-2">
             {[1,2,3,4].map(i => (
               <div key={i} className="w-5 h-5 md:w-6 md:h-6 rounded-full border-[1.5px] border-[#1A1A1A]"></div>
             ))}
           </div>
        </div>

        {/* 8. Bottom Right Text Block */}
        <div className="absolute bottom-[10%] right-[5%] md:right-[10%] z-50 pointer-events-none flex flex-col items-end">
           <div className="flex items-center gap-2 mb-2">
              {/* Connector line */}
              <div className="w-8 md:w-16 h-[1px] bg-[#E3A36D] relative">
                 <div className="absolute -left-1 -top-1 w-2 h-2 rounded-full bg-[#E3A36D]"></div>
              </div>
              <div className="flex flex-col text-right leading-none">
                 <span className="text-xl md:text-3xl font-black text-[#1A1A1A] tracking-tighter uppercase">Educator</span>
                 <span className="text-xl md:text-3xl font-black text-[#4A72A5] tracking-tighter uppercase">Developer</span>
              </div>
           </div>
           
           {/* Pill outline */}
           <div className="w-[180px] h-[30px] border border-[#F5F2EB]/50 rounded-full mt-2 relative overflow-hidden backdrop-blur-sm mix-blend-difference"></div>
        </div>
        
      </section>'''

content = re.sub(old_home, new_home, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Replaced Home section with the Arch Sketch Layout.')
