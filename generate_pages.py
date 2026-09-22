import re
import os

os.makedirs('src/pages', exist_ok=True)

with open('src/App_backup.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

hero_match = re.search(r'(<div className="relative" id="about">.*?)<SectionShell id="about-me"', content, re.DOTALL)
hero_jsx = hero_match.group(1).strip() if hero_match else ""

about_match = re.search(r'(<SectionShell id="about-me".*?)<SectionShell id="work"', content, re.DOTALL)
about_jsx = about_match.group(1).strip() if about_match else ""

work_match = re.search(r'(<SectionShell id="work".*?)<SectionShell id="service"', content, re.DOTALL)
work_jsx = work_match.group(1).strip() if work_match else ""

service_match = re.search(r'(<SectionShell id="service".*?)<SectionShell id="experience"', content, re.DOTALL)
service_jsx = service_match.group(1).strip() if service_match else ""

experience_match = re.search(r'(<SectionShell id="experience".*?)<div id="contact">', content, re.DOTALL)
experience_jsx = experience_match.group(1).strip() if experience_match else ""

pages_content = f"""import React, {{ useState }} from 'react';
import {{ motion, AnimatePresence }} from 'framer-motion';
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

export const PageTransition = ({{ children }}) => (
  <motion.div
    initial={{ opacity: 0, y: 20 }}
    animate={{ opacity: 1, y: 0 }}
    exit={{ opacity: 0, y: -20 }}
    transition={{ duration: 0.4, ease: "easeInOut" }}
    className="w-full h-full min-h-screen"
  >
    {{children}}
  </motion.div>
);

export function Home() {{
  const [index, setIndex] = useState(0); // For RotatingText if needed
  const words = ["INNOVATE", "CREATE", "INSPIRE"]; // if used
  
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
      </div>
    </PageTransition>
  );
}}

export function Contact() {{
  return (
    <PageTransition>
      <div className="pt-20">
        <div id="contact">
          <LetsWorkTogether />
        </div>
      </div>
    </PageTransition>
  );
}}
"""

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(pages_content)
print("Pages.jsx created!")
