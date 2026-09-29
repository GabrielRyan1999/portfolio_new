import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

new_home = '''export function Home() {
  return (
    <section id="home" className="relative min-h-screen w-full bg-[#F5F2EB] text-[#111C2B] overflow-hidden flex flex-col justify-between">
      
      {/* 1. Deep Navy Color Block (Left 40%) */}
      <div className="absolute top-0 left-0 w-[40vw] h-full bg-[#111C2B] z-0"></div>
      
      {/* 2. Sand/Gold Circle Accent */}
      <div className="absolute top-[-5%] right-[-5vw] w-64 md:w-[600px] aspect-square rounded-full bg-[#E5D5C5] mix-blend-multiply opacity-50 z-10 pointer-events-none"></div>

      {/* Abstract Editorial Decor: Giant Delicate Ring */}
      <div className="absolute bottom-[-20%] left-[-10vw] w-[50vw] md:w-[600px] aspect-square rounded-full border-[1px] border-[#F5F2EB] opacity-20 z-10 pointer-events-none mix-blend-difference"></div>

      {/* Abstract Editorial Decor: Architectural Crosshairs */}
      <div className="absolute top-[50%] left-[25vw] z-10 text-[#F5F2EB] opacity-30 pointer-events-none">
         <div className="text-2xl font-light leading-none">+</div>
      </div>
      <div className="absolute bottom-[30%] right-[30vw] z-10 text-[#111C2B] opacity-30 pointer-events-none">
         <div className="text-2xl font-light leading-none">+</div>
      </div>

      {/* Abstract Editorial Decor: Favicon Collage */}
      <div className="absolute top-[20%] right-[12vw] z-10 w-32 md:w-48 aspect-[3/4] pointer-events-none mix-blend-multiply opacity-70">
         <img src="/favicon.jpg" alt="Favicon Decor" className="w-full h-full object-cover grayscale contrast-125" />
         {/* Offset geometric border */}
         <div className="absolute -bottom-4 -left-4 w-full h-full border border-[#111C2B] opacity-30"></div>
         {/* Little tape or crosshair on the image */}
         <div className="absolute top-2 left-2 text-[#F5F2EB] mix-blend-difference text-lg font-light leading-none">+</div>
      </div>

      {/* 3. Typography Layer 1 (BACKGROUND: Behind Subject) */}
      <div className="absolute inset-0 flex flex-col items-center justify-center z-20 pointer-events-none mix-blend-difference">
         <h1 className="font-serif text-[18vw] md:text-[20vw] leading-[0.8] tracking-tighter font-black text-center text-white whitespace-nowrap">
            <span className="block">GABRIEL</span>
            <span className="block opacity-0">RYAN</span>
         </h1>
      </div>

      {/* 4. The Subject (Portrait) */}
      <div className="absolute bottom-0 w-full h-[75vh] md:h-[85vh] flex justify-center z-30 pointer-events-none">
         <img src="/profile-nobg.png" alt="Gabriel Ryan" className="h-full w-auto object-contain object-bottom drop-shadow-2xl grayscale contrast-125 hover:grayscale-0 transition-all duration-700" />
      </div>

      {/* 5. Typography Layer 2 (FOREGROUND: In front of Subject) */}
      <div className="absolute inset-0 flex flex-col items-center justify-center z-40 pointer-events-none mix-blend-difference">
         <h1 className="font-serif text-[18vw] md:text-[20vw] leading-[0.8] tracking-tighter font-black text-center text-white whitespace-nowrap">
            <span className="block opacity-0">GABRIEL</span>
            <span className="block">RYAN</span>
         </h1>
      </div>

      {/* Header Info */}
      <div className="relative z-50 w-full p-6 md:p-8 flex justify-between items-start pointer-events-none mix-blend-difference text-white">
        <div className="text-[10px] md:text-xs font-semibold tracking-[0.2em] uppercase">Archive / 2026</div>
      </div>

      {/* Footer Info & Animated Words */}
      <div className="relative z-50 w-full p-6 md:p-8 flex justify-between items-end pointer-events-none mix-blend-difference text-white">
        <div className="text-xs md:text-sm font-light tracking-[0.2em] leading-loose">
          BRIDGING CODE AND COMPREHENSION.<br/>
          I AM A <AnimatedWords words={["DEVELOPER.", "SYSTEM BUILDER.", "MENTOR."]} />
        </div>
      </div>

    </section>
  );
}'''

content = re.sub(r'export function Home\(\) \{.*?(?=export function About\(\) \{)', new_home + '\n\n', content, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Reverted to Pre-Impeccable state with mix-blend-difference bug fixed.')
