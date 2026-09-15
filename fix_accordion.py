import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace the mapping function for the service accordion
target_pattern = r"""                \].map\(\(service, index\) => \{
                  const isOpen = activeServiceIndex === index;
                  return \(
                    <motion\.div key=\{service\.title\} layout variants=\{fadeUp\} className="overflow-hidden">
                      <motion\.button
                          layout
                          onClick=\{\(\) => setActiveServiceIndex\(isOpen \? null : index\)\}
                          className=\{\`group w-full flex items-center justify-between py-6 md:py-8 px-4 rounded-3xl transition-all duration-300 hover:px-6 \$\{
                            isOpen \? "bg-\[var\(--card\)\] border-\[var\(--card-border\)\] text-slate-900 dark:text-zinc-100 shadow-xl shadow-slate-200/50 dark:shadow-none" : "bg-transparent text-slate-400 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-zinc-800/50"
                          \}\`\}
                        >
                          <motion\.div layout="position" className="flex items-center gap-4 md:gap-8">
                            <span className="text-sm md:text-xl text-slate-400 dark:text-zinc-500 font-mono font-bold">
                              0\{index \+ 1\}
                            </span>
                            <span className="text-2xl md:text-4xl lg:text-5xl font-black text-left group-hover:text-blue-600 transition-colors">
                              \{service\.title\}
                            </span>
                          </motion\.div>
                          <motion\.span
                            animate=\{\{ rotate: isOpen \? 45 : 0 \}\}
                            transition=\{\{ duration: 0\.3, ease: "easeInOut" \}\}
                            className="flex items-center justify-center w-10 h-10 md:w-12 md:h-12 rounded-full bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-300 group-hover:bg-blue-600 group-hover:text-white transition-colors shrink-0"
                          >
                            <Plus className="w-6 h-6 md:w-8 md:h-8" />
                          </motion\.span>
                        </motion\.button>
          
                      <AnimatePresence initial=\{false\}>
                        \{isOpen && \(
                          <motion\.div
                            key="content"
                            initial=\{\{ height: 0, opacity: 0 \}\}
                            animate=\{\{ height: "auto", opacity: 1 \}\}
                            exit=\{\{ height: 0, opacity: 0 \}\}
                            transition=\{\{ duration: 0\.4, ease: \[0\.16, 1, 0\.3, 1\] \}\}
                            className="bg-\[var\(--card\)\] border-\[var\(--card-border\)\] text-slate-900 dark:text-zinc-100 rounded-b-3xl px-4 md:px-8"
                          >
                            <div className="pb-8 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">"""

replacement = """                ].map((service, index) => {
                  const isOpen = activeServiceIndex === index;
                  return (
                    <motion.div 
                      key={service.title} 
                      layout 
                      variants={fadeUp} 
                      className={`overflow-hidden transition-all duration-300 rounded-3xl border border-transparent ${
                        isOpen 
                          ? "bg-[var(--card)] !border-[var(--card-border)] shadow-xl shadow-slate-200/50 dark:shadow-none" 
                          : "bg-transparent"
                      }`}
                    >
                      <motion.button
                          layout
                          onClick={() => setActiveServiceIndex(isOpen ? null : index)}
                          className={`group w-full flex items-center justify-between py-6 md:py-8 px-4 md:px-8 transition-colors ${
                            isOpen ? "text-slate-900 dark:text-zinc-100" : "text-slate-400 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-zinc-800/50"
                          }`}
                        >
                          <motion.div layout="position" className="flex items-center gap-4 md:gap-8">
                            <span className="text-sm md:text-xl text-slate-400 dark:text-zinc-500 font-mono font-bold">
                              0{index + 1}
                            </span>
                            <span className="text-2xl md:text-4xl lg:text-5xl font-black text-left group-hover:text-blue-600 transition-colors">
                              {service.title}
                            </span>
                          </motion.div>
                          <motion.span
                            animate={{ rotate: isOpen ? 45 : 0 }}
                            transition={{ duration: 0.3, ease: "easeInOut" }}
                            className="flex items-center justify-center w-10 h-10 md:w-12 md:h-12 rounded-full bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-300 group-hover:bg-blue-600 group-hover:text-white transition-colors shrink-0"
                          >
                            <Plus className="w-6 h-6 md:w-8 md:h-8" />
                          </motion.span>
                        </motion.button>
          
                      <AnimatePresence initial={false}>
                        {isOpen && (
                          <motion.div
                            key="content"
                            initial={{ height: 0, opacity: 0 }}
                            animate={{ height: "auto", opacity: 1 }}
                            exit={{ height: 0, opacity: 0 }}
                            transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
                            className="text-slate-900 dark:text-zinc-100 px-4 md:px-8"
                          >
                            <div className="pb-8 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">"""

new_content = re.sub(target_pattern, replacement, content)

if new_content == content:
    print("Regex failed to match!")
else:
    with open('src/App.jsx', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Accordion fixed")
