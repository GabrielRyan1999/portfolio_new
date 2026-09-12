import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("import CountUpPkg from 'react-countup';", "")
content = re.sub(r'function StepCard\(\{ number, title, color, bg, description, imageSrc, imageLabel \}\) \{[\s\S]*?\n\}\n', '', content)
content = re.sub(r'const slideRight = \{[\s\S]*?\}\n  \};\n', '', content)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed linting part 2")
