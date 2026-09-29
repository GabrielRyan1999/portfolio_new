import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

old_str = """                );
              })}
            </div>
  
          </section>
        </PageTransition>
      );
  }
export function Experience() {"""

new_str = """                );
              })}
            </div>
          </div>
          </section>
        </PageTransition>
      );
  }
export function Experience() {"""

content = content.replace(old_str, new_str)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed unclosed div using replace.')
