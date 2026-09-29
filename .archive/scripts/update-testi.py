import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the Testimonials Wrapper header
testi_pattern = r'\{\/\* Testimonials Wrapper \*\/\}[\s\S]*?\{\/\* Endorsements \*\/\}'
# Actually wait, let's just find the section tag
testi_pattern = r'\{\/\* Testimonials Wrapper \*\/.*?<section className="relative w-full bg-\[#F5F2EB\] py-32 border-t-2 border-\[#1A365D\] overflow-hidden">.*?<div className="w-full max-w-7xl mx-auto px-6 mb-16">.*?<span className="text-xs font-bold tracking-widest uppercase text-\[#1A365D\]\/50 font-mono mb-4 block text-center">Chapter 05 \/\/ Endorsements<\/span>.*?<\/div>'

testi_replacement = '''{/* Testimonials Wrapper */}
        <section className="relative w-full min-h-[100svh] bg-[#F5F2EB] text-[#1A365D] flex flex-col border-t-2 border-[#1A365D] overflow-hidden">
          
          {/* Header Row */}
          <div className="w-full flex items-center justify-between px-6 md:px-12 py-4 border-b border-[#1A365D] shrink-0 z-20 relative">
             <span className="text-xs font-bold tracking-widest uppercase">Chapter 05 // Endorsements</span>
             <span className="text-xs font-bold tracking-widest uppercase hidden md:inline-block">Yogyakarta, ID</span>
          </div>

          <div className="flex-1 flex flex-col w-full py-16 md:py-24 relative">'''

content = re.sub(testi_pattern, testi_replacement, content, flags=re.DOTALL)

# And add the closing div before </section>
content = re.sub(r'(<Testimonials \/>\s*)<\/section>', r'\1</div>\n        </section>', content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated Testimonials header in Pages.jsx.')
