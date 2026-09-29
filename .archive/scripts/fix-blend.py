import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Move mix-blend-difference from the h1 to the parent absolute divs for the Typography layers

# Typography Layer 1
old_layer1 = r'<div className="absolute inset-0 flex flex-col items-center justify-center z-20 pointer-events-none">\s*<h1 className="font-serif([^"]*)text-white mix-blend-difference">'
new_layer1 = r'<div className="absolute inset-0 flex flex-col items-center justify-center z-20 pointer-events-none mix-blend-difference">\n          <h1 className="font-serif\1text-white">'
content = re.sub(old_layer1, new_layer1, content)

# Typography Layer 2
old_layer2 = r'<div className="absolute inset-0 flex flex-col items-center justify-center z-40 pointer-events-none">\s*<h1 className="font-serif([^"]*)text-white mix-blend-difference">'
new_layer2 = r'<div className="absolute inset-0 flex flex-col items-center justify-center z-40 pointer-events-none mix-blend-difference">\n          <h1 className="font-serif\1text-white">'
content = re.sub(old_layer2, new_layer2, content)

# Write back
with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed stacking context for mix-blend-difference on typography.')
