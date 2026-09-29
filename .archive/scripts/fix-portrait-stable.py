import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

old_portrait = r'<div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-full flex justify-center z-20 pointer-events-none">\s*<img\s*src="/profile-nobg.png"\s*alt="Gabriel Ryan"\s*className="h-\[75vh\] md:h-\[85vh\] w-auto max-w-none object-contain object-bottom grayscale drop-shadow-2xl brightness-105 contrast-125 md:scale-110 origin-bottom"\s*/>\s*</div>'

new_portrait = '''<div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-[95%] md:w-[650px] lg:w-[750px] xl:w-[850px] flex justify-center z-20 pointer-events-none">
        <img 
          src="/profile-nobg.png" 
          alt="Gabriel Ryan" 
          className="w-full h-auto object-contain object-bottom grayscale drop-shadow-2xl brightness-105 contrast-125" 
        />
      </div>'''

content = re.sub(old_portrait, new_portrait, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Reverted to width-based constraints for stable scaling.")
