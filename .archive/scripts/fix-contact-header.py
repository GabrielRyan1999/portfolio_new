import re

with open('src/components/ui/lets-work-section.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the beginning of LetsWorkTogether
contact_pattern = r'<section className="relative w-full min-h-\[100svh\] bg-\[#1A365D\] flex flex-col justify-center items-center py-32 px-6 border-t-2 border-\[#F5F2EB\] text-\[#F5F2EB\] overflow-hidden">.*?<div className="absolute top-8 left-8">.*?<span className="font-mono text-xs tracking-widest uppercase opacity-50">Chapter 06 \/\/ Initiate<\/span>.*?<\/div>'

contact_replacement = '''<section className="relative w-full min-h-[100svh] bg-[#1A365D] flex flex-col border-t-2 border-[#F5F2EB] text-[#F5F2EB] overflow-hidden">
          
          {/* Header Row */}
          <div className="w-full flex items-center justify-between px-6 md:px-12 py-4 border-b border-[#F5F2EB]/30 shrink-0 z-20 relative">
             <span className="text-xs font-bold tracking-widest uppercase">Chapter 05 // Initiate Contact</span>
             <span className="text-xs font-bold tracking-widest uppercase hidden md:inline-block">Yogyakarta, ID</span>
          </div>

          <div className="flex-1 flex flex-col justify-center items-center py-16 md:py-24 px-6 relative w-full h-full">'''

content = re.sub(contact_pattern, contact_replacement, content, flags=re.DOTALL)

# Add closing div for the wrapper
content = re.sub(r'(<div className="w-full flex justify-between items-center text-xs font-mono tracking-widest uppercase opacity-50 mt-12 md:mt-0 pt-8 border-t border-\[#F5F2EB\]\/20">[\s\S]*?<\/div>\s*)<\/section>', r'\1</div>\n        </section>', content)

with open('src/components/ui/lets-work-section.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated Contact header.')
