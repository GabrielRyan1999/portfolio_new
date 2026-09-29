import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the portrait container and image
old_portrait = r'<div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-\[85%\] md:w-\[550px\] xl:w-\[600px\] max-w-2xl flex justify-center z-20 pointer-events-none">\s*<img\s*src="/profile-nobg.png"\s*alt="Gabriel Ryan"\s*className="w-full h-auto max-h-\[65vh\] md:max-h-\[70vh\] object-contain object-bottom grayscale drop-shadow-2xl brightness-105 contrast-125"\s*/>\s*</div>'

new_portrait = '''<div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-full flex justify-center z-20 pointer-events-none">
        <img 
          src="/profile-nobg.png" 
          alt="Gabriel Ryan" 
          className="h-[65vh] md:h-[75vh] xl:h-[80vh] w-auto object-contain object-bottom grayscale drop-shadow-2xl brightness-105 contrast-125" 
        />
      </div>'''

content = re.sub(old_portrait, new_portrait, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Portrait height scaling fixed.")
