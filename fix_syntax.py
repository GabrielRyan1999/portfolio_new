with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("initial={ opacity: 0, y: 20 }", "initial={{ opacity: 0, y: 20 }}")
content = content.replace("animate={ opacity: 1, y: 0 }", "animate={{ opacity: 1, y: 0 }}")
content = content.replace("exit={ opacity: 0, y: -20 }", "exit={{ opacity: 0, y: -20 }}")
content = content.replace('transition={ duration: 0.4, ease: "easeInOut" }', 'transition={{ duration: 0.4, ease: "easeInOut" }}')

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("Syntax fixed")
