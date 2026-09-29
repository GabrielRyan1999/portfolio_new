import re

with open('src/index.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Inter with Helvetica Neue
content = content.replace('--font-sans: "Inter", system-ui, sans-serif;', '--font-sans: "Helvetica Neue", Helvetica, Arial, sans-serif;')
content = content.replace('font-family: "Inter", system-ui, -apple-system, sans-serif;', 'font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;')

# Remove .bg-grid completely
bg_grid_pattern = r'\.bg-grid\s*\{[^}]+\}'
content = re.sub(bg_grid_pattern, '', content)

with open('src/index.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("Typeset applied. Removed Inter and bg-grid from index.css.")
