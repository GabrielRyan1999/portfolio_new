import re

with open('src/components/ui/lets-work-section.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Change function signature
content = content.replace("export function LetsWorkTogether() {", "export function LetsWorkTogether({ onContactClick }) {")

# We will just replace the whole form block with a button.
form_pattern = r'<form[\s\S]*?</form>'
button_replacement = """<div className="flex flex-col items-center md:items-start justify-center h-full space-y-6">
                 <p className="text-slate-500 dark:text-zinc-400 text-lg md:text-xl font-medium max-w-md">
                   Have a project in mind or want to explore an opportunity? I'm currently open for new collaborations.
                 </p>
                 <button 
                   onClick={onContactClick}
                   className="bg-blue-600 hover:bg-blue-700 text-white rounded-full px-8 py-4 flex items-center justify-center gap-3 text-lg font-bold transition-all shadow-xl shadow-blue-600/20 hover:scale-105"
                 >
                   Open Contact Form <ArrowUpRight className="w-5 h-5" />
                 </button>
               </div>"""

content = re.sub(form_pattern, button_replacement, content)

# Remove unused imports
content = content.replace('import { useForm, ValidationError } from "@formspree/react"\n', '')

# Remove unused state variables
state_vars = r'  const \[state, handleFormSubmit\] = useForm\("xgaekynq"\)\n'
content = re.sub(state_vars, '', content)

with open('src/components/ui/lets-work-section.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated lets-work-section.jsx")
