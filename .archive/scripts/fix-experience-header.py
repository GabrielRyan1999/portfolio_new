import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

bad = r'<section id="experience" className="relative w-full min-h-\[100svh\] bg-navy py-24 md:py-32 flex flex-col border-t-2 border-cream overflow-hidden text-cream">\s*\{\/\* Header \*\/\}'
good = r'''<section id="experience" className="relative w-full min-h-[100svh] bg-navy flex flex-col border-t-2 border-cream overflow-hidden text-cream">
          
          {/* Header Row */}
          <div className="w-full flex items-center justify-between px-6 md:px-12 py-4 border-b border-cream shrink-0 z-20 relative">
             <span className="text-xs font-bold tracking-widest uppercase text-cream">Chapter 04 // Professional Record</span>
             <span className="text-xs font-bold tracking-widest uppercase hidden md:inline-block text-cream">Yogyakarta, ID</span>
          </div>

          <div className="flex-1 flex flex-col w-full py-16 md:py-24 relative">
            {/* Header */}'''

content = re.sub(bad, good, content)

bad2 = r'              \)\)\}\n            <\/div>\n        <\/section>\n\n        \{\/\* Testimonials Wrapper \*\/\}'
good2 = r'              ))}\n            </div>\n          </div>\n        </section>\n\n        {/* Testimonials Wrapper */}'

content = re.sub(bad2, good2, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed Experience component")
