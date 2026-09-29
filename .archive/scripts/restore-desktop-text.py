import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix desktop text sizes back to the perfect 17vw
content = content.replace('text-[32vw] md:text-[23.5vw]', 'text-[26vw] md:text-[17vw]')
content = content.replace('text-[35vw] md:text-[22vw]', 'text-[35vw] md:text-[17vw]')
content = content.replace('md:top-[65%]', 'md:top-[40%]') # Also fix the Ryan text top position back to 40%

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Desktop text sizes and positions restored.")
