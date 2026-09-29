import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

layer4 = '''
      {/* LAYER 4: FRONT UI (Scroll Hint) */}
      <div className="absolute inset-0 z-30 pointer-events-none">
        {/* Right side (Navy text) */}
        <div className="absolute inset-0 text-[#213555]">
          <ScrollHint />
        </div>
        {/* Left side (Cream text masked) */}
        <div className="absolute inset-0 text-[#F5F2EB]" style={{ clipPath: 'polygon(0 0, 50% 0, 50% 100%, 0 100%)' }}>
          <ScrollHint />
        </div>
      </div>
    </section>'''

# Using re.DOTALL so .*? matches newlines
portrait_end_regex = r'(<img[^>]*src="/profile-nobg\.png"[^>]*/>\s*</div>\s*)</section>'
content = re.sub(portrait_end_regex, r'\1' + layer4, content, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Layer 4 added!")
