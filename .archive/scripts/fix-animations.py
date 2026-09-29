import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Revert ParallaxImage back to standard <img>
old_work_img = r'<ParallaxImage\s+src=\{workProjects\[workIndex\]\.img\}\s+alt=\{workProjects\[workIndex\]\.title\}\s+className="grayscale contrast-125 mix-blend-luminosity opacity-80 group-hover:grayscale-0 group-hover:mix-blend-normal group-hover:opacity-100 transition-all duration-700"\s+\/>'
new_work_img = '''<img 
  src={workProjects[workIndex].img} 
  alt={workProjects[workIndex].title}
  className="w-full h-full object-cover object-center grayscale contrast-125 mix-blend-luminosity opacity-80 group-hover:grayscale-0 group-hover:mix-blend-normal group-hover:opacity-100 transition-all duration-700" 
/>'''
content = re.sub(old_work_img, new_work_img, content)

# 2. Fix RevealLine (Use standard Y translation and fade, no overflow-hidden clipping which might be breaking it)
old_reveal = r'export function RevealLine\(\{ children, delay = 0, className = "" \}\) \{[\s\S]*?return \([\s\S]*?<\/div>\s*\);\s*\}'
new_reveal = '''export function RevealLine({ children, delay = 0, className = "" }) {
  return (
    <motion.span
      initial={{ opacity: 0, y: 30 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, amount: 0.3 }}
      transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1], delay }}
      className={`inline-block ${className}`}
    >
      {children}
    </motion.span>
  );
}'''
content = re.sub(old_reveal, new_reveal, content)

# 3. Fix LineDraw (Fix viewport syntax and origin)
old_linedraw = r'export function LineDraw\(\{ className, delay = 0 \}\) \{[\s\S]*?return \([\s\S]*?\/>\s*\);\s*\}'
new_linedraw = '''export function LineDraw({ className, delay = 0 }) {
  return (
    <motion.div
      initial={{ scaleX: 0 }}
      whileInView={{ scaleX: 1 }}
      viewport={{ once: true, amount: 0.1 }}
      transition={{ duration: 1.5, ease: [0.16, 1, 0.3, 1], delay }}
      style={{ transformOrigin: "left" }}
      className={className}
    />
  );
}'''
content = re.sub(old_linedraw, new_linedraw, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Reverted Parallax, fixed RevealLine and LineDraw.')
