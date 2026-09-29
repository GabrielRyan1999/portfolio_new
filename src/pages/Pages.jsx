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
// Editorial Brutalism Premium Animations
export function RevealLine({ children, delay = 0, className = "" }) {
  return (
    <motion.span
      initial={{ opacity: 0, y: 30 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, amount: 0.3 }}
      transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1], delay }}
      className={`inline-block ${className}`}
    >
      {children}
    </motion.span>
  );
}

export function LineDraw({ className, delay = 0 }) {
  return (
    <motion.div
      initial={{ scaleX: 0 }}
      whileInView={{ scaleX: 1 }}
      viewport={{ once: true, amount: 0.1 }}
      transition={{ duration: 1.5, ease: [0.16, 1, 0.3, 1], delay }}
      style={{ transformOrigin: "left" }}
      className={className}
    />
  );
}

export function ParallaxImage({ src, alt, className = "" }) {
  const ref = React.useRef(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start end", "end start"]
  });
  const y = useTransform(scrollYProgress, [0, 1], ["-15%", "15%"]);

  return (
    <div ref={ref} className="relative w-full h-full overflow-hidden">
      <motion.img 
        style={{ y, scale: 1.25 }}
        src={src} 
        alt={alt}
        className={`absolute inset-0 w-full h-full object-cover ${className}`}
      />
    </div>
  );
}

const Sparkle = ({ className }) => (
  <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" className={className}>
    <path d="M12 0L12.5 11.5L24 12L12.5 12.5L12 24L11.5 12.5L0 12L11.5 11.5L12 0Z" fill="currentColor"/>
  </svg>
);

const fadeUp = {
  hidden: { opacity: 0, y: 40 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.8, ease: [0.16, 1, 0.3, 1] } }
};

const AnimatedWords = ({ words = ['SOFTWARE ENGINEER.', 'EDUCATOR.', 'TECHNOLOGIST.'] }) => {
  const [index, setIndex] = useState(0);
  useEffect(() => {
    const timer = setInterval(() => {
      setIndex((prev) => (prev + 1) % words.length);
    }, 4000);
    return () => clearInterval(timer);
  }, [words]);
  
  return (
    <span className="relative inline-block min-w-[200px]">
      {/* Invisible placeholder to guarantee perfect baseline alignment and height */}
      <span className="opacity-0 pointer-events-none select-none">{words[1]}</span>
      <AnimatePresence mode="popLayout">
        <motion.span
          key={index}
          initial={{ y: 8, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          exit={{ y: -8, opacity: 0 }}
          transition={{ duration: 1.2, ease: [0.22, 1, 0.36, 1] }}
          className="absolute top-0 left-0 text-current"
        >
          {words[index]}
        </motion.span>
      </AnimatePresence>
    </span>
  );
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
      <span className="text-[10px] md:text-xs font-semibold tracking-widest mb-1 md:mb-2 uppercase drop-">Scroll</span>
      <motion.div
        animate={{ y: [0, 8, 0] }}
        transition={{ duration: 1.5, repeat: Infinity, ease: "easeInOut" }}
      >
        <ChevronDown className="w-4 h-4 md:w-5 md:h-5 opacity-70 drop-" />
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
      <a href="https://www.linkedin.com/in/gabrielryan1999/" target="_blank" rel="noreferrer" aria-label="LinkedIn" className="p-2 -m-2 hover:text-[var(--color-brand)] transition-colors"><Linkedin className="w-5 h-5" /></a>
      <a href="https://github.com/GabrielRyan1999" target="_blank" rel="noreferrer" aria-label="GitHub" className="p-2 -m-2 hover:text-[var(--foreground)] transition-colors"><Github className="w-5 h-5" /></a>
      <a href="https://www.instagram.com/heyitsgabrielryan/" target="_blank" rel="noreferrer" aria-label="Instagram" className="p-2 -m-2 hover:text-pink-600 transition-colors"><Instagram className="w-5 h-5" /></a>
    </div>
    <div className="text-sm text-center md:text-right hidden md:block">
      Created with ðŸ’™ by Ryan
    </div>
  </div>
);

export const PageTransition = ({ children }) => (<>{children}</>);


export function Home() {
  return (
    <section id="home" className="relative w-full h-[100svh] min-h-[600px] overflow-hidden bg-cream font-sans">
      
      {/* 
        LAYER 1: BASE (Right Side)
        Background: Cream, Text: Navy 
      */}
      <div className="absolute inset-0 z-0">
        {/* Background Shape */}
        <div className="absolute top-[-10vw] right-[-5vw] w-[40vw] h-[40vw] rounded-full bg-[#E5D5C5]"></div>
        
        {/* Texts */}
        <HomeContent side="right" />
      </div>

      {/* 
        LAYER 2: OVERLAY (Left Side)
        Background: Navy, Text: Cream 
        Clipped to precisely 50% width.
      */}
      <div className="absolute inset-0 bg-navy z-10" style={{ clipPath: 'polygon(0 0, 50% 0, 50% 100%, 0 100%)' }}>
        {/* Background Lines (Concentric Circles) */}
        <div className="absolute bottom-[-20vw] left-[-10vw] w-[40vw] h-[40vw] rounded-full border border-cream/20"></div>
        <div className="absolute bottom-[-30vw] left-[-20vw] w-[60vw] h-[60vw] rounded-full border border-cream/10"></div>
        
        {/* Texts (Exact same component, colors invert due to text-current and bg-navy) */}
        <HomeContent side="left" />
      </div>

      {/* LAYER 3: PORTRAIT (Topmost) */}
      <div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-[90%] md:w-[600px] max-w-3xl flex justify-center z-20 pointer-events-none">
        <img 
          src="/profile-nobg.png" 
          alt="Gabriel Ryan" 
          className="w-full h-auto max-h-[85vh] object-contain object-bottom grayscale drop-shadow-2xl brightness-110 contrast-125" 
        />
      </div>

    </section>
  );
}

function HomeContent({ side }) {
  const isLeft = side === 'left';
  const textColor = isLeft ? 'text-cream' : 'text-navy';
  
  return (
    <div className={`absolute inset-0 flex flex-col items-center justify-center pointer-events-none ${textColor}`}>
      
      {/* Center Typography */}
      <div className="relative w-full flex flex-col items-center justify-center mt-[-15vh]">
        <h1 className="font-serif text-[22vw] md:text-[18vw] font-black tracking-tighter leading-none uppercase z-10 relative">
          GABRIEL
        </h1>
        {/* Cursive text overlapping */}
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 mt-[10vw] ml-[5vw] z-20 opacity-90">
          <span className="font-mayonice text-[18vw] md:text-[14vw] leading-none whitespace-nowrap -rotate-3 inline-block drop-shadow-sm">
            Ryan
          </span>
        </div>
      </div>

      {/* Top Left Meta */}
      <div className="absolute top-8 left-8 md:top-12 md:left-12 flex flex-col gap-1 text-[10px] md:text-xs font-bold tracking-widest uppercase">
        <span>VOL. 01</span>
        <span>OCT / 2026</span>
      </div>

      {/* Top Right Meta */}
      <div className="absolute top-8 right-8 md:top-12 md:right-12 flex flex-col gap-1 text-[10px] md:text-xs font-bold tracking-widest uppercase text-right">
        <span>VISUAL STUDY</span>
        <span>BY GABRIEL RYAN</span>
      </div>

      {/* Bottom Left Meta */}
      <div className="absolute bottom-12 left-8 md:bottom-24 md:left-12 flex flex-col gap-6 text-[10px] md:text-xs font-bold tracking-widest uppercase">
        <span className="opacity-70">ROLE //</span>
        <span className="text-sm md:text-base font-black tracking-widest">EDUCATOR & DEVELOPER.</span>
        <div className="w-12 h-[1px] bg-current opacity-50"></div>
        <span>EST. 2026</span>
      </div>

      {/* Middle Right Stamp */}
      <div className="absolute top-1/2 -translate-y-1/2 right-4 md:right-16 flex items-center gap-2 md:gap-4 mt-24">
        {/* The Stamp Box */}
        <div className="w-20 h-20 md:w-28 md:h-28 bg-[#F5F2EB] p-1.5 md:p-2 shadow-xl border border-navy/10 transform rotate-3 flex items-center justify-center relative">
          <div className="w-full h-full border border-navy/20 flex items-center justify-center overflow-hidden">
             <img src="/favicon.jpg" alt="Author" className="w-full h-full object-cover grayscale contrast-125" onError={(e) => { e.target.style.display = 'none'; e.target.nextSibling.style.display = 'block'; }} />
             <span className="hidden font-serif font-bold text-navy opacity-50 text-2xl">GR</span>
          </div>
        </div>
        {/* Vertical Text */}
        <div className="flex items-center gap-2 text-[8px] md:text-[10px] font-bold tracking-widest uppercase opacity-70" style={{ writingMode: 'vertical-rl' }}>
          <span>FIG. 01 — AUTHOR</span>
        </div>
      </div>

    </div>
  );
}

export function About() {
  return (
    <PageTransition>
      <section id="about-me" className="relative w-full min-h-[100svh] bg-cream text-navy flex flex-col border-t-2 border-navy overflow-hidden">
        
        {/* Header Row */}
        <div className="w-full flex items-center justify-between px-6 md:px-12 py-4 border-b border-navy shrink-0">
           <span className="text-xs font-bold tracking-widest uppercase">Chapter 01 // About Me</span>
           <span className="text-xs font-bold tracking-widest uppercase hidden md:inline-block">Yogyakarta, ID</span>
        </div>

        {/* 2-Column Spread */}
        <div className="flex-1 flex flex-col md:flex-row w-full h-full">
           
           {/* Left Column: Text Content */}
           <div className="w-full md:w-1/2 p-6 md:p-12 lg:p-16 border-b md:border-b-0 md:border-r border-navy flex flex-col justify-center relative overflow-hidden">
               {/* Background Watermark Avatar (Editorial Style) */}
               <div className="absolute -bottom-20 -left-20 w-[400px] h-[400px] opacity-[0.03] pointer-events-none">
                  <img src="/favicon.jpg" loading="lazy" alt="" className="w-full h-full object-cover rounded-full grayscale" />
               </div>

               <motion.div variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: true }} className="relative z-10">
                   <motion.h2 variants={fadeUp} className="font-sans font-black text-6xl md:text-7xl lg:text-8xl tracking-tighter uppercase leading-[0.85] mb-4">
                       Gabriel Ryan<br/>Prima
                   </motion.h2>
                   <motion.div variants={fadeUp} className="font-sans font-bold text-lg md:text-xl text-blue-700 tracking-tight uppercase mb-12">
                       Educator, Developer, & System Builder.
                   </motion.div>
                   
                   <motion.p variants={fadeUp} className="font-serif text-lg md:text-xl leading-relaxed text-navy text-justify mb-8">
                      I work at the intersection of technology and education based in Yogyakarta, Indonesia. My background is in computer engineering, but somewhere along the way teaching became the thing I actually care about, and combining the two has become my life's focus ever since.
                   </motion.p>
                   
                   <motion.div variants={fadeUp} className="mb-8">
                      <h3 className="font-sans font-black text-xl md:text-2xl tracking-tighter uppercase mb-2">Background</h3>
                      <p className="font-serif text-base md:text-lg leading-relaxed text-navy text-justify">
                         I graduated in Computer Engineering, and that technical foundation is why I approach education the way I do: not as content delivery, but as a system you design with intention, one that has to hold up in practice, not just in theory.
                      </p>
                   </motion.div>

                   <motion.div variants={fadeUp}>
                      <h3 className="font-sans font-black text-xl md:text-2xl tracking-tighter uppercase mb-2">Outside of Work</h3>
                      <p className="font-serif text-base md:text-lg leading-relaxed text-navy text-justify">
                         When I'm not building or teaching, I'm usually gaming, gardening, or digging into personal finance and investing.
                      </p>
                   </motion.div>
               </motion.div>
           </div>

           {/* Right Column: 3 Cards (Editorial Grid) */}
           <div className="w-full md:w-1/2 flex flex-col bg-cream">
              
              {/* Row 1: Curriculum Development */}
              <div className="w-full flex-1 min-h-[250px] border-b border-navy p-8 md:p-12 flex flex-col justify-center relative group hover:bg-navy hover:text-cream transition-colors duration-500 cursor-default">
                  <span className="absolute top-6 left-6 md:top-8 md:left-8 text-xs font-mono font-bold tracking-widest uppercase opacity-50 group-hover:opacity-100 transition-opacity">01</span>
                  <h3 className="font-sans font-black text-4xl md:text-5xl lg:text-6xl tracking-tighter uppercase mb-4 leading-[0.9]">Curriculum<br className="hidden md:block"/>Development</h3>
                  <p className="font-serif text-lg md:text-xl leading-relaxed opacity-90 max-w-lg">
                     Designing structured, engaging, and industry-aligned tech learning paths for students of all levels.
                  </p>
              </div>

              {/* Row 2: Modern Web */}
              <div className="w-full flex-1 min-h-[250px] border-b border-navy p-8 md:p-12 flex flex-col justify-center relative group hover:bg-navy hover:text-cream transition-colors duration-500 cursor-default">
                  <span className="absolute top-6 left-6 md:top-8 md:left-8 text-xs font-mono font-bold tracking-widest uppercase opacity-50 group-hover:opacity-100 transition-opacity">02</span>
                  <h3 className="font-sans font-black text-4xl md:text-5xl lg:text-6xl tracking-tighter uppercase mb-4 leading-[0.9]">Modern Web</h3>
                  <p className="font-serif text-lg md:text-xl leading-relaxed opacity-90 max-w-lg">
                     Building fast, scalable full-stack applications.
                  </p>
              </div>

              {/* Row 3: Mentoring */}
              <div className="w-full flex-1 min-h-[250px] p-8 md:p-12 flex flex-col justify-center relative group hover:bg-navy hover:text-cream transition-colors duration-500 cursor-default">
                  <span className="absolute top-6 left-6 md:top-8 md:left-8 text-xs font-mono font-bold tracking-widest uppercase opacity-50 group-hover:opacity-100 transition-opacity">03</span>
                  <h3 className="font-sans font-black text-4xl md:text-5xl lg:text-6xl tracking-tighter uppercase mb-4 leading-[0.9]">Mentoring</h3>
                  <p className="font-serif text-lg md:text-xl leading-relaxed opacity-90 max-w-lg">
                     Guiding the next generation of software engineers.
                  </p>
              </div>

           </div>

        </div>
      </section>
    </PageTransition>
  );
}

export function Work() {
  const [workIndex, setWorkIndex] = useState(0);
  const nextWork = () => setWorkIndex((p) => (p + 1) % workProjects.length);
  const prevWork = () => setWorkIndex((p) => (p - 1 + workProjects.length) % workProjects.length);
  
  return (
    <PageTransition>
      <section id="work" className="relative w-full min-h-[100svh] bg-navy flex flex-col border-t-2 border-cream overflow-hidden text-cream">
        
        {/* Header Row */}
        <div className="w-full flex items-center justify-between px-6 md:px-12 py-4 border-b border-cream/30 shrink-0">
           <span className="text-xs font-bold tracking-widest uppercase">Chapter 02 // Selected Work</span>
           <span className="text-xs font-bold tracking-widest uppercase font-mono">
              0{workIndex + 1} / 0{workProjects.length}
           </span>
        </div>

        {/* Main Spread */}
        <div className="flex-1 flex flex-col md:flex-row w-full h-full relative">
           
           {/* Left Content Half */}
           <div className="w-full md:w-[40%] flex flex-col justify-between border-b md:border-b-0 md:border-r border-cream/30 relative z-10 shrink-0">
               
               {/* Project Details */}
               <div className="p-6 md:p-12 flex-1 flex flex-col justify-center">
                  <AnimatePresence mode="wait">
                    <motion.div
                      key={workIndex}
                      initial={{ opacity: 0, y: 10 }}
                      animate={{ opacity: 1, y: 0 }}
                      exit={{ opacity: 0, y: -10 }}
                      transition={{ duration: 0.3 }}
                      className="flex flex-col"
                    >
                      <div className="text-[10px] md:text-xs font-mono tracking-widest uppercase opacity-70 mb-4 border-b border-cream/30 pb-4">
                        {workProjects[workIndex].tag}
                      </div>
                      
                      <h3 className="font-serif text-5xl md:text-7xl font-black leading-[0.9] tracking-tighter mb-6">
                        {workProjects[workIndex].title}
                      </h3>
                      
                      <p className="font-serif text-base md:text-lg leading-relaxed opacity-90 mb-10">
                        {workProjects[workIndex].desc}
                      </p>
                      
                      {/* Tech Stack */}
                      <div className="flex flex-wrap gap-3 mb-12">
                        {workProjects[workIndex].tech.map(tech => (
                          <span key={tech} className="px-3 py-1 border border-cream/40 text-xs font-bold tracking-widest uppercase">
                            {tech}
                          </span>
                        ))}
                      </div>

                      <a href={workProjects[workIndex].url} target="_blank" rel="noreferrer" className="group flex items-center gap-4 w-fit hover:opacity-70 transition-opacity">
                         <span className="text-sm font-bold tracking-widest uppercase border-b border-cream pb-1">
                           View Live Project
                         </span>
                         <span className="font-mono text-lg leading-none group-hover:translate-x-2 transition-transform">→</span>
                      </a>
                    </motion.div>
                  </AnimatePresence>
               </div>

               {/* Brutalist Navigation Controls */}
               <div className="flex border-t border-cream/30 h-16 md:h-20 shrink-0">
                  <button
                        onClick={prevWork}
                        className="flex-1 border-r border-cream/30 flex items-center justify-center hover:bg-cream hover:text-navy transition-colors group"
                    >
                     <span className="text-xs font-bold tracking-widest uppercase">Previous</span>
                  </button>
                  <button
                        onClick={nextWork}
                        className="flex-1 flex items-center justify-center hover:bg-cream hover:text-navy transition-colors group"
                    >
                     <span className="text-xs font-bold tracking-widest uppercase">Next</span>
                  </button>
               </div>

           </div>
           
           {/* Right Image Half */}
           <div className="w-full md:w-[60%] relative h-[400px] md:h-auto bg-[#0a1526] overflow-hidden">
               <AnimatePresence mode="wait">
                  <motion.div
                      key={workIndex}
                      initial={{ opacity: 0, scale: 1.02 }}
                      animate={{ opacity: 1, scale: 1 }}
                      exit={{ opacity: 0 }}
                      transition={{ duration: 0.6 }}
                      className="absolute inset-0 flex items-center justify-center p-8 md:p-16 lg:p-24"
                  >
                     <div className="relative w-full h-full flex items-center justify-center">
                       {/* Subtle frame behind the image for an editorial look */}
                       <div className="absolute inset-0 border border-cream/10 bg-navy/30 shadow-2xl"></div>
                       
                       <img 
                          src={workProjects[workIndex].img} 
                          alt={workProjects[workIndex].title}
                          className="relative z-10 w-full h-full object-contain object-center grayscale contrast-125 mix-blend-luminosity opacity-80 hover:grayscale-0 hover:mix-blend-normal hover:opacity-100 transition-all duration-700"
                       />
                     </div>
                  </motion.div>
               </AnimatePresence>
               {/* Editorial Corner Mark */}
               <div className="absolute bottom-6 right-6 md:bottom-12 md:right-12 border border-cream/30 bg-navy/80 backdrop-blur-md px-4 py-2 pointer-events-none">
                  <span className="text-[10px] font-mono tracking-widest uppercase">Fig. 0{workIndex + 1}</span>
               </div>
           </div>

        </div>
      </section>
    </PageTransition>
  );
}

export function Service() {
    const [activeServiceIndex, setActiveServiceIndex] = useState(null);
    return (
      <PageTransition>
        <section id="service" className="relative w-full min-h-[100svh] bg-cream flex flex-col border-t-2 border-navy overflow-hidden">
          
          {/* Header Row */}
          <div className="w-full flex items-center justify-between px-6 md:px-12 py-4 border-b border-navy shrink-0 z-20 relative">
             <span className="text-xs font-bold tracking-widest uppercase">Chapter 03 // Services &amp; Expertise</span>
             <span className="text-xs font-bold tracking-widest uppercase hidden md:inline-block">Yogyakarta, ID</span>
          </div>

          <div className="flex-1 flex flex-col w-full py-16 md:py-24 relative">
          
          {/* Header */}
          <div className="w-full max-w-7xl mx-auto px-6 mb-16 md:mb-24 flex flex-col md:flex-row md:items-end justify-between gap-8 z-10">
             <div>
                <h2 className="font-serif text-5xl md:text-7xl lg:text-8xl font-black text-navy tracking-tighter leading-[0.85]">SERVICES<br/>& EXPERTISE</h2>
             </div>
             <p className="max-w-md text-navy/80 font-serif text-lg leading-relaxed border-l-2 border-navy pl-6">
                A rigorous approach to engineering and education. I partner with organizations to build resilient systems and the minds that maintain them.
             </p>
          </div>

          {/* Brutalist Accordion */}
          <div className="w-full flex flex-col z-10 border-b-2 border-navy">
            {[
              { title: "CUSTOM WEB PLATFORMS", desc: "Building fast, scalable, and robust web applications, internal dashboards, and custom platforms tailored to your business needs.", images: ["https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=400&q=80", "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=400&q=80", "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?w=400&q=80"] },
              { title: "EDTECH SOLUTIONS", desc: "Developing custom learning management systems (LMS) and student progress trackers designed with pedagogical best practices.", images: ["https://images.unsplash.com/photo-1501504905252-473c47e087f8?w=400&q=80", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400&q=80", "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=400&q=80"] },
              { title: "CURRICULUM DEV", desc: "Crafting structured, tech-focused syllabi and scalable learning materials for online, hybrid, and offline educational environments.", images: ["https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=400&q=80", "https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=400&q=80", "https://images.unsplash.com/photo-1503694978374-8a2fa686963a?w=400&q=80"] },
              { title: "1-ON-1 TECH MENTORING", desc: "Providing personalized coaching in programming, 3D modeling, and game development for students and professionals looking to level up their skills.", images: ["https://images.unsplash.com/photo-1531482615713-2afd69097998?w=400&q=80", "https://images.unsplash.com/photo-1573164713988-8665fc963095?w=400&q=80", "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=400&q=80"] }
            ].map((service, index) => {
              const isOpen = activeServiceIndex === index;
              return (
                <div key={service.title} className={`w-full border-t-2 border-navy overflow-hidden transition-colors duration-500 ${isOpen ? 'bg-navy text-cream' : 'bg-transparent text-navy'}`}>
                  
                  <button
                      onClick={() => setActiveServiceIndex(isOpen ? null : index)}
                      aria-expanded={isOpen}
                      className={`w-full flex items-center justify-between py-8 md:py-12 px-6 md:px-12 transition-colors ${isOpen ? '' : 'hover:bg-navy/5'}`}
                    >
                      <div className="flex items-center gap-6 md:gap-12">
                        <span className={`text-sm md:text-lg font-mono font-bold ${isOpen ? 'text-cream/50' : 'text-navy/50'}`} aria-hidden="true">
                          0{index + 1}
                        </span>
                        <span className="font-serif text-3xl md:text-5xl lg:text-7xl font-black text-left tracking-tighter uppercase transition-colors">
                          {service.title}
                        </span>
                      </div>
                      
                      <span className={`font-mono text-5xl md:text-7xl font-light leading-none ${isOpen ? 'text-cream' : 'text-navy opacity-30 group-hover:opacity-100'}`}>
                        {isOpen ? "-" : "+"}
                      </span>
                    </button>
      
                  <AnimatePresence initial={false}>
                    {isOpen && (
                      <motion.div
                        id={`service-panel-${index}`}
                        aria-labelledby={`service-button-${index}`}
                        initial="collapsed"
                        animate="open"
                        exit="collapsed"
                        variants={{
                          open: { opacity: 1, height: "auto" },
                          collapsed: { opacity: 0, height: 0 }
                        }}
                        transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
                        className="px-6 md:px-12"
                      >
                        <div className="pb-12 md:pb-16 pt-4 flex flex-col lg:flex-row gap-12 lg:gap-24">
                          
                          {/* Description Side */}
                          <div className="w-full lg:w-1/3">
                             <p className="text-cream/90 text-lg md:text-xl font-serif leading-relaxed">
                               {service.desc}
                             </p>
                          </div>
                          
                          {/* Images Side (Contact Sheet Grid) */}
                          <div className="w-full lg:w-2/3 grid grid-cols-1 sm:grid-cols-3 gap-0 border border-cream/20">
                            {service.images.map((img, i) => (
                              <div key={i} className={`aspect-square relative overflow-hidden bg-[#0a1526] ${i > 0 ? 'border-t sm:border-t-0 sm:border-l border-cream/20' : ''}`}>
                                <img
                                  src={img}
                                  alt=""
                                  loading="lazy"
                                  className="w-full h-full object-cover grayscale contrast-125 hover:grayscale-0 transition-all duration-700 opacity-80 hover:opacity-100 mix-blend-luminosity hover:mix-blend-normal"
                                />
                                <div className="absolute top-2 left-2 bg-cream px-2 py-0.5 pointer-events-none">
                                   <span className="text-[9px] font-mono font-bold text-navy">IMG_0{i+1}</span>
                                </div>
                              </div>
                            ))}
                          </div>

                        </div>
                      </motion.div>
                    )}
                  </AnimatePresence>

                </div>
              );
            })}
          </div>
          </div>
        </section>
      </PageTransition>
    );
}

export function Experience() {
    return (
      <PageTransition>
        <section id="experience" className="relative w-full min-h-[100svh] bg-navy flex flex-col border-t-2 border-cream overflow-hidden text-cream">
          
          {/* Header Row */}
          <div className="w-full flex items-center justify-between px-6 md:px-12 py-4 border-b border-cream shrink-0 z-20 relative">
             <span className="text-xs font-bold tracking-widest uppercase text-cream">Chapter 04 // Professional Record</span>
             <span className="text-xs font-bold tracking-widest uppercase hidden md:inline-block text-cream">Yogyakarta, ID</span>
          </div>

          <div className="flex-1 flex flex-col w-full py-16 md:py-24 relative">
            {/* Header */}
          <div className="w-full max-w-7xl mx-auto px-6 mb-16 md:mb-24 flex flex-col md:flex-row md:items-end justify-between gap-8 z-10">
             <div>
                <h2 className="font-serif text-5xl md:text-7xl lg:text-8xl font-black tracking-tighter leading-[0.85]">PROFESSIONAL<br/>RECORD</h2>
             </div>
             <div className="max-w-md text-cream/80 font-serif text-lg leading-relaxed border-l-2 border-cream pl-6 flex flex-col gap-4">
                <p>A chronological ledger of roles and responsibilities.</p>
                <div className="flex items-center gap-3">
                   <span className="w-2 h-2 bg-rose-500 rounded-none animate-pulse"></span>
                   <span className="text-xs font-mono tracking-widest uppercase opacity-70">Indicates Current Role</span>
                </div>
             </div>
          </div>

          {/* Brutalist Ledger Table */}
          <div className="w-full flex flex-col z-10 border-b-2 border-cream">
            {experienceJobs.map((job, i) => (
              <div key={i} className="flex flex-col md:flex-row border-t-2 border-cream group hover:border-navy hover:bg-cream hover:text-navy transition-colors duration-300">
                 
                 {/* Year Cell */}
                 <div className="w-full md:w-1/4 py-6 md:py-10 px-6 border-b-2 md:border-b-0 md:border-r-2 border-cream group-hover:border-navy transition-colors flex items-center justify-between md:justify-start">
                     <span className="font-mono text-sm md:text-base tracking-widest font-bold opacity-70 group-hover:opacity-100">{job.date}</span>
                     {job.isActive && <span className="w-2 h-2 bg-rose-500 rounded-none animate-pulse md:ml-6"></span>}
                 </div>
                 
                 {/* Company & Title Cell */}
                 <div className="w-full md:w-1/2 py-6 md:py-10 px-6 border-b-2 md:border-b-0 md:border-r-2 border-cream group-hover:border-navy transition-colors flex flex-col justify-center">
                     <h3 className="font-serif text-3xl md:text-5xl lg:text-6xl font-black tracking-tighter mb-2">{job.company}</h3>
                     <p className="font-sans text-xs md:text-sm font-bold tracking-widest uppercase opacity-70 group-hover:opacity-100">{job.title}</p>
                 </div>
                 
                 {/* Description Cell */}
                 <div className="w-full md:w-1/4 py-6 md:py-10 px-6 flex items-center">
                     <p className="font-serif text-base md:text-lg leading-relaxed opacity-80 group-hover:opacity-100">
                        {job.desc}
                     </p>
                 </div>
              </div>
            ))}
          </div>
          </div>
        </section>

        {/* Testimonials Wrapper */}
        <section className="relative w-full min-h-[100svh] bg-cream text-navy flex flex-col border-t-2 border-navy overflow-hidden">
          
          {/* Header Row */}
          <div className="w-full flex items-center justify-between px-6 md:px-12 py-4 border-b border-navy shrink-0 z-20 relative">
             <span className="text-xs font-bold tracking-widest uppercase">Chapter 05 // Testimonials</span>
             <span className="text-xs font-bold tracking-widest uppercase hidden md:inline-block">Yogyakarta, ID</span>
          </div>

          <div className="flex-1 flex flex-col w-full py-16 md:py-24 relative">
           <Testimonials />
        </div>
        </section>

      </PageTransition>
    );
}

// Could not extract new_contact from redesign-contact.py


export function Contact() {
  return (
    <PageTransition>
      <div id="contact">
        <LetsWorkTogether />
      </div>
    </PageTransition>
  );
}







