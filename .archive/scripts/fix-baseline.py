import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace AnimatedWords
old_comp = r'const AnimatedWords = \(\{ words \}\) => \{.*?^\};'
new_comp = '''const AnimatedWords = ({ words }) => {
  const [index, setIndex] = useState(0);
  useEffect(() => {
    const timer = setInterval(() => {
      setIndex((prev) => (prev + 1) % words.length);
    }, 2500);
    return () => clearInterval(timer);
  }, [words]);
  
  return (
    <span className="relative inline-block min-w-[200px]">
      {/* Invisible placeholder to guarantee perfect baseline alignment and height */}
      <span className="opacity-0 pointer-events-none select-none">{words[1]}</span>
      <AnimatePresence mode="popLayout">
        <motion.span
          key={index}
          initial={{ y: 15, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          exit={{ y: -15, opacity: 0 }}
          transition={{ duration: 0.5, ease: "anticipate" }}
          className="absolute top-0 left-0 text-[#D1C4B5]"
        >
          {words[index]}
        </motion.span>
      </AnimatePresence>
    </span>
  );
};'''
content = re.sub(old_comp, new_comp, content, flags=re.MULTILINE|re.DOTALL)

# Fix the container
old_container = r'<span className="flex items-center">\s*EDUCATOR & <AnimatedWords words=\{\[\'DEVELOPER\.\', \'SYSTEM BUILDER\.\', \'MENTOR\.\'\]\} />\s*</span>'
new_container = '''<span className="inline-flex items-baseline gap-2">
             <span>EDUCATOR &</span>
             <AnimatedWords words={['DEVELOPER.', 'SYSTEM BUILDER.', 'MENTOR.']} />
           </span>'''
content = re.sub(old_container, new_container, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed baseline alignment.')
