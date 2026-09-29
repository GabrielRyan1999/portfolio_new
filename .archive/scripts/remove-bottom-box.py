import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the Bottom Right Navy Block
block_regex = r'\{\/\* Bottom Right Navy Block \*\/\}[\s\S]*?<\/div>\s*<\/div>\s*<\/div>'
content = re.sub(block_regex, '', content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Removed Bottom Right Navy Block.')
