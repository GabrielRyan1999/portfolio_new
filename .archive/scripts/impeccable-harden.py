import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add aria-expanded to the accordion button
# The button currently looks like:
# <button
#     onClick={() => setActiveServiceIndex(isOpen ? null : index)}
#     className="w-full flex items-center justify-between py-8 px-6 md:px-12 text-left group hover:bg-[#1A365D] hover:text-[#F5F2EB] transition-colors"
# >

old_button = r'<button\s*onClick=\{([^}]+)\}\s*className="([^"]+)"\s*>'
new_button = r'<button\n                        onClick={\1}\n                        aria-expanded={isOpen}\n                        aria-controls={`service-panel-${index}`}\n                        id={`service-button-${index}`}\n                        className="\2"\n                    >'
content = re.sub(old_button, new_button, content)

# 2. Add id to the accordion panel
# The panel currently looks like:
# <motion.div
#   initial="collapsed"

old_panel = r'<motion\.div\s*initial="collapsed"'
new_panel = r'<motion.div\n                        id={`service-panel-${index}`}\n                        aria-labelledby={`service-button-${index}`}\n                        initial="collapsed"'
content = re.sub(old_panel, new_panel, content)

# 3. Add loading="lazy" to images
# There are two img tags.
# Home image: <img src="/favicon.jpg" alt="Gabriel Ryan Thumbnail" className="..."/>
# Services images: <img src={img} alt="" className="..."/>
content = content.replace('<img src="/favicon.jpg"', '<img src="/favicon.jpg" loading="lazy"')
content = content.replace('src={img}\n                                  alt=""', 'src={img}\n                                  alt=""\n                                  loading="lazy"')

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Harden (ARIA and Lazy Loading) applied to Pages.jsx")
