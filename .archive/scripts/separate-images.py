import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the left bird (Inverted silhouette) with the flower
old_left = r'<img src="/blue-bird\.jpg" alt="" className="w-full h-auto object-contain invert grayscale" />'
new_left = '<img src="/flower.jpg" alt="Centaurea cyanus" className="w-full h-auto object-contain invert grayscale" />'
content = re.sub(old_left, new_left, content)

# Replace the right bird (Multiply) with the new fairy-bluebird
old_right = r'<img src="/blue-bird\.jpg" alt="" className="w-full h-auto object-contain scale-x-\[-1\]" />'
new_right = '<img src="/bird.jpg" alt="Irena puella" className="w-full h-auto object-contain scale-x-[-1] contrast-[1.2]" />'
content = re.sub(old_right, new_right, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Separated the bird and flower illustrations.')
