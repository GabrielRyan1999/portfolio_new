import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Reduce giant typography from 20vw to 15vw
content = re.sub(
    r'text-\[18vw\] md:text-\[20vw\]',
    'text-[13vw] md:text-[15vw]',
    content
)

# 2. Shift the INNOVATE badge out of the way
# Currently: bottom-[35%] md:bottom-[40%] right-[25vw] md:right-[20vw]
# We'll move it down and right to anchor near the right block: bottom-[25%] right-[10vw]
old_innovate = r'bottom-\[35%\] md:bottom-\[40%\] right-\[25vw\] md:right-\[20vw\]'
new_innovate = r'bottom-[25%] right-[10vw] md:right-[15vw]'
content = re.sub(old_innovate, new_innovate, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Applied 15vw text scale and shifted INNOVATE badge.')
