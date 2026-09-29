import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

old_h1_left = r'<h1 className="font-serif text-\[13vw\] md:text-\[15vw\] leading-\[0\.85\] tracking-tighter font-black text-center whitespace-nowrap text-\[#F5F2EB\]">\s*<span className="block">GABRIEL</span>\s*<span className="block">RYAN</span>\s*</h1>'
new_h1_left = r'''<h1 className="font-sans font-black text-center whitespace-nowrap text-[#F5F2EB] tracking-tighter" style={{ transform: 'scaleY(2.2)', lineHeight: '0.8' }}>
                    <span className="block text-[15vw]">GABRIEL</span>
                    <span className="block text-[24vw] -mt-[3vw]">RYAN</span>
                 </h1>'''
content = re.sub(old_h1_left, new_h1_left, content)

old_h1_right = r'<h1 className="font-serif text-\[13vw\] md:text-\[15vw\] leading-\[0\.85\] tracking-tighter font-black text-center whitespace-nowrap text-\[#1A365D\]">\s*<span className="block">GABRIEL</span>\s*<span className="block">RYAN</span>\s*</h1>'
new_h1_right = r'''<h1 className="font-sans font-black text-center whitespace-nowrap text-[#1A365D] tracking-tighter" style={{ transform: 'scaleY(2.2)', lineHeight: '0.8' }}>
                    <span className="block text-[15vw]">GABRIEL</span>
                    <span className="block text-[24vw] -mt-[3vw]">RYAN</span>
                 </h1>'''
content = re.sub(old_h1_right, new_h1_right, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Applied ultra-tall condensed sans-serif typography.')
