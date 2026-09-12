import re

with open('src/components/ui/dock.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change root container position to bottom on mobile, top on desktop
content = content.replace(
    'className="fixed top-6 md:top-5 left-1/2 -translate-x-1/2 z-[100] flex flex-col items-center"',
    'className="fixed bottom-6 md:bottom-auto md:top-5 left-1/2 -translate-x-1/2 z-[100] flex flex-col items-center"'
)

# 2. Make gap smaller on mobile to prevent overflow
content = content.replace(
    'className={`flex items-center gap-2 md:gap-3',
    'className={`flex items-center gap-1 md:gap-3'
)

# 3. Make buttons slightly smaller on mobile
content = content.replace(
    'w-10 h-10 md:w-12 md:h-12',
    'w-9 h-9 md:w-12 md:h-12'
)

# 4. Move tooltips UP on mobile (-top-10), DOWN on desktop (md:top-14)
content = content.replace(
    'className="absolute top-14 left-1/2',
    'className="absolute -top-10 md:top-14 left-1/2'
)

# 5. Make the animation for Menu button slide from bottom instead of top
content = content.replace(
    'initial={{ opacity: 0, scale: 0.8, y: -20 }}',
    'initial={{ opacity: 0, scale: 0.8, y: 20 }}'
).replace(
    'exit={{ opacity: 0, scale: 0.8, y: -20 }}',
    'exit={{ opacity: 0, scale: 0.8, y: 20 }}'
)

with open('src/components/ui/dock.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated dock for mobile")
