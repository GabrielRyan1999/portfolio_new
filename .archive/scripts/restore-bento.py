import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

about_regex = r'export function About\(\) \{[\s\S]*?(?=export function Work\(\) \{)'

new_about = '''export function About() {
  return (
    <PageTransition>
      <section id="about-me" className="relative w-full min-h-[100svh] bg-[#F5F2EB] flex items-center py-20 overflow-hidden border-t-2 border-[#1A365D]">
        
        {/* Background Accent (Optional soft watermark style if desired, kept very subtle) */}
        <div className="absolute top-0 right-0 w-full h-full pointer-events-none overflow-hidden opacity-5">
           <div className="absolute -top-40 -right-40 w-[600px] h-[600px] rounded-full border-[1px] border-[#1A365D]"></div>
           <div className="absolute -bottom-40 -left-40 w-[800px] h-[800px] rounded-full border-[1px] border-[#1A365D]"></div>
        </div>

        <div className="w-full max-w-6xl mx-auto flex flex-col lg:flex-row items-center gap-12 lg:gap-20 px-6 relative z-10">
          
          {/* Left: Shortened Editorial Story */}
          <div className="w-full lg:w-1/2 flex flex-col justify-center space-y-8">
            <div>
              <motion.h3 variants={fadeUp} initial="hidden" whileInView="visible" viewport={{ once: true }} className="text-5xl md:text-7xl font-black font-serif text-[#1A365D] tracking-tighter mb-4">
                Gabriel<br/>Ryan Prima
              </motion.h3>
              <motion.p variants={fadeUp} initial="hidden" whileInView="visible" viewport={{ once: true }} className="text-[#1A365D]/70 font-bold uppercase tracking-widest text-xs md:text-sm">
                Educator, Developer, & System Builder.
              </motion.p>
            </div>
            
            <motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: true }} className="space-y-6 text-[#1A365D] text-base md:text-lg leading-relaxed font-serif">
              <motion.p variants={fadeUp}>
                I don't write long autobiographies. I work at the intersection of technology and education, focusing on building scalable architectures and cultivating the mental models required to understand them.
              </motion.p>
              
              <motion.div variants={fadeUp} className="border-l-2 border-[#1A365D] pl-6 py-2 mt-8">
                <h4 className="font-bold mb-2 tracking-widest font-sans uppercase text-xs opacity-70">The Philosophy</h4>
                <p className="italic text-xl md:text-2xl leading-snug">
                  "The goal isn't just to explain how a framework works, but to build the mental models that allow someone to learn the next three on their own."
                </p>
              </motion.div>
            </motion.div>
          </div>

          {/* Right: Core Pillars Bento Box (Adapted to Editorial Colors) */}
          <motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: true }} className="w-full lg:w-1/2 grid grid-cols-2 gap-4">
             
             {/* Box 01 */}
             <motion.div variants={fadeUp} className="col-span-2 bg-[#F5F2EB] border border-[#1A365D]/20 rounded-3xl p-8 md:p-10 flex flex-col justify-center hover:border-[#1A365D]/60 transition-colors shadow-sm group">
                <div className="w-12 h-12 rounded-full bg-[#1A365D]/5 text-[#1A365D] flex items-center justify-center mb-6 group-hover:bg-[#1A365D] group-hover:text-[#F5F2EB] transition-colors">
                   <span className="font-mono font-bold text-sm">01</span>
                </div>
                <h4 className="text-2xl md:text-3xl font-black text-[#1A365D] mb-3 font-serif tracking-tight">Curriculum Development</h4>
                <p className="text-[#1A365D]/70 text-base leading-relaxed">
                   Designing structured, engaging, and industry-aligned tech learning paths for students of all levels.
                </p>
             </motion.div>

             {/* Box 02 */}
             <motion.div variants={fadeUp} className="col-span-1 bg-[#F5F2EB] border border-[#1A365D]/20 rounded-3xl p-6 md:p-8 flex flex-col justify-center hover:border-[#1A365D]/60 transition-colors shadow-sm group">
                <div className="w-10 h-10 rounded-full bg-[#1A365D]/5 text-[#1A365D] flex items-center justify-center mb-6 group-hover:bg-[#1A365D] group-hover:text-[#F5F2EB] transition-colors">
                   <span className="font-mono font-bold text-xs">02</span>
                </div>
                <h4 className="text-xl font-black text-[#1A365D] mb-2 font-serif tracking-tight">Modern Web</h4>
                <p className="text-[#1A365D]/70 text-sm leading-relaxed">
                   Building fast, scalable full-stack applications.
                </p>
             </motion.div>

             {/* Box 03 (Accent Box) */}
             <motion.div variants={fadeUp} className="col-span-1 bg-[#1A365D] border border-[#1A365D] rounded-3xl p-6 md:p-8 flex flex-col justify-center shadow-lg group">
                <div className="w-10 h-10 rounded-full bg-[#F5F2EB]/10 text-[#F5F2EB] flex items-center justify-center mb-6">
                   <span className="font-mono font-bold text-xs">03</span>
                </div>
                <h4 className="text-xl font-black text-[#F5F2EB] mb-2 font-serif tracking-tight">Mentoring</h4>
                <p className="text-[#F5F2EB]/80 text-sm leading-relaxed">
                   Guiding the next generation of software engineers.
                </p>
             </motion.div>

          </motion.div>

        </div>
      </section>
    </PageTransition>
  );
}

'''

content = re.sub(about_regex, new_about, content, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Restored Bento layout and adapted to Editorial colors.')
