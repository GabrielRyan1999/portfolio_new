import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove <LetsWorkTogether /> from Home, About, Work, Service, Experience
# (Keep it only in Contact)
# Because I appended `<LetsWorkTogether />` right before `</PageTransition>`, I can replace `<LetsWorkTogether />\n    </PageTransition>` with just `</PageTransition>`.
# Wait, let's replace `<LetsWorkTogether />` with `<GlobalFooter />`!

global_footer_jsx = """
const GlobalFooter = () => (
  <div className="w-full max-w-7xl mx-auto px-6 md:px-8 lg:px-12 pb-8 pt-4">
    <div className="flex flex-col md:flex-row items-center justify-between w-full border-t border-slate-200/20 pt-6 text-slate-500 dark:text-zinc-500 dark:text-zinc-400 z-10 relative">
      <div className="text-sm font-medium text-center md:text-left">
        &copy; {new Date().getFullYear()} Gabriel Ryan.<br className="block md:hidden"/> All rights reserved.
      </div>
      <div className="flex flex-row gap-6 my-4 md:my-0">
        <a href="https://www.linkedin.com/in/gabrielryan1999/" target="_blank" rel="noreferrer" aria-label="LinkedIn" className="hover:text-blue-600 transition-colors"><Linkedin className="w-5 h-5" /></a>
        <a href="https://github.com/GabrielRyan1999" target="_blank" rel="noreferrer" aria-label="GitHub" className="hover:text-slate-900 dark:hover:text-zinc-100 transition-colors"><Github className="w-5 h-5" /></a>
        <a href="https://www.instagram.com/heyitsgabrielryan/" target="_blank" rel="noreferrer" aria-label="Instagram" className="hover:text-pink-600 transition-colors"><Instagram className="w-5 h-5" /></a>
      </div>
      <div className="text-sm text-center md:text-right hidden md:block">
        Created with 💙 by Ryan
      </div>
    </div>
  </div>
);
"""

# Insert GlobalFooter component definition before export const PageTransition
content = content.replace("export const PageTransition", global_footer_jsx + "\nexport const PageTransition")

# 2. Replace <LetsWorkTogether /> with <GlobalFooter /> in Home, About, Work, Service, Experience.
# We will do this carefully by targeting the specific component functions.
pages_to_update = ['Home', 'About', 'Work', 'Service', 'Experience']

for page in pages_to_update:
    # Find the function block
    pattern = r'(export function ' + page + r'\(\) \{.*?)<LetsWorkTogether />(.*?\})'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        content = content.replace(match.group(0), match.group(1) + '<GlobalFooter />' + match.group(2))

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("Replaced LetsWorkTogether with GlobalFooter on pages.")
