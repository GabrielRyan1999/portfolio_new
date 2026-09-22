import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract classroom
classroom_match = re.search(r'(<SectionShell label="/CLASSROOM".*?</SectionShell>)', content, re.DOTALL)
if classroom_match:
    classroom_jsx = classroom_match.group(1)
    
    # Add id="classroom" if it doesn't have one
    if 'id="classroom"' not in classroom_jsx:
        classroom_jsx_modified = classroom_jsx.replace('label="/CLASSROOM"', 'id="classroom" label="/CLASSROOM"')
    else:
        classroom_jsx_modified = classroom_jsx
        
    # Remove from About
    content = content.replace(classroom_jsx, '')
    
    # Inject into Work
    # Find the end of the Work section (which is right before </PageTransition> in the Work component)
    # The Work component is:
    # export function Work() {
    #   ...
    #   return (
    #     <PageTransition>
    #       <SectionShell id="work" ...>
    #       </SectionShell>
    #     </PageTransition>
    #   )
    # }
    
    # Let's just find the Work component's SectionShell and append it.
    work_shell_match = re.search(r'(export function Work\(\).*?<SectionShell id="work".*?</SectionShell>)', content, re.DOTALL)
    if work_shell_match:
        content = content.replace(work_shell_match.group(1), work_shell_match.group(1) + '\n\n' + classroom_jsx_modified)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
