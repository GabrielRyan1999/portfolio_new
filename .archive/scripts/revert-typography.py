import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the giant mix-blend typography block with the split typography BEHIND the subject
old_typography = r'\{\/\* 4\. Giant Typography \(Strictly IN FRONT of subject, using Mix Blend Difference\) \*\/\}\s*<div className="absolute inset-0 z-40 w-full h-full flex flex-col items-center justify-center pointer-events-none mix-blend-difference">\s*<h1 className="font-serif text-\[13vw\] md:text-\[15vw\] leading-\[0\.85\] tracking-tighter font-black text-center whitespace-nowrap text-white">\s*<span className="block">GABRIEL<\/span>\s*<span className="block">RYAN<\/span>\s*<\/h1>\s*<\/div>'

new_typography = '''{/* 4. Giant Typography (Strictly BEHIND subject for 3D Magazine effect) */}
        <div className="absolute inset-0 z-20 pointer-events-none">
           {/* Left Side (Cream Text on Blue BG) */}
           <div className="absolute top-0 left-0 w-[45vw] h-full overflow-hidden">
               <div className="absolute top-0 left-0 w-[100vw] h-full flex flex-col items-center justify-center">
                   <h1 className="font-serif text-[13vw] md:text-[15vw] leading-[0.85] tracking-tighter font-black text-center whitespace-nowrap text-[#F5F2EB]">
                      <span className="block">GABRIEL</span>
                      <span className="block">RYAN</span>
                   </h1>
               </div>
           </div>
           {/* Right Side (Blue Text on Cream BG) */}
           <div className="absolute top-0 right-0 w-[55vw] h-full overflow-hidden">
               <div className="absolute top-0 right-0 w-[100vw] h-full flex flex-col items-center justify-center">
                   <h1 className="font-serif text-[13vw] md:text-[15vw] leading-[0.85] tracking-tighter font-black text-center whitespace-nowrap text-[#1A365D]">
                      <span className="block">GABRIEL</span>
                      <span className="block">RYAN</span>
                   </h1>
               </div>
           </div>
        </div>'''

content = re.sub(old_typography, new_typography, content)

# Change subject z-index back to 30
old_subject = r'\{\/\* 5\. The Subject \(Portrait - BEHIND text\) \*\/\}\s*<div className="absolute bottom-0 w-full h-\[85vh\] md:h-\[90vh\] flex justify-center z-20 pointer-events-none">'
new_subject = '''{/* 5. The Subject (Portrait - Strictly IN FRONT of text) */}
        <div className="absolute bottom-0 w-full h-[85vh] md:h-[90vh] flex justify-center z-30 pointer-events-none">'''

content = re.sub(old_subject, new_subject, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Reverted to text-behind-subject layout.')
