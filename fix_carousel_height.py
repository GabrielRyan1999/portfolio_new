import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace min-h-[500px] with fixed heights across responsive breakpoints
old_class = 'className="w-full bg-[var(--background-secondary)] border border-[var(--card-border)] rounded-3xl md:rounded-[2.5rem] overflow-hidden flex flex-col md:flex-row shadow-2xl group mx-4 md:mx-0 min-h-[500px]"'
new_class = 'className="w-full bg-[var(--background-secondary)] border border-[var(--card-border)] rounded-3xl md:rounded-[2.5rem] overflow-hidden flex flex-col md:flex-row shadow-2xl group mx-4 md:mx-0 h-[550px] md:h-[480px] lg:h-[500px]"'

content = content.replace(old_class, new_class)

# Ensure the content half allows scrolling or just fits, and aligns beautifully
old_content_div = '<div className="w-full md:w-7/12 lg:w-1/2 p-6 md:p-8 lg:p-12 flex flex-col justify-center">'
new_content_div = '<div className="w-full md:w-7/12 lg:w-1/2 p-6 md:p-8 lg:p-12 flex flex-col justify-center h-full">'

content = content.replace(old_content_div, new_content_div)

# Ensure the image takes full height of the container on desktop
old_img_div = '<div className="w-full md:w-5/12 lg:w-1/2 h-[200px] md:h-auto relative overflow-hidden bg-zinc-950">'
new_img_div = '<div className="w-full md:w-5/12 lg:w-1/2 h-[220px] md:h-full relative overflow-hidden bg-zinc-950 shrink-0">'

content = content.replace(old_img_div, new_img_div)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
