import re
import os

with open('src/App_backup.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# We need precise extraction.
hero_match = re.search(r'(<div className="relative" id="about">.*?)<SectionShell id="about-me"', content, re.DOTALL)
hero_jsx = hero_match.group(1).strip() if hero_match else ""

about_match = re.search(r'(<SectionShell id="about-me".*?)<SectionShell id="work"', content, re.DOTALL)
about_jsx = about_match.group(1).strip() if about_match else ""

work_match = re.search(r'(<SectionShell id="work".*?)<SectionShell id="service"', content, re.DOTALL)
work_jsx = work_match.group(1).strip() if work_match else ""

service_match = re.search(r'(<SectionShell id="service".*?)<SectionShell id="experience"', content, re.DOTALL)
service_jsx = service_match.group(1).strip() if service_match else ""

experience_match = re.search(r'(<SectionShell id="experience".*?)<SectionShell label="/TESTIMONIALS"', content, re.DOTALL)
experience_jsx = experience_match.group(1).strip() if experience_match else ""

testimonial_match = re.search(r'(<SectionShell label="/TESTIMONIALS".*?)<div id="contact">', content, re.DOTALL)
testimonial_jsx = testimonial_match.group(1).strip() if testimonial_match else ""

contact_match = re.search(r'(<div id="contact">.*?</div>)', content, re.DOTALL)
contact_jsx = contact_match.group(1).strip() if contact_match else ""

# Also extract RotatingText
rotating_match = re.search(r'(function RotatingText.*?return .*?\n\})', content, re.DOTALL)
rotating_text = rotating_match.group(1) if rotating_match else ""

pages_content = f"""import React, {{ useState, useEffect }} from 'react';
import {{ motion, AnimatePresence }} from 'framer-motion';
import {{ Link }} from 'react-router-dom';
import {{ SectionShell }} from '../components/ui/SectionShell';
import {{ HoverExpandGallery }} from '../components/ui/hover-expand-gallery';
import {{ MentorReportingFeatures }} from '../components/ui/features-2';
import {{ Testimonials }} from '../components/ui/unique-testimonial';
import {{ Linkedin, Github, Instagram }} from '../components/ui/brand-icons';
import {{ ChevronLeft, ChevronRight, ExternalLink, Plus }} from 'lucide-react';
import {{ LetsWorkTogether }} from '../components/ui/lets-work-section';
import {{ experienceJobs, carouselSlides, workProjects }} from '../data';

// Animation configs
const fadeUp = {{
  hidden: {{ opacity: 0, y: 40 }},
  visible: {{ opacity: 1, y: 0, transition: {{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }} }}
}};
const staggerContainer = {{
  hidden: {{ opacity: 0 }},
  visible: {{ opacity: 1, transition: {{ staggerChildren: 0.1, delayChildren: 0.1 }} }}
}};
const slideInRight = {{
  hidden: {{ opacity: 0, x: 50 }},
  visible: {{ opacity: 1, x: 0, transition: {{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }} }}
}};

{rotating_text}

export const PageTransition = ({{ children }}) => (
  <motion.div
    initial={{{{ opacity: 0, y: 20 }}}}
    animate={{{{ opacity: 1, y: 0 }}}}
    exit={{{{ opacity: 0, y: -20 }}}}
    transition={{{{ duration: 0.4, ease: "easeInOut" }}}}
    className="w-full h-full min-h-screen"
  >
    {{children}}
  </motion.div>
);

export function Home() {{
  const [index, setIndex] = useState(0);
  const words = ["INNOVATE", "CREATE", "INSPIRE"];
  
  return (
    <PageTransition>
      {hero_jsx}
    </PageTransition>
  );
}}

export function About() {{
  return (
    <PageTransition>
      <div className="pt-20">
        {about_jsx}
      </div>
    </PageTransition>
  );
}}

export function Work() {{
  const [workIndex, setWorkIndex] = useState(0);
  return (
    <PageTransition>
      <div className="pt-20">
        {work_jsx}
      </div>
    </PageTransition>
  );
}}

export function Service() {{
  const [activeServiceIndex, setActiveServiceIndex] = useState(null);
  return (
    <PageTransition>
      <div className="pt-20">
        {service_jsx}
      </div>
    </PageTransition>
  );
}}

export function Experience() {{
  return (
    <PageTransition>
      <div className="pt-20">
        {experience_jsx}
        {testimonial_jsx}
      </div>
    </PageTransition>
  );
}}

export function Contact() {{
  return (
    <PageTransition>
      <div className="pt-20">
        {contact_jsx}
      </div>
    </PageTransition>
  );
}}
"""

# Replace only the specific #contact and #work links
pages_content = pages_content.replace('<a href="#contact"', '<Link to="/contact"')
# The </a> for these specific links must be replaced with </Link>
# We can do this with Regex
pages_content = re.sub(r'<Link to="/contact"(.*?)</a>', r'<Link to="/contact"\1</Link>', pages_content, flags=re.DOTALL)

pages_content = pages_content.replace('<a href="#work"', '<Link to="/work"')
pages_content = re.sub(r'<Link to="/work"(.*?)</a>', r'<Link to="/work"\1</Link>', pages_content, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(pages_content)
print("Pages.jsx perfectly regenerated!")
