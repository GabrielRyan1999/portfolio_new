import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

old_block = r"""             <div className="w-full md:w-1/2 flex flex-col bg-cream">
                
                \{/\* Top Card: Curriculum Development \*/\}
                <div className="w-full flex-1 min-h-\[300px\] border-b border-navy p-8 md:p-12 lg:p-16 flex flex-col justify-center relative group hover:bg-navy hover:text-cream transition-colors duration-500 cursor-default">
                    <span className="absolute top-6 left-6 md:top-8 md:left-8 text-xs font-mono font-bold tracking-widest uppercase opacity-50 group-hover:opacity-100 transition-opacity">01</span>
                    <h3 className="font-sans font-black text-4xl md:text-5xl lg:text-6xl tracking-tighter uppercase mb-6 leading-\[0\.9\]">Curriculum<br/>Development</h3>
                    <p className="font-serif text-lg md:text-xl leading-relaxed opacity-90 max-w-lg">
                       Designing structured, engaging, and industry-aligned tech learning paths for students of all levels\.
                    </p>
                </div>
  
                \{/\* Bottom Cards Wrapper \*/\}
                <div className="w-full flex-1 flex flex-col md:flex-row min-h-\[300px\]">
                   
                   \{/\* Bottom Left Card: Modern Web \*/\}
                   <div className="w-full md:w-1/2 border-b md:border-b-0 border-navy md:border-r p-8 md:p-10 flex flex-col justify-center relative group hover:bg-navy hover:text-cream transition-colors duration-500 cursor-default">
                      <span className="absolute top-6 left-6 md:top-8 md:left-8 text-xs font-mono font-bold tracking-widest uppercase opacity-50 group-hover:opacity-100 transition-opacity">02</span>
                      <h3 className="font-sans font-black text-3xl md:text-4xl tracking-tighter uppercase mb-4 leading-\[0\.9\]">Modern<br/>Web</h3>
                      <p className="font-serif text-base md:text-lg leading-relaxed opacity-90">
                         Building fast, scalable full-stack applications\.
                      </p>
                   </div>
  
                   \{/\* Bottom Right Card: Mentoring \*/\}
                   <div className="w-full md:w-1/2 p-8 md:p-10 flex flex-col justify-center relative bg-blue-600 text-white hover:bg-navy transition-colors duration-500 cursor-default">
                      <span className="absolute top-6 left-6 md:top-8 md:left-8 text-xs font-mono font-bold tracking-widest uppercase opacity-70 group-hover:opacity-100 transition-opacity">03</span>
                      <h3 className="font-sans font-black text-3xl md:text-4xl tracking-tighter uppercase mb-4 leading-\[0\.9\]">Mentoring</h3>
                      <p className="font-serif text-base md:text-lg leading-relaxed opacity-90">
                         Guiding the next generation of software engineers\.
                      </p>
                   </div>
                </div>
  
             </div>"""

new_block = """             <div className="w-full md:w-1/2 flex flex-col bg-cream">
                
                {/* Row 1: Curriculum Development */}
                <div className="w-full flex-1 min-h-[200px] border-b border-navy p-8 md:p-12 lg:p-16 flex flex-col justify-center relative group hover:bg-navy hover:text-cream transition-colors duration-500 cursor-default">
                    <span className="absolute top-6 left-6 md:top-8 md:left-8 text-xs font-mono font-bold tracking-widest uppercase opacity-50 group-hover:opacity-100 transition-opacity">01</span>
                    <h3 className="font-sans font-black text-4xl md:text-5xl lg:text-6xl tracking-tighter uppercase mb-4 leading-[0.9]">Curriculum<br className="hidden md:block"/>Development</h3>
                    <p className="font-serif text-lg md:text-xl leading-relaxed opacity-90 max-w-lg">
                       Designing structured, engaging, and industry-aligned tech learning paths for students of all levels.
                    </p>
                </div>
  
                {/* Row 2: Modern Web */}
                <div className="w-full flex-1 min-h-[200px] border-b border-navy p-8 md:p-12 lg:p-16 flex flex-col justify-center relative group hover:bg-navy hover:text-cream transition-colors duration-500 cursor-default">
                    <span className="absolute top-6 left-6 md:top-8 md:left-8 text-xs font-mono font-bold tracking-widest uppercase opacity-50 group-hover:opacity-100 transition-opacity">02</span>
                    <h3 className="font-sans font-black text-4xl md:text-5xl lg:text-6xl tracking-tighter uppercase mb-4 leading-[0.9]">Modern Web</h3>
                    <p className="font-serif text-lg md:text-xl leading-relaxed opacity-90 max-w-lg">
                       Building fast, scalable full-stack applications.
                    </p>
                </div>
  
                {/* Row 3: Mentoring */}
                <div className="w-full flex-1 min-h-[200px] p-8 md:p-12 lg:p-16 flex flex-col justify-center relative group hover:bg-navy hover:text-cream transition-colors duration-500 cursor-default">
                    <span className="absolute top-6 left-6 md:top-8 md:left-8 text-xs font-mono font-bold tracking-widest uppercase opacity-50 group-hover:opacity-100 transition-opacity">03</span>
                    <h3 className="font-sans font-black text-4xl md:text-5xl lg:text-6xl tracking-tighter uppercase mb-4 leading-[0.9]">Mentoring</h3>
                    <p className="font-serif text-lg md:text-xl leading-relaxed opacity-90 max-w-lg">
                       Guiding the next generation of software engineers.
                    </p>
                </div>
  
             </div>"""

content = re.sub(old_block, new_block, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated About section to 3 equal rows.")
