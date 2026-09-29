import re

# 1. Update index.css
with open('src/index.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

if '@font-face' not in css_content:
    font_face = """
@font-face {
  font-family: 'Mayonice';
  src: url('/fonts/Mayonice.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}
"""
    css_content = css_content.replace('@import "tailwindcss";', f'@import "tailwindcss";\n{font_face}')
    with open('src/index.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    print('Added @font-face to index.css')

# 2. Update Pages.jsx
with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    pages_content = f.read()

# Remove Google Font Link
pages_content = re.sub(r'\{\/\* Inject Google Font for Cursive \*\/\}[\s\S]*?<link href="https:\/\/fonts\.googleapis\.com.*? \/>', '', pages_content)

# Update font-family inline styles
old_style = r'style={{ fontFamily: "\'Caveat\', \'Brush Script MT\', \'Bradley Hand\', cursive" }}'
new_style = '''style={{ fontFamily: "'Mayonice', cursive" }}'''
pages_content = pages_content.replace(old_style, new_style)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(pages_content)
print('Updated Pages.jsx with Mayonice font.')
