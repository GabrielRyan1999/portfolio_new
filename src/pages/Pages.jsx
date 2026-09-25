import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence, useScroll, useTransform } from 'framer-motion';
import { Link } from 'react-router-dom';
import { SectionShell } from '../components/ui/SectionShell';
import { HoverExpandGallery } from '../components/ui/hover-expand-gallery';
import { MentorReportingFeatures } from '../components/ui/features-2';
import { Testimonials } from '../components/ui/unique-testimonial';
import { Linkedin, Github, Instagram } from '../components/ui/brand-icons';
import { ChevronLeft, ChevronRight, ChevronDown, ExternalLink, Plus } from 'lucide-react';
import { LetsWorkTogether } from '../components/ui/lets-work-section';
import { experienceJobs, carouselSlides, workProjects } from '../data';

// Animation configs
const fadeUp = {
  hidden: { opacity: 0, y: 40 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.8, ease: [0.16, 1, 0.3, 1] } }
};
const staggerContainer = {
  hidden: { opacity: 0 },
  visible: { opacity: 1, transition: { staggerChildren: 0.1, delayChildren: 0.1 } }
};
const slideInRight = {
  hidden: { opacity: 0, x: 50 },
  visible: { opacity: 1, x: 0, transition: { duration: 0.8, ease: [0.16, 1, 0.3, 1] } }
};

function RotatingText({ words }) {
  const [index, setIndex] = useState(0);
  
  useEffect(() => {
    const interval = setInterval(() => {
      setIndex((prev) => (prev + 1) % words.length);
    }, 2000);
    return () => clearInterval(interval);
  }, [words.length]);

  return (
    <div className="inline-grid [grid-template-areas:'stack'] overflow-hidden text-blue-600">
      <AnimatePresence mode="popLayout">
        <motion.span
          key={words[index]}
          initial={{ y: "100%", opacity: 0 }}
          animate={{ y: "0%", opacity: 1 }}
          exit={{ y: "-100%", opacity: 0 }}
          transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
          className="[grid-area:stack] inline-block"
        >
          {words[index]}
        </motion.span>
      </AnimatePresence>
    </div>
  );
}


const ScrollIndicator = () => {
  const { scrollY } = useScroll();
  const opacity = useTransform(scrollY, [0, 100], [1, 0]);
  
  return (
    <motion.div 
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ delay: 1, duration: 1 }}
      style={{ opacity }}
      className="fixed bottom-6 md:bottom-8 left-1/2 -translate-x-1/2 flex flex-col items-center justify-center text-slate-400 dark:text-zinc-500 z-[999] pointer-events-none"
    >
      <span className="text-[10px] md:text-xs font-semibold tracking-[0.2em] mb-1 md:mb-2 uppercase drop-shadow-md">Scroll</span>
      <motion.div
        animate={{ y: [0, 8, 0] }}
        transition={{ duration: 1.5, repeat: Infinity, ease: "easeInOut" }}
      >
        <ChevronDown className="w-4 h-4 md:w-5 md:h-5 opacity-70 drop-shadow-md" />
      </motion.div>
    </motion.div>
  );
};


const GlobalFooter = () => (
  <div className="flex flex-col md:flex-row items-center justify-between w-full border-t border-[var(--card-border)] pt-6 mt-8 text-[var(--foreground-muted)] z-10 relative">
    <div className="text-sm font-medium text-center md:text-left">
      &copy; {new Date().getFullYear()} Gabriel Ryan.<br className="block md:hidden"/> All rights reserved.
    </div>
    <div className="flex flex-row gap-6 my-4 md:my-0">
      <a href="https://www.linkedin.com/in/gabrielryan1999/" target="_blank" rel="noreferrer" aria-label="LinkedIn" className="hover:text-[var(--color-brand)] transition-colors"><Linkedin className="w-5 h-5" /></a>
      <a href="https://github.com/GabrielRyan1999" target="_blank" rel="noreferrer" aria-label="GitHub" className="hover:text-[var(--foreground)] transition-colors"><Github className="w-5 h-5" /></a>
      <a href="https://www.instagram.com/heyitsgabrielryan/" target="_blank" rel="noreferrer" aria-label="Instagram" className="hover:text-pink-600 transition-colors"><Instagram className="w-5 h-5" /></a>
    </div>
    <div className="text-sm text-center md:text-right hidden md:block">
      Created with 💙 by Ryan
    </div>
  </div>
);

export const PageTransition = ({ children }) => (
  <motion.div
    initial={{ opacity: 0, y: 20 }}
    animate={{ opacity: 1, y: 0 }}
    exit={{ opacity: 0, y: -20 }}
    transition={{ duration: 0.4, ease: "easeInOut" }}
    className="w-full h-full min-h-screen"
  >
    {children}
  </motion.div>
);

export function Home() {
  const words = ["INNOVATE", "CREATE", "INSPIRE"];
  
  return (
    <PageTransition>
<SectionShell header={
<nav className="w-full max-w-7xl mx-auto px-6 md:px-8 lg:px-12 py-6 flex items-center justify-between shrink-0 relative z-20">
            <h1 className="text-xl font-black tracking-tighter cursor-pointer text-zinc-900 dark:text-zinc-100 transition-colors">
              RYAN<span className="text-blue-600">.</span>
            </h1>
            <a href="#contact" className="bg-zinc-900 text-white dark:bg-zinc-100 dark:text-zinc-900 px-6 py-3 rounded-full text-sm font-bold hover:bg-blue-600 dark:hover:bg-zinc-300 transition-colors shadow-lg">
              Let's Talk
            </a>
          </nav>
          } dark={false} footer={<GlobalFooter />}>
            <motion.div variants={staggerContainer} initial="hidden" animate="visible" className="w-full flex flex-col items-center justify-center relative h-full">
              {/* Grouped Center Content */}
              <div className="flex flex-col items-center justify-center w-full z-10 relative">
                
                

                <motion.h1 variants={fadeUp} className="relative text-center text-[9.5vw] sm:text-6xl md:text-[9rem] font-black leading-none flex flex-row gap-2 md:gap-8 items-center justify-center z-10 w-full whitespace-nowrap">
                  <span className="shrink-0 text-transparent tracking-widest md:tracking-normal [-webkit-text-stroke:1px_#09090b] md:[-webkit-text-stroke:3px_#09090b] dark:[-webkit-text-stroke:1px_#fafafa] dark:md:[-webkit-text-stroke:3px_#fafafa]">GABRIEL</span>
                  <span className="shrink-0 text-zinc-900 dark:text-zinc-100">RYAN</span>
                </motion.h1>

                {/* Overlapping Photo with Negative Margin */}
                <motion.div variants={fadeUp} className="mx-auto w-[280px] md:w-[350px] aspect-[3/4] -mt-8 md:-mt-16 rounded-t-full bg-zinc-200 shadow-2xl shadow-zinc-900/20 overflow-hidden relative z-0 ring-1 ring-zinc-900/5 transition-transform hover:-translate-y-2 duration-500">
                  <img src="/profile_new.jpg" fetchpriority="high" alt="Gabriel Ryan" className="w-full h-full object-cover object-center grayscale hover:grayscale-0 transition-all duration-500" />
                </motion.div>
                
                {/* Footer text below the photo */}
                <motion.div variants={fadeUp} className="flex flex-col md:flex-row items-center md:items-end justify-between w-full max-w-5xl mx-auto mt-12 md:mt-20 pb-32 md:pb-0 gap-10 md:gap-8 z-10 px-4">
                  
                  <div className="space-y-5 text-center md:text-left flex-1">
                    <h2 className="text-3xl md:text-5xl font-black text-zinc-900 dark:text-zinc-100 tracking-tight leading-tight">
                      Educator & <br />
                      <RotatingText words={["Developer", "Designer", "Creator", "Engineer"]} />
                    </h2>
                    <p className="text-base md:text-lg text-zinc-500 dark:text-zinc-400 max-w-sm mx-auto md:mx-0 leading-relaxed font-medium">
                      Shaping digital learning through engineered platforms and teaching that are clear, engaging, and impactful.
                    </p>
                  </div>
                  
                  <div className="flex flex-row gap-4 md:gap-6 text-center items-center justify-center md:justify-end pb-2">
                    <a href="https://www.linkedin.com/in/gabrielryan1999/" target="_blank" rel="noreferrer" aria-label="LinkedIn" className="group flex items-center gap-3 text-zinc-500 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-100 font-bold transition-all duration-300">
                      <span className="w-11 h-11 rounded-full border-2 border-zinc-200 group-hover:border-blue-600 group-hover:bg-blue-600 group-hover:text-white flex items-center justify-center text-xs transition-all duration-300 shadow-sm"><Linkedin className="w-4 h-4" /></span> 
                      <span className="hidden lg:block text-sm tracking-wide">LinkedIn</span>
                    </a>
                    <a href="https://github.com/GabrielRyan1999" target="_blank" rel="noreferrer" aria-label="GitHub" className="group flex items-center gap-3 text-zinc-500 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-100 font-bold transition-all duration-300">
                      <span className="w-11 h-11 rounded-full border-2 border-zinc-200 group-hover:border-zinc-900 group-hover:bg-zinc-900 group-hover:text-white flex items-center justify-center text-xs transition-all duration-300 shadow-sm"><Github className="w-4 h-4" /></span> 
                      <span className="hidden lg:block text-sm tracking-wide">GitHub</span>
                    </a>
                    <a href="https://www.instagram.com/heyitsgabrielryan/" target="_blank" rel="noreferrer" aria-label="Instagram" className="group flex items-center gap-3 text-zinc-500 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-100 font-bold transition-all duration-300">
                      <span className="w-11 h-11 rounded-full border-2 border-zinc-200 group-hover:border-pink-600 group-hover:bg-pink-600 group-hover:text-white flex items-center justify-center text-xs transition-all duration-300 shadow-sm"><Instagram className="w-4 h-4" /></span> 
                      <span className="hidden lg:block text-sm tracking-wide">Instagram</span>
                    </a>
                  </div>

                </motion.div>
              </div>
            </motion.div>
          </SectionShell>
      
</PageTransition>
  );
}

export function About() {
  return (
    <PageTransition>
              <SectionShell id="about-me" label="/ABOUT ME" watermark="ABOUT" dark={true} footer={<GlobalFooter />}>
              {/* Background Avatar Watermarks */}
              <div className="absolute inset-0 pointer-events-none z-[0] overflow-hidden">
                <img src="/favicon.jpg" alt="" className="absolute top-10 md:top-20 -left-4 md:left-0 w-[250px] md:w-[400px] lg:w-[500px] blur-[2px] -rotate-12 rounded-full opacity-[0.05] dark:opacity-[0.03] grayscale" />
                <img src="/favicon.jpg" alt="" className="absolute bottom-10 md:bottom-32 -right-4 md:right-0 w-[280px] md:w-[450px] lg:w-[600px] blur-[2px] rotate-12 rounded-full opacity-[0.05] dark:opacity-[0.03] grayscale" />
              </div>
              <motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: false, amount: 0.2 }} className="w-full max-w-6xl mx-auto flex flex-col lg:flex-row items-stretch gap-8 lg:gap-16 px-4 relative z-10">
                
                
          {/* Left: Personal Story */}
                <div className="w-full lg:w-1/2 flex flex-col justify-center space-y-6">
                  <div>
                    <motion.h3 variants={fadeUp} className="text-3xl md:text-5xl font-black text-[var(--foreground)] tracking-tight mb-3">
                      Gabriel Ryan Prima
                    </motion.h3>
                    <motion.p variants={fadeUp} className="text-lg md:text-xl text-[var(--color-brand)] font-bold">
                      Educator, Developer, & System Builder.
                    </motion.p>
                  </div>
                  
                  <motion.div variants={fadeUp} className="space-y-5 text-[var(--foreground-muted)] text-sm md:text-base leading-relaxed">
                    <p>
                      I work at the intersection of technology and education based in Yogyakarta, Indonesia. My background is in computer engineering, but somewhere along the way teaching became the thing I actually care about, and combining the two has become my life's focus ever since.
                    </p>
                    
                    <div>
                      <h4 className="text-[var(--foreground)] font-bold mb-1 tracking-wide">Background</h4>
                      <p>
                        I graduated in Computer Engineering, and that technical foundation is why I approach education the way I do: not as content delivery, but as a system you design with intention, one that has to hold up in practice, not just in theory.
                      </p>
                    </div>
                    
                    <div>
                      <h4 className="text-[var(--foreground)] font-bold mb-1 tracking-wide">Outside of Work</h4>
                      <p>
                        When I'm not building or teaching, I'm usually gaming, gardening, or digging into personal finance and investing.
                      </p>
                    </div>
                  </motion.div>
                  
                </div>

                {/* Right: Core Pillars Bento Box */}
                <motion.div variants={fadeUp} className="w-full lg:w-1/2 grid grid-cols-2 gap-4 mt-8 lg:mt-0">
                   <div className="col-span-2 bg-[var(--background-secondary)] border border-[var(--card-border)] rounded-3xl p-6 md:p-8 flex flex-col justify-center shadow-lg hover:border-[var(--color-brand)]/50 transition-colors group">
                      <div className="w-12 h-12 rounded-2xl bg-blue-500/10 text-blue-500 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                         <span className="font-mono font-bold text-lg">01</span>
                      </div>
                      <h4 className="text-xl md:text-2xl font-black text-[var(--foreground)] mb-2 tracking-tight">Curriculum Development</h4>
                      <p className="text-[var(--foreground-muted)] text-sm md:text-base leading-relaxed">Designing structured, engaging, and industry-aligned tech learning paths for students of all levels.</p>
                   </div>
                   
                   <div className="col-span-1 bg-[var(--background-secondary)] border border-[var(--card-border)] rounded-3xl p-5 md:p-6 flex flex-col shadow-lg hover:border-pink-500/50 transition-colors group">
                      <div className="w-10 h-10 rounded-xl bg-pink-500/10 text-pink-500 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                         <span className="font-mono font-bold text-base">02</span>
                      </div>
                      <h4 className="text-lg md:text-xl font-black text-[var(--foreground)] mb-1.5 tracking-tight">Modern Web</h4>
                      <p className="text-[var(--foreground-muted)] text-xs md:text-sm leading-relaxed">Building fast, scalable full-stack applications.</p>
                   </div>
                   
                   <div className="col-span-1 bg-[var(--color-brand)] text-white rounded-3xl p-5 md:p-6 flex flex-col shadow-xl shadow-blue-500/20 hover:scale-[1.03] transition-transform group">
                      <div className="w-10 h-10 rounded-xl bg-white/20 text-white flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                         <span className="font-mono font-bold text-base">03</span>
                      </div>
                      <h4 className="text-lg md:text-xl font-black mb-1.5 tracking-tight">Mentoring</h4>
                      <p className="text-white/80 text-xs md:text-sm leading-relaxed">Guiding the next generation of software engineers.</p>
                   </div>
                </motion.div>
                
              </motion.div>
          </SectionShell>

          {/* Gallery */}
          

          {/* 2. Selected Work (Dark) */}
      
    </PageTransition>
  );
}

export function Work() {
  const [workIndex, setWorkIndex] = useState(0);
  const nextWork = () => setWorkIndex((p) => (p + 1) % workProjects.length);
  const prevWork = () => setWorkIndex((p) => (p - 1 + workProjects.length) % workProjects.length);
  return (
    <PageTransition>
              <SectionShell id="work" label="/SELECTED WORK" watermark="WORK" dark={true}>
            <motion.div variants={fadeUp} initial="hidden" whileInView="visible" viewport={{ once: false, amount: 0.2 }} className="w-full max-w-5xl mx-auto px-0 md:px-6 relative flex items-center justify-center min-h-[500px]">
              
              {/* Left Arrow */}
              <button onClick={prevWork} aria-label="Previous Project" className="absolute left-2 md:-left-8 lg:-left-16 z-20 p-3 md:p-4 rounded-full bg-[var(--background)]/80 backdrop-blur border border-[var(--card-border)] hover:bg-[var(--card)] text-[var(--foreground)] transition-all shadow-lg hover:scale-110">
                <ChevronLeft className="w-5 h-5 md:w-6 md:h-6" />
              </button>
              
              {/* Main Card */}
              <AnimatePresence mode="wait">
                <motion.div
                  key={workIndex}
                  initial={{ opacity: 0, scale: 0.95 }}
                  animate={{ opacity: 1, scale: 1 }}
                  exit={{ opacity: 0, scale: 0.95 }}
                  transition={{ duration: 0.3 }}
                  className="w-full bg-[var(--background-secondary)] border border-[var(--card-border)] rounded-3xl md:rounded-[2.5rem] overflow-hidden flex flex-col md:flex-row items-stretch shadow-2xl group mx-4 md:mx-0 min-h-[550px] md:min-h-[480px] lg:min-h-[500px]"
                >
                  {/* Image Half */}
                  <div className="w-full md:w-5/12 lg:w-1/2 min-h-[220px] relative overflow-hidden bg-zinc-950 shrink-0">
                    <motion.img 
                      src={workProjects[workIndex].img} 
                      alt={workProjects[workIndex].title}
                      loading="lazy"
                      className="absolute inset-0 w-full h-full object-cover opacity-80 group-hover:opacity-100 group-hover:scale-105 transition-all duration-700 ease-[cubic-bezier(0.16,1,0.3,1)]"
                    />
                    <div className="absolute inset-0 bg-gradient-to-t from-zinc-950/90 via-transparent to-transparent opacity-60 md:hidden" />
                    {/* Desktop gradient fade on the right side */}
                    <div className="hidden md:block absolute inset-y-0 right-0 w-24 bg-gradient-to-l from-[var(--background-secondary)] to-transparent" />
                  </div>
                  
                  {/* Content Half */}
                  <div className="w-full md:w-7/12 lg:w-1/2 p-6 md:p-8 lg:p-12 flex flex-col justify-center h-full">
                    <p className="text-[var(--color-brand)] text-xs md:text-sm font-black tracking-widest uppercase mb-2">{workProjects[workIndex].tag}</p>
                    <h3 className="text-3xl md:text-4xl lg:text-5xl font-black mb-4 text-[var(--foreground)] tracking-tight leading-tight">{workProjects[workIndex].title}</h3>
                    <p className="text-[var(--foreground-muted)] text-sm md:text-base leading-relaxed mb-8">{workProjects[workIndex].desc}</p>
                    
                    {/* Tech Stack */}
                    <div className="flex flex-wrap gap-2 mb-8">
                      {workProjects[workIndex].tech.map(tech => (
                        <span key={tech} className="px-3 py-1.5 bg-[var(--background)] border border-[var(--card-border)] text-[var(--foreground)] text-[10px] md:text-xs font-bold tracking-wide rounded-lg whitespace-nowrap">
                          {tech}
                        </span>
                      ))}
                    </div>

                    <a href={workProjects[workIndex].url} target="_blank" rel="noreferrer" className="inline-flex items-center gap-2 px-6 py-3.5 bg-[var(--color-brand)] text-white font-bold rounded-xl w-fit hover:shadow-[0_0_20px_rgba(37,99,235,0.4)] transition-all hover:-translate-y-1">
                       Visit Project <ExternalLink className="w-4 h-4" />
                    </a>
                  </div>
                </motion.div>
              </AnimatePresence>
              
              {/* Right Arrow */}
              <button onClick={nextWork} aria-label="Next Project" className="absolute right-2 md:-right-8 lg:-right-16 z-20 p-3 md:p-4 rounded-full bg-[var(--background)]/80 backdrop-blur border border-[var(--card-border)] hover:bg-[var(--card)] text-[var(--foreground)] transition-all shadow-lg hover:scale-110">
                <ChevronRight className="w-5 h-5 md:w-6 md:h-6" />
              </button>
              
            </motion.div>
            
            {/* Indicators */}
            <div className="flex items-center justify-center gap-3 mt-8">
              {workProjects.map((_, i) => (
                <button key={i} onClick={() => setWorkIndex(i)} className="w-10 h-10 flex items-center justify-center group" aria-label={`Go to project ${i + 1}`}>
                <span className={`block h-2.5 rounded-full transition-all duration-300 ${i === workIndex ? 'bg-[var(--color-brand)] w-8' : 'bg-[var(--card-border)] w-2.5 group-hover:bg-[var(--foreground-muted)]'}`} />
              </button>
              ))}
            </div>
          </SectionShell>

<SectionShell id="classroom" label="/CLASSROOM" watermark="GALLERY" dark={false}>
              <motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: false, amount: 0.2 }} className="w-full h-full flex items-center justify-center relative">
                 <motion.div variants={fadeUp} className="w-full h-full relative">
                    <HoverExpandGallery images={carouselSlides} />
                 </motion.div>
              </motion.div>
          </SectionShell>



          {/* 3. Service (White) */}


            {/* Case Study */}
            <SectionShell id="case-study" label="/CASE STUDY" watermark="SYSTEM" dark={false} footer={<GlobalFooter />}>
                <motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: false, amount: 0.3 }} className="w-full max-w-7xl mx-auto z-10">
                   <motion.div variants={fadeUp}>
                      <MentorReportingFeatures />
                   </motion.div>
                </motion.div>
            </SectionShell>
      
    </PageTransition>
  );
}

export function Service() {
  const [activeServiceIndex, setActiveServiceIndex] = useState(null);
  return (
    <PageTransition>
              <SectionShell id="service" label="/SERVICE" watermark="SERVICE" dark={true} footer={<GlobalFooter />}>
              <motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: false, amount: 0.2 }} className="w-full flex flex-col justify-center z-10 divide-y divide-gray-200">
                {[
                  { title: "CUSTOM WEB PLATFORMS", desc: "Building fast, scalable, and robust web applications, internal dashboards, and custom platforms tailored to your business needs.", images: ["https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=400&q=80", "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=400&q=80", "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?w=400&q=80"] },
                  { title: "EDTECH SOLUTIONS", desc: "Developing custom learning management systems (LMS) and student progress trackers designed with pedagogical best practices.", images: ["https://images.unsplash.com/photo-1501504905252-473c47e087f8?w=400&q=80", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400&q=80", "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=400&q=80"] },
                  { title: "CURRICULUM DEV", desc: "Crafting structured, tech-focused syllabi and scalable learning materials for online, hybrid, and offline educational environments.", images: ["https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=400&q=80", "https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=400&q=80", "https://images.unsplash.com/photo-1503694978374-8a2fa686963a?w=400&q=80"] },
                  { title: "1-ON-1 TECH MENTORING", desc: "Providing personalized coaching in programming, 3D modeling, and game development for students and professionals looking to level up their skills.", images: ["https://images.unsplash.com/photo-1531482615713-2afd69097998?w=400&q=80", "https://images.unsplash.com/photo-1573164713988-8665fc963095?w=400&q=80", "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=400&q=80"] }
                ].map((service, index) => {
                  const isOpen = activeServiceIndex === index;
                  return (
                    <motion.div 
                      key={service.title} 
                      layout 
                      variants={fadeUp} 
                      className={`overflow-hidden transition-all duration-300 rounded-3xl border border-transparent ${
                        isOpen 
                          ? "bg-[var(--card)] !border-[var(--card-border)] shadow-xl shadow-slate-200/50 dark:shadow-none" 
                          : "bg-transparent"
                      }`}
                    >
                      <motion.button
                          layout
                          onClick={() => setActiveServiceIndex(isOpen ? null : index)}
                          className={`group w-full flex items-center justify-between py-6 md:py-8 px-4 md:px-8 transition-colors ${
                            isOpen ? "text-slate-900 dark:text-zinc-100" : "text-slate-400 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-zinc-800/50"
                          }`}
                        >
                          <motion.div layout="position" className="flex items-center gap-4 md:gap-8">
                            <span className="text-sm md:text-xl text-slate-400 dark:text-zinc-500 font-mono font-bold">
                              0{index + 1}
                            </span>
                            <span className="text-2xl md:text-4xl lg:text-5xl font-black text-left group-hover:text-blue-600 transition-colors">
                              {service.title}
                            </span>
                          </motion.div>
                          <motion.span
                            animate={{ rotate: isOpen ? 45 : 0 }}
                            transition={{ duration: 0.3, ease: "easeInOut" }}
                            className="flex items-center justify-center w-10 h-10 md:w-12 md:h-12 rounded-full bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-300 group-hover:bg-blue-600 group-hover:text-white transition-colors shrink-0"
                          >
                            <Plus className="w-6 h-6 md:w-8 md:h-8" />
                          </motion.span>
                        </motion.button>
          
                      <AnimatePresence initial={false}>
                        {isOpen && (
                          <motion.div
                            key="content"
                            initial={{ height: 0, opacity: 0 }}
                            animate={{ height: "auto", opacity: 1 }}
                            exit={{ height: 0, opacity: 0 }}
                            transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
                            className="text-slate-900 dark:text-zinc-100 px-4 md:px-8"
                          >
                            <div className="pb-8 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
                              <p className="text-slate-600 dark:text-zinc-400 dark:text-zinc-300 max-w-md">{service.desc}</p>
                              {service.images.length > 0 && (
                                <div className="relative flex items-center justify-center shrink-0 w-40 h-40 md:w-56 md:h-40 ml-4 hidden sm:flex">
                                  {index === 0 && (
                                    /* Layout 1: Fan spread */
                                    service.images.map((src, imgIndex) => (
                                      <motion.img
                                        key={src} src={src} alt="Web Platform"
                                        initial={{ opacity: 0, x: 20 }}
                                        animate={{ opacity: 1, x: (imgIndex - 1) * 20, rotate: (imgIndex - 1) * 10 }}
                                        transition={{ delay: 0.15 + imgIndex * 0.1, duration: 0.5, type: "spring" }}
                                        className="absolute w-24 h-32 md:w-28 md:h-36 object-cover rounded-xl shadow-xl border border-black/10 dark:border-white/10"
                                      />
                                    ))
                                  )}
                                  {index === 1 && (
                                    /* Layout 2: Floating staggered grid */
                                    service.images.map((src, imgIndex) => (
                                      <motion.img
                                        key={src} src={src} alt="EdTech Solution"
                                        initial={{ opacity: 0, scale: 0.5 }}
                                        animate={{ opacity: 1, scale: 1, x: imgIndex === 0 ? -30 : imgIndex === 1 ? 30 : 0, y: imgIndex === 0 ? -20 : imgIndex === 1 ? -20 : 20 }}
                                        transition={{ delay: 0.15 + imgIndex * 0.15, duration: 0.5, type: "spring" }}
                                        className={`absolute object-cover rounded-xl shadow-lg border border-black/10 dark:border-white/10 ${imgIndex === 2 ? 'w-28 h-20 md:w-36 md:h-24 z-10' : 'w-20 h-20 md:w-24 md:h-24'}`}
                                      />
                                    ))
                                  )}
                                  {index === 2 && (
                                    /* Layout 3: Diagonal stepped */
                                    service.images.map((src, imgIndex) => (
                                      <motion.img
                                        key={src} src={src} alt="Curriculum Dev"
                                        initial={{ opacity: 0, y: 50 }}
                                        animate={{ opacity: 1, y: (imgIndex - 1) * -15, x: (imgIndex - 1) * 15 }}
                                        transition={{ delay: 0.2 + imgIndex * 0.1, duration: 0.5 }}
                                        className="absolute w-20 h-28 md:w-24 md:h-32 object-cover rounded-lg shadow-md border border-black/10 dark:border-white/10"
                                        style={{ zIndex: 3 - imgIndex }}
                                      />
                                    ))
                                  )}
                                  {index === 3 && (
                                    /* Layout 4: Central large with two orbiting small circles */
                                    service.images.map((src, imgIndex) => (
                                      <motion.img
                                        key={src} src={src} alt="Mentoring"
                                        initial={{ opacity: 0, rotate: -45, scale: 0.5 }}
                                        animate={{ opacity: 1, rotate: 0, scale: 1, 
                                          x: imgIndex === 0 ? 0 : imgIndex === 1 ? -40 : 40,
                                          y: imgIndex === 0 ? 0 : imgIndex === 1 ? 30 : -30
                                        }}
                                        transition={{ delay: 0.1 + imgIndex * 0.15, duration: 0.6, type: "spring" }}
                                        className={`absolute object-cover shadow-xl border border-black/10 dark:border-white/10 ${imgIndex === 0 ? 'w-28 h-28 md:w-32 md:h-32 rounded-2xl z-10' : 'w-16 h-16 md:w-20 md:h-20 rounded-full'}`}
                                      />
                                    ))
                                  )}
                                </div>
                              )}
                            </div>
                          </motion.div>
                        )}
                      </AnimatePresence>
                    </motion.div>
                  );
                })}
              </motion.div>
          </SectionShell>

          {/* 4. Experience (Dark) */}
      
    </PageTransition>
  );
}

export function Experience() {
  return (
    <PageTransition>
              <SectionShell id="experience" label="/EXPERIENCE" watermark="EXPERIENCE" dark={false} footer={
            <div className="w-full flex justify-end">
                <p className="text-blue-600 font-medium"></p>
            </div>
          }>
              <motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: false, amount: 0.4 }} className="w-full flex-1 overflow-y-auto scrollbar-hide space-y-6 md:space-y-8 h-full max-h-full">
                <ScrollIndicator />
                {experienceJobs.map((job, i) => (
                  <motion.div key={i} variants={fadeUp} className={`flex flex-col md:flex-row justify-between gap-4 p-6 rounded-3xl transition-colors ${job.isActive ? 'bg-blue-50 border border-blue-200 shadow-sm' : 'hover:bg-slate-50 dark:hover:bg-zinc-800 dark:bg-zinc-800/50'}`}>
                    <div className="flex-1">
                      <h3 className={`text-xl md:text-2xl font-bold mb-2 ${job.isActive ? 'text-blue-900 dark:text-blue-300' : 'text-slate-900 dark:text-zinc-100'}`}>{job.company}</h3>
                      <p className={`text-base md:text-lg ${job.isActive ? 'text-blue-600' : 'text-slate-600 dark:text-zinc-400 dark:text-zinc-300'}`}>{job.title}</p>
                    </div>
                    <div className="md:text-right flex-1 md:flex-none">
                      <div className="inline-flex items-center gap-2 mb-3">
                        <span className={`w-2 h-2 rounded-full ${job.isActive ? 'bg-blue-600 animate-pulse' : 'bg-slate-300'}`}></span>
                        <span className={`font-mono text-sm font-semibold ${job.isActive ? 'text-blue-600' : 'text-slate-500 dark:text-zinc-400'}`}>{job.date}</span>
                      </div>
                      <p className={`text-sm max-w-sm ml-0 md:ml-auto leading-relaxed ${job.isActive ? 'text-slate-600 dark:text-zinc-400 dark:text-zinc-300' : 'text-slate-500 dark:text-zinc-400'}`}>
                        {job.desc}
                      </p>
                    </div>
                  </motion.div>
                ))}
              </motion.div>
          </SectionShell>

          {/* Testimonials */}
        <SectionShell label="/TESTIMONIALS" watermark="STORIES" dark={true} footer={<GlobalFooter />}>
              <motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: false, amount: 0.2 }} className="w-full relative z-10 flex flex-col justify-center h-full">
                 <motion.div variants={fadeUp} className="w-full">
                    <Testimonials />
                 </motion.div>
              </motion.div>
          </SectionShell>

          {/* 5. Contact (White) */}
      
    </PageTransition>
  );
}

export function Contact() {
  return (
    <PageTransition>
              <div id="contact">
            <LetsWorkTogether />
          </div>
    </PageTransition>
  );
}
