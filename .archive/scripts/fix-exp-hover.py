import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Experience Ledger hover borders
old_row = r'<div key=\{i\} className="flex flex-col md:flex-row border-t-2 border-\[#F5F2EB\] group hover:bg-\[#F5F2EB\] hover:text-\[#1A365D\] transition-colors duration-300">'
new_row = r'<div key={i} className="flex flex-col md:flex-row border-t-2 border-[#F5F2EB] group hover:border-[#1A365D] hover:bg-[#F5F2EB] hover:text-[#1A365D] transition-colors duration-300">'

content = re.sub(old_row, new_row, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed Experience row borders.')
