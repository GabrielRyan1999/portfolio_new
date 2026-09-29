import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Target Col 2
old_col2 = r'\{\/\* Col 2: The Story \*\/\}.*?\{\/\* Col 3: The Pull Quote \*\/\}'

new_col2 = '''{/* Col 2: Operating Principles */}
           <div className="w-full md:w-[45%] p-6 md:p-12 border-b md:border-b-0 md:border-r border-[#1A365D] flex flex-col justify-center">
               <motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: true }} className="flex flex-col gap-8 md:gap-10">
                   
                   <motion.div variants={fadeUp} className="border-t border-[#1A365D] pt-4">
                      <div className="flex justify-between items-baseline mb-4">
                         <h3 className="font-sans text-xl md:text-2xl font-black uppercase tracking-tighter text-[#1A365D]">Architecture</h3>
                         <span className="font-mono text-xs font-bold opacity-50">01</span>
                      </div>
                      <p className="font-serif text-base md:text-lg leading-relaxed text-[#1A365D]">
                        Building systems that scale in practice, not just in theory. Fundamentals must always dictate the architecture, overriding the hype of modern frameworks.
                      </p>
                   </motion.div>

                   <motion.div variants={fadeUp} className="border-t border-[#1A365D] pt-4">
                      <div className="flex justify-between items-baseline mb-4">
                         <h3 className="font-sans text-xl md:text-2xl font-black uppercase tracking-tighter text-[#1A365D]">Mentorship</h3>
                         <span className="font-mono text-xs font-bold opacity-50">02</span>
                      </div>
                      <p className="font-serif text-base md:text-lg leading-relaxed text-[#1A365D]">
                        Education is a system designed with intention. The primary objective is to transfer resilient mental models, not just temporary syntax.
                      </p>
                   </motion.div>

                   <motion.div variants={fadeUp} className="border-t border-[#1A365D] pt-4 border-b pb-4">
                      <div className="flex justify-between items-baseline mb-4">
                         <h3 className="font-sans text-xl md:text-2xl font-black uppercase tracking-tighter text-[#1A365D]">Execution</h3>
                         <span className="font-mono text-xs font-bold opacity-50">03</span>
                      </div>
                      <p className="font-serif text-base md:text-lg leading-relaxed text-[#1A365D]">
                        No long-winded autobiographies. Delivering code that ships, logic that stands the test of time, and interfaces that respect the user.
                      </p>
                   </motion.div>

               </motion.div>
           </div>

           {/* Col 3: The Pull Quote */}'''

content = re.sub(old_col2, new_col2, content, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Replaced long story with Operating Principles index.')
