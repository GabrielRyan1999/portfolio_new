import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the closing section tag in Experience to include the missing div
old_str = """              ))}
            </div>
  
          </section>
  
          {/* Testimonials Wrapper */}"""

new_str = """              ))}
            </div>
          </div>
          </section>
  
          {/* Testimonials Wrapper */}"""

content = content.replace(old_str, new_str)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed unclosed div using replace.')
