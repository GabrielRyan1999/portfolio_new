import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Swap z-index of Subject and Typography so text overlaps the image
# Subject was z-30, Typography was z-20.
old_typography = r'\{\/\* 4\. Giant Typography \(Strictly BEHIND subject\) \*\/\}\s*<div className="absolute inset-0 z-20 pointer-events-none">'
new_typography = '''{/* 4. Giant Typography (Strictly IN FRONT of subject) */}
        <div className="absolute inset-0 z-40 pointer-events-none mix-blend-difference opacity-90">'''
# Wait, if I use mix-blend-difference, it will invert the photo colors too!
# Let's not use mix-blend-difference. I'll just change z-index to 40 so the split text overlaps the image directly!

old_typography = r'\{\/\* 4\. Giant Typography \(Strictly BEHIND subject\) \*\/\}\s*<div className="absolute inset-0 z-20 pointer-events-none">'
new_typography = '''{/* 4. Giant Typography (Strictly IN FRONT of subject) */}
        <div className="absolute inset-0 z-40 pointer-events-none">'''
content = re.sub(old_typography, new_typography, content)

old_subject = r'\{\/\* 5\. The Subject \(Portrait - Strictly IN FRONT of text\) \*\/\}\s*<div className="absolute bottom-0 w-full h-\[85vh\] md:h-\[90vh\] flex justify-center z-30 pointer-events-none">'
new_subject = '''{/* 5. The Subject (Portrait - BEHIND text) */}
        <div className="absolute bottom-0 w-full h-[85vh] md:h-[90vh] flex justify-center z-20 pointer-events-none">'''
content = re.sub(old_subject, new_subject, content)

# 2. Add Barcode and Japanese text
# Find EST 2026 and replace it with a barcode
old_est = r'<div className="w-12 h-\[1px\] bg-\[#F5F2EB\]\/50 mb-3"><\/div>\s*<div className="text-xs font-semibold tracking-widest uppercase">EST\. 2026<\/div>'
new_est = '''<div className="flex gap-1 h-6 mb-2">
            {[1,3,1,1,2,4,1,2,3,1,1,2].map((w,i) => <div key={i} style={{width: `${w}px`}} className="bg-[#F5F2EB] h-full"></div>)}
          </div>
          <div className="text-[10px] font-mono tracking-widest uppercase">ARCHIVE_2026</div>'''
content = re.sub(old_est, new_est, content)

# Find INNOVATE and replace with Japanese vertical text like the reference
old_innovate = r'<div className="absolute bottom-\[25%\] right-\[10vw\] md:right-\[15vw\] z-40 bg-\[#D4C5B3\] px-2 py-4 pointer-events-none mix-blend-multiply origin-center translate-x-1\/2">\s*<div className="\[writing-mode:vertical-lr\] text-\[#1A365D\] text-xs tracking-widest font-semibold uppercase rotate-180">\s*INNOVATE\.\s*<\/div>\s*<\/div>'
new_innovate = '''<div className="absolute bottom-[20%] right-[10vw] md:right-[15vw] z-40 bg-[#D4C5B3] px-2 py-6 pointer-events-none border border-[#1A365D]/20 origin-center translate-x-1/2">
           <div className="[writing-mode:vertical-lr] text-[#1A365D] text-xs md:text-sm tracking-widest font-serif">
              永遠の美しさ
           </div>
        </div>
        
        {/* Additional Crosshairs */}
        <div className="absolute top-[30%] left-[8%] text-[#F5F2EB] text-xl font-light">+</div>
        <div className="absolute top-[35%] right-[12%] text-[#1A365D] text-xl font-light">+</div>
        
        {/* Minimalist Grid Dots */}
        <div className="absolute bottom-[40%] right-[5%] grid grid-cols-4 gap-2 opacity-30">
           {[...Array(16)].map((_, i) => <div key={i} className="w-1 h-1 bg-[#1A365D] rounded-full"></div>)}
        </div>'''
content = re.sub(old_innovate, new_innovate, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated Home section to perfectly match the uploaded reference layout.')
