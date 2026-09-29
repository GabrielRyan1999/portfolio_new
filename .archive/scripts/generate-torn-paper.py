import random

# Generate a torn paper SVG path
width = 2000
height = 200
points = [(0, height), (0, 100)]

# Generate jagged points
x = 0
while x < width:
    x += random.randint(5, 20)
    y = 100 + random.randint(-15, 15)
    if x > width: x = width
    points.append((x, y))

points.append((width, height))

path_data = "M" + " L".join(f"{p[0]},{p[1]}" for p in points) + " Z"

svg_content = f"""<svg width="100%" height="100%" viewBox="0 0 {width} {height}" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="-5" stdDeviation="8" flood-opacity="0.1"/>
    </filter>
  </defs>
  <path d="{path_data}" fill="#FFFFFF" filter="url(#shadow)"/>
</svg>"""

with open('public/torn-paper.svg', 'w') as f:
    f.write(svg_content)

print("Generated torn-paper.svg")
