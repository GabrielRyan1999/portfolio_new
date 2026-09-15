import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add useScroll and useSpring
content = re.sub(
    r"import \{ motion, AnimatePresence \} from 'framer-motion';",
    "import { motion, AnimatePresence, useScroll, useSpring } from 'framer-motion';",
    content
)

# 2. Add hooks to App()
app_func_pattern = r"function App\(\) \{\n  const \[hasEntered, setHasEntered\] = useState\(false\);"
app_func_replacement = """function App() {
  const { scrollYProgress } = useScroll();
  const scaleX = useSpring(scrollYProgress, {
    stiffness: 100,
    damping: 30,
    restDelta: 0.001
  });

  const [hasEntered, setHasEntered] = useState(false);"""
content = re.sub(app_func_pattern, app_func_replacement, content)

# 3. Add progress bar to the return of App()
return_pattern = r"  return \(\n    <>\n      <FloatingDock"
return_replacement = """  return (
    <>
      <motion.div
        className="fixed top-0 left-0 right-0 h-1 md:h-1.5 bg-blue-600 origin-left z-[9999]"
        style={{ scaleX }}
      />
      <FloatingDock"""
content = re.sub(return_pattern, return_replacement, content)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected Scroll Progress Bar CORRECTLY")
