import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Tweak the Beige color (P3)
content = content.replace('#E5D8C5', '#DDC6A7') # Slightly deeper, more contrast

# 2. Add Scroll Hint
scroll_hint = '''
      {/* Scroll Hint (Bottom Center) */}
      <div className="absolute bottom-6 md:bottom-10 left-1/2 -translate-x-1/2 flex flex-col items-center gap-3 z-30 opacity-70">
        <span className="text-[7px] md:text-[9px] font-bold tracking-[0.4em] uppercase whitespace-nowrap">
          Scroll to explore
        </span>
        <div className="w-[1px] h-8 md:h-12 bg-current overflow-hidden relative opacity-50">
          <motion.div 
            className="absolute top-0 left-0 w-full h-[50%] bg-current"
            animate={{ y: ["-100%", "200%"] }}
            transition={{ duration: 1.5, repeat: Infinity, ease: "easeInOut" }}
          />
        </div>
      </div>
    </div>
  );
}'''

# Replace the end of HomeContent
# The original end is:
#         </div>
#       </div>
# 
#     </div>
#   );
# }

# We'll use regex to precisely insert it before the closing of the main HomeContent wrapper
regex_end_homecontent = r'</div\>\s*</div\>\s*\n\s*</div\>\s*\n\s*\);\s*\n\}'
content = re.sub(regex_end_homecontent, '</div>\n      </div>' + scroll_hint, content)


with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Visual tweaks and scroll hint applied.")
