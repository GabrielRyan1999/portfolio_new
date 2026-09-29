import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the entire Home component
old_home = r'export function Home\(\) \{.*?^\}\n'
new_home = '''export function Home() {
  return (
    <section id="home" className="relative w-full h-[100dvh] flex flex-col items-center justify-end overflow-hidden border-b border-[var(--card-border)] bg-[var(--background)]">
      
      {/* 1. BACKGROUND GRAPHIC (Avatar transformed into Blue Halftone) */}
      <div className="absolute inset-0 top-[30%] md:top-[40%] flex justify-center opacity-80 mix-blend-multiply dark:mix-blend-screen overflow-hidden z-0">
        <div className="absolute inset-0 bg-[var(--accent)] opacity-40 mix-blend-color"></div>
        <img src="/favicon.jpg" alt="Background Avatar" className="w-full h-full object-cover grayscale contrast-[1.5] brightness-75" />
        {/* Gradient fade at top so it blends with the sky/paper */}
        <div className="absolute inset-0 bg-gradient-to-b from-[var(--background)] via-transparent to-[var(--background)]"></div>
      </div>

      {/* 2. GIANT TOP TEXT (Background Layer) */}
      <div className="absolute top-16 md:top-12 w-full text-center z-10 select-none">
        <p className="text-xs md:text-sm font-bold uppercase tracking-[0.2em] text-[var(--foreground)] mb-2 md:mb-6">The Mind Forgets, But The Code Remembers</p>
        <h1 className="text-[22vw] md:text-[240px] leading-[0.75] font-serif font-black text-[var(--foreground)] tracking-tighter uppercase">
          GABRIEL
        </h1>
      </div>

      {/* 3. FOREGROUND SUBJECT (Profile Photo No BG) */}
      <div className="relative z-20 w-[85%] md:w-[500px] h-auto flex justify-center items-end mt-auto pointer-events-none">
        {/* We use profile-nobg.png here. Fallback to profile_new.jpg if not found, though it will look blocky without bg removal */}
        <img src="/profile-nobg.png" 
             onError={(e) => { e.target.onerror = null; e.target.src='/profile_new.jpg' }}
             alt="Gabriel Ryan" 
             className="w-full h-auto object-contain object-bottom grayscale contrast-[1.2] drop-shadow-2xl" 
             style={{ maxHeight: '75vh' }} />
      </div>

      {/* 4. GIANT BOTTOM TEXT (Foreground Overlapping) */}
      <div className="absolute bottom-8 md:bottom-12 left-4 md:left-12 z-30 select-none pointer-events-none">
        <h1 className="text-[20vw] md:text-[180px] leading-[0.8] font-serif font-black text-[var(--background)] [text-shadow:-1px_-1px_0_var(--foreground),1px_-1px_0_var(--foreground),-1px_1px_0_var(--foreground),1px_1px_0_var(--foreground)] tracking-tighter uppercase">
          RYAN
        </h1>
      </div>

      {/* 5. EDITORIAL DETAILS (Left & Right) */}
      <div className="absolute top-[40%] left-6 md:left-12 text-left z-30 hidden lg:block">
         <div className="text-[var(--accent)] text-5xl mb-4 font-serif">✦</div>
         <h3 className="font-black text-2xl uppercase leading-tight text-[var(--accent)]">A VISUAL<br/>SYSTEM BUILDER</h3>
         <p className="text-xs font-bold uppercase mt-2 tracking-widest text-[var(--foreground)]">Educator / Developer<br/>Based in Yogyakarta</p>
      </div>
      
      <div className="absolute top-[40%] right-6 md:right-12 text-right z-30 hidden lg:block">
         <p className="text-xs font-bold uppercase mb-1 tracking-widest text-[var(--foreground)]">Designed By</p>
         <h3 className="font-black text-2xl uppercase text-[var(--foreground)] leading-tight">RYAN<br/>PRIMA</h3>
         <p className="text-xs font-bold uppercase mt-2 tracking-widest text-[var(--foreground-muted)]">@heyitsgabrielryan</p>
         <div className="mt-8 text-[var(--foreground)] text-3xl font-serif">✦</div>
      </div>
      
      {/* Scroll indicator */}
      <div className="absolute bottom-4 right-4 md:bottom-8 md:right-12 z-40 text-xs font-bold uppercase tracking-widest flex items-center gap-2 text-[var(--foreground)]">
        <span className="animate-pulse text-[var(--accent)]">↓</span> SCROLL TO EXPLORE
      </div>

    </section>
  );
}
'''

content = re.sub(old_home, new_home, content, flags=re.MULTILINE|re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Home component rebuilt as Magazine Cover.')
