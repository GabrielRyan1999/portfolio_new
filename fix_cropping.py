import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

target = r"""              \{\/\* Background Avatar Watermarks \*\/\}\n              <div className="absolute inset-0 pointer-events-none z-\[0\] overflow-hidden flex items-center justify-between opacity-\[0\.06\] dark:opacity-\[0\.03\] grayscale">\n                <img src="/favicon\.jpg" alt="" className="w-\[300px\] md:w-\[500px\] lg:w-\[600px\] blur-\[2px\] -rotate-12 -translate-x-1/3 -translate-y-1/4 rounded-full" />\n                <img src="/favicon\.jpg" alt="" className="w-\[350px\] md:w-\[600px\] lg:w-\[700px\] blur-\[2px\] rotate-12 translate-x-1/4 translate-y-1/4 rounded-full" />\n              </div>"""

replacement = """              {/* Background Avatar Watermarks */}
              <div className="absolute inset-0 pointer-events-none z-[0] overflow-hidden">
                <img src="/favicon.jpg" alt="" className="absolute top-10 md:top-20 -left-4 md:left-0 w-[250px] md:w-[400px] lg:w-[500px] blur-[2px] -rotate-12 rounded-full opacity-[0.05] dark:opacity-[0.03] grayscale" />
                <img src="/favicon.jpg" alt="" className="absolute bottom-10 md:bottom-32 -right-4 md:right-0 w-[280px] md:w-[450px] lg:w-[600px] blur-[2px] rotate-12 rounded-full opacity-[0.05] dark:opacity-[0.03] grayscale" />
              </div>"""

if re.search(target, content):
    content = re.sub(target, replacement, content)
    with open('src/App.jsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS")
else:
    print("FAILED")
