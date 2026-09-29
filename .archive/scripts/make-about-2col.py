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
           <span className="text-xs font-bold tracking-widest uppercase">Chapter 01 // About Me</span>
           <span className="text-xs font-bold tracking-widest uppercase hidden md:inline-block">Yogyakarta, ID</span>
        </div>

        {/* 2-Column Spread */}
        <div className="flex-1 flex flex-col md:flex-row w-full h-full">
           
           {/* Left Column: Text Content */}
           <div className="w-full md:w-1/2 p-6 md:p-12 lg:p-16 border-b md:border-b-0 md:border-r border-[#1A365D] flex flex-col justify-center relative overflow-hidden">
               {/* Background Watermark Avatar (Editorial Style) */}
               <div className="absolute -bottom-20 -left-20 w-[400px] h-[400px] opacity-[0.03] pointer-events-none">
                  <img src="/favicon.jpg" alt="" className="w-full h-full object-cover rounded-full grayscale" />
               </div>

               <motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: true }} className="relative z-10">
                   <motion.h2 variants={fadeUp} className="font-sans font-black text-6xl md:text-7xl lg:text-8xl tracking-tighter uppercase leading-[0.85] mb-4">
                       Gabriel Ryan<br/>Prima
                   </motion.h2>
                   <motion.div variants={fadeUp} className="font-sans font-bold text-lg md:text-xl text-blue-700 tracking-tight uppercase mb-12">
                       Educator, Developer, & System Builder.
                   </motion.div>
                   
                   <motion.p variants={fadeUp} className="font-serif text-lg md:text-xl leading-relaxed text-[#1A365D] text-justify mb-8">
                      I work at the intersection of technology and education based in Yogyakarta, Indonesia. My background is in computer engineering, but somewhere along the way teaching became the thing I actually care about, and combining the two has become my life's focus ever since.
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

           {/* Right Column: 3 Cards (Editorial Grid) */}
           <div className="w-full md:w-1/2 flex flex-col bg-[#F5F2EB]">
              
              {/* Top Card: Curriculum Development */}
              <div className="w-full flex-1 min-h-[300px] border-b border-[#1A365D] p-8 md:p-12 lg:p-16 flex flex-col justify-center relative group hover:bg-[#1A365D] hover:text-[#F5F2EB] transition-colors duration-500 cursor-default">
                  <span className="absolute top-6 left-6 md:top-8 md:left-8 text-xs font-mono font-bold tracking-widest uppercase opacity-50 group-hover:opacity-100 transition-opacity">01</span>
                  <h3 className="font-sans font-black text-4xl md:text-5xl lg:text-6xl tracking-tighter uppercase mb-6 leading-[0.9]">Curriculum<br/>Development</h3>
                  <p className="font-serif text-lg md:text-xl leading-relaxed opacity-90 max-w-lg">
                     Designing structured, engaging, and industry-aligned tech learning paths for students of all levels.
                  </p>
              </div>

              {/* Bottom Cards Wrapper */}
              <div className="w-full flex-1 flex flex-col md:flex-row min-h-[300px]">
                 
                 {/* Bottom Left Card: Modern Web */}
                 <div className="w-full md:w-1/2 border-b md:border-b-0 border-[#1A365D] md:border-r p-8 md:p-10 flex flex-col justify-center relative group hover:bg-[#1A365D] hover:text-[#F5F2EB] transition-colors duration-500 cursor-default">
                    <span className="absolute top-6 left-6 md:top-8 md:left-8 text-xs font-mono font-bold tracking-widest uppercase opacity-50 group-hover:opacity-100 transition-opacity">02</span>
                    <h3 className="font-sans font-black text-3xl md:text-4xl tracking-tighter uppercase mb-4 leading-[0.9]">Modern<br/>Web</h3>
                    <p className="font-serif text-base md:text-lg leading-relaxed opacity-90">
                       Building fast, scalable full-stack applications.
                    </p>
                 </div>

                 {/* Bottom Right Card: Mentoring */}
                 <div className="w-full md:w-1/2 p-8 md:p-10 flex flex-col justify-center relative bg-blue-600 text-white hover:bg-[#1A365D] transition-colors duration-500 cursor-default">
                    <span className="absolute top-6 left-6 md:top-8 md:left-8 text-xs font-mono font-bold tracking-widest uppercase opacity-70 group-hover:opacity-100 transition-opacity">03</span>
                    <h3 className="font-sans font-black text-3xl md:text-4xl tracking-tighter uppercase mb-4 leading-[0.9]">Mentoring</h3>
                    <p className="font-serif text-base md:text-lg leading-relaxed opacity-90">
                       Guiding the next generation of software engineers.
                    </p>
                 </div>
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
print('Updated About section to exactly match user layout.')
