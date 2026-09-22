import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Just literally replace all `<div className="pt-20">` and the corresponding `</div>` right before `</PageTransition>`.
content = content.replace('<div className="pt-20">\n', '')
content = content.replace('      </div>\n    </PageTransition>', '    </PageTransition>')

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
