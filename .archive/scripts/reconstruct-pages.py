import re

# 1. Get the base file up to Home()
with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

header_match = re.search(r'([\s\S]*?)(?=export function Home\(\))', content)
header = header_match.group(1) if header_match else ''


# 2. Extract components from scripts
def extract_from_script(script_path, variable_name):
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            script_content = f.read()
        
        # We look for variable_name = '''...''' or """..."""
        pattern = variable_name + r'\s*=\s*(?:\'\'\'|\"\"\")([\s\S]*?)(?:\'\'\'|\"\"\")'
        match = re.search(pattern, script_content)
        if match:
            return match.group(1)
        return f"// Could not extract {variable_name} from {script_path}\n"
    except Exception as e:
        return f"// Error reading {script_path}: {str(e)}\n"


home_code = extract_from_script('rebuild-editorial.py', 'new_home')
about_code = extract_from_script('make-about-2col.py', 'new_about')
work_code = extract_from_script('redesign-work.py', 'new_work')
service_code = extract_from_script('redesign-service.py', 'new_service')
experience_code = extract_from_script('redesign-experience.py', 'new_experience')
contact_code = extract_from_script('redesign-contact.py', 'new_contact')

# 3. Assemble
final_code = header + '\n' + home_code + '\n' + about_code + '\n' + work_code + '\n' + service_code + '\n' + experience_code + '\n' + contact_code + '\n'

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(final_code)

print("Pages.jsx reconstructed from source scripts.")
