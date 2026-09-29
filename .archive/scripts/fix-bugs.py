import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix AnimatedWords component width and clipping
old_anim = r'<div className="inline-block relative overflow-hidden min-w-\[120px\] h-\[1\.5em\] align-middle">'
new_anim = '<div className="inline-block relative min-w-[250px] h-[1.5em] align-middle">'
content = re.sub(old_anim, new_anim, content)

# 2. Fix AnimatedWords text color (it was blue, making it hard to read on navy)
old_anim_color = r'className="absolute left-0 text-\[var\(--accent\)\]"'
new_anim_color = 'className="absolute left-0 text-[#D1C4B5]"' # Sand color
content = re.sub(old_anim_color, new_anim_color, content)

# 3. Fix the invisible vertical box (It was on the left over Navy, multiplied it became black. Move it to right over Cream)
old_vertical_box = r'<div className="absolute top-\[65\%\] left-\[20vw\] z-40 hidden lg:flex items-center justify-center bg-\[#D1C4B5\] p-3 py-10 shadow-lg mix-blend-multiply">'
new_vertical_box = '<div className="absolute top-[65%] right-[25vw] z-40 hidden lg:flex items-center justify-center bg-[#D1C4B5] p-3 py-10 shadow-lg mix-blend-multiply">'
content = re.sub(old_vertical_box, new_vertical_box, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed layout bugs.')
