import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# The current text block
old_text = r'\{\/\* 4\. Magic Inverted Text.*?<\/h1>\s*<\/div>'
new_text = '''{/* 4. Background Text (GABRIEL) */}
      <div className="absolute inset-0 flex flex-col items-center justify-center z-20 pointer-events-none mix-blend-difference text-white pt-10">
        <h1 className="text-[18vw] md:text-[220px] leading-[0.75] font-serif font-black tracking-tighter uppercase text-center flex flex-col w-full px-4">
          <span className="w-full text-center">GABRIEL</span>
          {/* Invisible RYAN to maintain exact spacing/alignment */}
          <span className="w-full text-center tracking-[0.25em] ml-[0.25em] opacity-0">RYAN</span>
        </h1>
      </div>'''
      
content = re.sub(old_text, new_text, content, flags=re.DOTALL)

# Add Foreground text after the image
old_img = r'\{\/\* 5\. Foreground Subject \(Profile Photo\).*?<\/div>'
# Need to match the entire image div
img_match = re.search(old_img, content, flags=re.DOTALL)
if img_match:
    img_code = img_match.group(0)
    foreground_text = '''\n\n      {/* 5.5 Foreground Text (RYAN) - Placed IN FRONT of the photo */}
      <div className="absolute inset-0 flex flex-col items-center justify-center z-40 pointer-events-none mix-blend-difference text-white pt-10">
        <h1 className="text-[18vw] md:text-[220px] leading-[0.75] font-serif font-black tracking-tighter uppercase text-center flex flex-col w-full px-4">
          {/* Invisible GABRIEL to maintain exact spacing/alignment */}
          <span className="w-full text-center opacity-0">GABRIEL</span>
          <span className="w-full text-center tracking-[0.25em] ml-[0.25em]">RYAN</span>
        </h1>
      </div>'''
    content = content.replace(img_code, img_code + foreground_text)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Layered typography implemented.')
