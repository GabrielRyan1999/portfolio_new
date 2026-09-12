import re

with open('src/components/ui/dock.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Change function signature
content = content.replace("export function FloatingDock() {", "export function FloatingDock({ onContactClick }) {")

# Modify scrollTo
scrollTo_old = """const scrollTo = (id) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
    // Auto collapse after clicking a link if we are scrolled down
    if (isScrolled) {
      setIsExpanded(false);
    }
  };"""

scrollTo_new = """const scrollTo = (id) => {
    if (id === 'contact' && onContactClick) {
      onContactClick();
    } else {
      const el = document.getElementById(id);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth' });
      }
    }
    
    // Auto collapse after clicking a link if we are scrolled down
    if (isScrolled) {
      setIsExpanded(false);
    }
  };"""

content = content.replace(scrollTo_old, scrollTo_new)

with open('src/components/ui/dock.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated dock.jsx")
