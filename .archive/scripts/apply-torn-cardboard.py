import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Match from <section id="home"> to </section>
old_home = r'<section id="home" className="relative min-h-screen w-full bg-\[#F5F2EB\] text-\[#1A365D\] overflow-hidden">[\s\S]*?<\/section>'

new_home = '''<section id="home" className="relative min-h-screen w-full bg-[#F5F2EB] text-[#1A365D] overflow-hidden">
          
          {/* 0. Photorealistic Torn Cardboard Background */}
          <div className="absolute bottom-0 left-0 w-full h-[55vh] z-0 pointer-events-none mix-blend-multiply opacity-90" style={{ backgroundImage: "url('/torn-cardboard.jpg')", backgroundSize: "cover", backgroundPosition: "top center", backgroundRepeat: "no-repeat" }}></div>
  
          {/* 2. Abstract Geometric Decors (Kept as requested) */}
          <div className="absolute top-[-5%] right-[2vw] w-[30vw] max-w-[400px] aspect-square rounded-full bg-[#E5D5C5] mix-blend-multiply opacity-80 z-10 pointer-events-none"></div>
          <div className="absolute bottom-[-10%] left-[-10vw] w-[40vw] max-w-[500px] aspect-square rounded-full border-[1px] border-[#1A365D] opacity-10 z-10 pointer-events-none"></div>
          <div className="absolute bottom-[-20%] left-[-5vw] w-[50vw] max-w-[600px] aspect-square rounded-full border-[1px] border-[#1A365D] opacity-5 z-10 pointer-events-none"></div>
    
          {/* 3. Editorial Text Elements */}
          
          {/* Top Left Meta */}
          <div className="absolute top-8 left-8 md:top-12 md:left-12 z-40 text-[#1A365D] text-xs font-semibold tracking-widest uppercase leading-relaxed pointer-events-none">
            VOL. 01 <br/> OCT / 2026
          </div>
    
          {/* Top Right Meta */}
          <div className="absolute top-8 right-8 md:top-12 md:right-12 z-40 flex flex-col items-end pointer-events-none">
            <div className="text-[#1A365D] text-xs font-semibold tracking-widest uppercase text-right leading-relaxed mb-4">
              VISUAL STUDY <br/> BY GABRIEL RYAN
            </div>
          </div>
  
          {/* Mid Right Inset Photo (Favicon Polaroid - Kept in place) */}
          <div className="absolute top-[45%] md:top-[50%] right-[8vw] md:right-[12vw] z-40 pointer-events-none hidden lg:block">
             <div className="absolute -top-4 -left-4 w-full h-full bg-[#1A365D] opacity-10"></div>
             <div className="relative p-2 bg-[#F5F2EB] border border-[#1A365D]/30 shadow-xl">
               <img src="/favicon.jpg" alt="Gabriel Ryan Thumbnail" className="w-24 h-24 md:w-32 md:h-32 object-cover grayscale contrast-125 mix-blend-multiply" />
             </div>
             <div className="absolute -right-8 top-1/2 -translate-y-1/2 [writing-mode:vertical-rl] text-[#1A365D] text-[9px] tracking-[0.2em] uppercase font-semibold">
                FIG. 01 — AUTHOR
             </div>
          </div>
    
          {/* Bottom Left Content Group (Updated to match new sketch) */}
          <div className="absolute bottom-12 left-8 md:bottom-20 md:left-12 z-40 flex flex-col gap-6 pointer-events-none">
            <div className="text-[#1A365D] font-mono text-sm md:text-base font-medium tracking-tight leading-snug w-48">
              Shaping digital<br/>learning through<br/>engineered platforms—
            </div>
            <div className="flex gap-2">
               <div className="w-6 h-6 rounded-full border-[1.5px] border-[#1A365D]"></div>
               <div className="w-6 h-6 rounded-full border-[1.5px] border-[#1A365D]"></div>
               <div className="w-6 h-6 rounded-full border-[1.5px] border-[#1A365D]"></div>
               <div className="w-6 h-6 rounded-full border-[1.5px] border-[#1A365D]"></div>
            </div>
          </div>

          {/* Bottom Right Callout (Updated to match new sketch) */}
          <div className="absolute bottom-16 right-8 md:bottom-24 md:right-16 z-40 flex items-center pointer-events-none">
              {/* Line Graphic */}
              <div className="flex items-center mr-3 md:mr-4">
                  <div className="w-2 h-2 rounded-full bg-[#E5D5C5] border border-[#1A365D]"></div>
                  <div className="w-12 md:w-20 h-[1.5px] bg-[#1A365D]"></div>
              </div>
              <div className="flex flex-col">
                  <span className="font-serif font-black text-4xl md:text-5xl text-[#1A365D] leading-[0.85] uppercase">Educator</span>
                  <span className="font-sans font-black text-4xl md:text-5xl text-[#60A5FA] leading-[0.85] uppercase">Developer</span>
              </div>
          </div>
    
          {/* 4. Giant Typography (Solid Navy on Cream) */}
          <div className="absolute top-[8%] md:top-[10%] left-0 w-full h-[40vh] z-20 pointer-events-none">
             
             {/* GABRIEL */}
             <div className="absolute top-0 left-0 w-full flex justify-center">
                 <h1 className="font-serif text-[16vw] md:text-[18vw] leading-none tracking-tighter font-black text-[#1A365D] uppercase whitespace-nowrap">
                    GABRIEL
                 </h1>
             </div>
             
             {/* RYAN - Softer blue cursive */}
             <div className="absolute top-[30%] md:top-[25%] left-1/2 -translate-x-1/2 w-full flex justify-center z-30">
                 <h2 
                   className="text-[14vw] md:text-[16vw] leading-none text-[#234E8A] -rotate-[10deg] ml-[20vw] drop-shadow-xl whitespace-nowrap" 
                   style={{ fontFamily: "'Mayonice', 'Brush Script MT', 'Bradley Hand', cursive" }}
                 >
                    Ryan
                 </h2>
             </div>
             
          </div>
  
          {/* 5. The Subject (Portrait - Strictly IN FRONT of text and cardboard) */}
          <div className="absolute bottom-0 w-full h-[85vh] md:h-[90vh] flex justify-center z-30 pointer-events-none">
             <img src="/profile-nobg.png" alt="Gabriel Ryan" className="h-full w-auto object-contain object-bottom drop-shadow-2xl grayscale contrast-125 hover:grayscale-0 transition-all duration-700" />
          </div>
          
        </section>'''

content = re.sub(old_home, new_home, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Applied Photorealistic Torn Cardboard layout.')
