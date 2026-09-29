import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the entire z-40 Ghost Outline Layer
ghost_regex = r'\{\/\* 5\. Ghost Outline Text \(FOREGROUND: In front of Subject\) \*\/\}.*?</div>\s*</div>\s*</div>'
content = re.sub(ghost_regex, '', content, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Removed Billie Eilish ghost text overlay.')
