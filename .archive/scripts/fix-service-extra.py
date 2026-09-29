import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

bad = r'          <\/div>\n\n          <\/div>\n          <\/section>'
good = r'          </div>\n        </section>'

content = re.sub(bad, good, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed extra div from Service")
