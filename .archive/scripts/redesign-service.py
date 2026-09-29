import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the entire Service function
service_regex = r'export function Service\(\) \{[\s\S]*?(?=export function Experience\(\) \{)'

new_service = '''export function Service() {
    const [activeServiceIndex, setActiveServiceIndex] = useState(null);
    return (
      <PageTransition>
        <section id="service" className="relative w-full min-h-[100svh] bg-[#F5F2EB] py-24 md:py-32 flex flex-col border-t-2 border-[#1A365D] overflow-hidden">
          
          {/* Header */}
          <div className="w-full max-w-7xl mx-auto px-6 mb-16 md:mb-24 flex flex-col md:flex-row md:items-end justify-between gap-8 z-10">
             <div>
                <span className="text-xs font-bold tracking-widest uppercase text-[#1A365D]/50 font-mono mb-4 block">Chapter 03</span>
                <h2 className="font-serif text-5xl md:text-7xl lg:text-8xl font-black text-[#1A365D] tracking-tighter leading-[0.85]">SERVICES<br/>& EXPERTISE</h2>
             </div>
             <p className="max-w-md text-[#1A365D]/80 font-serif text-lg leading-relaxed border-l-2 border-[#1A365D] pl-6">
                A rigorous approach to engineering and education. I partner with organizations to build resilient systems and the minds that maintain them.
             </p>
          </div>

          {/* Brutalist Accordion */}
          <div className="w-full flex flex-col z-10 border-b-2 border-[#1A365D]">
            {[
              { title: "CUSTOM WEB PLATFORMS", desc: "Building fast, scalable, and robust web applications, internal dashboards, and custom platforms tailored to your business needs.", images: ["https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=400&q=80", "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=400&q=80", "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?w=400&q=80"] },
              { title: "EDTECH SOLUTIONS", desc: "Developing custom learning management systems (LMS) and student progress trackers designed with pedagogical best practices.", images: ["https://images.unsplash.com/photo-1501504905252-473c47e087f8?w=400&q=80", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400&q=80", "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=400&q=80"] },
              { title: "CURRICULUM DEV", desc: "Crafting structured, tech-focused syllabi and scalable learning materials for online, hybrid, and offline educational environments.", images: ["https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=400&q=80", "https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=400&q=80", "https://images.unsplash.com/photo-1503694978374-8a2fa686963a?w=400&q=80"] },
              { title: "1-ON-1 TECH MENTORING", desc: "Providing personalized coaching in programming, 3D modeling, and game development for students and professionals looking to level up their skills.", images: ["https://images.unsplash.com/photo-1531482615713-2afd69097998?w=400&q=80", "https://images.unsplash.com/photo-1573164713988-8665fc963095?w=400&q=80", "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=400&q=80"] }
            ].map((service, index) => {
              const isOpen = activeServiceIndex === index;
              return (
                <div key={service.title} className={`w-full border-t-2 border-[#1A365D] overflow-hidden transition-colors duration-500 ${isOpen ? 'bg-[#1A365D] text-[#F5F2EB]' : 'bg-transparent text-[#1A365D]'}`}>
                  
                  <button
                      onClick={() => setActiveServiceIndex(isOpen ? null : index)}
                      aria-expanded={isOpen}
                      className={`w-full flex items-center justify-between py-8 md:py-12 px-6 md:px-12 transition-colors ${isOpen ? '' : 'hover:bg-[#1A365D]/5'}`}
                    >
                      <div className="flex items-center gap-6 md:gap-12">
                        <span className={`text-sm md:text-lg font-mono font-bold ${isOpen ? 'text-[#F5F2EB]/50' : 'text-[#1A365D]/50'}`} aria-hidden="true">
                          0{index + 1}
                        </span>
                        <span className="font-serif text-3xl md:text-5xl lg:text-7xl font-black text-left tracking-tighter uppercase transition-colors">
                          {service.title}
                        </span>
                      </div>
                      
                      <span className={`font-mono text-5xl md:text-7xl font-light leading-none ${isOpen ? 'text-[#F5F2EB]' : 'text-[#1A365D] opacity-30 group-hover:opacity-100'}`}>
                        {isOpen ? "-" : "+"}
                      </span>
                    </button>
      
                  <AnimatePresence initial={false}>
                    {isOpen && (
                      <motion.div
                        initial="collapsed"
                        animate="open"
                        exit="collapsed"
                        variants={{
                          open: { opacity: 1, height: "auto" },
                          collapsed: { opacity: 0, height: 0 }
                        }}
                        transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
                        className="px-6 md:px-12"
                      >
                        <div className="pb-12 md:pb-16 pt-4 flex flex-col lg:flex-row gap-12 lg:gap-24">
                          
                          {/* Description Side */}
                          <div className="w-full lg:w-1/3">
                             <p className="text-[#F5F2EB]/90 text-lg md:text-xl font-serif leading-relaxed">
                               {service.desc}
                             </p>
                          </div>
                          
                          {/* Images Side (Contact Sheet Grid) */}
                          <div className="w-full lg:w-2/3 grid grid-cols-1 sm:grid-cols-3 gap-0 border border-[#F5F2EB]/20">
                            {service.images.map((img, i) => (
                              <div key={i} className={`aspect-square relative overflow-hidden bg-[#0a1526] ${i > 0 ? 'border-t sm:border-t-0 sm:border-l border-[#F5F2EB]/20' : ''}`}>
                                <img
                                  src={img}
                                  alt=""
                                  className="w-full h-full object-cover grayscale contrast-125 hover:grayscale-0 transition-all duration-700 opacity-80 hover:opacity-100 mix-blend-luminosity hover:mix-blend-normal"
                                />
                                <div className="absolute top-2 left-2 bg-[#F5F2EB] px-2 py-0.5 pointer-events-none">
                                   <span className="text-[9px] font-mono font-bold text-[#1A365D]">IMG_0{i+1}</span>
                                </div>
                              </div>
                            ))}
                          </div>

                        </div>
                      </motion.div>
                    )}
                  </AnimatePresence>

                </div>
              );
            })}
          </div>

        </section>
      </PageTransition>
    );
}
'''

content = re.sub(service_regex, new_service, content, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Redesigned Service section with Editorial Brutalism.')
