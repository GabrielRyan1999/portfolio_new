import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the IntroScreen import
content = re.sub(r"import \{ IntroScreen \} from '\./components/IntroScreen';\n", '', content)

# Remove the hasEntered state
content = re.sub(r"  const \[hasEntered, setHasEntered\] = useState\(false\);\n", '', content)

# Remove the AnimatePresence block for IntroScreen
target_intro = r"""        <AnimatePresence>
          {!hasEntered && <IntroScreen key="intro" onEnter={() => setHasEntered(true)} />}
        </AnimatePresence>"""
content = re.sub(target_intro, '', content)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("IntroScreen removed")
