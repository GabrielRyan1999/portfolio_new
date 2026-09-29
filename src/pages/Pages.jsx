import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence, useReducedMotion } from 'framer-motion';
import { Testimonials } from '../components/ui/unique-testimonial';
import { LetsWorkTogether } from '../components/ui/lets-work-section';
import { experienceJobs, workProjects } from '../data';

// Animation configs
const heroEase = [0.16, 1, 0.3, 1];

const fadeUp = {
  hidden: { opacity: 0, y: 24 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.6, ease: heroEase } }
};

const staggerContainer = {
  hidden: { opacity: 0 },
  visible: { opacity: 1, transition: { staggerChildren: 0.08, delayChildren: 0.05 } }
};

const createHeroVariants = (shouldReduce) => ({
  title: {
    hidden: { opacity: 0, y: shouldReduce ? 0 : 50 },
    visible: {
      opacity: 1,
      y: 0,
      transition: { duration: 0.85, ease: heroEase, delay: 0.1 }
    }
  },
  cursive: {
    hidden: { opacity: 0, y: shouldReduce ? 0 : 25, scale: shouldReduce ? 1 : 0.95 },
    visible: {
      opacity: 0.9,
      y: 0,
      scale: 1,
      transition: { duration: 0.8, ease: heroEase, delay: 0.35 }
    }
  },
  portrait: {
    hidden: { opacity: 0, y: shouldReduce ? 0 : 55, scale: shouldReduce ? 1 : 0.97 },
    visible: {
      opacity: 1,
      y: 0,
      scale: 1,
      transition: { duration: 0.95, ease: heroEase, delay: 0.2 }
    }
  },
  metaTopLeft: {
    hidden: { opacity: 0, y: shouldReduce ? 0 : -12 },
    visible: {
      opacity: 1,
      y: 0,
      transition: { duration: 0.6, ease: heroEase, delay: 0.5 }
    }
  },
  metaTopRight: {
    hidden: { opacity: 0, y: shouldReduce ? 0 : -12 },
    visible: {
      opacity: 1,
      y: 0,
      transition: { duration: 0.6, ease: heroEase, delay: 0.55 }
    }
  },
  metaBottom: {
    hidden: { opacity: 0, y: shouldReduce ? 0 : 20 },
    visible: {
      opacity: 1,
      y: 0,
      transition: { duration: 0.7, ease: heroEase, delay: 0.65 }
    }
  },
  stamp: {
    hidden: { opacity: 0, scale: shouldReduce ? 1 : 0.88, y: shouldReduce ? 0 : 15 },
    visible: {
      opacity: 1,
      scale: 1,
      y: 0,
      transition: { duration: 0.65, ease: heroEase, delay: 0.8 }
    }
  },
  scrollHint: {
    hidden: { opacity: 0, y: shouldReduce ? 0 : 10 },
    visible: {
      opacity: 0.9,
      y: 0,
      transition: { duration: 0.6, ease: heroEase, delay: 1.0 }
    }
  }
});

export const PageTransition = ({ children }) => (<>{children}</>);

const ROLES = [
  "DEVELOPER.",
  "SYSTEM BUILDER.",
  "CURRICULUM ARCHITECT.",
  "TECH MENTOR.",
  "SOFTWARE ENGINEER."
];

export function Home() {
  const [roleIndex, setRoleIndex] = useState(0);
  const shouldReduceMotion = useReducedMotion();
  const heroVariants = createHeroVariants(shouldReduceMotion);

  useEffect(() => {
    const timer = setInterval(() => {
      setRoleIndex((prev) => (prev + 1) % ROLES.length);
    }, 3200);
    return () => clearInterval(timer);
  }, []);

  return (
    <section id="home" className="relative w-full h-[100svh] min-h-[600px] overflow-hidden bg-cream font-sans">
      
      {/* 
        LAYER 1: BASE (Right Side)
      */}
      <div className="absolute inset-0 z-0">
        <div className="absolute top-[-25vw] right-[-15vw] w-[55vw] h-[55vw] rounded-full bg-[#D4C5A5]"></div>
        <HomeBackgroundTypography side="right" variants={heroVariants} />
      </div>

      {/* 
        LAYER 2: OVERLAY (Left Side)
      */}
      <div className="absolute inset-0 bg-navy z-10" style={{ clipPath: 'polygon(0 0, 50% 0, 50% 100%, 0 100%)' }}>
        <div className="absolute bottom-[-15vw] left-[-20vw] w-[50vw] h-[50vw] rounded-full border-[0.5px] border-cream/20"></div>
        <div className="absolute bottom-[-25vw] left-[-30vw] w-[70vw] h-[70vw] rounded-full border-[0.5px] border-cream/10"></div>
        <HomeBackgroundTypography side="left" variants={heroVariants} />
      </div>

      {/* LAYER 3: PORTRAIT (Center Subject) */}
      <motion.div 
        variants={heroVariants.portrait}
        initial="hidden"
        animate="visible"
        className="absolute bottom-0 left-1/2 -translate-x-1/2 w-full flex justify-center z-20 pointer-events-none origin-bottom"
      >
        <img 
          src="/profile-nobg.png" 
          alt="Gabriel Ryan" 
          className="w-[130%] sm:w-[85%] md:w-auto h-auto max-h-[72vh] xl:max-h-[78vh] max-w-[580px] lg:max-w-none object-contain object-bottom grayscale drop-shadow-2xl brightness-105 contrast-125" 
        />
      </motion.div>

      {/* LAYER 4: FRONT EDITORIAL METADATA & UI (Always elevated in front of portrait) */}
      <div className="absolute inset-0 z-30 pointer-events-none">
        
        {/* Top Left Meta (Left side -> Cream) */}
        <motion.div 
          variants={heroVariants.metaTopLeft}
          initial="hidden"
          animate="visible"
          className="absolute top-8 left-8 md:top-12 md:left-12 flex flex-col gap-1 text-[10px] md:text-xs font-bold tracking-[0.2em] uppercase text-cream"
        >
          <span>VOL. 01</span>
          <span>OCT / 2026</span>
        </motion.div>

        {/* Top Right Meta (Right side -> Navy) */}
        <motion.div 
          variants={heroVariants.metaTopRight}
          initial="hidden"
          animate="visible"
          className="absolute top-8 right-8 md:top-12 md:right-12 flex flex-col gap-1 text-[10px] md:text-xs font-bold tracking-[0.2em] uppercase text-right text-navy"
        >
          <span>VISUAL STUDY</span>
          <span>BY GABRIEL RYAN</span>
        </motion.div>

        {/* Bottom Left Meta (Role & Est. - 2-line vertical stack, never occluded by portrait) */}
        <motion.div 
          variants={heroVariants.metaBottom}
          initial="hidden"
          animate="visible"
          className="absolute bottom-10 left-6 sm:left-8 md:bottom-20 md:left-12 flex flex-col gap-3 sm:gap-4 md:gap-5 text-[10px] md:text-xs font-bold tracking-[0.15em] uppercase text-cream max-w-[200px] sm:max-w-[240px] md:max-w-xs"
        >
          <span className="opacity-70 tracking-[0.2em] text-[9px] sm:text-[10px] md:text-xs">ROLE //</span>
          <div className="flex flex-col text-xs sm:text-sm md:text-base font-black tracking-[0.08em] drop-shadow-md leading-tight">
            <span className="whitespace-nowrap">EDUCATOR &amp;</span>
            <span className="relative inline-grid [grid-template-areas:'stack'] overflow-hidden h-[1.3em]">
              <AnimatePresence mode="popLayout" initial={false}>
                <motion.span
                  key={roleIndex}
                  initial={{ y: "100%", opacity: 0 }}
                  animate={{ y: "0%", opacity: 1 }}
                  exit={{ y: "-100%", opacity: 0 }}
                  transition={{ duration: 0.5, ease: heroEase }}
                  className="[grid-area:stack] inline-block whitespace-nowrap text-cream"
                >
                  {ROLES[roleIndex]}
                </motion.span>
              </AnimatePresence>
            </span>
          </div>
          <div className="w-10 sm:w-12 h-[1px] bg-cream opacity-50"></div>
          <span className="tracking-[0.2em] text-[9px] sm:text-[10px] md:text-xs">EST. 2020</span>
        </motion.div>

        {/* Middle Right Stamp (Right side -> Navy & Cream card) */}
        <motion.div 
          variants={heroVariants.stamp}
          initial="hidden"
          animate="visible"
          className="absolute top-[45%] md:top-1/2 -translate-y-1/2 right-6 sm:right-10 md:right-24 flex items-center mt-12 md:mt-24 pointer-events-auto"
        >
          <div className="relative w-16 h-16 sm:w-20 sm:h-20 md:w-28 md:h-28 z-10">
            <div className="absolute inset-0 bg-navy/15 transform translate-x-2 translate-y-2 md:translate-x-3 md:translate-y-3"></div>
            <div className="absolute inset-0 bg-cream p-2 shadow-sm border border-navy/30 flex items-center justify-center">
              <img src="/favicon.jpg" alt="Author" className="w-full h-full object-cover grayscale contrast-125 bg-gray-200" onError={(e) => { e.target.src = 'https://api.dicebear.com/7.x/notionists/svg?seed=Gabriel&backgroundColor=e5e5e5'; }} />
            </div>
          </div>
          <div className="absolute right-[-3.8rem] sm:right-[-4.5rem] md:right-[-5.5rem] top-1/2 -translate-y-1/2 origin-center rotate-90 text-[8px] md:text-[9px] font-bold tracking-[0.25em] uppercase text-navy opacity-70 whitespace-nowrap drop-shadow-md">
            FIG. 01 // AUTHOR
          </div>
        </motion.div>

        {/* Scroll Hint */}
        <motion.div variants={heroVariants.scrollHint} initial="hidden" animate="visible">
          <ScrollHint />
        </motion.div>
      </div>
    </section>
  );
}

function ScrollHint() {
  return (
    <div className="absolute bottom-6 md:bottom-10 left-1/2 -translate-x-1/2 flex flex-col items-center gap-3 opacity-90 drop-shadow-md">
      <span className="text-[7px] md:text-[9px] font-bold tracking-[0.4em] uppercase whitespace-nowrap text-cream">
        Scroll to explore
      </span>
      <div className="w-[1px] h-8 md:h-12 bg-cream/60 overflow-hidden relative">
        <motion.div 
          className="absolute top-0 left-0 w-full h-[50%] bg-cream"
          animate={{ y: ["-100%", "200%"] }}
          transition={{ duration: 1.5, repeat: Infinity, ease: "easeInOut" }}
        />
      </div>
    </div>
  );
}

function HomeBackgroundTypography({ side, variants }) {
  const isLeft = side === 'left';
  
  const gabrielColor = isLeft ? 'text-cream' : 'text-navy';
  const ryanColor = isLeft ? 'text-cream' : 'text-[#C9B996]';
  
  return (
    <div className="absolute inset-0 flex flex-col pointer-events-none">
      {/* Center Typography */}
      <div className="absolute top-[25%] md:top-[12%] left-0 w-full flex flex-col items-center justify-start">
        <motion.h1 
          variants={variants?.title}
          initial="hidden"
          animate="visible"
          className={`font-serif text-[26vw] md:text-[17vw] font-black tracking-[-0.04em] leading-[0.8] uppercase z-10 relative ${gabrielColor}`}
        >
          GABRIEL
        </motion.h1>
        {/* Cursive text overlapping */}
        <motion.div 
          variants={variants?.cursive}
          initial="hidden"
          animate="visible"
          className={`absolute top-[60%] md:top-[40%] left-1/2 -translate-x-1/2 mt-[2vw] ml-[6vw] z-20 opacity-90 ${ryanColor}`}
        >
          <span className="font-mayonice text-[35vw] md:text-[17vw] leading-none whitespace-nowrap -rotate-[5deg] inline-block drop-shadow-sm">
            Ryan
          </span>
        </motion.div>
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
                   <motion.h2 variants={fadeUp} className="font-sans font-black text-5xl sm:text-6xl md:text-5xl lg:text-6xl xl:text-7xl 2xl:text-8xl tracking-tighter uppercase leading-[0.85] mb-4">
                       Gabriel Ryan<br/>Prima
                   </motion.h2>
                   <motion.div variants={fadeUp} className="font-sans font-bold text-lg md:text-xl text-navy tracking-tight uppercase mb-12">
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
           <motion.div 
             variants={staggerContainer}
             initial="hidden"
             whileInView="visible"
             viewport={{ once: true, margin: "-60px" }}
             className="w-full md:w-1/2 flex flex-col bg-cream"
           >
              
              {/* Row 1: Curriculum Development */}
              <motion.div variants={fadeUp} className="w-full flex-1 min-h-[250px] border-b border-navy p-8 md:p-12 flex flex-col justify-center relative group hover:bg-navy hover:text-cream transition-colors duration-500 cursor-default">
                  <span className="absolute top-6 left-6 md:top-8 md:left-8 text-xs font-mono font-bold tracking-widest uppercase opacity-50 group-hover:opacity-100 transition-opacity">01</span>
                  <h3 className="font-sans font-black text-4xl md:text-5xl lg:text-6xl tracking-tighter uppercase mb-4 leading-[0.9]">Curriculum<br className="hidden md:block"/>Development</h3>
                  <p className="font-serif text-lg md:text-xl leading-relaxed opacity-90 max-w-lg">
                     Designing structured, engaging, and industry-aligned tech learning paths for students of all levels.
                  </p>
              </motion.div>

              {/* Row 2: Modern Web */}
              <motion.div variants={fadeUp} className="w-full flex-1 min-h-[250px] border-b border-navy p-8 md:p-12 flex flex-col justify-center relative group hover:bg-navy hover:text-cream transition-colors duration-500 cursor-default">
                  <span className="absolute top-6 left-6 md:top-8 md:left-8 text-xs font-mono font-bold tracking-widest uppercase opacity-50 group-hover:opacity-100 transition-opacity">02</span>
                  <h3 className="font-sans font-black text-4xl md:text-5xl lg:text-6xl tracking-tighter uppercase mb-4 leading-[0.9]">Modern Web</h3>
                  <p className="font-serif text-lg md:text-xl leading-relaxed opacity-90 max-w-lg">
                     Building fast, scalable full-stack applications.
                  </p>
              </motion.div>

              {/* Row 3: Mentoring */}
              <motion.div variants={fadeUp} className="w-full flex-1 min-h-[250px] p-8 md:p-12 flex flex-col justify-center relative group hover:bg-navy hover:text-cream transition-colors duration-500 cursor-default">
                  <span className="absolute top-6 left-6 md:top-8 md:left-8 text-xs font-mono font-bold tracking-widest uppercase opacity-50 group-hover:opacity-100 transition-opacity">03</span>
                  <h3 className="font-sans font-black text-4xl md:text-5xl lg:text-6xl tracking-tighter uppercase mb-4 leading-[0.9]">Mentoring</h3>
                  <p className="font-serif text-lg md:text-xl leading-relaxed opacity-90 max-w-lg">
                     Guiding the next generation of software engineers.
                  </p>
              </motion.div>

           </motion.div>

        </div>
      </section>
    </PageTransition>
  );
}

export function Work() {
  const [workIndex, setWorkIndex] = useState(0);
  const nextWork = () => setWorkIndex((p) => (p + 1) % workProjects.length);
  const prevWork = () => setWorkIndex((p) => (p - 1 + workProjects.length) % workProjects.length);

  useEffect(() => {
    const handleKeyDown = (e) => {
      if (['INPUT', 'TEXTAREA'].includes(document.activeElement?.tagName)) return;
      if (e.key === 'ArrowRight') {
        nextWork();
      } else if (e.key === 'ArrowLeft') {
        prevWork();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);
  
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

        {/* Project Selector Tabs Strip */}
        <motion.div 
          variants={fadeUp}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: "-40px" }}
          className="w-full flex flex-wrap border-b border-cream/30 bg-navy/80 shrink-0"
        >
          {workProjects.map((p, idx) => {
            const isSelected = workIndex === idx;
            return (
              <button
                key={p.title}
                onClick={() => setWorkIndex(idx)}
                className={`flex-1 min-w-[200px] py-3.5 px-4 md:px-8 font-mono text-[11px] md:text-xs tracking-widest uppercase text-left transition-colors cursor-pointer border-r last:border-r-0 border-cream/30 flex items-center justify-between group ${
                  isSelected
                    ? 'bg-cream text-navy font-black shadow-[inset_0px_2px_0px_0px_#1E4E8C]'
                    : 'text-cream/70 hover:text-cream hover:bg-cream/10'
                }`}
              >
                <span className="truncate">
                  0{idx + 1} // {p.title}
                </span>
                <span className={`text-[10px] tracking-wider ml-2 hidden sm:inline ${isSelected ? 'text-navy/70' : 'text-cream/50'}`}>
                  {p.tag}
                </span>
              </button>
            );
          })}
        </motion.div>

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
                      </a>
                    </motion.div>
                  </AnimatePresence>
               </div>

               {/* Brutalist Navigation Controls */}
               <div className="flex border-t border-cream/30 h-16 md:h-20 shrink-0">
                  <button
                        onClick={prevWork}
                        className="flex-1 border-r border-cream/30 flex items-center justify-center hover:bg-cream hover:text-navy transition-colors group cursor-pointer"
                    >
                     <span className="text-xs font-bold tracking-widest uppercase">Previous</span>
                  </button>
                  <button
                        onClick={nextWork}
                        className="flex-1 flex items-center justify-center hover:bg-cream hover:text-navy transition-colors group cursor-pointer"
                    >
                     <span className="text-xs font-bold tracking-widest uppercase">Next</span>
                  </button>
               </div>

           </div>
           
           {/* Right Image Half */}
           <div className="w-full md:w-[60%] relative h-[400px] md:h-auto bg-[#153966] overflow-hidden">
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
          <motion.div 
            variants={staggerContainer}
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, margin: "-60px" }}
            className="w-full max-w-7xl mx-auto px-6 mb-16 md:mb-24 flex flex-col md:flex-row md:items-end justify-between gap-8 z-10"
          >
             <motion.div variants={fadeUp}>
                <h2 className="font-serif text-5xl md:text-7xl lg:text-8xl font-black text-navy tracking-tighter leading-[0.85]">SERVICES<br/>& EXPERTISE</h2>
             </motion.div>
             <motion.p variants={fadeUp} className="max-w-md text-navy/80 font-serif text-lg leading-relaxed border-l-2 border-navy pl-6">
                A rigorous approach to engineering and education. I partner with organizations to build resilient systems and the minds that maintain them.
             </motion.p>
          </motion.div>

          {/* Brutalist Accordion */}
          <motion.div 
            variants={staggerContainer}
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, margin: "-40px" }}
            className="w-full flex flex-col z-10 border-b-2 border-navy"
          >
            {[
              { 
                title: "CUSTOM WEB PLATFORMS", 
                desc: "Building fast, scalable, and robust web applications, internal dashboards, and custom platforms tailored to your business needs.", 
                images: ["/projects/mentor-reporting.svg", "/projects/reminder-app.svg", "/projects/ryans-toolkit.svg"] 
              },
              { 
                title: "EDTECH SOLUTIONS", 
                desc: "Developing custom learning management systems (LMS) and student progress trackers designed with pedagogical best practices.", 
                images: ["/projects/mentor-reporting.svg", "/gallery_1.jpg", "/gallery_2.jpg"] 
              },
              { 
                title: "CURRICULUM DEV", 
                desc: "Crafting structured, tech-focused syllabi and scalable learning materials for online, hybrid, and offline educational environments.", 
                images: ["/gallery_1.jpg", "/gallery_3.jpg", "/gallery_4.jpg"] 
              },
              { 
                title: "1-ON-1 TECH MENTORING", 
                desc: "Providing personalized coaching in programming, 3D modeling, and game development for students and professionals looking to level up their skills.", 
                images: ["/gallery_2.jpg", "/gallery_4.jpg", "/gallery_5.jpg"] 
              }
            ].map((service, index) => {
              const isOpen = activeServiceIndex === index;
              return (
                <motion.div 
                  variants={fadeUp}
                  key={service.title} 
                  className={`w-full border-t-2 border-navy overflow-hidden transition-colors duration-500 ${isOpen ? 'bg-navy text-cream' : 'bg-transparent text-navy'}`}
                >
                  
                  <button
                      id={`service-button-${index}`}
                      onClick={() => setActiveServiceIndex(isOpen ? null : index)}
                      aria-expanded={isOpen}
                      aria-controls={`service-panel-${index}`}
                      className={`w-full flex items-center justify-between py-8 md:py-12 px-6 md:px-12 transition-colors cursor-pointer ${isOpen ? '' : 'hover:bg-navy/5'}`}
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
                              <div key={i} className={`aspect-square relative overflow-hidden bg-[#153966] ${i > 0 ? 'border-t sm:border-t-0 sm:border-l border-cream/20' : ''}`}>
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

                </motion.div>
              );
            })}
          </motion.div>
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
          <motion.div 
            variants={staggerContainer}
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, margin: "-60px" }}
            className="w-full max-w-7xl mx-auto px-6 mb-16 md:mb-24 flex flex-col md:flex-row md:items-end justify-between gap-8 z-10"
          >
             <motion.div variants={fadeUp}>
                <h2 className="font-serif text-5xl md:text-7xl lg:text-8xl font-black tracking-tighter leading-[0.85]">PROFESSIONAL<br/>RECORD</h2>
             </motion.div>
             <motion.div variants={fadeUp} className="max-w-md text-cream/80 font-serif text-lg leading-relaxed border-l-2 border-cream pl-6 flex flex-col gap-4">
                <p>A chronological ledger of roles and responsibilities.</p>
                <div className="flex items-center gap-3">
                   <span className="w-2 h-2 bg-rose-500 rounded-none animate-pulse"></span>
                   <span className="text-xs font-mono tracking-widest uppercase opacity-70">Indicates Current Role</span>
                </div>
             </motion.div>
          </motion.div>

          {/* Brutalist Ledger Table */}
          <motion.div 
            variants={staggerContainer}
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, margin: "-40px" }}
            className="w-full flex flex-col z-10 border-b-2 border-cream"
          >
            {experienceJobs.map((job, i) => (
              <motion.div 
                variants={fadeUp}
                key={i} 
                className="flex flex-col md:flex-row border-t-2 border-cream group hover:border-navy hover:bg-cream hover:text-navy transition-colors duration-300"
              >
                 
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
              </motion.div>
            ))}
          </motion.div>
          </div>
        </section>

        {/* Testimonials Wrapper */}
        <section id="testimonials" className="relative w-full min-h-[100svh] bg-cream text-navy flex flex-col border-t-2 border-navy overflow-hidden">
          
          {/* Header Row */}
          <div className="w-full flex items-center justify-between px-6 md:px-12 py-4 border-b border-navy shrink-0 z-20 relative">
             <span className="text-xs font-bold tracking-widest uppercase">Chapter 05 // Testimonials</span>
             <span className="text-xs font-bold tracking-widest uppercase hidden md:inline-block">Yogyakarta, ID</span>
          </div>

          <div className="flex-1 flex flex-col w-full py-16 md:py-24 relative">
            {/* Header */}
            <motion.div 
              variants={staggerContainer}
              initial="hidden"
              whileInView="visible"
              viewport={{ once: true, margin: "-60px" }}
              className="w-full max-w-7xl mx-auto px-6 mb-12 md:mb-16 flex flex-col md:flex-row md:items-end justify-between gap-8 z-10"
            >
               <motion.div variants={fadeUp}>
                  <span className="text-xs font-mono font-bold tracking-widest uppercase opacity-70 block mb-2">VERIFIED FIELD REPORTS</span>
                  <h2 className="font-serif text-5xl md:text-7xl lg:text-8xl font-black tracking-tighter leading-[0.85]">
                     TESTIMONIALS<br/>& ARCHIVES
                  </h2>
               </motion.div>
               <motion.div variants={fadeUp} className="max-w-md text-navy/80 font-serif text-lg leading-relaxed border-l-2 border-navy pl-6 flex flex-col gap-2">
                  <p>Direct observations and endorsements from partner schools and edtech platforms.</p>
                  <span className="text-xs font-mono tracking-widest uppercase opacity-60">OFFICIAL ENDORSEMENTS</span>
               </motion.div>
            </motion.div>

            <motion.div variants={fadeUp} initial="hidden" whileInView="visible" viewport={{ once: true, margin: "-40px" }}>
              <Testimonials />
            </motion.div>
          </div>
        </section>

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
