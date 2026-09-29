with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "GABRIEL" in line and "RYAN" in line:
        print("".join(lines[i-15:i+5]))
        break
