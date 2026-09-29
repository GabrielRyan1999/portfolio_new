import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove Mid Right Philosophy
old_philosophy = r'\{\/\* Mid Right Philosophy \*\/\}[\s\S]*?WEB\.\s*<\/div>'
content = re.sub(old_philosophy, '', content)

# 2. Combine Mid Left Role and Bottom Left Meta into one stacked group at the bottom
old_role_and_meta = r'\{\/\* Mid Left Role \*\/\}[\s\S]*?EST\. 2026<\/div>\s*<\/div>'

new_bottom_left = '''{/* Bottom Left Content Group */}
        <div className="absolute bottom-8 left-4 md:bottom-12 md:left-8 z-40 flex flex-col gap-10 pointer-events-none">
          {/* Role */}
          <div className="text-[#F5F2EB] text-xs font-semibold tracking-widest uppercase leading-relaxed">
            <span className="opacity-50">ROLE //</span><br/><br/>
            EDUCATOR & <AnimatedWords words={["DEVELOPER.", "SYSTEM BUILDER.", "MENTOR."]} />
          </div>
          {/* Meta */}
          <div className="text-[#F5F2EB] flex flex-col">
            <div className="w-12 h-[1px] bg-[#F5F2EB]/50 mb-3"></div>
            <div className="text-xs font-semibold tracking-widest uppercase">EST. 2026</div>
          </div>
        </div>'''

content = re.sub(old_role_and_meta, new_bottom_left, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Moved ROLE and deleted Philosophy.')
