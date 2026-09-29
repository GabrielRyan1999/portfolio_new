import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

case_study_jsx = """

            {/* Case Study */}
            <SectionShell id="case-study" label="/CASE STUDY" watermark="SYSTEM" dark={false}>
                <motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: false, amount: 0.3 }} className="w-full max-w-7xl mx-auto z-10">
                   <motion.div variants={fadeUp}>
                      <MentorReportingFeatures />
                   </motion.div>
                </motion.div>
            </SectionShell>
"""

# Append case_study_jsx right before the closing </PageTransition> in the Work component
# Find the exact spot
work_shell_match = re.search(r'(export function Work\(\).*?</SectionShell>\s*</SectionShell>)', content, re.DOTALL)
if work_shell_match:
    content = content.replace(work_shell_match.group(1), work_shell_match.group(1) + case_study_jsx)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
