import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Add useEffect import if not present
if 'useEffect' not in content:
    content = content.replace("import React from 'react';", "import React, { useEffect } from 'react';")

# Inject window.scrollTo(0, 0) inside App component
old_app = r'function App\(\) \{'
new_app = '''function App() {
  // Force scroll to top on refresh
  useEffect(() => {
    window.history.scrollRestoration = 'manual';
    window.scrollTo(0, 0);
  }, []);'''

content = re.sub(old_app, new_app, content)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Added scroll-to-top on refresh.')
