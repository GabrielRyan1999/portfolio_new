import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# The target block
target = """          {/* About Me */}
          <SectionShell id="about-me" label="/ABOUT ME" watermark="ABOUT" dark={true}>
                <motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: false, amount: 0.2 }} className="w-full max-w-6xl mx-auto flex flex-col lg:flex-row items-stretch gap-8 lg:gap-16 px-4">"""

# The replacement block with background avatars
replacement = """          {/* About Me */}
          <SectionShell id="about-me" label="/ABOUT ME" watermark="ABOUT" dark={true}>
                {/* Background Avatar Watermarks */}
                <div className="absolute inset-0 pointer-events-none z-[-1] overflow-hidden flex items-center justify-between">
                  <img src="/favicon.jpg" alt="" className="w-[300px] md:w-[500px] lg:w-[600px] opacity-[0.06] dark:opacity-[0.03] grayscale blur-[2px] -rotate-12 -translate-x-1/3 -translate-y-1/4 rounded-full" />
                  <img src="/favicon.jpg" alt="" className="w-[350px] md:w-[600px] lg:w-[700px] opacity-[0.06] dark:opacity-[0.03] grayscale blur-[2px] rotate-12 translate-x-1/4 translate-y-1/4 rounded-full" />
                </div>

                <motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: false, amount: 0.2 }} className="w-full max-w-6xl mx-auto flex flex-col lg:flex-row items-stretch gap-8 lg:gap-16 px-4 relative z-10">"""

if target in content:
    content = content.replace(target, replacement)
    with open('src/App.jsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS")
else:
    print("TARGET NOT FOUND")
