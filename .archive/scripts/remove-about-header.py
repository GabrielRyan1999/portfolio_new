import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the Header Row from the About section
header_regex = r'\{\/\* Header Row \*\/.*?<\/div>'
# Wait, let's just do it cleanly
header_pattern = r'\{\/\*\s*Header Row\s*\*\/.*?<div className="w-full flex items-center justify-between px-6 md:px-12 py-4 border-b border-\[#1A365D\] shrink-0">.*?<\/div>\s*\{\/\*\s*Main Grid Spread\s*\*\/\}'

# Easier regex
content = re.sub(
    r'\{\/\* Header Row \*\/\}[\s\S]*?\{\/\* Main Grid Spread \*\/\}',
    '{/* Main Grid Spread */}',
    content
)

# Also remove the top border from the section so it spans perfectly
content = re.sub(
    r'<section id="about-me" className="relative w-full min-h-\[100svh\] bg-\[#F5F2EB\] text-\[#1A365D\] flex flex-col border-t-2 border-\[#1A365D\] overflow-hidden">',
    r'<section id="about-me" className="relative w-full min-h-[100svh] bg-[#F5F2EB] text-[#1A365D] flex flex-col overflow-hidden">',
    content
)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Removed Header Row from About.')
