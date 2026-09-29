import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Add the z-40 Ghost Outline Layer
ghost_layer = '''      {/* 5. Ghost Outline Text (FOREGROUND: In front of Subject) */}
      {/* This creates the Billie Eilish magazine effect where the text outlines wrap over the subject */}
      <div className="absolute inset-0 z-40 pointer-events-none">
         {/* Left Side (Cream Outline) */}
         <div className="absolute top-0 left-0 w-[45vw] h-full overflow-hidden">
             <div className="absolute top-0 left-0 w-[100vw] h-full flex flex-col items-center justify-center">
                 <h1 className="font-serif text-[13vw] md:text-[15vw] leading-[0.85] tracking-tighter font-black text-center whitespace-nowrap text-transparent" style={{ WebkitTextStroke: '1px rgba(245, 242, 235, 0.7)' }}>
                    <span className="block">GABRIEL</span>
                    <span className="block">RYAN</span>
                 </h1>
             </div>
         </div>
         {/* Right Side (Yale Blue Outline) */}
         <div className="absolute top-0 right-0 w-[55vw] h-full overflow-hidden">
             <div className="absolute top-0 right-0 w-[100vw] h-full flex flex-col items-center justify-center">
                 <h1 className="font-serif text-[13vw] md:text-[15vw] leading-[0.85] tracking-tighter font-black text-center whitespace-nowrap text-transparent" style={{ WebkitTextStroke: '1px rgba(26, 54, 93, 0.7)' }}>
                    <span className="block">GABRIEL</span>
                    <span className="block">RYAN</span>
                 </h1>
             </div>
         </div>
      </div>'''

# Insert it right after the portrait (z-30)
content = re.sub(
    r'(\{\/\* 5\. The Subject \(Portrait - Strictly IN FRONT of text\) \*\/\}[\s\S]*?</div>)',
    r'\1\n\n' + ghost_layer,
    content
)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Added Billie Eilish ghost text overlay.')
