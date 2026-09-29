import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove rounded corners (rounded-lg, rounded-xl, rounded-2xl, rounded-3xl, rounded-full, rounded-t-full, etc)
# Except maybe rounded-full on small icons, but let's just make everything sharp.
content = re.sub(r'\brounded-(?:sm|md|lg|xl|2xl|3xl|full|t-full|b-full|l-full|r-full|t-3xl)\b', 'rounded-none', content)

# 2. Add border to the profile picture
content = re.sub(r'rounded-none bg-zinc-200 shadow-2xl shadow-zinc-900/20 overflow-hidden relative z-0 ring-1 ring-zinc-900/5',
                 r'rounded-none bg-[var(--card)] border border-[var(--card-border)] overflow-hidden relative z-0', content)

# 3. Add grayscale and halftone filter class (using mix-blend-mode) to the profile picture
# We already have grayscale on it. Let's make it halftone-like.
content = re.sub(r'grayscale hover:grayscale-0', r'grayscale contrast-125 hover:grayscale-0', content)

# 4. Remove shadows for a flatter, editorial look
content = re.sub(r'\bshadow-(?:sm|md|lg|xl|2xl)\b', '', content)
content = re.sub(r'\bshadow-zinc-\S+\b', '', content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Rounded corners, shadows removed. Editorial sharp corners applied.')
