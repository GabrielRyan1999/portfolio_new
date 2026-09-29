import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the Background of the Home section
# We'll remove the split Navy/Cream background and just use a solid grainy Cream for the whole section.
old_home_bg = r'<section id="home" className="relative min-h-screen w-full bg-\[#F5F2EB\] text-\[#1A365D\] overflow-hidden">'
new_home_bg = '''<section id="home" className="relative min-h-screen w-full bg-[#EBE7DF] text-[#1a1a1a] overflow-hidden">
        {/* SVG Filter for Halftone Effect */}
        <svg width="0" height="0" className="hidden">
          <filter id="bitmap">
            <feColorMatrix type="matrix" values="0.2126 0.7152 0.0722 0 0  0.2126 0.7152 0.0722 0 0  0.2126 0.7152 0.0722 0 0  0 0 0 1 0" result="gray" />
            <feComponentTransfer in="gray" result="highContrast">
              <feFuncR type="linear" slope="3" intercept="-1" />
              <feFuncG type="linear" slope="3" intercept="-1" />
              <feFuncB type="linear" slope="3" intercept="-1" />
            </feComponentTransfer>
          </filter>
        </svg>'''
content = re.sub(old_home_bg, new_home_bg, content)

# Remove the left Navy block
content = re.sub(r'\{\/\* 1\. Deep Navy Color Block \(Left 45%\) \*\/\}[\s\S]*?z-0 pointer-events-none"><\/div>', '', content)

# Remove the bottom right Navy block
content = re.sub(r'\{\/\* Bottom Right Navy Block \*\/\}[\s\S]*?<\/div>\s*<\/div>\s*<\/div>', '', content)

# 2. Re-arrange Giant Typography
# Top Center "GABRIEL", Bottom Left "RYAN"
old_typography = r'\{\/\* 4\. Giant Typography \(Strictly BEHIND subject for 3D Magazine effect\) \*\/\}[\s\S]*?\{\/\* 5\. The Subject \(Portrait - Strictly IN FRONT of text\) \*\/\}'

new_typography = '''{/* 4. Giant Typography (Strictly BEHIND subject for 3D Magazine effect) */}
        <div className="absolute inset-0 z-20 pointer-events-none flex flex-col justify-between py-12">
           
           {/* Top Text: GABRIEL (Split Color) */}
           <div className="w-full text-center">
               <h1 className="font-serif text-[20vw] leading-[0.8] tracking-tighter font-black whitespace-nowrap">
                  <span className="text-[#1a1a1a]">GAB</span>
                  <span className="text-[#8B1515]">RIEL</span>
               </h1>
           </div>

           {/* Bottom Text: RYAN */}
           <div className="w-full text-left pl-8 md:pl-16 mb-12">
               <h1 className="font-serif text-[18vw] leading-[0.8] tracking-tighter font-black whitespace-nowrap text-[#F5F2EB]" style={{ WebkitTextStroke: "2px #1a1a1a" }}>
                  RYAN
               </h1>
           </div>
        </div>

        {/* 5. The Subject (Portrait - Strictly IN FRONT of text) */}'''
content = re.sub(old_typography, new_typography, content)

# 3. Apply Bitmap/Halftone effect to the Subject
old_subject = r'<img src="\/profile-nobg\.png" alt="Gabriel Ryan" className="h-full w-auto object-contain object-bottom drop-shadow-2xl grayscale contrast-125 hover:grayscale-0 transition-all duration-700" \/>'
new_subject = '''<div className="relative h-full w-auto flex justify-center">
             <img src="/profile-nobg.png" alt="Gabriel Ryan" className="h-full w-auto object-contain object-bottom mix-blend-multiply transition-all duration-700" style={{ filter: "url(#bitmap)" }} />
             {/* Halftone Dot Overlay */}
             <div className="absolute inset-0 mix-blend-overlay opacity-40 pointer-events-none" style={{ backgroundImage: "radial-gradient(circle, #000 1px, transparent 1.5px)", backgroundSize: "4px 4px" }}></div>
           </div>'''
content = re.sub(old_subject, new_subject, content)


with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Applied Grunge Bitmap Poster layout.')
