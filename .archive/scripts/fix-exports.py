import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Home export
content = re.sub(r'^function Home\(\) \{', 'export function Home() {', content, flags=re.MULTILINE)

# Fix About export
content = re.sub(r'^function About\(\) \{', 'export function About() {', content, flags=re.MULTILINE)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed exports.')
