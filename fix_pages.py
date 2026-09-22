import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the old duplicate Case Study
# The old one doesn't have an ID.
old_case_study = """          {/* Case Study */}
          <SectionShell label="/CASE STUDY" watermark="SYSTEM" dark={false}>
              <motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: false, amount: 0.3 }} className="w-full max-w-7xl mx-auto z-10">
                 <motion.div variants={fadeUp}>
                    <MentorReportingFeatures />
                 </motion.div>
              </motion.div>
          </SectionShell>"""
          
content = content.replace(old_case_study, "")

# 2. Add LetsWorkTogether (Footer) to the bottom of all pages except Contact
# Contact already has it.
# We will replace `</PageTransition>` with `<LetsWorkTogether />\n    </PageTransition>` for Home, About, Work, Service, Experience

pages_to_update = ['Home', 'About', 'Work', 'Service', 'Experience']

for page in pages_to_update:
    # Use regex to find the specific component and replace its last </PageTransition>
    pattern = r'(export function ' + page + r'\(\) \{.*?)(\s*</PageTransition>\s*\)\s*;?\s*\})'
    
    match = re.search(pattern, content, re.DOTALL)
    if match:
        new_component = match.group(1) + '\n      <LetsWorkTogether />' + match.group(2)
        content = content.replace(match.group(0), new_component)


with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("Duplicate Case Study removed and Footer added to all pages.")
