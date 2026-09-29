import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'(\}\)\}\s*<\/div>\s*)(<\/section>\s*<\/PageTransition>\s*\);\s*\}\s*export function Experience\(\) \{)', r'\1  </div>\n          \2', content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed unclosed div using flexible regex.')
