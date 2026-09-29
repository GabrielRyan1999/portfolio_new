import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Adjust Typography Size to give side elements breathing room
content = re.sub(
    r'text-\[18vw\] md:text-\[20vw\]',
    r'text-[15vw] md:text-[17vw]',
    content
)

# 2. Move "INNOVATE" box up so it doesn't overlap the navy footer
content = re.sub(
    r'absolute bottom-\[20%\] right-\[25vw\] md:right-\[20vw\]',
    r'absolute bottom-[35%] md:bottom-[40%] right-[25vw] md:right-[20vw]',
    content
)

# 3. Move "TIMELESS LOGIC" to the right edge
content = re.sub(
    r'absolute top-\[45%\] right-8 md:right-12',
    r'absolute top-[45%] right-4 md:right-8',
    content
)

# 4. Move "ROLE //" to the left edge
content = re.sub(
    r'absolute top-\[40%\] left-8 md:left-12',
    r'absolute top-[40%] left-4 md:left-8',
    content
)

# 5. Move Sand Circle up and right
content = re.sub(
    r'absolute top-\[5%\] right-\[10vw\]',
    r'absolute top-[-5%] right-[2vw]',
    content
)

# 6. Move Dot Grid right
content = re.sub(
    r'absolute top-\[30%\] right-\[5vw\]',
    r'absolute top-[25%] right-[2vw]',
    content
)

# 7. Make Portrait slightly taller to match the master screenshot
content = re.sub(
    r'h-\[75vh\] md:h-\[85vh\]',
    r'h-[80vh] md:h-[90vh]',
    content
)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Tidied up the layout elements.')
