import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the redundant "Chapter 03" text
c3_pattern = r'<span className="text-xs font-bold tracking-widest uppercase text-\[#1A365D\]\/50 font-mono mb-4 block">Chapter 03<\/span>\n\s*'
content = re.sub(c3_pattern, '', content)

# Remove the redundant "Chapter 04" text
c4_pattern = r'<span className="text-xs font-bold tracking-widest uppercase text-\[#F5F2EB\]\/50 font-mono mb-4 block">Chapter 04<\/span>\n\s*'
content = re.sub(c4_pattern, '', content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Removed redundant chapter tags.')
