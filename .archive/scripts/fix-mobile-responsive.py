import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the entire HomeContent and Home to ensure perfect responsive classes

regex = r'export function Home\(\) \{[\s\S]*?\}\s*export function About\(\)'

new_home = '''export function Home() {
  return (
    <section id="home" className="relative w-full h-[100svh] min-h-[600px] overflow-hidden bg-[#F5F2EB] font-sans">
      
      {/* 
        LAYER 1: BASE (Right Side)
      */}
      <div className="absolute inset-0 z-0">
        <div className="absolute top-[-25vw] right-[-15vw] w-[55vw] h-[55vw] rounded-full bg-[#E5D8C5]"></div>
        <HomeContent side="right" />
      </div>

      {/* 
        LAYER 2: OVERLAY (Left Side)
      */}
      <div className="absolute inset-0 bg-[#213555] z-10" style={{ clipPath: 'polygon(0 0, 50% 0, 50% 100%, 0 100%)' }}>
        <div className="absolute bottom-[-15vw] left-[-20vw] w-[50vw] h-[50vw] rounded-full border-[0.5px] border-cream/20"></div>
        <div className="absolute bottom-[-25vw] left-[-30vw] w-[70vw] h-[70vw] rounded-full border-[0.5px] border-cream/10"></div>
        <HomeContent side="left" />
      </div>

      {/* LAYER 3: PORTRAIT (Topmost) */}
      {/* Fixed the scaling: Mobile uses a controlled width so it doesn't become gigantically tall and cover the UI. Desktop uses vh so it accurately reaches the text. */}
      <div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-full flex justify-center z-20 pointer-events-none">
        <img 
          src="/profile-nobg.png" 
          alt="Gabriel Ryan" 
          className="w-[130%] sm:w-[90%] md:w-auto h-auto md:h-[75vh] xl:h-[80vh] max-w-none object-contain object-bottom grayscale drop-shadow-2xl brightness-105 contrast-125" 
        />
      </div>

    </section>
  );
}

function HomeContent({ side }) {
  const isLeft = side === 'left';
  
  const gabrielColor = isLeft ? 'text-[#F5F2EB]' : 'text-[#213555]';
  const ryanColor = isLeft ? 'text-[#F5F2EB]' : 'text-[#E5D8C5]';
  const metaColor = isLeft ? 'text-[#F5F2EB]' : 'text-[#213555]';
  
  return (
    <div className={`absolute inset-0 flex flex-col pointer-events-none ${metaColor}`}>
      
      {/* Center Typography (Adjusted for mobile to drop down to meet the smaller portrait) */}
      <div className="absolute top-[25%] md:top-[12%] left-0 w-full flex flex-col items-center justify-start">
        <h1 className={`font-serif text-[32vw] md:text-[23.5vw] font-black tracking-[-0.04em] leading-[0.8] uppercase z-10 relative ${gabrielColor}`}>
          GABRIEL
        </h1>
        {/* Cursive text overlapping */}
        <div className={`absolute top-[60%] md:top-[65%] left-1/2 -translate-x-1/2 mt-[2vw] ml-[6vw] z-20 opacity-90 ${ryanColor}`}>
          <span className="font-mayonice text-[35vw] md:text-[22vw] leading-none whitespace-nowrap -rotate-[5deg] inline-block drop-shadow-sm">
            Ryan
          </span>
        </div>
      </div>

      {/* Top Left Meta (z-30 to stay above portrait on mobile) */}
      <div className="absolute top-8 left-8 md:top-12 md:left-12 flex flex-col gap-1 text-[10px] md:text-xs font-bold tracking-[0.2em] uppercase z-30">
        <span>VOL. 01</span>
        <span>OCT / 2026</span>
      </div>

      {/* Top Right Meta */}
      <div className="absolute top-8 right-8 md:top-12 md:right-12 flex flex-col gap-1 text-[10px] md:text-xs font-bold tracking-[0.2em] uppercase text-right z-30">
        <span>VISUAL STUDY</span>
        <span>BY GABRIEL RYAN</span>
      </div>

      {/* Bottom Left Meta (z-30 guarantees it is never covered by the suit on narrow screens) */}
      <div className="absolute bottom-12 left-8 md:bottom-24 md:left-12 flex flex-col gap-6 text-[10px] md:text-xs font-bold tracking-[0.15em] uppercase z-30">
        <span className="opacity-70 tracking-[0.2em]">ROLE //</span>
        <span className="text-sm md:text-base font-black tracking-[0.1em] drop-shadow-md">EDUCATOR & DEVELOPER.</span>
        <div className="w-12 h-[1px] bg-current opacity-50"></div>
        <span className="tracking-[0.2em]">EST. 2026</span>
      </div>

      {/* Middle Right Stamp */}
      <div className="absolute top-[45%] md:top-1/2 -translate-y-1/2 right-12 md:right-24 flex items-center mt-12 md:mt-24 z-30">
        <div className="relative w-20 h-20 md:w-28 md:h-28 z-10">
           <div className="absolute inset-0 bg-[#E0DFDC] transform translate-x-2 translate-y-2 md:translate-x-3 md:translate-y-3"></div>
           <div className="absolute inset-0 bg-[#F5F2EB] p-2 shadow-sm border border-[#E0DFDC] flex items-center justify-center">
              <img src="/favicon.jpg" alt="Author" className="w-full h-full object-cover grayscale contrast-125 bg-gray-200" onError={(e) => { e.target.src = 'https://api.dicebear.com/7.x/notionists/svg?seed=Gabriel&backgroundColor=e5e5e5'; }} />
           </div>
        </div>
        <div className="absolute right-[-4.5rem] md:right-[-5.5rem] top-1/2 -translate-y-1/2 origin-center rotate-90 text-[8px] md:text-[9px] font-bold tracking-[0.25em] uppercase opacity-70 whitespace-nowrap drop-shadow-md">
          FIG. 01 &mdash; AUTHOR
        </div>
      </div>

    </div>
  );
}

export function About()'''

content = re.sub(regex, new_home, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Responsive logic fixed.")
