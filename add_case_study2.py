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

# The Work component ends right before export function Service()
# Wait, let's find the closing </PageTransition> of Work().
# Let's extract the Work component:
work_match = re.search(r'(export function Work\(\) \{.*?\n  \);\n\})', content, re.DOTALL)
if work_match:
    work_code = work_match.group(1)
    # Inside work_code, replace the last </PageTransition> with the case_study_jsx + \n    </PageTransition>
    new_work_code = work_code.replace('    </PageTransition>\n  );\n}', case_study_jsx + '    </PageTransition>\n  );\n}')
    content = content.replace(work_code, new_work_code)
    
with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
