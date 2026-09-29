import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

new_home = '''export function Home() {
  return (
    <section id="home" className="relative min-h-screen w-full overflow-hidden flex items-center justify-center bg-[#F5F2EB]">
      
      {/* 1. Clean Background Split */}
      <div className="absolute inset-0 w-full h-full flex">
         <div className="w-[35%] md:w-[40%] h-full bg-[#111C2B]"></div>
         <div className="w-[65%] md:w-[60%] h-full bg-[#F5F2EB]"></div>
      </div>

      {/* 2. Top Editorial Meta Bar */}
      <div className="absolute top-0 left-0 w-full p-6 md:p-12 flex justify-between uppercase tracking-[0.2em] text-[10px] md:text-xs font-semibold z-50 pointer-events-none">
        <span className="text-white mix-blend-difference">ARCHIVE / 2026</span>
        <span className="text-[#111C2B] mix-blend-multiply text-right">TECH & EDUCATION<br/>VISUAL STUDY</span>
      </div>

      {/* 3. Typography Layer 1 (BACKGROUND: Behind Subject) */}
      <div className="absolute inset-0 flex flex-col items-center justify-center z-20 pointer-events-none">
          <h1 className="font-serif text-[22vw] leading-[0.8] tracking-tighter font-bold text-center whitespace-nowrap text-white mix-blend-difference">
            <span className="block">GABRIEL</span>
            <span className="block opacity-0">RYAN</span>
          </h1>
      </div>

      {/* 4. The Subject (Portrait) */}
      <div className="absolute bottom-0 w-full h-[70vh] md:h-[85vh] flex justify-center z-30 pointer-events-none">
         <img src="/profile-nobg.png" alt="Gabriel Ryan" className="h-full w-auto object-contain object-bottom drop-shadow-2xl grayscale contrast-[1.15]" />
      </div>

      {/* 5. Typography Layer 2 (FOREGROUND: In front of Subject) */}
      <div className="absolute inset-0 flex flex-col items-center justify-center z-40 pointer-events-none">
          <h1 className="font-serif text-[22vw] leading-[0.8] tracking-tighter font-bold text-center whitespace-nowrap text-white mix-blend-difference">
            <span className="block opacity-0">GABRIEL</span>
            <span className="block">RYAN</span>
          </h1>
      </div>

      {/* 6. Clean Animated Role (Bottom Left) */}
      <div className="absolute bottom-12 left-6 md:bottom-24 md:left-12 z-50 text-white mix-blend-difference">
         <div className="text-[10px] md:text-xs font-light tracking-[0.2em] leading-loose">
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
print('Reverted to Brutalist Clean layout.')
