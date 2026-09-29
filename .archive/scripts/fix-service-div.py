import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix unclosed div in Service
service_end_pattern = r'(?<=        \}\)\}\n          <\/div>\n  )\n          <\/section>'
service_end_replacement = r'          </div>\n          </section>'

content = re.sub(service_end_pattern, service_end_replacement, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed unclosed div in Service section.')
