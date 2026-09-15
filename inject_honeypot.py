import re

with open('src/components/ui/lets-work-section.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

target = """                 <div>
                   <input 
                     type="email\""""

honeypot = """                 {/* Formspree Honeypot for Anti-Spam */}
                 <input type="text" name="_gotcha" style={{ display: 'none' }} />
                 
                 <div>
                   <input 
                     type="email\""""

content = content.replace(target, honeypot)

with open('src/components/ui/lets-work-section.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Honeypot injected")
