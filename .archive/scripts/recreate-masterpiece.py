import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

masterpiece_home = '''export function Home() {
  return (
    <section id="home" className="relative min-h-screen w-full bg-[#F5F2EB] text-[#111C2B] overflow-hidden">
      
      {/* 1. Deep Navy Color Block (Left 45%) */}
      <div className="absolute top-0 left-0 w-[45vw] h-full bg-[#111C2B] z-0 pointer-events-none"></div>
      
      {/* 2. Abstract Geometric Decors */}
      {/* Large Sand Circle (Top Right) */}
      <div className="absolute top-[5%] right-[10vw] w-[30vw] max-w-[400px] aspect-square rounded-full bg-[#E5D5C5] mix-blend-multiply opacity-80 z-10 pointer-events-none"></div>
      
      {/* Dot Grid (Mid Right) */}
      <div className="absolute top-[30%] right-[5vw] w-24 h-24 z-10 pointer-events-none opacity-40" style={{ backgroundImage: 'radial-gradient(#111C2B 2px, transparent 2px)', backgroundSize: '10px 10px' }}></div>
      
      {/* Thin Arcs (Bottom Left) */}
      <div className="absolute bottom-[-10%] left-[-10vw] w-[40vw] max-w-[500px] aspect-square rounded-full border-[1px] border-[#F5F2EB] opacity-20 z-10 pointer-events-none"></div>
      <div className="absolute bottom-[-20%] left-[-5vw] w-[50vw] max-w-[600px] aspect-square rounded-full border-[1px] border-[#F5F2EB] opacity-10 z-10 pointer-events-none"></div>

      {/* 3. Editorial Text Elements (Absolute positioned) */}
      
      {/* Top Left Meta */}
      <div className="absolute top-8 left-8 md:top-12 md:left-12 z-40 text-[#F5F2EB] text-[9px] md:text-[10px] font-semibold tracking-[0.2em] uppercase leading-relaxed pointer-events-none">
        VOL. 01 <br/> OCT / 2026
        <div className="mt-4">+</div>
      </div>

      {/* Top Right Meta */}
      <div className="absolute top-8 right-8 md:top-12 md:right-12 z-40 text-[#111C2B] text-[9px] md:text-[10px] font-semibold tracking-[0.2em] uppercase text-right leading-relaxed pointer-events-none">
        VISUAL STUDY <br/> BY GABRIEL RYAN
        <div className="mt-4">+</div>
      </div>

      {/* Mid Left Role */}
      <div className="absolute top-[40%] left-8 md:left-12 z-40 text-[#F5F2EB] text-[9px] md:text-[10px] font-semibold tracking-[0.2em] uppercase leading-relaxed pointer-events-none">
        <span className="opacity-50">ROLE //</span><br/><br/>
        EDUCATOR & <AnimatedWords words={["DEVELOPER.", "SYSTEM BUILDER.", "MENTOR."]} />
        <div className="mt-6">+</div>
      </div>

      {/* Mid Right Philosophy */}
      <div className="absolute top-[45%] right-8 md:right-12 z-40 text-[#111C2B] text-[9px] md:text-[10px] font-semibold tracking-[0.2em] uppercase text-right leading-relaxed pointer-events-none">
        TIMELESS<br/>LOGIC.<br/>MODERN<br/>WEB.
        <div className="mt-6">+</div>
      </div>

      {/* Bottom Left Barcode */}
      <div className="absolute bottom-8 left-8 md:bottom-12 md:left-12 z-40 text-[#F5F2EB] pointer-events-none flex flex-col">
        <div className="mb-4 text-[10px]">+</div>
        {/* CSS Barcode simulation */}
        <div className="flex h-6 mb-2 opacity-80">
          <div className="w-1 h-full bg-[#F5F2EB] mr-1"></div>
          <div className="w-2 h-full bg-[#F5F2EB] mr-[2px]"></div>
          <div className="w-1 h-full bg-[#F5F2EB] mr-1"></div>
          <div className="w-[2px] h-full bg-[#F5F2EB] mr-1"></div>
          <div className="w-3 h-full bg-[#F5F2EB] mr-[2px]"></div>
          <div className="w-1 h-full bg-[#F5F2EB] mr-1"></div>
          <div className="w-2 h-full bg-[#F5F2EB] mr-1"></div>
          <div className="w-[2px] h-full bg-[#F5F2EB] mr-[2px]"></div>
          <div className="w-1 h-full bg-[#F5F2EB]"></div>
        </div>
        <div className="text-[9px] md:text-[10px] font-bold tracking-[0.2em] uppercase">ARCHIVE_2026</div>
      </div>

      {/* Bottom Right Navy Block */}
      <div className="absolute bottom-0 right-0 w-[45vw] md:w-[35vw] bg-[#111C2B] p-6 md:p-10 z-40 flex flex-col justify-between text-[#F5F2EB]">
         <div className="border-b border-[#F5F2EB]/30 pb-4 mb-4 text-[9px] md:text-[10px] tracking-[0.2em] uppercase font-semibold">
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

      {/* Rotated Innovate Text */}
      <div className="absolute bottom-[20%] right-[25vw] md:right-[20vw] z-40 bg-[#D4C5B3] px-2 py-4 pointer-events-none mix-blend-multiply origin-center translate-x-1/2">
         <div className="[writing-mode:vertical-lr] text-[#111C2B] text-[9px] md:text-[10px] tracking-[0.3em] font-semibold uppercase rotate-180">
            INNOVATE.
         </div>
      </div>

      {/* 4. Giant Typography (Strictly BEHIND subject) */}
      <div className="absolute inset-0 flex flex-col items-center justify-center z-20 pointer-events-none mix-blend-difference">
         <h1 className="font-serif text-[18vw] md:text-[20vw] leading-[0.85] tracking-tighter font-black text-center text-white whitespace-nowrap">
            <span className="block">GABRIEL</span>
            <span className="block">RYAN</span>
         </h1>
      </div>

      {/* 5. The Subject (Portrait - Strictly IN FRONT of text) */}
      <div className="absolute bottom-0 w-full h-[75vh] md:h-[85vh] flex justify-center z-30 pointer-events-none">
         <img src="/profile-nobg.png" alt="Gabriel Ryan" className="h-full w-auto object-contain object-bottom drop-shadow-2xl grayscale contrast-125 hover:grayscale-0 transition-all duration-700" />
      </div>

    </section>
  );
}'''

content = re.sub(r'export function Home\(\) \{.*?(?=export function About\(\) \{)', masterpiece_home + '\n\n', content, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Recreated the exact master layout from the user screenshot.')
