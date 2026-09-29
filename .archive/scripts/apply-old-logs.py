import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Typography modifications
# Restore vertical centering (remove justify-start and pt-[...])
content = re.sub(r'justify-start pt-\[18vh\] md:pt-\[15vh\]', 'justify-center', content)

# Modify the <h1> tags to compress line-height and stretch RYAN
old_h1_left = r'<h1 className="font-serif text-\[18vw\] md:text-\[20vw\] leading-\[0\.85\] tracking-tighter font-black text-center whitespace-nowrap text-\[#F5F2EB\]">\s*<span className="block">GABRIEL</span>\s*<span className="block">RYAN</span>\s*</h1>'
new_h1_left = r'''<h1 className="font-serif text-[18vw] md:text-[20vw] leading-[0.65] font-black text-center whitespace-nowrap text-[#F5F2EB] flex flex-col items-center">
                    <span className="block tracking-tighter">GABRIEL</span>
                    <span className="block tracking-[0.4em] ml-[0.2em] md:ml-[0.4em]">RYAN</span>
                 </h1>'''
content = content.replace(old_h1_left, new_h1_left)

old_h1_right = r'<h1 className="font-serif text-\[18vw\] md:text-\[20vw\] leading-\[0\.85\] tracking-tighter font-black text-center whitespace-nowrap text-\[#1A365D\]">\s*<span className="block">GABRIEL</span>\s*<span className="block">RYAN</span>\s*</h1>'
new_h1_right = r'''<h1 className="font-serif text-[18vw] md:text-[20vw] leading-[0.65] font-black text-center whitespace-nowrap text-[#1A365D] flex flex-col items-center">
                    <span className="block tracking-tighter">GABRIEL</span>
                    <span className="block tracking-[0.4em] ml-[0.2em] md:ml-[0.4em]">RYAN</span>
                 </h1>'''
content = content.replace(old_h1_right, new_h1_right)

# 2. Modify Portrait to 100vh
old_portrait = r'<div className="absolute bottom-0 w-full h-\[80vh\] md:h-\[90vh\] flex justify-center z-30 pointer-events-none">'
new_portrait = r'<div className="absolute bottom-0 w-full h-[100vh] flex justify-center z-30 pointer-events-none">'
content = content.replace(old_portrait, new_portrait)


with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Applied exact formatting requested from previous logs.')
