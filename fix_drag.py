import re

with open('src/components/ui/unique-testimonial.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change onDragEnd logic
old_drag = """                onDragEnd={(e, { offset, velocity }) => {
                  const swipe = offset.x;
                  if (swipe < -50) {
                    handleNext(); // swipe left goes next
                  } else if (swipe > 50) {
                    handlePrev(); // swipe right goes prev
                  }
                }}"""

new_drag = """                onDragEnd={(e, { offset, velocity }) => {
                  const swipe = Math.abs(offset.x);
                  if (swipe > 50) {
                    handleNext(); // swipe left or right discards the front card
                  }
                }}"""
content = content.replace(old_drag, new_drag)

# 2. Remove layout prop
old_div = """              <motion.div
                key={card.id}
                layout
                initial={{ opacity: 0, scale: 0.8, y: 50 }}"""
new_div = """              <motion.div
                key={card.id}
                initial={{ opacity: 0, scale: 0.8, y: 50 }}"""
content = content.replace(old_div, new_div)

# 3. drag prop
old_drag_prop = """                drag="x\""""
new_drag_prop = """                drag={index === 0 ? "x" : false}"""
content = content.replace(old_drag_prop, new_drag_prop)

# Let's ensure front card goes back to 0 explicitly
# Find animate={{ ... }} and add x: 0
old_animate = """                animate={{
                  y: index * -25, // Stack cards upwards
                  scale: 1 - index * 0.06, // Cards in back get smaller
                  zIndex: cards.length - index,
                  opacity: 1 - index * 0.25, // Cards in back fade out
                }}"""
new_animate = """                animate={{
                  y: index * -25, // Stack cards upwards
                  scale: 1 - index * 0.06, // Cards in back get smaller
                  zIndex: cards.length - index,
                  opacity: 1 - index * 0.25, // Cards in back fade out
                  x: 0, // ensure card snaps back to center
                }}"""
content = content.replace(old_animate, new_animate)

with open('src/components/ui/unique-testimonial.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Drag fixed")
