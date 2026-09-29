import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Beige Color
content = content.replace('bg-[#D7C4A5]', 'bg-[#E5D8C5]')
content = content.replace('text-[#D7C4A5]', 'text-[#E5D8C5]')

# Fix GABRIEL position (higher)
content = content.replace('top-[12%] md:top-[15%]', 'top-[8%] md:top-[10%]')

# Fix Ryan position (higher) and size (larger)
content = content.replace('top-[50%] md:top-[60%] left-1/2 -translate-x-1/2 mt-[2vw] ml-[4vw]', 'top-[35%] md:top-[40%] left-1/2 -translate-x-1/2 ml-[3vw]')
content = content.replace('text-[18vw] md:text-[14vw]', 'text-[22vw] md:text-[17vw]')

# Fix Portrait size (smaller, capped height so it doesn't hit GABRIEL)
content = content.replace('w-[95%] md:w-[750px] max-w-4xl', 'w-[85%] md:w-[550px] xl:w-[600px] max-w-2xl')
content = content.replace('w-full h-auto object-contain', 'w-full h-auto max-h-[65vh] md:max-h-[70vh] object-contain')


with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Adjustments applied.")
