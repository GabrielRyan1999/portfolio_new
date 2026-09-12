import re

# Fix App.jsx
with open('src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("import { useState, useEffect, useRef } from 'react';", "import { useState, useEffect } from 'react';")
content = content.replace("import { Mail, ArrowUpRight, ChevronLeft, ChevronRight, ExternalLink, Plus } from 'lucide-react';", "import { ChevronLeft, ChevronRight, ExternalLink, Plus } from 'lucide-react';")
content = content.replace("import { motion, AnimatePresence, useScroll, useTransform } from 'framer-motion';", "import { motion, AnimatePresence } from 'framer-motion';")
content = content.replace("const CountUp = CountUpPkg.default ?? CountUpPkg;\n", "")
content = content.replace("const slideRight = {\n    hidden: { opacity: 0, x: -60, filter: 'blur(10px)' },\n    visible: { opacity: 1, x: 0, filter: 'blur(0px)', transition: { duration: 0.8, ease: [0.16, 1, 0.3, 1] } }\n  };", "")
content = re.sub(r'function StepCard\(\{.*?\}\) \{.*?\n  \)\n\}\n', '', content, flags=re.DOTALL)
content = re.sub(r'const \[roleIndex, setRoleIndex\] = useState\(0\);', '', content)


with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

# Fix lets-work-section.jsx
with open('src/components/ui/lets-work-section.jsx', 'r', encoding='utf-8') as f:
    content2 = f.read()

content2 = content2.replace('import { ArrowUpRight, Calendar, Send } from "lucide-react"', 'import { ArrowUpRight } from "lucide-react"')
content2 = content2.replace('const [isButtonHovered, setIsButtonHovered] = useState(false)', '')
content2 = re.sub(r'const handleBookCall = \(\) => \{\n    window\.open\("https://cal\.com/jatin-yadav05/15min", "_blank"\)\n  \}\n', '', content2)

with open('src/components/ui/lets-work-section.jsx', 'w', encoding='utf-8') as f:
    f.write(content2)

print("Fixed linting")
