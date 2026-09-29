import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix justify-center
content = content.replace('justify-start pt-[18vh] md:pt-[15vh]', 'justify-center')

# Fix h1 text block
new_h1_cream = '''<h1 className="font-serif text-[18vw] md:text-[20vw] leading-[0.65] font-black text-center whitespace-nowrap text-[#F5F2EB] flex flex-col items-center">
                    <span className="block tracking-tighter">GABRIEL</span>
                    <span className="block tracking-[0.4em] ml-[0.2em] md:ml-[0.4em]">RYAN</span>
                 </h1>'''

new_h1_blue = '''<h1 className="font-serif text-[18vw] md:text-[20vw] leading-[0.65] font-black text-center whitespace-nowrap text-[#1A365D] flex flex-col items-center">
                    <span className="block tracking-tighter">GABRIEL</span>
                    <span className="block tracking-[0.4em] ml-[0.2em] md:ml-[0.4em]">RYAN</span>
                 </h1>'''

# Replace the Left Side h1
content = re.sub(
    r'<h1[^>]*text-\[#F5F2EB\][^>]*>[\s\S]*?</h1>',
    new_h1_cream,
    content
)

# Replace the Right Side h1
content = re.sub(
    r'<h1[^>]*text-\[#1A365D\][^>]*>[\s\S]*?</h1>',
    new_h1_blue,
    content
)

# Fix portrait height
content = re.sub(
    r'<div className="absolute bottom-0 w-full h-\[80vh\] md:h-\[90vh\] flex justify-center z-30 pointer-events-none">',
    '<div className="absolute bottom-0 w-full h-[100vh] flex justify-center z-30 pointer-events-none">',
    content
)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Applied exact formatting requested from previous logs.')
