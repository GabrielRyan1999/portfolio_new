import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Add the z-40 foreground layer for RYAN so it sits over the suit

foreground_layer = '''      {/* 5. Typography Layer 2 (FOREGROUND: In front of Subject, ONLY RYAN) */}
      <div className="absolute inset-0 z-40 pointer-events-none">
         {/* Left Side (Cream Text) */}
         <div className="absolute top-0 left-0 w-[45vw] h-full overflow-hidden">
             <div className="absolute top-0 left-0 w-[100vw] h-full flex flex-col items-center justify-center">
                 <h1 className="font-serif text-[18vw] md:text-[20vw] leading-[0.85] tracking-tighter font-black text-center whitespace-nowrap text-[#F5F2EB]">
                    <span className="block opacity-0">GABRIEL</span>
                    <span className="block">RYAN</span>
                 </h1>
             </div>
         </div>
         {/* Right Side (Blue Text with Cream Stroke for contrast on dark suit) */}
         <div className="absolute top-0 right-0 w-[55vw] h-full overflow-hidden">
             <div className="absolute top-0 right-0 w-[100vw] h-full flex flex-col items-center justify-center">
                 <h1 className="font-serif text-[18vw] md:text-[20vw] leading-[0.85] tracking-tighter font-black text-center whitespace-nowrap text-[#1A365D]">
                    <span className="block opacity-0">GABRIEL</span>
                    <span className="block" style={{ WebkitTextStroke: '2px #F5F2EB' }}>RYAN</span>
                 </h1>
             </div>
         </div>
      </div>'''

content = re.sub(
    r'(\{\/\* 5\. The Subject \(Portrait - Strictly IN FRONT of text\) \*\/\}[\s\S]*?</div>)',
    r'\1\n\n' + foreground_layer,
    content
)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Added z-40 foreground layer for RYAN.')
