import re

files = [
    'src/components/ui/lets-work-section.jsx',
    'src/components/ui/features-2.jsx',
    'src/components/ui/unique-testimonial.jsx'
]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(r'\brounded-(?:sm|md|lg|xl|2xl|3xl|full|t-full|b-full|l-full|r-full|t-3xl)\b', 'rounded-none', content)
    content = re.sub(r'\bshadow-(?:sm|md|lg|xl|2xl)\b', '', content)
    content = re.sub(r'\bshadow-zinc-\S+\b', '', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Flattened child components.')
