with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

old_span = '<span className="text-transparent [-webkit-text-stroke:2px_#09090b] md:[-webkit-text-stroke:3px_#09090b] dark:[-webkit-text-stroke:2px_#fafafa] dark:md:[-webkit-text-stroke:3px_#fafafa]">GABRIEL</span>'
new_span = '<span className="text-transparent tracking-[0.1em] md:tracking-normal [-webkit-text-stroke:1px_#09090b] md:[-webkit-text-stroke:3px_#09090b] dark:[-webkit-text-stroke:1px_#fafafa] dark:md:[-webkit-text-stroke:3px_#fafafa]">GABRIEL</span>'
content = content.replace(old_span, new_span)

import re
# Find the div immediately inside SectionShell id="home" to add bottom padding for mobile
home_pattern = r'(<SectionShell id="home" label="/HOME" watermark="RYAN" dark=\{false\}>\s*<div className="w-full h-full flex flex-col items-center justify-center relative)( pt-16 md:pt-0)?(">\s*<div className="w-full max-w-4xl)'
# Wait, let's just find the div above the h1.
# Let's see what the container above h1 is.
h1_pattern = r'(<motion\.h1 variants=\{fadeUp\} className="relative text-center)'

content = content.replace(
    '<motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: false, amount: 0.1 }} className="w-full h-full flex items-center justify-center relative">',
    '<motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: false, amount: 0.1 }} className="w-full h-full flex items-center justify-center relative pb-28 md:pb-0">'
)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied stroke fix.")
