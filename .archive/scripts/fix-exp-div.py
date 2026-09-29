import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Add closing div for the wrapper right before </section> in Experience
# We look for the end of the Brutalist Ledger Table loop and the closing section tag.
exp_pattern = r'(\{\/\* Brutalist Ledger Table \*\/\}[\s\S]*?\{experienceJobs\.map[\s\S]*?<\/div>\s*)<\/section>'
exp_replacement = r'\1</div>\n        </section>'

content = re.sub(exp_pattern, exp_replacement, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed unclosed div in Experience section.')
