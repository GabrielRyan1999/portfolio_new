import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix prevWork button
bad_prev = r'<button\n                        onClick=\{prevWork\}\n                        aria-expanded=\{isOpen\}\n                        aria-controls=\{`service-panel-\$\{index\}`\}\n                        id=\{`service-button-\$\{index\}`\}\n                        className="([^"]+)"\n                    >'

good_prev = r'<button\n                        onClick={prevWork}\n                        className="\1"\n                    >'

content = re.sub(bad_prev, good_prev, content)

# Fix nextWork button
bad_next = r'<button\n                        onClick=\{nextWork\}\n                        aria-expanded=\{isOpen\}\n                        aria-controls=\{`service-panel-\$\{index\}`\}\n                        id=\{`service-button-\$\{index\}`\}\n                        className="([^"]+)"\n                    >'

good_next = r'<button\n                        onClick={nextWork}\n                        className="\1"\n                    >'

content = re.sub(bad_next, good_next, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed Work navigation buttons")
