import re

html_content = """<!doctype html>
<html lang="en" class="dark">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    
    <!-- Primary Meta Tags -->
    <title>Gabriel Ryan | Educator & Developer</title>
    <meta name="title" content="Gabriel Ryan | Educator & Developer" />
    <meta name="description" content="Personal portfolio of Gabriel Ryan, a passionate IT Specialist, Educator, and Developer crafting elegant digital experiences." />

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://portfolio-gabriel-ryan.vercel.app/" />
    <meta property="og:title" content="Gabriel Ryan | Educator & Developer" />
    <meta property="og:description" content="Personal portfolio of Gabriel Ryan, a passionate IT Specialist, Educator, and Developer crafting elegant digital experiences." />
    <meta property="og:image" content="https://portfolio-gabriel-ryan.vercel.app/favicon.jpg" />

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image" />
    <meta property="twitter:url" content="https://portfolio-gabriel-ryan.vercel.app/" />
    <meta property="twitter:title" content="Gabriel Ryan | Educator & Developer" />
    <meta property="twitter:description" content="Personal portfolio of Gabriel Ryan, a passionate IT Specialist, Educator, and Developer crafting elegant digital experiences." />
    <meta property="twitter:image" content="https://portfolio-gabriel-ryan.vercel.app/favicon.jpg" />

    <link rel="icon" type="image/jpeg" href="/favicon.jpg" />
  </head>
  <body class="bg-slate-950 text-slate-50 min-h-screen">
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updated index.html")
