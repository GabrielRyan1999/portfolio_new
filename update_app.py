import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Add import
content = content.replace("import { LetsWorkTogether } from './components/ui/lets-work-section';", "import { LetsWorkTogether } from './components/ui/lets-work-section';\nimport { ContactModal } from './components/ui/ContactModal';")

# Add state
content = content.replace("const [isDark, setIsDark] = useState(true);", "const [isDark, setIsDark] = useState(true);\n  const [isContactOpen, setIsContactOpen] = useState(false);")

# Change Hero button
hero_btn_old = """<a href="#contact" className="bg-zinc-900 text-white dark:bg-zinc-100 dark:text-zinc-900 px-6 py-2.5 rounded-full text-sm font-bold hover:bg-blue-600 dark:hover:bg-zinc-300 transition-colors shadow-lg">
                Let's Talk
              </a>"""
hero_btn_new = """<button onClick={() => setIsContactOpen(true)} className="bg-zinc-900 text-white dark:bg-zinc-100 dark:text-zinc-900 px-6 py-2.5 rounded-full text-sm font-bold hover:bg-blue-600 dark:hover:bg-zinc-300 transition-colors shadow-lg cursor-pointer">
                Let's Talk
              </button>"""
content = content.replace(hero_btn_old, hero_btn_new)

# Add ContactModal and pass state
content = content.replace("<FloatingDock />", "<FloatingDock onContactClick={() => setIsContactOpen(true)} />")
content = content.replace("<LetsWorkTogether />", "<LetsWorkTogether onContactClick={() => setIsContactOpen(true)} />")
content = content.replace("</ReactLenis>", "  <ContactModal isOpen={isContactOpen} onClose={() => setIsContactOpen(false)} />\n    </ReactLenis>")

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated App.jsx")
