import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Completely replace the About function
# Using Work() as the lookahead since it's the next exported function
about_regex = r'export function About\(\) \{[\s\S]*?(?=export function Work\(\) \{)'

new_about = '''export function About() {
  return (
    <PageTransition>
      <section id="about-me" className="relative w-full min-h-[100svh] bg-[#F5F2EB] text-[#1A365D] flex flex-col border-t-2 border-[#1A365D] overflow-hidden">
        
        {/* Header Row */}
        <div className="w-full flex items-center justify-between px-6 md:px-12 py-4 border-b border-[#1A365D] shrink-0">
           <span className="text-xs font-bold tracking-widest uppercase">Chapter 01 // Biography</span>
           <span className="text-xs font-bold tracking-widest uppercase hidden md:inline-block">Yogyakarta, ID</span>
        </div>

        {/* Main Grid Spread */}
        <div className="flex-1 flex flex-col md:flex-row w-full">
           
           {/* Col 1: Title & Stats */}
           <div className="w-full md:w-[25%] p-6 md:p-12 border-b md:border-b-0 md:border-r border-[#1A365D] flex flex-col justify-between shrink-0">
               <motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: true }}>
                   <motion.h2 variants={fadeUp} className="font-sans font-black text-5xl md:text-6xl tracking-tighter uppercase leading-[0.8] mb-12">
                       Gabriel<br/>Ryan<br/>Prima
                   </motion.h2>
                   
                   <motion.div variants={fadeUp} className="mb-8">
                     <div className="text-[10px] md:text-xs tracking-widest uppercase font-semibold opacity-60 mb-2">Primary Role</div>
                     <div className="text-sm font-bold uppercase">Educator & System Builder</div>
                   </motion.div>
                   
                   <motion.div variants={fadeUp} className="mb-8">
                     <div className="text-[10px] md:text-xs tracking-widest uppercase font-semibold opacity-60 mb-2">Experience</div>
                     <div className="text-sm font-bold uppercase">5+ Years</div>
                   </motion.div>
               </motion.div>
               
               <motion.div initial={{ opacity: 0 }} whileInView={{ opacity: 1 }} transition={{ delay: 0.5 }} className="hidden md:block w-full aspect-square border border-[#1A365D] p-2 bg-[#F5F2EB]">
                   <img src="/favicon.jpg" alt="Gabriel" className="w-full h-full object-cover grayscale contrast-125 mix-blend-multiply" />
               </motion.div>
           </div>

           {/* Col 2: The Story */}
           <div className="w-full md:w-[45%] p-6 md:p-12 border-b md:border-b-0 md:border-r border-[#1A365D] flex flex-col justify-center">
               <motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: true }}>
                  <motion.p variants={fadeUp} className="font-serif text-lg md:text-xl leading-relaxed text-[#1A365D] text-justify mb-8">
                     <span className="float-left text-7xl md:text-8xl font-serif font-black leading-[0.7] mr-4 md:mr-6 text-[#1A365D] mt-2">I</span>
                     work at the intersection of technology and education based in Yogyakarta, Indonesia. My background is in computer engineering, but somewhere along the way teaching became the thing I actually care about, and combining the two has become my life's focus ever since.
                  </motion.p>
                  <motion.p variants={fadeUp} className="font-serif text-base md:text-lg leading-relaxed text-[#1A365D] text-justify mb-8">
                     I graduated in Computer Engineering, and that technical foundation is why I approach education the way I do: not as content delivery, but as a system you design with intention, one that has to hold up in practice, not just in theory.
                  </motion.p>
                  <motion.p variants={fadeUp} className="font-serif text-base md:text-lg leading-relaxed text-[#1A365D] text-justify">
                     If I'm not designing systems or teaching, I'm probably experimenting with front-end frameworks, writing, or exploring new ways to make complex concepts simple.
                  </motion.p>
               </motion.div>
           </div>

           {/* Col 3: The Pull Quote */}
           <div className="w-full md:w-[30%] bg-[#1A365D] text-[#F5F2EB] flex flex-col justify-center p-6 md:p-12 shrink-0">
               <motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: true }}>
                 <motion.div variants={fadeUp} className="text-[10px] md:text-xs tracking-widest uppercase font-semibold opacity-70 mb-8 border-b border-[#F5F2EB]/30 pb-4">
                     Teaching Philosophy
                 </motion.div>
                 <motion.div variants={fadeUp} className="font-serif text-2xl md:text-4xl leading-snug italic">
                    "The goal isn't just to explain how a framework works, but to build the mental models that allow someone to learn the next three on their own."
                 </motion.div>
               </motion.div>
           </div>

        </div>
      </section>
    </PageTransition>
  );
}
'''

content = re.sub(about_regex, new_about, content, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Redesigned About section with Editorial Brutalism (fixed regex match).')
