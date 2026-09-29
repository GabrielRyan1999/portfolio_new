import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the entire Work function
work_regex = r'export function Work\(\) \{[\s\S]*?(?=export function Service\(\) \{)'

new_work = '''export function Work() {
  const [workIndex, setWorkIndex] = useState(0);
  const nextWork = () => setWorkIndex((p) => (p + 1) % workProjects.length);
  const prevWork = () => setWorkIndex((p) => (p - 1 + workProjects.length) % workProjects.length);
  
  return (
    <PageTransition>
      <section id="work" className="relative w-full min-h-[100svh] bg-[#1A365D] flex flex-col border-t-2 border-[#F5F2EB] overflow-hidden text-[#F5F2EB]">
        
        {/* Header Row */}
        <div className="w-full flex items-center justify-between px-6 md:px-12 py-4 border-b border-[#F5F2EB]/30 shrink-0">
           <span className="text-xs font-bold tracking-widest uppercase">Chapter 02 // Selected Work</span>
           <span className="text-xs font-bold tracking-widest uppercase font-mono">
              0{workIndex + 1} / 0{workProjects.length}
           </span>
        </div>

        {/* Main Spread */}
        <div className="flex-1 flex flex-col md:flex-row w-full h-full relative">
           
           {/* Left Content Half */}
           <div className="w-full md:w-[40%] flex flex-col justify-between border-b md:border-b-0 md:border-r border-[#F5F2EB]/30 relative z-10 shrink-0">
               
               {/* Project Details */}
               <div className="p-6 md:p-12 flex-1 flex flex-col justify-center">
                  <AnimatePresence mode="wait">
                    <motion.div
                      key={workIndex}
                      initial={{ opacity: 0, y: 10 }}
                      animate={{ opacity: 1, y: 0 }}
                      exit={{ opacity: 0, y: -10 }}
                      transition={{ duration: 0.3 }}
                      className="flex flex-col"
                    >
                      <div className="text-[10px] md:text-xs font-mono tracking-widest uppercase opacity-70 mb-4 border-b border-[#F5F2EB]/30 pb-4">
                        {workProjects[workIndex].tag}
                      </div>
                      
                      <h3 className="font-serif text-5xl md:text-7xl font-black leading-[0.9] tracking-tighter mb-6">
                        {workProjects[workIndex].title}
                      </h3>
                      
                      <p className="font-serif text-base md:text-lg leading-relaxed opacity-90 mb-10">
                        {workProjects[workIndex].desc}
                      </p>
                      
                      {/* Tech Stack */}
                      <div className="flex flex-wrap gap-3 mb-12">
                        {workProjects[workIndex].tech.map(tech => (
                          <span key={tech} className="px-3 py-1 border border-[#F5F2EB]/40 text-xs font-bold tracking-widest uppercase">
                            {tech}
                          </span>
                        ))}
                      </div>

                      <a href={workProjects[workIndex].url} target="_blank" rel="noreferrer" className="group flex items-center gap-4 w-fit hover:opacity-70 transition-opacity">
                         <span className="text-sm font-bold tracking-widest uppercase border-b border-[#F5F2EB] pb-1">
                           View Live Project
                         </span>
                         <span className="font-mono text-lg leading-none group-hover:translate-x-2 transition-transform">→</span>
                      </a>
                    </motion.div>
                  </AnimatePresence>
               </div>

               {/* Brutalist Navigation Controls */}
               <div className="flex border-t border-[#F5F2EB]/30 h-16 md:h-20 shrink-0">
                  <button onClick={prevWork} className="flex-1 border-r border-[#F5F2EB]/30 flex items-center justify-center hover:bg-[#F5F2EB] hover:text-[#1A365D] transition-colors group">
                     <span className="text-xs font-bold tracking-widest uppercase">Previous</span>
                  </button>
                  <button onClick={nextWork} className="flex-1 flex items-center justify-center hover:bg-[#F5F2EB] hover:text-[#1A365D] transition-colors group">
                     <span className="text-xs font-bold tracking-widest uppercase">Next</span>
                  </button>
               </div>

           </div>
           
           {/* Right Image Half */}
           <div className="w-full md:w-[60%] relative h-[400px] md:h-auto bg-[#0a1526] overflow-hidden">
               <AnimatePresence mode="wait">
                  <motion.div
                      key={workIndex}
                      initial={{ opacity: 0, scale: 1.05 }}
                      animate={{ opacity: 1, scale: 1 }}
                      exit={{ opacity: 0 }}
                      transition={{ duration: 0.6 }}
                      className="absolute inset-0"
                  >
                     <img 
                        src={workProjects[workIndex].img} 
                        alt={workProjects[workIndex].title}
                        className="w-full h-full object-cover object-center grayscale contrast-125 mix-blend-luminosity opacity-80 hover:grayscale-0 hover:mix-blend-normal hover:opacity-100 transition-all duration-700"
                     />
                  </motion.div>
               </AnimatePresence>
               {/* Editorial Corner Mark */}
               <div className="absolute bottom-6 right-6 md:bottom-12 md:right-12 border border-[#F5F2EB]/30 bg-[#1A365D]/80 backdrop-blur-md px-4 py-2 pointer-events-none">
                  <span className="text-[10px] font-mono tracking-widest uppercase">Fig. 0{workIndex + 1}</span>
               </div>
           </div>

        </div>
      </section>
    </PageTransition>
  );
}
'''

content = re.sub(work_regex, new_work, content, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Redesigned Work section with Editorial Brutalism.')
