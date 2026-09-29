import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the typography block
old_typo_regex = r'\{\/\* 4\. Giant Typography \(Strictly BEHIND subject\) \*\/\}.*?<div className="absolute inset-0 flex flex-col items-center justify-center z-20 pointer-events-none mix-blend-difference">.*?</h1>\s*</div>'

new_typo = '''{/* 4. Giant Typography (Strictly BEHIND subject) */}
      <div className="absolute inset-0 z-20 pointer-events-none">
         {/* Left Side (Cream Text on Blue BG) */}
         <div className="absolute top-0 left-0 w-[45vw] h-full overflow-hidden">
             <div className="absolute top-0 left-0 w-[100vw] h-full flex flex-col items-center justify-center">
                 <h1 className="font-serif text-[18vw] md:text-[20vw] leading-[0.85] tracking-tighter font-black text-center whitespace-nowrap text-[#F5F2EB]">
                    <span className="block">GABRIEL</span>
                    <span className="block">RYAN</span>
                 </h1>
             </div>
         </div>
         {/* Right Side (Blue Text on Cream BG) */}
         <div className="absolute top-0 right-0 w-[55vw] h-full overflow-hidden">
             <div className="absolute top-0 right-0 w-[100vw] h-full flex flex-col items-center justify-center">
                 <h1 className="font-serif text-[18vw] md:text-[20vw] leading-[0.85] tracking-tighter font-black text-center whitespace-nowrap text-[#1A365D]">
                    <span className="block">GABRIEL</span>
                    <span className="block">RYAN</span>
                 </h1>
             </div>
         </div>
      </div>'''

content = re.sub(old_typo_regex, new_typo, content, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Restored massive typography and fixed colors using split technique.')
