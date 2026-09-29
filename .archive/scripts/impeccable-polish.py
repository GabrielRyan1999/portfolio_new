import os
import re

CSS_FILE = 'src/index.css'

# 1. Update index.css to add colors
with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css_content = f.read()

if '--color-cream' not in css_content:
    theme_block = """@theme {
  --color-cream: #F5F2EB;
  --color-navy: #1A365D;"""
    css_content = css_content.replace('@theme {', theme_block)
    with open(CSS_FILE, 'w', encoding='utf-8') as f:
        f.write(css_content)


# 2. Replace hardcoded colors in JSX
JSX_FILES = [
    'src/App.jsx',
    'src/pages/Pages.jsx',
    'src/components/ui/lets-work-section.jsx',
    'src/components/ui/unique-testimonial.jsx'
]

def replace_colors(content):
    # Cream replacements
    content = content.replace('[#F5F2EB]', 'cream')
    # Navy replacements
    content = content.replace('[#1A365D]', 'navy')
    return content

for file_path in JSX_FILES:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = replace_colors(content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Polish applied. Extracted colors into Tailwind tokens.")
