import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the entire Home section with the final hybrid layout
old_home = r'<section id="home" className="relative min-h-screen w-full bg-\[#F5F2EB\] text-\[#1A365D\] overflow-hidden">[\s\S]*?<\/section>'

new_home = '''<section id="home" className="relative min-h-screen w-full bg-[#F5F2EB] text-[#1A365D] overflow-hidden">
        
        {/* 1. Base Cream Background is already applied */}

        {/* 2. The Massive Navy Arch Background */}
        <div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-[90vw] md:w-[70vw] h-[45vw] md:h-[35vw] bg-[#1A365D] rounded-t-full z-10 pointer-events-none transition-all duration-700"></div>
  
        {/* 3. Editorial Text Elements from Previous Layout */}
        
        {/* Top Left Meta */}
        <div className="absolute top-8 left-8 md:top-12 md:left-12 z-40 text-[#1A365D] text-xs font-semibold tracking-widest uppercase leading-relaxed pointer-events-none">
          VOL. 01 <br/> OCT / 2026
        </div>
  
        {/* Mid Right Inset Photo (Favicon) */}
        <div className="absolute top-[45%] md:top-[50%] right-[8vw] md:right-[12vw] z-40 pointer-events-none">
           <div className="absolute -top-4 -left-4 w-full h-full bg-[#1A365D] opacity-10"></div>
           <div className="relative p-2 bg-[#F5F2EB] border border-[#1A365D]/30 shadow-xl">
             <img src="/favicon.jpg" alt="Gabriel Ryan Thumbnail" className="w-24 h-24 md:w-32 md:h-32 object-cover grayscale contrast-125 mix-blend-multiply" />
           </div>
           <div className="absolute -right-8 top-1/2 -translate-y-1/2 [writing-mode:vertical-rl] text-[#1A365D] text-[9px] tracking-[0.2em] uppercase font-semibold">
              FIG. 01 — AUTHOR
           </div>
        </div>
  
        {/* Bottom Left Content Group */}
        <div className="absolute bottom-8 left-4 md:bottom-12 md:left-8 z-40 flex flex-col gap-10 pointer-events-none">
          {/* Role */}
          <div className="text-[#1A365D] text-xs font-semibold tracking-widest uppercase leading-relaxed">
            <span className="opacity-50">ROLE //</span><br/><br/>
            EDUCATOR & <AnimatedWords words={["DEVELOPER.", "SYSTEM BUILDER.", "MENTOR."]} />
          </div>
          {/* Meta */}
          <div className="text-[#1A365D] flex flex-col">
            <div className="w-12 h-[1px] bg-[#1A365D]/50 mb-3"></div>
            <div className="text-xs font-semibold tracking-widest uppercase">EST. 2026</div>
          </div>
        </div>
  
        {/* Bottom Right Navy Block */}
        <div className="absolute bottom-0 right-0 w-[45vw] md:w-[35vw] bg-[#1A365D] p-6 md:p-10 z-40 flex flex-col justify-between text-[#F5F2EB]">
           <div className="border-b border-[#F5F2EB]/30 pb-4 mb-4 text-xs tracking-widest uppercase font-semibold">
             BUILD YOUR OWN SYSTEM
           </div>
           <div className="text-xs md:text-sm font-bold tracking-widest uppercase mb-8">
             INSPIRE. CREATE. BECOME.
           </div>
           <div className="flex justify-between items-center text-[10px]">
             <span>+</span>
             <span className="text-lg">↗</span>
           </div>
        </div>
  
        {/* 4. Giant Typography (Strictly BEHIND subject, Mix Blend Difference for dynamic Arch overlap) */}
        <div className="absolute inset-0 z-20 w-full h-full flex flex-col items-center justify-center pointer-events-none mix-blend-difference">
             <h1 className="font-serif text-[13vw] md:text-[15vw] leading-[0.85] tracking-tighter font-black text-center whitespace-nowrap text-white">
                <span className="block">GABRIEL</span>
                <span className="block">RYAN</span>
             </h1>
        </div>
  
        {/* 5. The Subject (Portrait - Strictly IN FRONT of text, so no X-Ray face!) */}
        <div className="absolute bottom-0 w-full h-[85vh] md:h-[90vh] flex justify-center z-30 pointer-events-none">
           <img src="/profile-nobg.png" alt="Gabriel Ryan" className="h-full w-auto object-contain object-bottom drop-shadow-2xl grayscale contrast-125 hover:grayscale-0 transition-all duration-700" />
        </div>
        
      </section>'''

content = re.sub(old_home, new_home, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Applied Arch Background with Original Layout.')
