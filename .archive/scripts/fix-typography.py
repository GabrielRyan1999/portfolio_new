import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the entire Giant Typography block
old_typography = r'\{\/\* 4\. Giant Typography \(Strictly IN FRONT of subject\) \*\/\}\s*<div className="absolute inset-0 z-40 pointer-events-none">[\s\S]*?<\/div>\s*<\/div>\s*<\/div>'
new_typography = '''{/* 4. Giant Typography (Strictly IN FRONT of subject, using Mix Blend Difference) */}
        <div className="absolute inset-0 z-40 w-full h-full flex flex-col items-center justify-center pointer-events-none mix-blend-difference">
             <h1 className="font-serif text-[13vw] md:text-[15vw] leading-[0.85] tracking-tighter font-black text-center whitespace-nowrap text-white">
                <span className="block">GABRIEL</span>
                <span className="block">RYAN</span>
             </h1>
        </div>'''

content = re.sub(old_typography, new_typography, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Replaced split typography with a single mix-blend-difference layer.')
