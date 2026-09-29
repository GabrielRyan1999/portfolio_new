import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

old_home = r'export function Home\(\) \{.*?^\}\n'
new_home = '''export function Home() {
  return (
    <section id="home" className="relative w-full h-[100dvh] overflow-hidden bg-[#F5F2EB]">
      {/* 1. Deep Navy Color Block (Left 40%) */}
      <div className="absolute top-0 left-0 w-[40vw] h-full bg-[#111C2B]"></div>
      
      {/* 2. Sand/Gold Circle Accent - Large and offset to the right */}
      <div className="absolute top-[-5%] right-[-5vw] w-64 md:w-[600px] aspect-square rounded-full bg-[#E5D5C5] mix-blend-multiply opacity-50 z-10 pointer-events-none"></div>
      
      {/* Small Graphic Accent - Dot Grid */}
      <div className="absolute top-[25%] right-[12vw] w-32 h-32 z-10 opacity-30" style={{ backgroundImage: 'radial-gradient(#111C2B 2px, transparent 2px)', backgroundSize: '16px 16px' }}></div>

      {/* 3. Small Graphic Details (Corners) */}
      <div className="absolute top-8 left-8 md:top-12 md:left-12 z-20 text-[#F5F2EB]">
         <p className="text-[10px] uppercase tracking-[0.2em] mb-1">Vol. 01</p>
         <p className="text-[10px] uppercase tracking-[0.2em]">Oct / 2026</p>
         <div className="mt-6 text-2xl font-light">+</div>
      </div>

      <div className="absolute bottom-8 left-8 md:bottom-12 md:left-12 z-20 hidden md:block">
         {/* Animated Role Text moved here to avoid overlapping giant text */}
         <div className="text-[10px] uppercase tracking-[0.3em] font-bold leading-loose flex flex-col gap-1 mb-10 text-[#F5F2EB]">
           <span className="opacity-50 text-[8px] mb-2">ROLE //</span>
           <span className="flex items-center">
             EDUCATOR & <AnimatedWords words={['DEVELOPER.', 'SYSTEM BUILDER.', 'MENTOR.']} />
           </span>
         </div>
         
         <div className="flex gap-[2px] h-6 mb-2 opacity-80 mix-blend-difference">
            <div className="w-1 bg-white"></div>
            <div className="w-2 bg-white"></div>
            <div className="w-1 bg-white"></div>
            <div className="w-[2px] bg-white"></div>
            <div className="w-3 bg-white"></div>
            <div className="w-1 bg-white"></div>
            <div className="w-[2px] bg-white"></div>
            <div className="w-2 bg-white"></div>
         </div>
         <p className="text-[10px] uppercase tracking-widest text-[#F5F2EB] font-bold mix-blend-difference">ARCHIVE_2026</p>
      </div>

      <div className="absolute top-8 right-8 md:top-12 md:right-12 z-20 text-right hidden md:block">
         <p className="text-[10px] uppercase tracking-widest text-[#111C2B]">Visual Study</p>
         <p className="text-[10px] uppercase tracking-widest text-[#111C2B] font-bold">By Gabriel Ryan</p>
         <div className="mt-4 text-2xl font-light text-[#111C2B]">+</div>
      </div>

      {/* 4. Magic Inverted Text (GABRIEL RYAN) - Tighter leading, better proportions */}
      <div className="absolute inset-0 flex flex-col items-center justify-center z-20 pointer-events-none mix-blend-difference text-white pt-10">
        <h1 className="text-[18vw] md:text-[220px] leading-[0.75] font-serif font-black tracking-tighter uppercase text-center flex flex-col w-full px-4">
          <span className="w-full text-center">GABRIEL</span>
          <span className="w-full text-center tracking-[0.25em] ml-[0.25em]">RYAN</span>
        </h1>
      </div>

      {/* 5. Foreground Subject (Profile Photo) - Scaled up for drama */}
      <div className="absolute bottom-0 left-[50%] -translate-x-1/2 z-30 w-[100%] md:w-[850px] pointer-events-none flex justify-center">
        <img src="/profile-nobg.png" 
             onError={(e) => { e.target.onerror = null; e.target.src='/profile_new.jpg' }}
             alt="Gabriel Ryan" 
             className="w-full h-auto object-contain object-bottom grayscale contrast-[1.15] brightness-90" 
             style={{ maxHeight: '100vh' }} />
      </div>

      {/* 6. Text Blocks intersecting background */}
      <div className="absolute top-[45%] right-[8vw] z-40 hidden lg:block text-[#111C2B]">
         <p className="text-[10px] uppercase tracking-[0.4em] font-bold leading-[2.5]">
           TIMELESS<br/>LOGIC.<br/>MODERN<br/>WEB.
         </p>
         <div className="mt-4 text-xl">+</div>
      </div>
      
      {/* 7. Bottom Right Dark Block - Cleaned up */}
      <div className="absolute bottom-0 right-0 z-40 hidden lg:flex flex-col justify-between w-[25vw] min-w-[320px] h-40 bg-[#111C2B] text-[#F5F2EB] p-8">
         <div>
            <p className="text-[9px] uppercase tracking-[0.2em] mb-4 flex items-center gap-4 text-[#F5F2EB]/50">
              BUILD YOUR OWN SYSTEM <span className="flex-1 h-[1px] bg-[#F5F2EB] opacity-20"></span>
            </p>
            <p className="text-xs uppercase tracking-widest font-bold">INSPIRE. CREATE. BECOME.</p>
         </div>
         <div className="flex justify-between items-end">
            <span className="text-sm font-serif italic">Gabriel Ryan</span>
            <span className="text-2xl leading-none">↗</span>
         </div>
      </div>
      
    </section>
  );
}
'''

content = re.sub(old_home, new_home, content, flags=re.MULTILINE|re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Home component redesigned for maximum elegance.')
