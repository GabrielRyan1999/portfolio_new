import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the Arch Background
old_arch = r'\{\/\* 1\. Deep Navy Arch Background \(Centered Bottom\) \*\/\}[\s\S]*?z-0 pointer-events-none"><\/div>'
new_arch = '''{/* 0. Torn Paper Texture Background */}
          <div className="absolute bottom-0 left-0 w-full h-[40vh] z-0 pointer-events-none opacity-80 mix-blend-multiply" style={{ backgroundImage: "url('/torn-paper.svg')", backgroundSize: "100% 100%", backgroundRepeat: "no-repeat" }}></div>

          {/* 1. Academic Blue Arch Background (Centered Bottom) */}
          <div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-[95vw] md:w-[70vw] h-[47.5vw] md:h-[35vw] bg-[#234E8A] rounded-t-full z-0 pointer-events-none shadow-2xl"></div>'''
content = re.sub(old_arch, new_arch, content)

# 2. Update the Cursive text color to match the Academic Blue
old_cursive = r'text-\[#2D507B\]'
new_cursive = 'text-[#234E8A]'
content = content.replace(old_cursive, new_cursive)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Added torn paper and Academic Blue.')
