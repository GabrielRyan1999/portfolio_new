import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Match the entire Home and HomeContent functions
regex = r'export function Home\(\) \{[\s\S]*?\}\s*function HomeContent\(\{ side \}\) \{[\s\S]*?\}\s*export function About\(\)'

new_home = '''export function Home() {
  return (
    <section id="home" className="relative w-full h-[100svh] min-h-[600px] overflow-hidden bg-cream font-sans">
      
      {/* 
        LAYER 1: BASE (Right Side)
        Background: Cream, Text: Navy (GABRIEL), Beige (Ryan)
      */}
      <div className="absolute inset-0 z-0">
        {/* Background Shape */}
        <div className="absolute top-[-15vw] right-[-10vw] w-[45vw] h-[45vw] rounded-full bg-[#D7C4A5]"></div>
        
        {/* Texts */}
        <HomeContent side="right" />
      </div>

      {/* 
        LAYER 2: OVERLAY (Left Side)
        Background: Navy, Text: Cream
        Clipped to precisely 50% width.
      */}
      <div className="absolute inset-0 bg-[#213555] z-10" style={{ clipPath: 'polygon(0 0, 50% 0, 50% 100%, 0 100%)' }}>
        {/* Background Lines (Concentric Circles) */}
        <div className="absolute bottom-[-15vw] left-[-15vw] w-[45vw] h-[45vw] rounded-full border-[0.5px] border-cream/20"></div>
        <div className="absolute bottom-[-25vw] left-[-25vw] w-[65vw] h-[65vw] rounded-full border-[0.5px] border-cream/10"></div>
        
        {/* Texts */}
        <HomeContent side="left" />
      </div>

      {/* LAYER 3: PORTRAIT (Topmost) */}
      <div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-[85%] md:w-[600px] max-w-3xl flex justify-center z-20 pointer-events-none">
        <img 
          src="/profile-nobg.png" 
          alt="Gabriel Ryan" 
          className="w-full h-auto max-h-[85vh] object-contain object-bottom grayscale drop-shadow-2xl brightness-105 contrast-125" 
        />
      </div>

    </section>
  );
}

function HomeContent({ side }) {
  const isLeft = side === 'left';
  
  // Exact color mapping based on side
  const gabrielColor = isLeft ? 'text-[#F5F2EB]' : 'text-[#213555]';
  const ryanColor = isLeft ? 'text-[#F5F2EB]' : 'text-[#D7C4A5]';
  const metaColor = isLeft ? 'text-cream' : 'text-[#213555]';
  
  return (
    <div className={`absolute inset-0 flex flex-col items-center justify-center pointer-events-none ${metaColor}`}>
      
      {/* Center Typography */}
      <div className="relative w-full flex flex-col items-center justify-center mt-[-15vh]">
        <h1 className={`font-serif text-[22vw] md:text-[19vw] font-black tracking-[-0.03em] leading-none uppercase z-10 relative ${gabrielColor}`}>
          GABRIEL
        </h1>
        {/* Cursive text overlapping */}
        <div className={`absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 mt-[6vw] ml-[3vw] z-20 opacity-90 ${ryanColor}`}>
          <span className="font-mayonice text-[18vw] md:text-[15vw] leading-none whitespace-nowrap -rotate-[6deg] inline-block drop-shadow-sm">
            Ryan
          </span>
        </div>
      </div>

      {/* Top Left Meta */}
      <div className="absolute top-8 left-8 md:top-12 md:left-12 flex flex-col gap-1 text-[10px] md:text-xs font-bold tracking-[0.2em] uppercase">
        <span>VOL. 01</span>
        <span>OCT / 2026</span>
      </div>

      {/* Top Right Meta */}
      <div className="absolute top-8 right-8 md:top-12 md:right-12 flex flex-col gap-1 text-[10px] md:text-xs font-bold tracking-[0.2em] uppercase text-right">
        <span>VISUAL STUDY</span>
        <span>BY GABRIEL RYAN</span>
      </div>

      {/* Bottom Left Meta */}
      <div className="absolute bottom-12 left-8 md:bottom-24 md:left-12 flex flex-col gap-6 text-[10px] md:text-xs font-bold tracking-[0.15em] uppercase">
        <span className="opacity-70 tracking-[0.2em]">ROLE //</span>
        <span className="text-sm md:text-base font-black tracking-[0.1em]">EDUCATOR & DEVELOPER.</span>
        <div className="w-12 h-[1px] bg-current opacity-50"></div>
        <span className="tracking-[0.2em]">EST. 2026</span>
      </div>

      {/* Middle Right Stamp */}
      <div className="absolute top-1/2 -translate-y-1/2 right-4 md:right-16 flex items-center gap-4 md:gap-6 mt-16">
        {/* The Stamp Box */}
        <div className="relative w-24 h-24 md:w-32 md:h-32">
           {/* Offset Shadow Box */}
           <div className="absolute inset-0 bg-[#E0DFDC] transform translate-x-2 translate-y-2 md:translate-x-3 md:translate-y-3"></div>
           {/* Main Photo Box */}
           <div className="absolute inset-0 bg-[#F5F2EB] p-2 md:p-3 shadow-sm border border-[#E0DFDC] flex items-center justify-center">
              <img src="/favicon.jpg" alt="Author" className="w-full h-full object-cover grayscale contrast-125 bg-gray-200" onError={(e) => { e.target.src = 'https://api.dicebear.com/7.x/notionists/svg?seed=Gabriel&backgroundColor=e5e5e5'; }} />
           </div>
        </div>
        {/* Vertical Text */}
        <div className="flex items-center gap-2 text-[8px] md:text-[9px] font-bold tracking-[0.25em] uppercase opacity-70" style={{ writingMode: 'vertical-rl' }}>
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

print("Hero section fully rewritten to exactly match the mockup")
