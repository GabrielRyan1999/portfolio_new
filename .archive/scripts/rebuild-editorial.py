import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

new_home = '''function Home() {
  return (
    <section id="home" className="relative min-h-screen w-full bg-[#F5F2EB] text-[#111C2B] overflow-hidden pt-24 md:pt-32 px-6 md:px-16 flex flex-col justify-between">
      
      {/* Top Editorial Meta Bar */}
      <div className="w-full flex justify-between items-end uppercase tracking-[0.2em] text-[10px] md:text-xs font-semibold pb-4 border-b border-[#111C2B]/20 relative z-20">
        <span>Archive / 2026</span>
        <span className="text-right">Tech & Education<br/>Visual Study</span>
      </div>

      {/* Main Content Grid */}
      <div className="flex-1 grid grid-cols-1 md:grid-cols-12 gap-8 md:gap-12 mt-8 md:mt-12 relative z-20">
        
        {/* Left: Giant Typography & Intro */}
        <div className="md:col-span-7 flex flex-col justify-center pb-12 md:pb-24">
          <h1 className="font-serif text-[18vw] md:text-[9.5vw] font-bold leading-[0.85] tracking-tight">
            GABRIEL
            <br />
            RYAN<span className="text-blue-700">.</span>
          </h1>
          
          <div className="mt-8 md:mt-16 max-w-lg border-l-2 border-[#111C2B]/20 pl-6">
            <h2 className="text-lg md:text-2xl font-light leading-relaxed text-slate-800">
              Bridging the gap between complex engineering and human comprehension.
            </h2>
            <div className="mt-6 flex items-baseline space-x-2 text-sm md:text-base font-medium tracking-widest uppercase text-blue-800">
              <span>I AM A</span>
              <span className="border-b border-blue-800 pb-1">
                <AnimatedWords />
              </span>
            </div>
          </div>
        </div>

        {/* Right: Anchored Portrait */}
        <div className="md:col-span-5 h-[50vh] md:h-auto relative flex items-end justify-center md:justify-end">
          {/* Architectural Arch Backdrop */}
          <div className="absolute bottom-0 w-[80%] md:w-full h-[90%] bg-[#E5D5C5] rounded-t-full shadow-inner border border-[#111C2B]/10"></div>
          
          {/* Portrait Image */}
          <div className="relative z-10 w-[90%] md:w-[110%] h-full flex items-end">
             <img 
               src="/profile-nobg.png" 
               alt="Gabriel Ryan" 
               className="w-full h-auto max-h-[75vh] object-contain object-bottom drop-shadow-2xl grayscale contrast-125 hover:grayscale-0 transition-all duration-700" 
             />
          </div>
        </div>
      </div>

      {/* Background Ambient Decor (Extremely Subtle) */}
      <div className="absolute top-[20%] left-[-10vw] w-[40vw] aspect-square rounded-full border-[1px] border-[#111C2B] opacity-5 pointer-events-none"></div>
    </section>
  );
}'''

# Replace the Home component
content = re.sub(r'function Home\(\) \{.*?(?=function About\(\) \{)', new_home + '\n\n', content, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Rebuilt Home section as Clean Editorial.')
