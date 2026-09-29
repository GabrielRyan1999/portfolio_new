import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to match the 01 decoration div
# Note: I used `div className="absolute top-[15%] right-[-5vw] z-0 pointer-events-none opacity-10 select-none"`
pattern_01 = r'\{\/\* Abstract Editorial Decor: Giant Hollow Number \*\/.*?<\/h2>\s*<\/div>'

content = re.sub(pattern_01, '', content, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Removed 01 decoration.')
