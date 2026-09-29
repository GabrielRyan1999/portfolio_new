import re

with open('pages_broken.jsx', 'r', encoding='utf-16') as f:
    content = f.read()

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
