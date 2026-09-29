import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Add favicon collage decoration
favicon_decor = '''      {/* Abstract Editorial Decor: Favicon Collage */}
      <div className="absolute top-[20%] right-[12vw] z-10 w-32 md:w-48 aspect-[3/4] pointer-events-none mix-blend-multiply opacity-70">
         <img src="/favicon.jpg" alt="Favicon Decor" className="w-full h-full object-cover grayscale contrast-125" />
         {/* Offset geometric border */}
         <div className="absolute -bottom-4 -left-4 w-full h-full border border-[#111C2B] opacity-30"></div>
         {/* Little tape or crosshair on the image */}
         <div className="absolute top-2 left-2 text-[#F5F2EB] mix-blend-difference text-lg font-light leading-none">+</div>
      </div>'''

# Inject before the closing section tag of Home
content = re.sub(r'(\s*)(</section>\s*\);\s*\})', r'\n' + favicon_decor + r'\1\2', content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Favicon decoration added.')
