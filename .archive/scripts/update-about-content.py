import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

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
        <div className="flex-1 flex flex-col md:flex-row w-full h-full overflow-y-auto md:overflow-hidden">
           
           {/* Col 1: Title & Stats */}
           <div className="w-full md:w-[25%] p-6 md:p-12 border-b md:border-b-0 md:border-r border-[#1A365D] flex flex-col justify-between shrink-0">
               <motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: true }}>
                   <motion.h2 variants={fadeUp} className="font-sans font-black text-5xl md:text-6xl tracking-tighter uppercase leading-[0.8] mb-12">
                       Gabriel<br/>Ryan<br/>Prima
                   </motion.h2>
                   
                   <motion.div variants={fadeUp} className="mb-8">
                     <div className="text-[10px] md:text-xs tracking-widest uppercase font-semibold opacity-60 mb-2">Primary Role</div>
                     <div className="text-sm font-bold uppercase text-blue-700">Educator & System Builder</div>
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
           <div className="w-full md:w-[45%] p-6 md:p-12 border-b md:border-b-0 md:border-r border-[#1A365D] flex flex-col justify-center overflow-y-auto">
               <motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: true }}>
                  <motion.p variants={fadeUp} className="font-serif text-lg md:text-xl leading-relaxed text-[#1A365D] text-justify mb-8">
                     <span className="float-left text-7xl md:text-8xl font-serif font-black leading-[0.7] mr-4 md:mr-6 text-[#1A365D] mt-2">I</span>
                     work at the intersection of technology and education based in Yogyakarta, Indonesia. My background is in computer engineering, but somewhere along the way teaching became the thing I actually care about, and combining the two has become my life's focus ever since.
                  </motion.p>
                  
                  <motion.div variants={fadeUp} className="mb-8">
                     <h3 className="font-sans font-black text-xl md:text-2xl tracking-tighter uppercase mb-2">Background</h3>
                     <p className="font-serif text-base md:text-lg leading-relaxed text-[#1A365D] text-justify">
                        I graduated in Computer Engineering, and that technical foundation is why I approach education the way I do: not as content delivery, but as a system you design with intention, one that has to hold up in practice, not just in theory.
                     </p>
                  </motion.div>

                  <motion.div variants={fadeUp}>
                     <h3 className="font-sans font-black text-xl md:text-2xl tracking-tighter uppercase mb-2">Outside of Work</h3>
                     <p className="font-serif text-base md:text-lg leading-relaxed text-[#1A365D] text-justify">
                        When I'm not building or teaching, I'm usually gaming, gardening, or digging into personal finance and investing.
                     </p>
                  </motion.div>
               </motion.div>
           </div>

           {/* Col 3: The 3 Cards */}
           <div className="w-full md:w-[30%] bg-[#1A365D] text-[#F5F2EB] flex flex-col shrink-0 p-0">
               
               {/* Card 1: Curriculum Development */}
               <div className="flex-1 border-b border-[#F5F2EB]/30 p-6 md:p-8 lg:p-12 flex flex-col justify-center relative group hover:bg-[#F5F2EB] hover:text-[#1A365D] transition-colors duration-500 cursor-default">
                  <span className="absolute top-4 left-6 text-[10px] font-mono tracking-widest uppercase opacity-50 group-hover:opacity-100 transition-opacity">01</span>
                  <h3 className="font-sans font-black text-2xl md:text-3xl lg:text-4xl tracking-tighter uppercase mb-4 mt-2 leading-[0.9]">Curriculum<br/>Development</h3>
                  <p className="font-serif text-sm md:text-base leading-relaxed opacity-80 group-hover:opacity-100 transition-opacity">
                     Designing structured, engaging, and industry-aligned tech learning paths for students of all levels.
                  </p>
               </div>

               {/* Card 2: Modern Web */}
               <div className="flex-1 border-b border-[#F5F2EB]/30 p-6 md:p-8 lg:p-12 flex flex-col justify-center relative group hover:bg-[#F5F2EB] hover:text-[#1A365D] transition-colors duration-500 cursor-default">
                  <span className="absolute top-4 left-6 text-[10px] font-mono tracking-widest uppercase opacity-50 group-hover:opacity-100 transition-opacity">02</span>
                  <h3 className="font-sans font-black text-2xl md:text-3xl lg:text-4xl tracking-tighter uppercase mb-4 mt-2 leading-[0.9]">Modern<br/>Web</h3>
                  <p className="font-serif text-sm md:text-base leading-relaxed opacity-80 group-hover:opacity-100 transition-opacity">
                     Building fast, scalable full-stack applications.
                  </p>
               </div>

               {/* Card 3: Mentoring */}
               <div className="flex-1 p-6 md:p-8 lg:p-12 flex flex-col justify-center relative bg-blue-600 text-white hover:bg-[#F5F2EB] hover:text-[#1A365D] transition-colors duration-500 cursor-default">
                  <span className="absolute top-4 left-6 text-[10px] font-mono tracking-widest uppercase opacity-70 group-hover:opacity-100 transition-opacity">03</span>
                  <h3 className="font-sans font-black text-2xl md:text-3xl lg:text-4xl tracking-tighter uppercase mb-4 mt-2 leading-[0.9]">Mentoring</h3>
                  <p className="font-serif text-sm md:text-base leading-relaxed opacity-90 group-hover:opacity-100 transition-opacity">
                     Guiding the next generation of software engineers.
                  </p>
               </div>

           </div>

        </div>
      </section>
    </PageTransition>
  );
}
'''

content = re.sub(about_regex, new_about + '\n', content, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated About section content.')
