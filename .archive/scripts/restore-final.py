import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the entire Home section with the absolute final perfection version
old_home = r'<section id="home" className="relative min-h-screen w-full bg-\[#F5F2EB\] text-\[#1A365D\] overflow-hidden">[\s\S]*?<\/section>'

new_home = '''<section id="home" className="relative min-h-screen w-full bg-[#F5F2EB] text-[#1A365D] overflow-hidden">
        
        {/* 1. Deep Navy Color Block (Left 45%) */}
        <div className="absolute top-0 left-0 w-[45vw] h-full bg-[#1A365D] z-0 pointer-events-none"></div>

        {/* 2. Abstract Geometric Decors */}
        <div className="absolute top-[-5%] right-[2vw] w-[30vw] max-w-[400px] aspect-square rounded-full bg-[#E5D5C5] mix-blend-multiply opacity-80 z-10 pointer-events-none"></div>
        <div className="absolute bottom-[-10%] left-[-10vw] w-[40vw] max-w-[500px] aspect-square rounded-full border-[1px] border-[#F5F2EB] opacity-20 z-10 pointer-events-none"></div>
        <div className="absolute bottom-[-20%] left-[-5vw] w-[50vw] max-w-[600px] aspect-square rounded-full border-[1px] border-[#F5F2EB] opacity-10 z-10 pointer-events-none"></div>
  
        {/* 3. Editorial Text Elements */}
        
        {/* Top Left Meta */}
        <div className="absolute top-8 left-8 md:top-12 md:left-12 z-40 text-[#F5F2EB] text-xs font-semibold tracking-widest uppercase leading-relaxed pointer-events-none">
          VOL. 01 <br/> OCT / 2026
        </div>
  
        {/* Top Right Meta */}
        <div className="absolute top-8 right-8 md:top-12 md:right-12 z-40 flex flex-col items-end pointer-events-none">
          <div className="text-[#1A365D] text-xs font-semibold tracking-widest uppercase text-right leading-relaxed mb-4">
            VISUAL STUDY <br/> BY GABRIEL RYAN
          </div>
        </div>

        {/* Mid Right Inset Photo (Favicon Polaroid) */}
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
  
        {/* Bottom Left Content Group (ROLE + EST) */}
        <div className="absolute bottom-8 left-4 md:bottom-12 md:left-8 z-40 flex flex-col gap-10 pointer-events-none">
          {/* Role */}
          <div className="text-[#F5F2EB] text-xs font-semibold tracking-widest uppercase leading-relaxed">
            <span className="opacity-50">ROLE //</span><br/><br/>
            EDUCATOR & <AnimatedWords words={["DEVELOPER.", "SYSTEM BUILDER.", "MENTOR."]} />
          </div>
          {/* Meta */}
          <div className="text-[#F5F2EB] flex flex-col">
            <div className="w-12 h-[1px] bg-[#F5F2EB]/50 mb-3"></div>
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
  
        {/* 4. Giant Typography (Strictly BEHIND subject for 3D Magazine effect) */}
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
  
        {/* 5. The Subject (Portrait - Strictly IN FRONT of text) */}
        <div className="absolute bottom-0 w-full h-[85vh] md:h-[90vh] flex justify-center z-30 pointer-events-none">
           <img src="/profile-nobg.png" alt="Gabriel Ryan" className="h-full w-auto object-contain object-bottom drop-shadow-2xl grayscale contrast-125 hover:grayscale-0 transition-all duration-700" />
        </div>
        
      </section>'''

content = re.sub(old_home, new_home, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Restored the final perfect split layout.')
