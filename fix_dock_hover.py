import re

with open('src/components/ui/dock.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the tooltip container
old_html = """<motion.div
                        initial={{ opacity: 0, y: -10, scale: 0.8 }}
                        animate={{ opacity: 1, y: 0, scale: 1 }}
                        exit={{ opacity: 0, y: -10, scale: 0.8 }}
                        // For mobile (bottom) it drops UP (-top-X), for desktop (top) it drops DOWN (top-14)
                        className="absolute bottom-12 md:bottom-auto md:top-14 left-1/2 -translate-x-1/2 bg-[#1a1a1a] border border-white/10 text-white rounded-xl shadow-2xl z-50 overflow-hidden flex flex-col min-w-[140px]"
                      >"""

new_html = """<motion.div
                        initial={{ opacity: 0, y: -10, scale: 0.8 }}
                        animate={{ opacity: 1, y: 0, scale: 1 }}
                        exit={{ opacity: 0, y: -10, scale: 0.8 }}
                        className="absolute bottom-full mb-2 md:mb-0 md:bottom-auto md:top-full md:mt-2 left-1/2 -translate-x-1/2 z-50 py-2"
                      >
                        <div className="bg-[#1a1a1a] border border-white/10 text-white rounded-xl shadow-2xl overflow-hidden flex flex-col min-w-[140px]">"""

content = content.replace(old_html, new_html)

# We also need to add a closing </div> for the new <div className="bg-[#1a1a1a]...">
content = content.replace(
"""                        )}
                      </motion.div>""",
"""                        )}
                        </div>
                      </motion.div>"""
)

# And fix the theme tooltip
old_theme = """<motion.div
                    initial={{ opacity: 0, y: -10, scale: 0.8 }}
                    animate={{ opacity: 1, y: 0, scale: 1 }}
                    exit={{ opacity: 0, y: -10, scale: 0.8 }}
                    className="absolute bottom-12 md:bottom-auto md:top-14 left-1/2 -translate-x-1/2 px-3 py-1.5 bg-[#1a1a1a] border border-white/10 text-white text-xs font-medium rounded-lg whitespace-nowrap shadow-xl z-50 pointer-events-none"
                  >"""

new_theme = """<motion.div
                    initial={{ opacity: 0, y: -10, scale: 0.8 }}
                    animate={{ opacity: 1, y: 0, scale: 1 }}
                    exit={{ opacity: 0, y: -10, scale: 0.8 }}
                    className="absolute bottom-full mb-4 md:mb-0 md:bottom-auto md:top-full md:mt-4 left-1/2 -translate-x-1/2 px-3 py-1.5 bg-[#1a1a1a] border border-white/10 text-white text-xs font-medium rounded-lg whitespace-nowrap shadow-xl z-50 pointer-events-none"
                  >"""
content = content.replace(old_theme, new_theme)

with open('src/components/ui/dock.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
