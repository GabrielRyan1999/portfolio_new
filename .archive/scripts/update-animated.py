import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add AnimatedWords component
animated_component = '''
const AnimatedWords = ({ words }) => {
  const [index, setIndex] = useState(0);
  useEffect(() => {
    const timer = setInterval(() => {
      setIndex((prev) => (prev + 1) % words.length);
    }, 2500);
    return () => clearInterval(timer);
  }, [words]);
  
  return (
    <div className="inline-block relative overflow-hidden min-w-[120px] h-[1.5em] align-middle">
      <AnimatePresence mode="popLayout">
        <motion.span
          key={index}
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          exit={{ y: -20, opacity: 0 }}
          transition={{ duration: 0.5, ease: "anticipate" }}
          className="absolute left-0 text-[var(--accent)]"
        >
          {words[index]}
        </motion.span>
      </AnimatePresence>
    </div>
  );
};
'''

# Insert after imports/animation configs
if 'const AnimatedWords' not in content:
    content = re.sub(r'const staggerContainer = \{', animated_component + '\nconst staggerContainer = {', content)

# 2. Update Home to use it
old_home = r'export function Home\(\) \{.*?^\}\n'
new_home = '''export function Home() {
  return (
    <section id="home" className="relative w-full h-[100dvh] overflow-hidden bg-[#F5F2EB]">
      {/* 1. Deep Navy Color Block (Left) */}
      <div className="absolute top-0 left-0 w-[45vw] h-full bg-[#111C2B]"></div>
      
      {/* 2. Sand/Gold Circle Accent */}
      <div className="absolute top-[15%] right-[15vw] w-48 md:w-80 aspect-square rounded-full bg-[#D1C4B5] mix-blend-multiply opacity-70 z-10"></div>
      
      {/* Small Graphic Accent - Dot Grid */}
      <div className="absolute top-[30%] right-[8vw] w-24 h-24 z-10 opacity-30" style={{ backgroundImage: 'radial-gradient(#111C2B 2px, transparent 2px)', backgroundSize: '12px 12px' }}></div>

      {/* 3. Small Graphic Details (Corners) */}
      <div className="absolute top-8 left-8 md:top-12 md:left-12 z-20 text-[#F5F2EB]">
         <p className="text-[10px] uppercase tracking-widest mb-1">Vol. 01</p>
         <p className="text-[10px] uppercase tracking-widest">Oct / 2026</p>
         <div className="mt-4 text-xl">+</div>
      </div>

      <div className="absolute bottom-8 left-8 md:bottom-12 md:left-12 z-20 hidden md:block">
         <div className="text-xl text-[#F5F2EB] mb-4">+</div>
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
         <p className="text-[10px] uppercase tracking-widest text-[#111C2B]">By Gabriel Ryan</p>
         <div className="mt-2 text-xl text-[#111C2B]">+</div>
      </div>

      {/* 4. Magic Inverted Text (GABRIEL RYAN) */}
      <div className="absolute inset-0 flex flex-col items-center justify-center z-20 pointer-events-none mix-blend-difference text-white pt-0">
        <h1 className="text-[18vw] md:text-[230px] leading-[0.85] font-serif font-black tracking-tighter uppercase text-center flex flex-col w-full px-4">
          <span className="w-full text-center">GABRIEL</span>
          <span className="w-full text-center tracking-[0.1em] md:tracking-[0.2em] ml-2 md:ml-6">RYAN</span>
        </h1>
      </div>

      {/* 5. Foreground Subject (Profile Photo) */}
      <div className="absolute bottom-0 left-[55%] -translate-x-1/2 z-30 w-[95%] md:w-[750px] pointer-events-none flex justify-center">
        <img src="/profile-nobg.png" 
             onError={(e) => { e.target.onerror = null; e.target.src='/profile_new.jpg' }}
             alt="Gabriel Ryan" 
             className="w-full h-auto object-contain object-bottom grayscale contrast-125 brightness-95" 
             style={{ maxHeight: '90vh' }} />
      </div>
      
      {/* 6. Text Blocks intersecting background */}
      <div className="absolute top-[40%] left-[6vw] z-40 hidden lg:block text-[#F5F2EB]">
         <div className="text-[10px] uppercase tracking-[0.3em] font-bold leading-loose flex flex-col gap-1">
           <span className="opacity-50 text-[8px] mb-2">ROLE //</span>
           <span className="flex items-center">
             EDUCATOR & <AnimatedWords words={['DEVELOPER.', 'SYSTEM BUILDER.', 'MENTOR.']} />
           </span>
         </div>
         <div className="mt-4 text-lg">+</div>
      </div>

      <div className="absolute top-[45%] right-[6vw] z-40 hidden lg:block text-[#111C2B]">
         <p className="text-[10px] uppercase tracking-[0.3em] font-bold leading-loose">
           TIMELESS<br/>LOGIC.<br/>MODERN<br/>WEB.
         </p>
         <div className="mt-2 text-lg">+</div>
      </div>
      
      {/* 7. Bottom Right Dark Block */}
      <div className="absolute bottom-0 right-0 z-40 hidden lg:flex flex-col justify-between w-[25vw] min-w-[300px] h-40 bg-[#111C2B] text-[#F5F2EB] p-8 shadow-2xl">
         <div>
            <p className="text-[10px] uppercase tracking-[0.2em] mb-4 flex items-center gap-4">
              BUILD YOUR OWN SYSTEM <span className="flex-1 h-[1px] bg-[#F5F2EB] opacity-30"></span>
            </p>
            <p className="text-xs uppercase tracking-widest font-bold">INSPIRE. CREATE. BECOME.</p>
         </div>
         <div className="flex justify-between items-end">
            <span className="text-sm">+</span>
            <span className="text-2xl leading-none">↗</span>
         </div>
      </div>
      
      {/* Vertical Accent Box */}
      <div className="absolute top-[65%] left-[20vw] z-40 hidden lg:flex items-center justify-center bg-[#D1C4B5] p-3 py-10 shadow-lg mix-blend-multiply">
         <p className="text-[#111C2B] font-serif text-lg tracking-[0.3em] uppercase" style={{ writingMode: 'vertical-rl' }}>
            INNOVATE.
         </p>
      </div>

    </section>
  );
}
'''

content = re.sub(old_home, new_home, content, flags=re.MULTILINE|re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Animated words added.')
