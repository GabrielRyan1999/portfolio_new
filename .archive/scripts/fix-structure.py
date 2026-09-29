import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add <PageTransition> to the start of Home()
home_start_old = r'export function Home\(\) \{\s*return \(\s*<section id="home"'
home_start_new = '''export function Home() {
    return (
      <PageTransition>
      <section id="home"'''
content = re.sub(home_start_old, home_start_new, content)

# 2. Extract and remove all About() blocks
about_regex = r'export function About\(\) \{[\s\S]*?(?=export function )'
# Find the first one to keep it
abouts = re.findall(about_regex, content)
about_code = abouts[0] if abouts else ""

# Remove all About() blocks
content = re.sub(about_regex, '', content)

# 3. Insert ONE About() block before Service()
content = content.replace('export function Service()', about_code + 'export function Service()')

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed all JSX structure issues!')
