import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the Background Decor 1 and 2 (Birds/Flowers)
bg1_pattern = r'\{\/\* Background Decor 1:.*?<\/div>'
bg2_pattern = r'\{\/\* Background Decor 2:.*?<\/div>'
content = re.sub(bg1_pattern, '', content, flags=re.DOTALL)
content = re.sub(bg2_pattern, '', content, flags=re.DOTALL)

# Add new minimalist editorial decorations
new_decor = '''      {/* Abstract Editorial Decor: Giant Hollow Number */}
      <div className="absolute top-[15%] right-[-5vw] z-0 pointer-events-none opacity-10 select-none">
         <h2 className="text-[40vw] font-serif font-black leading-none text-transparent" style={{ WebkitTextStroke: '2px #111C2B' }}>
            01
         </h2>
      </div>

      {/* Abstract Editorial Decor: Giant Delicate Ring */}
      <div className="absolute bottom-[-20%] left-[-10vw] w-[50vw] md:w-[600px] aspect-square rounded-full border-[1px] border-[#F5F2EB] opacity-20 z-10 pointer-events-none mix-blend-difference"></div>

      {/* Abstract Editorial Decor: Architectural Crosshairs */}
      <div className="absolute top-[50%] left-[25vw] z-10 text-[#F5F2EB] opacity-30 pointer-events-none">
         <div className="text-2xl font-light leading-none">+</div>
      </div>
      <div className="absolute bottom-[30%] right-[30vw] z-10 text-[#111C2B] opacity-30 pointer-events-none">
         <div className="text-2xl font-light leading-none">+</div>
      </div>'''

# Inject before the closing section tag of Home
content = re.sub(r'(\s*)(</section>\s*\);\s*\})', r'\n' + new_decor + r'\1\2', content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Birds removed. Minimalist geometric decorations added.')
