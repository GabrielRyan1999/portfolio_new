import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Service Header
service_pattern = r'<section id="service" className="relative w-full min-h-\[100svh\] bg-\[#F5F2EB\] py-24 md:py-32 flex flex-col overflow-hidden">.*?<div className="absolute top-0 left-0 w-full"><LineDraw className="w-full h-\[2px\] bg-\[#1A365D\]" \/><\/div>.*?\{\/\* Header \*\/\}'
service_replacement = '''<section id="service" className="relative w-full min-h-[100svh] bg-[#F5F2EB] text-[#1A365D] flex flex-col border-t-2 border-[#1A365D] overflow-hidden">
          
          {/* Header Row */}
          <div className="w-full flex items-center justify-between px-6 md:px-12 py-4 border-b border-[#1A365D] shrink-0">
             <span className="text-xs font-bold tracking-widest uppercase">Chapter 03 // Services & Expertise</span>
             <span className="text-xs font-bold tracking-widest uppercase hidden md:inline-block">Yogyakarta, ID</span>
          </div>

          <div className="flex-1 flex flex-col w-full py-16 md:py-24 relative">
            {/* Header */}'''

content = re.sub(service_pattern, service_replacement, content, flags=re.DOTALL)

# Add closing div for the wrapper in Service
service_end_pattern = r'(<\/div>\s*<\/section>\s*<\/PageTransition>\s*\);\s*\})'
service_end_replacement = r'  </div>\n            \1'
# Wait, I need to make sure I only replace it for Service
content = re.sub(r'(<div className="w-full max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8 z-10">[\s\S]*?<\/div>\s*)<\/section>', r'\1</div>\n          </section>', content)


# Fix Experience Header
exp_pattern = r'<section id="experience" className="relative w-full min-h-\[100svh\] bg-\[#1A365D\] py-24 md:py-32 flex flex-col border-t-2 border-\[#F5F2EB\] overflow-hidden text-\[#F5F2EB\]">.*?<div className="absolute top-0 left-0 w-full"><LineDraw className="w-full h-\[2px\] bg-\[#1A365D\]" \/><\/div>.*?\{\/\* Header \*\/\}'
exp_replacement = '''<section id="experience" className="relative w-full min-h-[100svh] bg-[#1A365D] flex flex-col border-t-2 border-[#F5F2EB] overflow-hidden text-[#F5F2EB]">
          
          {/* Header Row */}
          <div className="w-full flex items-center justify-between px-6 md:px-12 py-4 border-b border-[#F5F2EB]/30 shrink-0 z-20 relative">
             <span className="text-xs font-bold tracking-widest uppercase">Chapter 04 // Professional Record</span>
             <span className="text-xs font-bold tracking-widest uppercase hidden md:inline-block">Yogyakarta, ID</span>
          </div>

          <div className="flex-1 flex flex-col w-full py-16 md:py-24 relative">
            {/* Header */}'''

content = re.sub(exp_pattern, exp_replacement, content, flags=re.DOTALL)

# Add closing div for the wrapper in Experience
content = re.sub(r'(<div className="w-full max-w-7xl mx-auto px-6 flex flex-col gap-6 md:gap-8 z-10 relative">[\s\S]*?<\/div>\s*)<\/section>', r'\1</div>\n          </section>', content)


with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated Service and Experience headers.')
