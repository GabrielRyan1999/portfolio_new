import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the old ScrollIndicator definition
old_indicator = """const ScrollIndicator = () => (
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
);"""

new_indicator = """import { useTransform } from 'framer-motion';

const ScrollIndicator = () => {
  const { scrollY } = useScroll();
  const opacity = useTransform(scrollY, [0, 100], [1, 0]);
  
  return (
    <motion.div 
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ delay: 1, duration: 1 }}
      style={{ opacity }}
      className="fixed bottom-6 md:bottom-8 left-1/2 -translate-x-1/2 flex flex-col items-center justify-center text-slate-400 dark:text-zinc-500 z-[999] pointer-events-none"
    >
      <span className="text-[10px] md:text-xs font-semibold tracking-[0.2em] mb-1 md:mb-2 uppercase drop-shadow-md">Scroll</span>
      <motion.div
        animate={{ y: [0, 8, 0] }}
        transition={{ duration: 1.5, repeat: Infinity, ease: "easeInOut" }}
      >
        <ChevronDown className="w-4 h-4 md:w-5 md:h-5 opacity-70 drop-shadow-md" />
      </motion.div>
    </motion.div>
  );
};"""

# Wait, `useScroll` is already imported from framer-motion in App.jsx but NOT in Pages.jsx!
# Let's add useScroll and useTransform to Pages.jsx imports.
content = content.replace(
    "import { motion, AnimatePresence } from 'framer-motion';",
    "import { motion, AnimatePresence, useScroll, useTransform } from 'framer-motion';"
)

content = content.replace(old_indicator, new_indicator)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Scroll indicator updated to fixed + fade on scroll')
