import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the entire z-40 foreground layer for RYAN (the one with the ugly stroke)
foreground_regex = r'\{\/\* 5\. Typography Layer 2 \(FOREGROUND: In front of Subject, ONLY RYAN\) \*\/\}.*?</div>\s*</div>\s*</div>'
content = re.sub(foreground_regex, '', content, flags=re.DOTALL)

# 2. Shift the z-20 background layer UP so it clears his broad shoulders
# Change justify-center to justify-start and add padding top
old_z20_left = r'<div className="absolute top-0 left-0 w-\[100vw\] h-full flex flex-col items-center justify-center">'
new_z20_left = r'<div className="absolute top-0 left-0 w-[100vw] h-full flex flex-col items-center justify-start pt-[18vh] md:pt-[15vh]">'
content = content.replace(old_z20_left, new_z20_left)

old_z20_right = r'<div className="absolute top-0 right-0 w-\[100vw\] h-full flex flex-col items-center justify-center">'
new_z20_right = r'<div className="absolute top-0 right-0 w-[100vw] h-full flex flex-col items-center justify-start pt-[18vh] md:pt-[15vh]">'
content = content.replace(old_z20_right, new_z20_right)


with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Removed ugly foreground layer and shifted typography UP to clear the shoulders.')
