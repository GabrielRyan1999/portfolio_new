import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

target = 'className="w-full flex flex-col justify-center z-10 divide-y divide-gray-200 overflow-y-auto h-full max-h-full custom-scrollbar pr-4"'
replacement = 'className="w-full flex flex-col justify-center z-10 divide-y divide-gray-200"'

content = content.replace(target, replacement)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed internal scrollbar")
