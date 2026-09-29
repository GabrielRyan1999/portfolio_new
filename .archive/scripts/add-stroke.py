import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Left side text (add Navy outline)
old_left = r'<h1 className="font-serif text-\[13vw\] md:text-\[15vw\] leading-\[0\.85\] tracking-tighter font-black text-center whitespace-nowrap text-\[#F5F2EB\]">'
new_left = '''<h1 className="font-serif text-[13vw] md:text-[15vw] leading-[0.85] tracking-tighter font-black text-center whitespace-nowrap text-[#F5F2EB]" style={{ WebkitTextStroke: "2px #1A365D" }}>'''
content = re.sub(old_left, new_left, content)

# Right side text (add Cream outline)
old_right = r'<h1 className="font-serif text-\[13vw\] md:text-\[15vw\] leading-\[0\.85\] tracking-tighter font-black text-center whitespace-nowrap text-\[#1A365D\]">'
new_right = '''<h1 className="font-serif text-[13vw] md:text-[15vw] leading-[0.85] tracking-tighter font-black text-center whitespace-nowrap text-[#1A365D]" style={{ WebkitTextStroke: "2px #F5F2EB" }}>'''
content = re.sub(old_right, new_right, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Added WebkitTextStroke to Giant Typography.')
