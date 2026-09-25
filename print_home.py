import re
with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'(<SectionShell id="home".*?<motion\.h1)', content, re.DOTALL)
if m:
    print(m.group(1))
