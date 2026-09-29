import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the shortened story with the original 3 paragraphs, adapted to the new typography
old_left_story = r'<motion\.div variants=\{staggerContainer\} initial="hidden" whileInView="visible" viewport=\{\{ once: true \}\} className="space-y-6 text-\[#1A365D\] text-base md:text-lg leading-relaxed font-serif">.*?<\/motion\.div>'

new_left_story = '''<motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: true }} className="space-y-6 text-[#1A365D] text-base leading-relaxed">
              <motion.p variants={fadeUp}>
                I work at the intersection of technology and education based in Yogyakarta, Indonesia. My background is in computer engineering, but somewhere along the way teaching became the thing I actually care about, and combining the two has become my life's focus ever since.
              </motion.p>
              
              <motion.div variants={fadeUp}>
                <h4 className="font-bold mb-1 tracking-widest font-sans uppercase text-xs opacity-70">Background</h4>
                <p className="font-serif">
                  I graduated in Computer Engineering, and that technical foundation is why I approach education the way I do: not as content delivery, but as a system you design with intention, one that has to hold up in practice, not just in theory.
                </p>
              </motion.div>
              
              <motion.div variants={fadeUp}>
                <h4 className="font-bold mb-1 tracking-widest font-sans uppercase text-xs opacity-70">Outside of Work</h4>
                <p className="font-serif">
                  When I'm not building or teaching, I'm usually gaming, gardening, or digging into personal finance and investing.
                </p>
              </motion.div>
            </motion.div>'''

content = re.sub(old_left_story, new_left_story, content, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Restored the original 3 paragraphs.')
