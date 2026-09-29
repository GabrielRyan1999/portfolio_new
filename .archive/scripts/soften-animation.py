import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Slow down the interval from 2500ms to 4000ms
content = re.sub(
    r'setIndex\(\(prev\) => \(prev \+ 1\) % words\.length\);\s*\}, 2500\);',
    r'setIndex((prev) => (prev + 1) % words.length);\n    }, 4000);',
    content
)

# Soften the animation transition and reduce the y distance
old_motion = r'''<motion\.span
          key=\{index\}
          initial=\{\{ y: 15, opacity: 0 \}\}
          animate=\{\{ y: 0, opacity: 1 \}\}
          exit=\{\{ y: -15, opacity: 0 \}\}
          transition=\{\{ duration: 0\.5, ease: "anticipate" \}\}'''

new_motion = '''<motion.span
          key={index}
          initial={{ y: 8, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          exit={{ y: -8, opacity: 0 }}
          transition={{ duration: 1.2, ease: [0.22, 1, 0.36, 1] }}'''

content = re.sub(old_motion, new_motion, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Softened the AnimatedWords animation.')
