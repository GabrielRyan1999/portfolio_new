import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

index_page_comp = '''function IndexPage() {
  return (
    <div className="flex flex-col w-full">
      <Home />
      <About />
      <Work />
      <Service />
      <Experience />
      <Contact />
    </div>
  );
}

function AnimatedRoutes'''

content = content.replace('function AnimatedRoutes', index_page_comp)

routes_regex = r'<Routes location=\{location\} key=\{location\.pathname\}>.*?</Routes>'
new_routes = '''<Routes location={location} key={location.pathname}>
        <Route path="/" element={<IndexPage />} />
      </Routes>'''

content = re.sub(routes_regex, new_routes, content, flags=re.DOTALL)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("App.jsx routing updated cleanly.")
