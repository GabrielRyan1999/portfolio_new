import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = r'             <div className="w-full md:w-1/2 flex flex-col bg-cream">'
end_marker = r'Guiding the next generation of software engineers\.\n                      </p>\n                   </div>\n                </div>\n  \n             </div>'

pattern = start_marker + r'.*?' + end_marker

new_block = """             <div className="w-full md:w-1/2 flex flex-col bg-cream">
                
                {/* Row 1: Curriculum Development */}
                <div className="w-full flex-1 min-h-[250px] border-b border-navy p-8 md:p-12 lg:p-16 flex flex-col justify-center relative group hover:bg-navy hover:text-cream transition-colors duration-500 cursor-default">
                    <span className="absolute top-6 left-6 md:top-8 md:left-8 text-xs font-mono font-bold tracking-widest uppercase opacity-50 group-hover:opacity-100 transition-opacity">01</span>
                    <h3 className="font-sans font-black text-4xl md:text-5xl lg:text-6xl tracking-tighter uppercase mb-4 leading-[0.9]">Curriculum<br className="hidden md:block"/>Development</h3>
                    <p className="font-serif text-lg md:text-xl leading-relaxed opacity-90 max-w-lg">
                       Designing structured, engaging, and industry-aligned tech learning paths for students of all levels.
                    </p>
                </div>
  
                {/* Row 2: Modern Web */}
                <div className="w-full flex-1 min-h-[250px] border-b border-navy p-8 md:p-12 lg:p-16 flex flex-col justify-center relative group hover:bg-navy hover:text-cream transition-colors duration-500 cursor-default">
                    <span className="absolute top-6 left-6 md:top-8 md:left-8 text-xs font-mono font-bold tracking-widest uppercase opacity-50 group-hover:opacity-100 transition-opacity">02</span>
                    <h3 className="font-sans font-black text-4xl md:text-5xl lg:text-6xl tracking-tighter uppercase mb-4 leading-[0.9]">Modern Web</h3>
                    <p className="font-serif text-lg md:text-xl leading-relaxed opacity-90 max-w-lg">
                       Building fast, scalable full-stack applications.
                    </p>
                </div>
  
                {/* Row 3: Mentoring */}
                <div className="w-full flex-1 min-h-[250px] p-8 md:p-12 lg:p-16 flex flex-col justify-center relative group hover:bg-navy hover:text-cream transition-colors duration-500 cursor-default">
                    <span className="absolute top-6 left-6 md:top-8 md:left-8 text-xs font-mono font-bold tracking-widest uppercase opacity-50 group-hover:opacity-100 transition-opacity">03</span>
                    <h3 className="font-sans font-black text-4xl md:text-5xl lg:text-6xl tracking-tighter uppercase mb-4 leading-[0.9]">Mentoring</h3>
                    <p className="font-serif text-lg md:text-xl leading-relaxed opacity-90 max-w-lg">
                       Guiding the next generation of software engineers.
                    </p>
                </div>
  
             </div>"""

content = re.sub(pattern, new_block, content, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Finally applied 3-row layout!")
