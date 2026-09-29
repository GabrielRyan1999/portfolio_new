import re

with open('src/components/ui/lets-work-section.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Change Chapter 05 to Chapter 06
content = content.replace('Chapter 05 // Initiate Contact', 'Chapter 06 // Initiate Contact')

with open('src/components/ui/lets-work-section.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated Contact to Chapter 06.')
