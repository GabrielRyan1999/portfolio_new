import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Add ContactModal before </>
content = content.replace("    </>\n  );\n}", "      <ContactModal isOpen={isContactOpen} onClose={() => setIsContactOpen(false)} />\n    </>\n  );\n}")

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected ContactModal")
