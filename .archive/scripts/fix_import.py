import re
with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("import { useTransform } from 'framer-motion';\n\nconst ScrollIndicator", "const ScrollIndicator")

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("Duplicate import removed")
