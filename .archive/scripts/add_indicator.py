import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Add a generic scroll indicator component before export const PageTransition
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

# import ChevronDown
content = content.replace("ChevronRight, ExternalLink, Plus } from 'lucide-react';", "ChevronRight, ChevronDown, ExternalLink, Plus } from 'lucide-react';")

content = content.replace("export const PageTransition", scroll_indicator + "\nexport const PageTransition")

# Now inject <ScrollIndicator /> right before the first </SectionShell> in About and Experience.
# We can just do a regex replace for the About and Experience components.

# For About:
# Find: export function About() { ... return ( ... <div className="pt-20"> ... {about_jsx} ... </div> ... )
# Wait, about_jsx is just a string, it's already rendered into the file!
# Let's see how About looks right now.
