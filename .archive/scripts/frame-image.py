import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Target the Right Image Half
old_right_image = r'\{\/\* Right Image Half \*\/\}[\s\S]*?<\/div>\s*<\/div>\s*<\/section>'

new_right_image = '''{/* Right Image Half (Framed Gallery Style) */}
           <div className="w-full md:w-[60%] relative h-[50vh] md:h-auto bg-[#1A365D] flex items-center justify-center p-8 md:p-20 lg:p-32">
               
               {/* The Frame */}
               <div className="relative w-full h-full max-h-[60vh] border border-[#F5F2EB]/30 bg-zinc-950 overflow-hidden shadow-2xl group">
                   <AnimatePresence mode="wait">
                      <motion.div
                          key={workIndex}
                          initial={{ opacity: 0, scale: 1.02 }}
                          animate={{ opacity: 1, scale: 1 }}
                          exit={{ opacity: 0 }}
                          transition={{ duration: 0.6 }}
                          className="absolute inset-0"
                      >
                         <img 
                            src={workProjects[workIndex].img} 
                            alt={workProjects[workIndex].title}
                            className="w-full h-full object-cover object-center grayscale contrast-125 mix-blend-luminosity opacity-80 group-hover:grayscale-0 group-hover:mix-blend-normal group-hover:opacity-100 transition-all duration-700"
                         />
                      </motion.div>
                   </AnimatePresence>
                   
                   {/* Editorial Corner Mark (Moved inside the frame) */}
                   <div className="absolute bottom-0 right-0 border-t border-l border-[#F5F2EB]/30 bg-[#1A365D] px-4 py-2 pointer-events-none">
                      <span className="text-[10px] font-mono tracking-widest uppercase text-[#F5F2EB]">Fig. 0{workIndex + 1}</span>
                   </div>
               </div>

           </div>

        </div>
      </section>'''

content = re.sub(old_right_image, new_right_image, content, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Framed the oversized image.')
