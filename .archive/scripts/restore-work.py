import re
import subprocess

# Get the original file from git
result = subprocess.run(['git', 'show', 'HEAD:src/pages/Pages.jsx'], capture_output=True, text=True, encoding='utf-8')
head_content = result.stdout

# Extract Work() block
work_regex = r'(export function Work\(\) \{[\s\S]*?(?=export function Service\(\) \{))'
work_match = re.search(work_regex, head_content)

if work_match:
    work_code = work_match.group(1)
    
    # Read current Pages.jsx
    with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
        current = f.read()
    
    # Insert Work() right before Service()
    current = current.replace('export function Service()', work_code + '\nexport function Service()')
    
    with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
        f.write(current)
    print('Restored Work component!')
else:
    print('Could not find Work in HEAD.')
