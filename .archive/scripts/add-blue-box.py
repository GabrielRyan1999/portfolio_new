import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Add the Blue Japanese Accent Box
blue_box = '''      {/* Vertical Accent Box (Vibrant Blue + Japanese Katakana) */}
      <div className="absolute top-[50%] right-[22vw] z-40 hidden lg:flex flex-col items-center justify-center bg-[var(--accent)] text-white p-3 py-8 shadow-2xl">
         <p className="font-serif text-xl tracking-[0.4em] opacity-90" style={{ writingMode: 'vertical-rl' }}>
            システムビルダー
         </p>
         <div className="mt-4 w-[1px] h-12 bg-white/50"></div>
         <p className="mt-4 text-[8px] uppercase tracking-[0.3em] font-bold opacity-80" style={{ writingMode: 'vertical-rl' }}>
            SYS_BUILDER
         </p>
      </div>'''

# Insert it before the closing section tag of Home
content = re.sub(r'(\s*)(</section>\s*\);\s*\})', r'\n' + blue_box + r'\1\2', content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Blue Japanese accent box added.')
