import re
with open('src/App_backup.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

hero_match = re.search(r'(<div className="relative" id="about">.*?)<SectionShell id="about-me"', content, re.DOTALL)
hero = hero_match.group(1).strip()
print("Ends with:", hero[-50:])
