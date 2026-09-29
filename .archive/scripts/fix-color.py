import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the hardcoded color in AnimatedWords component so it inherits the parent's color
old_class = r'className="absolute top-0 left-0 text-\[#D1C4B5\]"'
new_class = 'className="absolute top-0 left-0 text-current"'
content = re.sub(old_class, new_class, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed AnimatedWords text color.')
