import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the broken Right Image Half container
old_image_container = r'\{\/\* Right Image Half \*\/\}[\s\S]*?(?=\{\/\* Editorial Corner Mark \*\/\})'

new_image_container = '''{/* Right Image Half */}
           <div className="w-full md:w-[60%] relative h-[400px] md:h-auto bg-[#0a1526] overflow-hidden">
               <AnimatePresence mode="wait">
                  <motion.div
                      key={workIndex}
                      initial={{ opacity: 0, scale: 1.02 }}
                      animate={{ opacity: 1, scale: 1 }}
                      exit={{ opacity: 0 }}
                      transition={{ duration: 0.6 }}
                      className="absolute inset-0 flex items-center justify-center p-8 md:p-16 lg:p-24"
                  >
                     <div className="relative w-full h-full flex items-center justify-center">
                       {/* Subtle frame behind the image for an editorial look */}
                       <div className="absolute inset-0 border border-[#F5F2EB]/10 bg-[#1A365D]/30 shadow-2xl"></div>
                       
                       <img 
                          src={workProjects[workIndex].img} 
                          alt={workProjects[workIndex].title}
                          className="relative z-10 w-full h-full object-contain object-center grayscale contrast-125 mix-blend-luminosity opacity-80 hover:grayscale-0 hover:mix-blend-normal hover:opacity-100 transition-all duration-700"
                       />
                     </div>
                  </motion.div>
               </AnimatePresence>
               '''

content = re.sub(old_image_container, new_image_container, content, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed flexbox explosion in Right Image Half.')
