import re

with open('src/components/ui/lets-work-section.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace exactly 4 closing divs with 2 closing divs?
# Let's count them! 
# We have:
#         </div>
#         
#         </div>
#         </div>
#         </div>
#         {/* Footer */}

bad = r'        <\/div>\n        \n        <\/div>\n        <\/div>\n        <\/div>\n        \{\/\* Footer \*\/\}'
good = r'        </div>\n        </div>\n        {/* Footer */}'

content = re.sub(bad, good, content)

with open('src/components/ui/lets-work-section.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed divs in Contact")
