with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if ">GABRIEL</span>" in line:
        print("".join(lines[i-10:i+10]))
        break
