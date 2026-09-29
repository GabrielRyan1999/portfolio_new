import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the invalid style block with a valid link tag
old_style = r'\{\/\* Inject Google Font for Cursive \*\/\}[\s\S]*?`\}\} \/>'
new_style = '''{/* Inject Google Font for Cursive */}
        <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@700&display=swap" rel="stylesheet" />'''
content = re.sub(old_style, new_style, content)

# Update the className to include inline font-family
old_cursive_left = r'<h2 className="font-cursive text-\[12vw\] md:text-\[15vw\] leading-none text-\[#F5F2EB\] -rotate-6 drop-shadow-2xl ml-\[10vw\]">'
new_cursive_left = '''<h2 className="text-[12vw] md:text-[15vw] leading-none text-[#F5F2EB] -rotate-6 drop-shadow-2xl ml-[10vw]" style={{ fontFamily: "'Caveat', 'Brush Script MT', 'Bradley Hand', cursive" }}>'''
content = content.replace(old_cursive_left, new_cursive_left)

old_cursive_right = r'<h2 className="font-cursive text-\[12vw\] md:text-\[15vw\] leading-none text-\[#1A365D\] -rotate-6 drop-shadow-2xl ml-\[10vw\]">'
new_cursive_right = '''<h2 className="text-[12vw] md:text-[15vw] leading-none text-[#1A365D] -rotate-6 drop-shadow-2xl ml-[10vw]" style={{ fontFamily: "'Caveat', 'Brush Script MT', 'Bradley Hand', cursive" }}>'''
content = content.replace(old_cursive_right, new_cursive_right)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed cursive font loading.')
