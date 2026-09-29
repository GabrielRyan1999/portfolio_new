import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

old_h1 = r'<motion\.h1 variants=\{fadeUp\} className=\"relative text-center text-\[9\.5vw\] sm:text-6xl md:text-\[9rem\] font-black leading-none flex flex-row gap-2 md:gap-8 items-center justify-center z-10 w-full whitespace-nowrap\">.*?</motion\.h1>'
new_h1 = '''<motion.h1 variants={fadeUp} className="relative text-center text-[12vw] sm:text-7xl md:text-[10rem] font-serif font-black leading-none flex flex-row gap-3 md:gap-6 items-center justify-center z-10 w-full whitespace-nowrap text-[var(--foreground)] tracking-tighter uppercase">
                  <span className="shrink-0">Gabriel</span>
                  <span className="shrink-0 text-[var(--accent)] font-medium italic">Ryan</span>
                </motion.h1>'''

content = re.sub(old_h1, new_h1, content, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Hero updated.')
