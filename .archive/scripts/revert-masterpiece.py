import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Restore the elegant Masterpiece Typography (tight tracking, elegant line-height)
# Left Side
content = re.sub(
    r'<h1 className="font-serif text-\[18vw\] md:text-\[20vw\] leading-\[0\.65\] font-black text-center whitespace-nowrap text-\[#F5F2EB\] flex flex-col items-center">\s*<span className="block tracking-tighter">GABRIEL</span>\s*<span className="block tracking-\[0\.4em\] ml-\[0\.2em\] md:ml-\[0\.4em\]">RYAN</span>\s*</h1>',
    r'''<h1 className="font-serif text-[18vw] md:text-[20vw] leading-[0.85] tracking-tighter font-black text-center whitespace-nowrap text-[#F5F2EB]">
                    <span className="block">GABRIEL</span>
                    <span className="block">RYAN</span>
                 </h1>''',
    content
)

# Right Side
content = re.sub(
    r'<h1 className="font-serif text-\[18vw\] md:text-\[20vw\] leading-\[0\.65\] font-black text-center whitespace-nowrap text-\[#1A365D\] flex flex-col items-center">\s*<span className="block tracking-tighter">GABRIEL</span>\s*<span className="block tracking-\[0\.4em\] ml-\[0\.2em\] md:ml-\[0\.4em\]">RYAN</span>\s*</h1>',
    r'''<h1 className="font-serif text-[18vw] md:text-[20vw] leading-[0.85] tracking-tighter font-black text-center whitespace-nowrap text-[#1A365D]">
                    <span className="block">GABRIEL</span>
                    <span className="block">RYAN</span>
                 </h1>''',
    content
)


# 2. Restore the Portrait scale so it breathes better
content = re.sub(
    r'<div className="absolute bottom-0 w-full h-\[100vh\] flex justify-center z-30 pointer-events-none">',
    r'<div className="absolute bottom-0 w-full h-[85vh] md:h-[90vh] flex justify-center z-30 pointer-events-none">',
    content
)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Restored Masterpiece typography and portrait scale.')
