import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the Japanese Blue box
japanese_box_pattern = r'\{\/\*\s*Vertical Accent Box \(Vibrant Blue \+ Japanese Katakana\).*?<\/div>'
content = re.sub(japanese_box_pattern, '', content, flags=re.DOTALL)

# 2. Add the Botanical Bird illustration
bird_code = '''      {/* Botanical Accent: Vintage Blue Bird (mix-blend-multiply removes the white background!) */}
      <div className="absolute top-[20%] right-[2vw] md:right-[8vw] z-10 w-[40vw] md:w-[350px] opacity-80 mix-blend-multiply pointer-events-none">
         <img src="/blue-bird.jpg" alt="Vintage Blue Bird" className="w-full h-auto object-contain grayscale-[0.3] contrast-[1.2]" />
      </div>'''

# Inject right before the closing section tag
content = re.sub(r'(\s*)(</section>\s*\);\s*\})', r'\n' + bird_code + r'\1\2', content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Japanese text replaced with botanical blue bird.')
