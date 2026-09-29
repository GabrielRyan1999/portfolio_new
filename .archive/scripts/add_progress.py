import re
with open('src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

import_old = "import { AnimatePresence } from 'framer-motion';"
import_new = "import { AnimatePresence, motion, useScroll, useSpring } from 'framer-motion';"
content = content.replace(import_old, import_new)

app_old = """function App() {
  return (
    <BrowserRouter>"""

app_new = """function App() {
  const { scrollYProgress } = useScroll();
  const scaleX = useSpring(scrollYProgress, {
    stiffness: 100,
    damping: 30,
    restDelta: 0.001
  });

  return (
    <BrowserRouter>
      <motion.div
        className="fixed top-0 left-0 right-0 h-1 md:h-1.5 bg-blue-600 origin-left z-[9999]"
        style={{ scaleX }}
      />"""

content = content.replace(app_old, app_new)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
