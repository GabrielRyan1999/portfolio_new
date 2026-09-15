import re

with open('src/main.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    "import App from './App.jsx'", 
    "import App from './App.jsx'\nimport { Analytics } from '@vercel/analytics/react'"
)

content = content.replace(
    "<App />",
    "<App />\n    <Analytics />"
)

with open('src/main.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected Analytics")
