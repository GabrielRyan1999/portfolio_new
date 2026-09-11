import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Add Plus to lucide-react imports
if 'Plus' not in content:
    content = content.replace("ExternalLink } from 'lucide-react';", "ExternalLink, Plus } from 'lucide-react';")

# Update the button content
old_btn_content = """                          <motion.span layout="position" className="text-2xl md:text-5xl font-black">
                            {service.title}
                          </motion.span>
                          <motion.span
                            animate={{ rotate: isOpen ? 135 : 0 }}
                            transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
                          >
                            <ArrowUpRight className="w-8 h-8" />
                          </motion.span>"""

new_btn_content = """                          <motion.div layout="position" className="flex items-center gap-4 md:gap-8">
                            <span className="text-sm md:text-xl text-slate-400 dark:text-zinc-500 font-mono font-bold">
                              0{index + 1}
                            </span>
                            <span className="text-2xl md:text-4xl lg:text-5xl font-black text-left">
                              {service.title}
                            </span>
                          </motion.div>
                          <motion.span
                            animate={{ rotate: isOpen ? 45 : 0 }}
                            transition={{ duration: 0.3, ease: "easeInOut" }}
                            className="flex items-center justify-center w-10 h-10 md:w-12 md:h-12 rounded-full bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-300 group-hover:bg-blue-600 group-hover:text-white transition-colors"
                          >
                            <Plus className="w-6 h-6 md:w-8 md:h-8" />
                          </motion.span>"""

# We should also add 'group' to the button className for the hover effect
old_btn_class = """                          className={`w-full flex items-center justify-between py-6 md:py-8 px-4 rounded-3xl transition-colors duration-300 ${
                            isOpen ? "bg-[var(--card)] border-[var(--card-border)] text-slate-900 dark:text-zinc-100" : "bg-transparent text-slate-300"
                          }`}"""

new_btn_class = """                          className={`group w-full flex items-center justify-between py-6 md:py-8 px-4 rounded-3xl transition-all duration-300 hover:px-6 ${
                            isOpen ? "bg-[var(--card)] border-[var(--card-border)] text-slate-900 dark:text-zinc-100 shadow-xl shadow-slate-200/50 dark:shadow-none" : "bg-transparent text-slate-400 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-zinc-800/50"
                          }`}"""

content = content.replace(old_btn_content, new_btn_content)
content = content.replace(old_btn_class, new_btn_class)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
