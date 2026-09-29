import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Match the entire Home function
regex = r'export function Home\(\) \{[\s\S]*?\}\s*export function About\(\)'

new_home = '''export function Home() {
  return (
    <section id="home" className="relative w-full h-[100svh] min-h-[600px] overflow-hidden bg-cream font-sans">
      
      {/* 
        LAYER 1: BASE (Right Side)
        Background: Cream, Text: Navy 
      */}
      <div className="absolute inset-0 z-0">
        {/* Background Shape */}
        <div className="absolute top-[-10vw] right-[-5vw] w-[40vw] h-[40vw] rounded-full bg-[#E5D5C5]"></div>
        
        {/* Texts */}
        <HomeContent side="right" />
      </div>

      {/* 
        LAYER 2: OVERLAY (Left Side)
        Background: Navy, Text: Cream 
        Clipped to precisely 50% width.
      */}
      <div className="absolute inset-0 bg-navy z-10" style={{ clipPath: 'polygon(0 0, 50% 0, 50% 100%, 0 100%)' }}>
        {/* Background Lines (Concentric Circles) */}
        <div className="absolute bottom-[-20vw] left-[-10vw] w-[40vw] h-[40vw] rounded-full border border-cream/20"></div>
        <div className="absolute bottom-[-30vw] left-[-20vw] w-[60vw] h-[60vw] rounded-full border border-cream/10"></div>
        
        {/* Texts (Exact same component, colors invert due to text-current and bg-navy) */}
        <HomeContent side="left" />
      </div>

      {/* LAYER 3: PORTRAIT (Topmost) */}
      <div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-[90%] md:w-[600px] max-w-3xl flex justify-center z-20 pointer-events-none">
        <img 
          src="/profile-nobg.png" 
          alt="Gabriel Ryan" 
          className="w-full h-auto max-h-[85vh] object-contain object-bottom grayscale drop-shadow-2xl brightness-110 contrast-125" 
        />
      </div>

    </section>
  );
}

function HomeContent({ side }) {
  const isLeft = side === 'left';
  const textColor = isLeft ? 'text-cream' : 'text-navy';
  
  return (
    <div className={`absolute inset-0 flex flex-col items-center justify-center pointer-events-none ${textColor}`}>
      
      {/* Center Typography */}
      <div className="relative w-full flex flex-col items-center justify-center mt-[-15vh]">
        <h1 className="font-serif text-[22vw] md:text-[18vw] font-black tracking-tighter leading-none uppercase z-10 relative">
          GABRIEL
        </h1>
        {/* Cursive text overlapping */}
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 mt-[10vw] ml-[5vw] z-20 opacity-90">
          <span className="font-mayonice text-[18vw] md:text-[14vw] leading-none whitespace-nowrap -rotate-3 inline-block drop-shadow-sm">
            Ryan
          </span>
        </div>
      </div>

      {/* Top Left Meta */}
      <div className="absolute top-8 left-8 md:top-12 md:left-12 flex flex-col gap-1 text-[10px] md:text-xs font-bold tracking-widest uppercase">
        <span>VOL. 01</span>
        <span>OCT / 2026</span>
      </div>

      {/* Top Right Meta */}
      <div className="absolute top-8 right-8 md:top-12 md:right-12 flex flex-col gap-1 text-[10px] md:text-xs font-bold tracking-widest uppercase text-right">
        <span>VISUAL STUDY</span>
        <span>BY GABRIEL RYAN</span>
      </div>

      {/* Bottom Left Meta */}
      <div className="absolute bottom-12 left-8 md:bottom-24 md:left-12 flex flex-col gap-6 text-[10px] md:text-xs font-bold tracking-widest uppercase">
        <span className="opacity-70">ROLE //</span>
        <span className="text-sm md:text-base font-black tracking-widest">EDUCATOR & DEVELOPER.</span>
        <div className="w-12 h-[1px] bg-current opacity-50"></div>
        <span>EST. 2026</span>
      </div>

      {/* Middle Right Stamp */}
      <div className="absolute top-1/2 -translate-y-1/2 right-4 md:right-16 flex items-center gap-2 md:gap-4 mt-24">
        {/* The Stamp Box */}
        <div className="w-20 h-20 md:w-28 md:h-28 bg-[#F5F2EB] p-1.5 md:p-2 shadow-xl border border-navy/10 transform rotate-3 flex items-center justify-center relative">
          <div className="w-full h-full border border-navy/20 flex items-center justify-center overflow-hidden">
             <img src="/favicon.jpg" alt="Author" className="w-full h-full object-cover grayscale contrast-125" onError={(e) => { e.target.style.display = 'none'; e.target.nextSibling.style.display = 'block'; }} />
             <span className="hidden font-serif font-bold text-navy opacity-50 text-2xl">GR</span>
          </div>
        </div>
        {/* Vertical Text */}
        <div className="flex items-center gap-2 text-[8px] md:text-[10px] font-bold tracking-widest uppercase opacity-70" style={{ writingMode: 'vertical-rl' }}>
          <span>FIG. 01 — AUTHOR</span>
        </div>
      </div>

    </div>
  );
}

export function About()'''

content = re.sub(regex, new_home, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Hero section fully rewritten")
