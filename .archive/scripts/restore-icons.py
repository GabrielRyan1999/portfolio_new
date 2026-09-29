import re

with open('src/components/ui/lets-work-section.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the text-based social links with Icon-based ones
old_socials = r'<div className="flex flex-row gap-8 my-4 md:my-0">\s*<a href="https:\/\/www\.linkedin\.com\/in\/gabrielryan1999\/" target="_blank" rel="noreferrer" className="hover:text-\[#F5F2EB\] transition-colors">LinkedIn<\/a>\s*<a href="https:\/\/github\.com\/GabrielRyan1999" target="_blank" rel="noreferrer" className="hover:text-\[#F5F2EB\] transition-colors">GitHub<\/a>\s*<a href="https:\/\/www\.instagram\.com\/heyitsgabrielryan\/" target="_blank" rel="noreferrer" className="hover:text-\[#F5F2EB\] transition-colors">Instagram<\/a>\s*<\/div>'

new_socials = '''<div className="flex flex-row items-center gap-8 my-4 md:my-0">
            <a href="https://www.linkedin.com/in/gabrielryan1999/" target="_blank" rel="noreferrer" aria-label="LinkedIn" className="hover:text-[#F5F2EB] transition-transform hover:scale-110">
               <Linkedin className="w-5 h-5" />
            </a>
            <a href="https://github.com/GabrielRyan1999" target="_blank" rel="noreferrer" aria-label="GitHub" className="hover:text-[#F5F2EB] transition-transform hover:scale-110">
               <Github className="w-5 h-5" />
            </a>
            <a href="https://www.instagram.com/heyitsgabrielryan/" target="_blank" rel="noreferrer" aria-label="Instagram" className="hover:text-[#F5F2EB] transition-transform hover:scale-110">
               <Instagram className="w-5 h-5" />
            </a>
          </div>'''

content = re.sub(old_socials, new_socials, content, flags=re.DOTALL)

with open('src/components/ui/lets-work-section.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Restored social icons in footer.')
