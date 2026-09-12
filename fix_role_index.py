import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove `const roles = [...]`
content = re.sub(r'const roles = \["Developer\.", "Mentor\.", "Innovator\.", "Creator\."\];\n', '', content)

# Remove the useEffect that sets roleIndex
useEffect_pattern = r'  useEffect\(\(\) => \{\n    const interval = setInterval\(\(\) => \{\n      setRoleIndex\(\(prev\) => \(prev \+ 1\) % roles\.length\);\n    \}, 2500\);\n    return \(\) => clearInterval\(interval\);\n  \}, \[\]\);\n'
content = re.sub(useEffect_pattern, '', content)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed unused useEffect and roles")
