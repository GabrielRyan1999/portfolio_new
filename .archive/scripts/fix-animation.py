import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the scattered animation triggers with a single parent wrapper

old_structure = r'''<div className="w-full max-w-6xl mx-auto flex flex-col lg:flex-row items-stretch gap-12 lg:gap-20 px-6 relative z-10">
          
          \{\/\* Left: Original 3 Paragraphs \*\/\}
          <div className="w-full lg:w-1/2 flex flex-col justify-center space-y-8">
            <div>
              <motion\.h3 variants=\{fadeUp\} initial="hidden" whileInView="visible" viewport=\{\{ once: true \}\} className="text-5xl md:text-7xl font-black font-serif text-\[#1A365D\] tracking-tighter mb-4">
                Gabriel<br\/>Ryan Prima
              <\/motion\.h3>
              <motion\.p variants=\{fadeUp\} initial="hidden" whileInView="visible" viewport=\{\{ once: true \}\} className="text-\[#1A365D\]\/70 font-bold uppercase tracking-widest text-xs md:text-sm">
                Educator, Developer, & System Builder\.
              <\/motion\.p>
            <\/div>
            
            <motion\.div variants=\{staggerContainer\} initial="hidden" whileInView="visible" viewport=\{\{ once: true \}\} className="space-y-6 text-\[#1A365D\] text-base leading-relaxed">
              <motion\.p variants=\{fadeUp\}>
                I work at the intersection of technology and education based in Yogyakarta, Indonesia\. My background is in computer engineering, but somewhere along the way teaching became the thing I actually care about, and combining the two has become my life's focus ever since\.
              <\/motion\.p>
              
              <motion\.div variants=\{fadeUp\}>
                <h4 className="font-bold mb-1 tracking-widest font-sans uppercase text-xs opacity-70">Background<\/h4>
                <p className="font-serif">
                  I graduated in Computer Engineering, and that technical foundation is why I approach education the way I do: not as content delivery, but as a system you design with intention, one that has to hold up in practice, not just in theory\.
                <\/p>
              <\/motion\.div>
              
              <motion\.div variants=\{fadeUp\}>
                <h4 className="font-bold mb-1 tracking-widest font-sans uppercase text-xs opacity-70">Outside of Work<\/h4>
                <p className="font-serif">
                  When I'm not building or teaching, I'm usually gaming, gardening, or digging into personal finance and investing\.
                <\/p>
              <\/motion\.div>
            <\/motion\.div>
          <\/div>

          \{\/\* Right: Core Pillars Bento Box \(Adapted to Editorial Colors\) \*\/\}
          <motion\.div variants=\{staggerContainer\} initial="hidden" whileInView="visible" viewport=\{\{ once: true \}\} className="w-full lg:w-1/2 grid grid-cols-2 gap-4 mt-8 lg:mt-0">'''

new_structure = '''<motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: false, amount: 0.2 }} className="w-full max-w-6xl mx-auto flex flex-col lg:flex-row items-stretch gap-12 lg:gap-20 px-6 relative z-10">
          
          {/* Left: Original 3 Paragraphs */}
          <div className="w-full lg:w-1/2 flex flex-col justify-center space-y-8">
            <div>
              <motion.h3 variants={fadeUp} className="text-5xl md:text-7xl font-black font-serif text-[#1A365D] tracking-tighter mb-4">
                Gabriel<br/>Ryan Prima
              </motion.h3>
              <motion.p variants={fadeUp} className="text-[#1A365D]/70 font-bold uppercase tracking-widest text-xs md:text-sm">
                Educator, Developer, & System Builder.
              </motion.p>
            </div>
            
            <motion.div variants={fadeUp} className="space-y-6 text-[#1A365D] text-base leading-relaxed">
              <p>
                I work at the intersection of technology and education based in Yogyakarta, Indonesia. My background is in computer engineering, but somewhere along the way teaching became the thing I actually care about, and combining the two has become my life's focus ever since.
              </p>
              
              <div>
                <h4 className="font-bold mb-1 tracking-widest font-sans uppercase text-xs opacity-70">Background</h4>
                <p className="font-serif">
                  I graduated in Computer Engineering, and that technical foundation is why I approach education the way I do: not as content delivery, but as a system you design with intention, one that has to hold up in practice, not just in theory.
                </p>
              </div>
              
              <div>
                <h4 className="font-bold mb-1 tracking-widest font-sans uppercase text-xs opacity-70">Outside of Work</h4>
                <p className="font-serif">
                  When I'm not building or teaching, I'm usually gaming, gardening, or digging into personal finance and investing.
                </p>
              </div>
            </motion.div>
          </div>

          {/* Right: Core Pillars Bento Box (Adapted to Editorial Colors) */}
          <div className="w-full lg:w-1/2 grid grid-cols-2 gap-4 mt-8 lg:mt-0">'''

content = re.sub(old_structure, new_structure, content, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed animation bug making text invisible.')
