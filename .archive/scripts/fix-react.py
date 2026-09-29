import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the missing words prop in the new Home section
old_tag = r'<AnimatedWords />'
new_tag = '<AnimatedWords words={["DEVELOPER.", "SYSTEM BUILDER.", "MENTOR."]} />'
content = re.sub(old_tag, new_tag, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed AnimatedWords missing prop.')
