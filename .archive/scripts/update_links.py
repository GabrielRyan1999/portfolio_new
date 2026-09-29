import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("import { SectionShell }", "import { Link } from 'react-router-dom';\nimport { SectionShell }")
content = content.replace('<a href="#contact"', '<Link to="/contact"')
content = content.replace('<a href="#work"', '<Link to="/work"')
content = content.replace('</a>', '</Link>')

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Links updated in Pages.jsx')
