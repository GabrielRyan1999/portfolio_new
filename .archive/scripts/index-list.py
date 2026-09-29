import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Target the Right Side Bento Box
old_right_side = r'\{\/\* Right: Core Pillars Bento Box \*\/\}[\s\S]*?<\/div>\s*<\/motion\.div>'

new_right_side = '''{/* Right: Editorial Index List */}
          <div className="w-full lg:w-1/2 flex flex-col mt-8 lg:mt-0 lg:pl-10">
             
             {/* Item 01 */}
             <motion.div variants={fadeUp} className="group border-t-2 border-[#1A365D] py-8 flex flex-col justify-center cursor-default hover:pr-4 transition-all duration-300">
                <div className="flex items-baseline gap-4 mb-3">
                   <span className="font-mono font-bold text-xs opacity-50 text-[#1A365D] tracking-widest">01</span>
                   <h4 className="text-2xl md:text-3xl font-black text-[#1A365D] font-serif tracking-tight">Curriculum Development</h4>
                </div>
                <p className="text-[#1A365D]/70 text-base md:text-lg leading-relaxed pl-8 md:pl-10">
                   Designing structured, engaging, and industry-aligned tech learning paths for students of all levels.
                </p>
             </motion.div>

             {/* Item 02 */}
             <motion.div variants={fadeUp} className="group border-t-2 border-[#1A365D] py-8 flex flex-col justify-center cursor-default hover:pr-4 transition-all duration-300">
                <div className="flex items-baseline gap-4 mb-3">
                   <span className="font-mono font-bold text-xs opacity-50 text-[#1A365D] tracking-widest">02</span>
                   <h4 className="text-2xl md:text-3xl font-black text-[#1A365D] font-serif tracking-tight">Modern Web</h4>
                </div>
                <p className="text-[#1A365D]/70 text-base md:text-lg leading-relaxed pl-8 md:pl-10">
                   Building fast, scalable full-stack applications with an emphasis on timeless architecture.
                </p>
             </motion.div>

             {/* Item 03 */}
             <motion.div variants={fadeUp} className="group border-t-2 border-b-2 border-[#1A365D] py-8 flex flex-col justify-center cursor-default hover:pr-4 transition-all duration-300 hover:bg-[#1A365D] px-4 -mx-4 rounded-sm">
                <div className="flex items-baseline gap-4 mb-3">
                   <span className="font-mono font-bold text-xs opacity-50 text-[#1A365D] group-hover:text-[#F5F2EB] tracking-widest transition-colors duration-300">03</span>
                   <h4 className="text-2xl md:text-3xl font-black text-[#1A365D] group-hover:text-[#F5F2EB] font-serif tracking-tight transition-colors duration-300">Mentoring</h4>
                </div>
                <p className="text-[#1A365D]/70 group-hover:text-[#F5F2EB]/80 text-base md:text-lg leading-relaxed pl-8 md:pl-10 transition-colors duration-300">
                   Guiding the next generation of software engineers by transferring durable mental models.
                </p>
             </motion.div>

          </div>

        </motion.div>'''

content = re.sub(old_right_side, new_right_side, content, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Replaced Bento box with Editorial Index List.')
