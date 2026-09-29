import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

scroll_indicator = """
const ScrollIndicator = () => (
  <motion.div 
    initial={{ opacity: 0 }}
    animate={{ opacity: 1 }}
    transition={{ delay: 1, duration: 1 }}
    className="absolute bottom-8 left-1/2 -translate-x-1/2 flex flex-col items-center justify-center text-slate-400 dark:text-zinc-500 z-50 pointer-events-none"
  >
    <span className="text-xs font-semibold tracking-[0.2em] mb-2 uppercase">Scroll</span>
    <motion.div
      animate={{ y: [0, 8, 0] }}
      transition={{ duration: 1.5, repeat: Infinity, ease: "easeInOut" }}
    >
      <ChevronDown className="w-5 h-5 opacity-70" />
    </motion.div>
  </motion.div>
);
"""

content = content.replace("ChevronRight, ExternalLink, Plus } from 'lucide-react';", "ChevronRight, ChevronDown, ExternalLink, Plus } from 'lucide-react';")
content = content.replace("export const PageTransition", scroll_indicator + "\nexport const PageTransition")

# Let's add <ScrollIndicator /> to the bottom of the About Me SectionShell
content = content.replace(
    '          {/* Left: Personal Story */}',
    '          <ScrollIndicator />\n          {/* Left: Personal Story */}'
)

# And for Experience:
# Search for id="experience" and add ScrollIndicator inside it
content = content.replace(
    '          {/* 4. Experience (Dark) */}',
    '          {/* 4. Experience (Dark) */}'
)
# Wait, let's inject it into Experience SectionShell
content = content.replace(
    '<SectionShell id="experience" label="/EXPERIENCE" watermark="EXPERIENCE" dark={false} footer={',
    '<SectionShell id="experience" label="/EXPERIENCE" watermark="EXPERIENCE" dark={false} footer={'
)
# Better: Just put it right before the mapping of experienceJobs
content = content.replace(
    '{experienceJobs.map((job, i) => (',
    '<ScrollIndicator />\n                {experienceJobs.map((job, i) => ('
)


with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
