import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the scroll hint from HomeContent
scroll_hint_regex = r'\s*\{\/\* Scroll Hint \(Bottom Center\) \*\/\}.*?<\/div>\s*<\/div>'
content = re.sub(scroll_hint_regex, '', content, flags=re.DOTALL)

# 2. Add ScrollHint component definition
scroll_hint_comp = '''
function ScrollHint() {
  return (
    <div className="absolute bottom-6 md:bottom-10 left-1/2 -translate-x-1/2 flex flex-col items-center gap-3 opacity-70">
      <span className="text-[7px] md:text-[9px] font-bold tracking-[0.4em] uppercase whitespace-nowrap">
        Scroll to explore
      </span>
      <div className="w-[1px] h-8 md:h-12 bg-current overflow-hidden relative opacity-50">
        <motion.div 
          className="absolute top-0 left-0 w-full h-[50%] bg-current"
          animate={{ y: ["-100%", "200%"] }}
          transition={{ duration: 1.5, repeat: Infinity, ease: "easeInOut" }}
        />
      </div>
    </div>
  );
}

function HomeContent'''
content = content.replace('function HomeContent', scroll_hint_comp)


# 3. Add Layer 4 only to the Home section
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

# Find the specific closing </section> for the Home component
# The Home component ends right after the portrait layer
portrait_end_regex = r'(<img src="/profile-nobg\.png" .*? />\s*</div>\s*)</section>'
content = re.sub(portrait_end_regex, r'\1' + layer4, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed!")
