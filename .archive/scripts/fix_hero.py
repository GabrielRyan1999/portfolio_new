import re
with open('src/App_backup.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Hero is EXACTLY the first <SectionShell> block
# It starts at: <SectionShell header={
# It ends at: </SectionShell> before {/* About Me */}
hero_match = re.search(r'(<SectionShell header=\{.*?</SectionShell>)\s*\{\/\*\s*About Me', content, re.DOTALL)
hero_jsx = hero_match.group(1).strip() if hero_match else "HERO NOT FOUND"

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    pages_content = f.read()

# The current Home component in Pages.jsx looks like:
# export function Home() { ... return ( ... <PageTransition> ... <div className="relative" id="about"> ... </PageTransition> ); }
# We want to replace everything inside <PageTransition> with hero_jsx.
pages_content = re.sub(r'(<PageTransition>).*?(</PageTransition>)', lambda m: m.group(1) + '\n' + hero_jsx + '\n' + m.group(2), pages_content, count=1, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(pages_content)
print("Pages.jsx Hero fixed")
