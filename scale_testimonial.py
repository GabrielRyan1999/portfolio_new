import re

with open('src/components/ui/unique-testimonial.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Container Size
content = content.replace(
    'className="relative w-full max-w-xl h-[320px] md:h-[280px] flex justify-center items-center perspective-1000 mt-10"',
    'className="relative w-full max-w-4xl h-[380px] md:h-[350px] lg:h-[450px] flex justify-center items-center perspective-1000 mt-10 md:mt-20"'
)

# 2. Update Card padding
content = content.replace(
    'p-8 md:p-10 shadow-2xl flex flex-col justify-between',
    'p-8 md:p-12 lg:p-16 shadow-2xl flex flex-col justify-between'
)

# 3. Update Quote Icon Size and Position
content = content.replace(
    '<Quote className="w-12 h-12 text-blue-600/30 absolute -top-4 -left-4 md:-top-2 md:-left-2 rotate-180" />',
    '<Quote className="w-16 h-16 md:w-24 md:h-24 lg:w-32 lg:h-32 text-blue-600/20 absolute -top-4 -left-4 md:-top-6 md:-left-6 rotate-180" />'
)

# 4. Update Quote Text Size
content = content.replace(
    '<p className="text-lg md:text-xl text-slate-200 dark:text-zinc-200 font-medium leading-relaxed mt-6 relative z-10">',
    '<p className="text-lg md:text-2xl lg:text-4xl text-slate-200 dark:text-zinc-200 font-medium leading-relaxed mt-6 relative z-10">'
)

# 5. Update Author Text Size
content = content.replace(
    '<p className="text-white dark:text-white font-bold text-lg md:text-xl">{card.author}</p>',
    '<p className="text-white dark:text-white font-bold text-xl md:text-2xl lg:text-3xl">{card.author}</p>'
)

# 6. Update Role Text Size
content = content.replace(
    '<p className="text-blue-400 dark:text-blue-400 font-mono text-sm uppercase tracking-wider mt-1">{card.role}</p>',
    '<p className="text-blue-400 dark:text-blue-400 font-mono text-sm md:text-base uppercase tracking-wider mt-1 md:mt-2">{card.role}</p>'
)

# 7. Update Stack y offset and scale (we need cards to peek out more visually since they are bigger)
# Since they are taller, index * -25 might be too tight. Let's use -35 on mobile, -50 on desktop.
# Framer Motion doesn't support responsive classes in `animate`, so we'll just use a slightly bigger static number.
content = content.replace(
    'y: index * -25, // Stack cards upwards',
    'y: index * -35, // Stack cards upwards'
)

with open('src/components/ui/unique-testimonial.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Testimonial scaled up")
