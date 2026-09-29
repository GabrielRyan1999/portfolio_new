import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Change Endorsements to Testimonials
content = content.replace('Chapter 05 // Endorsements', 'Chapter 05 // Testimonials')

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated Endorsements to Testimonials.')
