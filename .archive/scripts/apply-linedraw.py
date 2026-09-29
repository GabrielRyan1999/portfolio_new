import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Apply LineDraw to Service top border
old_service_border = r'className="relative w-full min-h-\[100svh\] bg-\[#F5F2EB\] py-24 md:py-32 flex flex-col border-t-2 border-\[#1A365D\] overflow-hidden"'
new_service_border = '''className="relative w-full min-h-[100svh] bg-[#F5F2EB] py-24 md:py-32 flex flex-col overflow-hidden"'''
# Add LineDraw at the very top of Service
old_service_top = r'\{\/\* Header \*\/\}'
new_service_top = '''<div className="absolute top-0 left-0 w-full"><LineDraw className="w-full h-[2px] bg-[#1A365D]" /></div>\n          {/* Header */}'''

content = re.sub(old_service_border, new_service_border, content)
content = re.sub(old_service_top, new_service_top, content)

# Apply LineDraw to Experience top border
old_exp_border = r'className="relative w-full min-h-\[100svh\] bg-\[#1A365D\] py-24 md:py-32 flex flex-col border-t-2 border-\[#F5F2EB\] overflow-hidden text-\[#F5F2EB\]"'
new_exp_border = '''className="relative w-full min-h-[100svh] bg-[#1A365D] py-24 md:py-32 flex flex-col overflow-hidden text-[#F5F2EB]"'''
# Add LineDraw at the very top of Experience
old_exp_top = r'\{\/\* Header \*\/\}' # wait, there's a Header comment in Experience too
new_exp_top = '''<div className="absolute top-0 left-0 w-full"><LineDraw className="w-full h-[2px] bg-[#F5F2EB]" /></div>\n          {/* Header */}'''

# Since we might match the Header comment in Service again, let's just do it directly on the section tag
# Actually I'll use a more precise regex.

old_exp = r'<section id="experience" className="relative w-full min-h-\[100svh\] bg-\[#1A365D\] py-24 md:py-32 flex flex-col border-t-2 border-\[#F5F2EB\] overflow-hidden text-\[#F5F2EB\]">\s*\{\/\* Header \*\/\}'
new_exp = '''<section id="experience" className="relative w-full min-h-[100svh] bg-[#1A365D] py-24 md:py-32 flex flex-col overflow-hidden text-[#F5F2EB]">
          <div className="absolute top-0 left-0 w-full"><LineDraw className="w-full h-[2px] bg-[#F5F2EB]" /></div>
          {/* Header */}'''
content = re.sub(old_exp, new_exp, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Applied LineDraw animations.')
