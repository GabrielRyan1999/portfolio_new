import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

watermark_block = r"""                \{\/\* Background Avatar Watermarks \*\/\}\n                <div className="absolute inset-0 pointer-events-none z-\[0\] overflow-hidden flex items-center justify-between opacity-\[0\.05\] dark:opacity-\[0\.03\] grayscale">\n                  <img src="/favicon\.jpg" alt="" className="w-\[300px\] md:w-\[500px\] lg:w-\[600px\] blur-\[2px\] -rotate-12 -translate-x-1/3 -translate-y-1/4 rounded-full" />\n                  <img src="/favicon\.jpg" alt="" className="w-\[350px\] md:w-\[600px\] lg:w-\[700px\] blur-\[2px\] rotate-12 translate-x-1/4 translate-y-1/4 rounded-full" />\n                </div>\n"""

# Remove from Hero
content = re.sub(watermark_block, "", content)

# Add to About Me
about_me_target = r"""          <SectionShell id="about-me" label="/ABOUT ME" watermark="ABOUT" dark=\{true\}>\n"""
about_me_replacement = """          <SectionShell id="about-me" label="/ABOUT ME" watermark="ABOUT" dark={true}>
              {/* Background Avatar Watermarks */}
              <div className="absolute inset-0 pointer-events-none z-[0] overflow-hidden flex items-center justify-between opacity-[0.06] dark:opacity-[0.03] grayscale">
                <img src="/favicon.jpg" alt="" className="w-[300px] md:w-[500px] lg:w-[600px] blur-[2px] -rotate-12 -translate-x-1/3 -translate-y-1/4 rounded-full" />
                <img src="/favicon.jpg" alt="" className="w-[350px] md:w-[600px] lg:w-[700px] blur-[2px] rotate-12 translate-x-1/4 translate-y-1/4 rounded-full" />
              </div>\n"""

content = re.sub(about_me_target, about_me_replacement, content)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Moved watermarks back to About Me")
