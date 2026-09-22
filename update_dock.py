import re

with open('src/components/ui/dock.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
"""      subItems: [
        { id: 'work', label: 'Selected Work' },
        { id: 'classroom', label: 'Classroom' }
      ]""",
"""      subItems: [
        { id: 'work', label: 'Selected Work' },
        { id: 'classroom', label: 'Classroom' },
        { id: 'case-study', label: 'Case Study' }
      ]"""
)

with open('src/components/ui/dock.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
