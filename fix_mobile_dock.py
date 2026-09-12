import re

with open('src/components/ui/dock.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Change mobile positioning from top to bottom
content = content.replace('className="fixed top-6 md:top-5 left-1/2 -translate-x-1/2 z-[100] flex flex-col items-center"', 
                          'className="fixed bottom-6 md:bottom-auto md:top-5 left-1/2 -translate-x-1/2 z-[100] flex flex-col items-center"')

with open('src/components/ui/dock.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated dock to be at bottom on mobile")
