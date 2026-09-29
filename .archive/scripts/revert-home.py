import re

# Read as utf-16 since powershell Get-Content > file uses utf-16
with open('pages_broken.jsx', 'r', encoding='utf-16') as f:
    broken = f.read()

# Extract the Home section from the backup
home_regex = r'(<section id="home" className="relative min-h-screen w-full bg-\[#F5F2EB\] text-\[#1A365D\] overflow-hidden">[\s\S]*?<\/section>)'
home_match = re.search(home_regex, broken)
old_home_code = home_match.group(1)

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    current = f.read()

# Replace the current Home section with the old Home code
current = re.sub(home_regex, old_home_code.replace('\\', '\\\\'), current)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(current)
print('Reverted Home to Editorial Brutalism Split Layout.')
