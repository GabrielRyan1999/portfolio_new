import re

with open('src/components/ui/dock.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<div className="w-[1px] h-6 bg-white/20 mx-1 md:mx-2"></div>',
    '<div className="w-[1px] h-6 bg-slate-300 dark:bg-white/20 mx-1 md:mx-2"></div>'
)

with open('src/components/ui/dock.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
