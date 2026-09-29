import re

# 1. Update index.css to enforce the font
with open('src/index.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace existing @font-face with a stronger one and a utility class
old_font_face = r'@font-face \{[\s\S]*?\}'
new_font_face = '''@font-face {
  font-family: 'Mayonice';
  src: url('/fonts/Mayonice.otf') format('opentype'),
       url('/fonts/Mayonice.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
  font-display: swap;
}

.font-mayonice {
  font-family: 'Mayonice', 'Brush Script MT', 'Bradley Hand', cursive !important;
}'''

if '@font-face' in css_content:
    css_content = re.sub(old_font_face, new_font_face, css_content)
else:
    css_content = css_content.replace('@import "tailwindcss";', f'@import "tailwindcss";\n{new_font_face}')

with open('src/index.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

# 2. Update Pages.jsx to use the class and fix the overlap position
with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    pages_content = f.read()

# Left Side Ryan
old_ryan_left = r'<h2 className="text-\[12vw\] md:text-\[15vw\] leading-none text-\[#F5F2EB\] -rotate-6 drop-shadow-2xl ml-\[10vw\]" style={{ fontFamily: "\'Mayonice\', cursive" }}>'
new_ryan_left = '''<h2 className="font-mayonice text-[15vw] md:text-[18vw] leading-none text-[#F5F2EB] -rotate-12 drop-shadow-2xl ml-[10vw]">'''
pages_content = pages_content.replace(old_ryan_left, new_ryan_left)

# Right Side Ryan
old_ryan_right = r'<h2 className="text-\[12vw\] md:text-\[15vw\] leading-none text-\[#1A365D\] -rotate-6 drop-shadow-2xl ml-\[10vw\]" style={{ fontFamily: "\'Mayonice\', cursive" }}>'
new_ryan_right = '''<h2 className="font-mayonice text-[15vw] md:text-[18vw] leading-none text-[#1A365D] -rotate-12 drop-shadow-2xl ml-[10vw]">'''
pages_content = pages_content.replace(old_ryan_right, new_ryan_right)

# Move Ryan UP to overlap GABRIEL
# Current: className="absolute top-[55%] md:top-[45%] left-1/2 -translate-x-1/2 w-full text-center"
# Target: top-[15%] md:top-[15%]
pages_content = pages_content.replace('top-[55%] md:top-[45%]', 'top-[15%] md:top-[15%]')

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(pages_content)
print('Forced Mayonice font and fixed overlap.')
