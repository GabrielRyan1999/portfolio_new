import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

bad = r'          <\/div>\\r\\n          <\/div>\\r\\n        <\/section>\\r\\n      <\/PageTransition>\\r\\n    \);\\r\\n\}\\r\\n\\r\\nexport function Experience'
good = r'''          </div>
          </div>
        </section>
      </PageTransition>
    );
}

export function Experience'''

content = re.sub(bad, good, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed literal r n from PowerShell")
