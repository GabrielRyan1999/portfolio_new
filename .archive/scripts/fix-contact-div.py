import re

with open('src/components/ui/lets-work-section.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Add closing div for the wrapper right before {/* Footer */}
content = re.sub(r'(\{\/\*\s*Footer\s*\*\/\})', r'</div>\n        \1', content)

with open('src/components/ui/lets-work-section.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed unclosed div in Contact section.')
