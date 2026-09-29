import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix literal `r`n
content = content.replace('{/* Center Typography */}`r`n      <div className="relative w-full flex flex-col items-center justify-center">', '{/* Center Typography */}\n      <div className="relative w-full flex flex-col items-center justify-center mb-[20vh] md:mb-[25vh]">')

# Also remove the mt-[-15vh] if it's still there
content = content.replace('mt-[-15vh]', '')

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed positioning")
