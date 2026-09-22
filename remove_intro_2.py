import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

target_intro = r"""      <AnimatePresence>
        \{!hasEntered && <IntroScreen key="intro" onEnter=\{\(\) => setHasEntered\(true\)\} />\}
      </AnimatePresence>"""

content = re.sub(target_intro, '', content)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
