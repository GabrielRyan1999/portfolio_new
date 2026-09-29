import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the typography size, leading, and mix-blend-difference stacking context
# We need to make it exactly like the first screenshot: smaller text, wider leading, properly inverted.

old_layer1 = r'<div className="absolute inset-0 flex flex-col items-center justify-center z-20 pointer-events-none">\s*<h1 className="font-serif text-\[18vw\] md:text-\[20vw\] leading-\[0\.8\] tracking-tighter font-black text-center text-white whitespace-nowrap mix-blend-difference">'
new_layer1 = r'''<div className="absolute inset-0 flex flex-col items-center justify-center z-20 pointer-events-none mix-blend-difference">
         <h1 className="font-serif text-[16vw] md:text-[15vw] leading-[0.95] tracking-tighter font-black text-center text-white whitespace-nowrap">'''
content = re.sub(old_layer1, new_layer1, content)

old_layer2 = r'<div className="absolute inset-0 flex flex-col items-center justify-center z-40 pointer-events-none">\s*<h1 className="font-serif text-\[18vw\] md:text-\[20vw\] leading-\[0\.8\] tracking-tighter font-black text-center text-white whitespace-nowrap mix-blend-difference">'
new_layer2 = r'''<div className="absolute inset-0 flex flex-col items-center justify-center z-40 pointer-events-none mix-blend-difference">
         <h1 className="font-serif text-[16vw] md:text-[15vw] leading-[0.95] tracking-tighter font-black text-center text-white whitespace-nowrap">'''
content = re.sub(old_layer2, new_layer2, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed typography scaling, line-height, and blend modes.')
