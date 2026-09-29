import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the portrait image class
old_class = 'className="h-[65vh] md:h-[75vh] xl:h-[80vh] w-auto object-contain object-bottom grayscale drop-shadow-2xl brightness-105 contrast-125"'
new_class = 'className="h-[75vh] md:h-[85vh] w-auto max-w-none object-contain object-bottom grayscale drop-shadow-2xl brightness-105 contrast-125 md:scale-110 origin-bottom"'

content = content.replace(old_class, new_class)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added max-w-none and increased height.")
