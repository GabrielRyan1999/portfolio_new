import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the current bird div
old_bird_pattern = r'\{\/\* Botanical Accent: Vintage Blue Bird.*?<\/div>'
content = re.sub(old_bird_pattern, '', content, flags=re.DOTALL)

# Create the new background bird decorations
new_birds = '''      {/* Background Decor 1: Left Side (Over Navy) - Inverted to act as faint white line-art */}
      <div className="absolute top-[25%] left-[-15vw] md:left-[-10vw] z-10 w-[60vw] md:w-[600px] opacity-[0.15] mix-blend-screen pointer-events-none">
         <img src="/blue-bird.jpg" alt="" className="w-full h-auto object-contain invert grayscale" />
      </div>

      {/* Background Decor 2: Right Side (Over Cream) - Multiplied to act as a vintage stamp */}
      <div className="absolute bottom-[5%] right-[-20vw] md:right-[-12vw] z-10 w-[70vw] md:w-[700px] opacity-20 mix-blend-multiply pointer-events-none">
         {/* scale-x-[-1] flips the image horizontally so it faces inward */}
         <img src="/blue-bird.jpg" alt="" className="w-full h-auto object-contain scale-x-[-1]" />
      </div>'''

# Inject after the dot grid (which is at z-10)
# Let's find the Dot Grid comment
dot_grid = r'\{\/\* Small Graphic Accent - Dot Grid \*\/.*?<\/div>'
content = re.sub(dot_grid, lambda m: m.group(0) + '\n\n' + new_birds, content, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Birds moved to background as ambient decorations.')
