import React, { useState, useEffect, useRef, useLayoutEffect } from 'react';
import { motion, AnimatePresence, useReducedMotion, MotionConfig } from 'framer-motion';
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
  // Toggle between HomeOptionA, HomeOptionB, or HomeOriginal
  return <HomeOptionB />;
}

export function HomeOptionB() {
  const [roleIndex, setRoleIndex] = useState(0);
  const [stage, setStage] = useState('center');
  const h1Ref = useRef(null);
  const [offsetY, setOffsetY] = useState(() => {
    if (typeof window !== 'undefined') {
      return Math.round(window.innerHeight / 2 - 80);
    }
    return 320;
  });

  useEffect(() => {
    const timer = setInterval(() => {
      setRoleIndex((prev) => (prev + 1) % ROLES.length);
    }, 3200);
    return () => clearInterval(timer);
  }, []);

  useLayoutEffect(() => {
    const measureOffset = () => {
      if (h1Ref.current) {
        const header = h1Ref.current.closest('header');
        if (header) {
          const headerRect = header.getBoundingClientRect();
          const naturalCenter = headerRect.top + (h1Ref.current.offsetTop || 35) + (h1Ref.current.offsetHeight / 2);
          const screenCenter = window.innerHeight / 2;
          const delta = screenCenter - naturalCenter;
          if (delta > 0) {
            setOffsetY(Math.round(delta));
          }
        }
      }
    };

    measureOffset();
    window.addEventListener('resize', measureOffset);
    return () => window.removeEventListener('resize', measureOffset);
  }, []);

  useEffect(() => {
    // Stage 1: GABRIEL RYAN appears at screen center for 900ms
    const moveTimer = setTimeout(() => {
      setStage('moving');
    }, 900);

    // Stage 2: Once docked at top, reveal all remaining broadsheet content
    const readyTimer = setTimeout(() => {
      setStage('ready');
    }, 1850);

    return () => {
      clearTimeout(moveTimer);
      clearTimeout(readyTimer);
    };
  }, []);

  const handleScrollClick = (id = 'about-me') => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  };

  const isReady = stage === 'ready';

  return (
    <MotionConfig reducedMotion="never">
    <section id="home" className="relative w-full h-[100svh] min-h-[600px] max-h-[100svh] bg-cream text-navy font-sans select-none flex flex-col justify-between p-3 sm:p-4 md:p-5 lg:p-6 border-b-2 border-navy overflow-hidden">
      
      {/* Editorial Canvas Outer Inset Frame & Corner Crosshairs */}
      <motion.div 
        initial={{ opacity: 0 }}
        animate={{ opacity: isReady ? 1 : 0.3 }}
        transition={{ duration: 1.2, ease: "easeOut" }}
        className="absolute inset-2 sm:inset-3 md:inset-4 border border-navy/15 pointer-events-none z-0"
      >
        <motion.div initial={{ opacity: 0, scale: 0.5 }} animate={{ opacity: isReady ? 1 : 0.4, scale: isReady ? 1 : 0.7 }} transition={{ delay: 0.1, duration: 0.4 }} className="absolute -top-1 -left-1 font-mono text-[8px] text-navy/40 leading-none select-none">+</motion.div>
        <motion.div initial={{ opacity: 0, scale: 0.5 }} animate={{ opacity: isReady ? 1 : 0.4, scale: isReady ? 1 : 0.7 }} transition={{ delay: 0.15, duration: 0.4 }} className="absolute -top-1 -right-1 font-mono text-[8px] text-navy/40 leading-none select-none">+</motion.div>
        <motion.div initial={{ opacity: 0, scale: 0.5 }} animate={{ opacity: isReady ? 1 : 0.4, scale: isReady ? 1 : 0.7 }} transition={{ delay: 0.2, duration: 0.4 }} className="absolute -bottom-1 -left-1 font-mono text-[8px] text-navy/40 leading-none select-none">+</motion.div>
        <motion.div initial={{ opacity: 0, scale: 0.5 }} animate={{ opacity: isReady ? 1 : 0.4, scale: isReady ? 1 : 0.7 }} transition={{ delay: 0.25, duration: 0.4 }} className="absolute -bottom-1 -right-1 font-mono text-[8px] text-navy/40 leading-none select-none">+</motion.div>
      </motion.div>

      {/* TOP: Broadsheet Masthead with Center-to-Dock Animation */}
      <header className="relative z-20 w-full pt-1 shrink-0">
        {/* Top Dateline */}
        <motion.div 
          initial={{ opacity: 0, y: -8 }}
          animate={{ opacity: isReady ? 1 : 0, y: isReady ? 0 : -8 }}
          transition={{ duration: 0.6, ease: heroEase }}
          className="flex items-center justify-between text-[8px] sm:text-[9px] md:text-[10px] font-mono tracking-[0.25em] uppercase text-navy/70 pb-1.5"
        >
          <span>THE RYAN CHRONICLE // VOL. 01</span>
          <span className="hidden sm:inline">INDEPENDENT FOLIO OF SOFTWARE &amp; PEDAGOGY</span>
          <span>YOGYAKARTA, OCT 2026</span>
        </motion.div>

        {/* Dateline Separator Line Draw */}
        <motion.div 
          initial={{ scaleX: 0 }}
          animate={{ scaleX: isReady ? 1 : 0 }}
          transition={{ duration: 0.8, ease: heroEase }}
          className="w-full h-[1px] bg-navy/30 origin-left"
        />

        {/* Giant Newspaper Masthead with Centered Welcome to Dock Animation */}
        <div className="py-1 sm:py-2 md:py-2.5 text-center relative z-20">
          <motion.h1 
            ref={h1Ref}
            initial={{ opacity: 0, scale: 0.98, y: offsetY }}
            animate={{ 
              opacity: 1, 
              scale: stage === 'center' ? 1.04 : 1,
              y: stage === 'center' ? offsetY : 0
            }}
            transition={{ 
              y: { duration: 0.95, ease: heroEase },
              scale: { duration: 0.95, ease: heroEase },
              opacity: { duration: 0.6, ease: "easeOut" }
            }}
            className="font-serif text-4xl sm:text-6xl md:text-7xl lg:text-8xl xl:text-9xl font-black tracking-[-0.04em] uppercase text-navy leading-none selection:bg-navy selection:text-cream pointer-events-auto"
          >
            GABRIEL RYAN
          </motion.h1>
        </div>

        {/* Sub-Masthead Hairline Draw */}
        <motion.div 
          initial={{ scaleX: 0 }}
          animate={{ scaleX: isReady ? 1 : 0 }}
          transition={{ duration: 0.85, ease: heroEase }}
          className="w-full h-[1px] bg-navy/30 origin-center"
        />

        {/* Sub-Masthead Ticker Bar with Live Pulse Beacon */}
        <motion.div 
          initial={{ opacity: 0 }}
          animate={{ opacity: isReady ? 1 : 0 }}
          transition={{ duration: 0.6, ease: heroEase }}
          className="flex items-center justify-between text-[8px] sm:text-[9px] md:text-[10px] font-mono tracking-[0.2em] uppercase text-navy/80 py-1.5"
        >
          <div className="flex items-center gap-2">
            <span className="relative flex h-2 w-2">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-navy/50 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2 w-2 bg-navy"></span>
            </span>
            <span>DISPATCH NO. 01</span>
          </div>
          <span className="hidden md:inline font-serif italic text-xs tracking-normal font-normal">
            &ldquo;Bridging rigorous pedagogical discipline and software craftsmanship.&rdquo;
          </span>
          <span>CIRCULATION: GLOBAL</span>
        </motion.div>

        {/* Sub-Masthead Bottom Hairline Rule */}
        <motion.div 
          initial={{ scaleX: 0 }}
          animate={{ scaleX: isReady ? 1 : 0 }}
          transition={{ duration: 0.9, ease: heroEase }}
          className="w-full h-[2px] bg-navy origin-center"
        />
      </header>

      {/* CENTER: 3-Column Broadsheet Grid with Vertical Hairline Draws */}
      <div className="relative z-10 w-full flex-1 min-h-0 py-2 md:py-3.5 grid grid-cols-1 md:grid-cols-12 gap-4 md:gap-0 items-stretch overflow-hidden">
        
        {/* Col 1 (Left): Lead Editorial Dispatch & Philosophy (Cols 1-3) */}
        <div className="md:col-span-3 relative flex flex-col justify-between md:pr-4 lg:pr-6 gap-3 min-h-0 overflow-hidden">
          {/* Vertical Separator Line Draw */}
          <motion.div 
            initial={{ scaleY: 0 }}
            animate={{ scaleY: isReady ? 1 : 0 }}
            transition={{ duration: 0.95, delay: 0.1, ease: heroEase }}
            className="hidden md:block absolute right-0 top-0 bottom-0 w-[1px] bg-navy/20 origin-top pointer-events-none"
          />

          <div className="flex flex-col gap-2.5">
            <motion.h2 
              initial={{ opacity: 0, y: 16 }}
              animate={{ opacity: isReady ? 1 : 0, y: isReady ? 0 : 16 }}
              transition={{ duration: 0.7, delay: 0.1, ease: heroEase }}
              className="font-serif text-base sm:text-lg md:text-xl font-bold leading-[1.15] text-navy tracking-tight"
            >
              Cultivating Systems Builders &amp; Software Craftsmen.
            </motion.h2>
            <motion.p 
              initial={{ opacity: 0, y: 12 }}
              animate={{ opacity: isReady ? 1 : 0, y: isReady ? 0 : 12 }}
              transition={{ duration: 0.7, delay: 0.2, ease: heroEase }}
              className="text-xs sm:text-[13px] font-sans text-navy/80 leading-relaxed"
            >
              Based in Yogyakarta. Structuring foundational computer science, architectural discipline, and human-centered engineering to bridge theory with production craftsmanship.
            </motion.p>
          </div>

          {/* Authentic Editorial Philosophy Quote */}
          <motion.div 
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: isReady ? 1 : 0, y: isReady ? 0 : 10 }}
            transition={{ duration: 0.7, delay: 0.3, ease: heroEase }}
            className="pt-3 border-t border-navy/15 flex flex-col gap-2 font-mono text-[9px] sm:text-[10px] text-navy/70"
          >
            <div className="flex items-center gap-2 text-navy/50 text-[8px] uppercase tracking-widest">
              <span>PHILOSOPHY //</span>
              <div className="flex-1 h-[1px] bg-navy/20"></div>
            </div>
            <blockquote className="font-serif italic text-xs sm:text-[13px] text-navy/85 leading-snug">
              &ldquo;Software architecture is the deliberate design of clarity, resilience, and human understanding.&rdquo;
            </blockquote>
            <span className="text-[8px] font-mono tracking-widest uppercase opacity-50 pt-0.5">
              EST. 2020 // YOGYAKARTA ARCHIVE
            </span>
          </motion.div>
        </div>

        {/* Col 2 (Center): The Studio Portrait - Exact Viewport Fit with Grand Reveal */}
        <div className="md:col-span-6 flex flex-col items-center justify-end px-2 md:px-4 relative h-full min-h-0 overflow-hidden">
          <div className="relative w-full h-full flex items-end justify-center overflow-hidden">
            <motion.img 
              initial={{ opacity: 0, y: 45, scale: 0.96 }}
              animate={{ 
                opacity: isReady ? 1 : 0, 
                y: isReady ? 0 : 45, 
                scale: isReady ? 1 : 0.96 
              }}
              transition={{ duration: 1.05, delay: 0.1, ease: heroEase }}
              src="/profile-nobg.png" 
              alt="Gabriel Ryan - Broadsheet Portrait" 
              className="w-auto h-full max-h-full object-contain object-bottom grayscale contrast-[1.18] brightness-[1.03] drop-shadow-[0_16px_32px_rgba(21,57,102,0.18)]"
            />
            {/* Dateline Overlay Tag with Stamp Reveal */}
            <motion.div 
              initial={{ opacity: 0, scale: 0.9, y: 8 }}
              animate={{ 
                opacity: isReady ? 1 : 0, 
                scale: isReady ? 1 : 0.9, 
                y: isReady ? 0 : 8 
              }}
              transition={{ duration: 0.55, delay: 0.45, ease: heroEase }}
              className="absolute bottom-2 left-2 px-2 py-0.5 bg-cream/95 backdrop-blur-sm border border-navy/30 font-mono text-[8px] uppercase tracking-widest text-navy shadow-sm z-10"
            >
              FIG. 01 // STUDIO PORTRAIT — YOGYAKARTA
            </motion.div>
          </div>
        </div>

        {/* Col 3 (Right): Active Practice, Rotating Role & Dispatch Index (Cols 9-12) */}
        <div className="md:col-span-3 relative flex flex-col justify-between md:pl-4 lg:pl-6 gap-3 min-h-0 overflow-hidden">
          {/* Vertical Separator Line Draw */}
          <motion.div 
            initial={{ scaleY: 0 }}
            animate={{ scaleY: isReady ? 1 : 0 }}
            transition={{ duration: 0.95, delay: 0.15, ease: heroEase }}
            className="hidden md:block absolute left-0 top-0 bottom-0 w-[1px] bg-navy/20 origin-top pointer-events-none"
          />

          <div className="flex flex-col gap-2.5">
            <motion.div 
              initial={{ opacity: 0, y: 16 }}
              animate={{ opacity: isReady ? 1 : 0, y: isReady ? 0 : 16 }}
              transition={{ duration: 0.7, delay: 0.15, ease: heroEase }}
              className="flex flex-col gap-1"
            >
              <span className="font-mono text-[9px] uppercase tracking-[0.2em] text-navy/60">ACTIVE PRACTICE</span>
              <div className="flex flex-col text-sm sm:text-base lg:text-lg font-black tracking-wide text-navy">
                <span>EDUCATOR &amp;</span>
                <span className="relative inline-grid [grid-template-areas:'stack'] overflow-hidden h-[1.3em]">
                  <AnimatePresence mode="popLayout" initial={false}>
                    <motion.span
                      key={roleIndex}
                      initial={{ y: "100%", opacity: 0 }}
                      animate={{ y: "0%", opacity: 1 }}
                      exit={{ y: "-100%", opacity: 0 }}
                      transition={{ duration: 0.55, ease: heroEase }}
                      className="[grid-area:stack] inline-block whitespace-nowrap text-navy underline decoration-navy/40 underline-offset-4"
                    >
                      {ROLES[roleIndex]}
                    </motion.span>
                  </AnimatePresence>
                </span>
              </div>
            </motion.div>

            <motion.p 
              initial={{ opacity: 0, y: 12 }}
              animate={{ opacity: isReady ? 1 : 0, y: isReady ? 0 : 12 }}
              transition={{ duration: 0.7, delay: 0.25, ease: heroEase }}
              className="text-xs sm:text-[13px] font-sans text-navy/80 leading-relaxed pt-0.5"
            >
              Structuring technical learning paths while engineering responsive distributed web platforms.
            </motion.p>
          </div>

          {/* Broadsheet Index Table with Interactive Motion */}
          <motion.div 
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: isReady ? 1 : 0, y: isReady ? 0 : 10 }}
            transition={{ duration: 0.7, delay: 0.35, ease: heroEase }}
            className="pt-3 border-t border-navy/15 flex flex-col gap-1 font-mono text-[9px] sm:text-[10px] uppercase tracking-[0.15em] text-navy/70"
          >
            <div className="flex items-center justify-between text-[8px] text-navy/40 pb-0.5">
              <span>DISPATCH INDEX //</span>
              <span>FOLIO VOL. 01</span>
            </div>
            
            <button 
              onClick={() => handleScrollClick('about-me')} 
              className="text-left hover:text-navy cursor-pointer flex justify-between items-center group py-0.5 transition-colors"
            >
              <span className="group-hover:translate-x-1.5 transition-transform duration-200">01. CHRONICLE (ABOUT)</span>
              <span className="text-[9px] opacity-50 group-hover:opacity-100 group-hover:translate-x-1 transition-all duration-200">P. 01 →</span>
            </button>
            <button 
              onClick={() => handleScrollClick('work')} 
              className="text-left hover:text-navy cursor-pointer flex justify-between items-center group py-0.5 transition-colors"
            >
              <span className="group-hover:translate-x-1.5 transition-transform duration-200">02. CASE STUDIES (WORK)</span>
              <span className="text-[9px] opacity-50 group-hover:opacity-100 group-hover:translate-x-1 transition-all duration-200">P. 02 →</span>
            </button>
            <button 
              onClick={() => handleScrollClick('service')} 
              className="text-left hover:text-navy cursor-pointer flex justify-between items-center group py-0.5 transition-colors"
            >
              <span className="group-hover:translate-x-1.5 transition-transform duration-200">03. SERVICES OFFERED</span>
              <span className="text-[9px] opacity-50 group-hover:opacity-100 group-hover:translate-x-1 transition-all duration-200">P. 03 →</span>
            </button>
            <button 
              onClick={() => handleScrollClick('experience')} 
              className="text-left hover:text-navy cursor-pointer flex justify-between items-center group py-0.5 transition-colors"
            >
              <span className="group-hover:translate-x-1.5 transition-transform duration-200">04. PEDAGOGIC RECORD</span>
              <span className="text-[9px] opacity-50 group-hover:opacity-100 group-hover:translate-x-1 transition-all duration-200">P. 04 →</span>
            </button>
          </motion.div>
        </div>

      </div>

      {/* BOTTOM: Newspaper Running Footer with Line Draw & Animated Scroll Prompt */}
      <footer className="relative z-10 w-full pt-2 shrink-0 flex flex-col gap-1.5">
        <motion.div 
          initial={{ scaleX: 0 }}
          animate={{ scaleX: isReady ? 1 : 0 }}
          transition={{ duration: 0.9, delay: 0.2, ease: heroEase }}
          className="w-full h-[2px] bg-navy origin-left"
        />

        <div className="flex items-center justify-between text-[8px] sm:text-[9px] md:text-[10px] font-mono tracking-[0.2em] uppercase text-navy/70 pt-0.5">
          <motion.div 
            initial={{ opacity: 0 }}
            animate={{ opacity: isReady ? 1 : 0 }}
            transition={{ duration: 0.6, delay: 0.3 }}
            className="flex items-center gap-3"
          >
            <span>FIRST EDITION // 2026</span>
            <span className="opacity-40 hidden sm:inline">|</span>
            <span className="hidden sm:inline">TYPESET IN EDITORIAL SERIF</span>
          </motion.div>
          <motion.button 
            initial={{ opacity: 0, y: 8 }}
            animate={{ opacity: isReady ? 1 : 0, y: isReady ? 0 : 8 }}
            transition={{ duration: 0.6, delay: 0.35, ease: heroEase }}
            onClick={() => handleScrollClick('about-me')}
            className="flex items-center gap-2 hover:text-navy cursor-pointer group"
            aria-label="Scroll to read issue"
          >
            <span className="group-hover:underline">PROCEED TO CHRONICLE</span>
            <motion.span 
              animate={{ y: [0, 3, 0] }}
              transition={{ repeat: Infinity, duration: 1.6, ease: "easeInOut" }}
              className="inline-block"
            >
              ↓
            </motion.span>
          </motion.button>
        </div>
      </footer>

    </section>
    </MotionConfig>
  );
}

export function HomeOptionA() {
  const [roleIndex, setRoleIndex] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setRoleIndex((prev) => (prev + 1) % ROLES.length);
    }, 3200);
    return () => clearInterval(timer);
  }, []);

  const handleScrollClick = (id = 'about-me') => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <section id="home" className="relative w-full min-h-[100svh] bg-cream text-navy font-sans select-none flex flex-col justify-between p-4 sm:p-6 md:p-10 lg:p-12 border-b-2 border-navy overflow-hidden">
      
      {/* Editorial Canvas Outer Inset Frame */}
      <div className="absolute inset-2 sm:inset-3 md:inset-5 border border-navy/15 pointer-events-none z-0">
        <div className="absolute -top-1 -left-1 font-mono text-[8px] text-navy/40 leading-none select-none">+</div>
        <div className="absolute -top-1 -right-1 font-mono text-[8px] text-navy/40 leading-none select-none">+</div>
        <div className="absolute -bottom-1 -left-1 font-mono text-[8px] text-navy/40 leading-none select-none">+</div>
        <div className="absolute -bottom-1 -right-1 font-mono text-[8px] text-navy/40 leading-none select-none">+</div>
      </div>

      {/* TOP: Disciplined Publication Masthead */}
      <header className="relative z-10 w-full pt-1 pb-4 md:pb-6 border-b border-navy/20 flex flex-col gap-2">
        <div className="flex items-center justify-between text-[9px] sm:text-[10px] md:text-xs font-mono tracking-[0.2em] uppercase text-navy/70">
          <div className="flex items-center gap-2">
            <span className="w-1.5 h-1.5 rounded-full bg-navy"></span>
            <span>MONOGRAPH NO. 01</span>
            <span className="hidden sm:inline opacity-40">// 2026 EDITION</span>
          </div>
          <div className="hidden md:flex items-center gap-3">
            <span>YOGYAKARTA, ID</span>
            <span className="opacity-40">/</span>
            <span>GLOBAL ENGINEERING PRACTICE</span>
          </div>
          <div>
            <span>VOL. 01 — ARCHIVE</span>
          </div>
        </div>

        {/* Big Publication Masthead */}
        <div className="flex flex-col sm:flex-row sm:items-baseline justify-between pt-1 gap-1">
          <h1 className="font-serif text-4xl sm:text-5xl md:text-6xl lg:text-7xl xl:text-8xl font-black tracking-[-0.03em] uppercase text-navy leading-none">
            GABRIEL RYAN
          </h1>
          <span className="font-mono text-[9px] sm:text-[10px] md:text-xs uppercase tracking-[0.25em] text-navy/60 font-semibold">
            FOLIO &amp; CURATED INDEX
          </span>
        </div>
      </header>

      {/* CENTER: Exhibition Spread (Editorial Column + Framed Portrait Plate) */}
      <div className="relative z-10 w-full flex-1 py-6 md:py-8 lg:py-10 grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center">
        
        {/* Left Column: Lead Cover Essay & Active Practice (Cols 1-7) */}
        <div className="lg:col-span-7 flex flex-col justify-center gap-4 sm:gap-6 max-w-2xl">
          <div className="flex items-center gap-2 text-[10px] sm:text-xs font-mono tracking-[0.2em] uppercase text-navy/60">
            <span>COVER STORY</span>
            <span>//</span>
            <span>DISCIPLINE STUDY</span>
          </div>

          <h2 className="font-serif text-2xl sm:text-4xl md:text-5xl lg:text-5xl font-black leading-[1.05] tracking-[-0.02em] text-navy">
            THE ARCHITECTURE OF SYSTEMS, CODE &amp; PEDAGOGY.
          </h2>

          <p className="text-xs sm:text-sm md:text-base font-sans text-navy/80 leading-relaxed max-w-xl">
            A comprehensive visual index exploring software architecture, digital craftsmanship, and the curriculum frameworks designed to cultivate the next cohort of engineers.
          </p>

          {/* Active Discipline / Rotating Role */}
          <div className="pt-2 flex flex-col gap-2">
            <span className="text-[9px] sm:text-[10px] font-mono tracking-[0.25em] uppercase text-navy/60">
              CURRENT PRACTICE //
            </span>
            <div className="flex items-baseline gap-2 text-sm sm:text-base md:text-lg font-black tracking-wide text-navy">
              <span>EDUCATOR &amp;</span>
              <span className="relative inline-grid [grid-template-areas:'stack'] overflow-hidden h-[1.3em]">
                <AnimatePresence mode="popLayout" initial={false}>
                  <motion.span
                    key={roleIndex}
                    initial={{ y: "100%", opacity: 0 }}
                    animate={{ y: "0%", opacity: 1 }}
                    exit={{ y: "-100%", opacity: 0 }}
                    transition={{ duration: 0.5, ease: heroEase }}
                    className="[grid-area:stack] inline-block whitespace-nowrap text-navy underline decoration-navy/30 underline-offset-4"
                  >
                    {ROLES[roleIndex]}
                  </motion.span>
                </AnimatePresence>
              </span>
            </div>
          </div>

          {/* Quick Chapter Navigation Index */}
          <div className="pt-3 border-t border-navy/15 flex flex-wrap gap-4 sm:gap-6 text-[9px] sm:text-[10px] md:text-xs font-mono uppercase tracking-[0.15em] text-navy/70">
            <button onClick={() => handleScrollClick('about-me')} className="hover:text-navy hover:underline cursor-pointer">
              01. ABOUT →
            </button>
            <button onClick={() => handleScrollClick('work')} className="hover:text-navy hover:underline cursor-pointer">
              02. WORK →
            </button>
            <button onClick={() => handleScrollClick('service')} className="hover:text-navy hover:underline cursor-pointer">
              03. SERVICES →
            </button>
            <button onClick={() => handleScrollClick('experience')} className="hover:text-navy hover:underline cursor-pointer">
              04. RECORD →
            </button>
          </div>
        </div>

        {/* Right Column: The Framed Exhibition Plate (Cols 8-12) */}
        <div className="lg:col-span-5 flex flex-col items-center justify-center">
          <div className="relative w-full max-w-[280px] sm:max-w-[320px] md:max-w-[350px] bg-[#F4EFE6] border border-navy/30 p-3 sm:p-4 shadow-xl">
            {/* Fine Corner Accents */}
            <div className="absolute top-1 left-1 text-[8px] font-mono text-navy/30 leading-none select-none">┌</div>
            <div className="absolute top-1 right-1 text-[8px] font-mono text-navy/30 leading-none select-none">┐</div>
            <div className="absolute bottom-1 left-1 text-[8px] font-mono text-navy/30 leading-none select-none">└</div>
            <div className="absolute bottom-1 right-1 text-[8px] font-mono text-navy/30 leading-none select-none">┘</div>

            {/* Inner Plate Matting */}
            <div className="relative aspect-[3/4] w-full overflow-hidden bg-[#DFD7C5] border border-navy/20 flex items-end justify-center">
              <img 
                src="/profile-nobg.png" 
                alt="Gabriel Ryan - Studio Portrait" 
                className="w-full h-auto max-h-[96%] object-contain object-bottom grayscale contrast-125 brightness-105"
              />
              <div className="absolute top-2 right-2 px-1.5 py-0.5 bg-cream/90 border border-navy/20 font-mono text-[8px] uppercase tracking-widest text-navy/80">
                FIG. 01
              </div>
            </div>

            {/* Curatorial Plate Caption */}
            <div className="pt-2.5 flex flex-col gap-0.5 text-navy">
              <div className="flex items-center justify-between font-mono text-[8px] sm:text-[9px] tracking-[0.2em] uppercase font-bold">
                <span>PLATE NO. 01</span>
                <span>OCT / 2026</span>
              </div>
              <p className="text-[9px] sm:text-[10px] font-serif italic text-navy/70 leading-snug">
                Studio portrait of Gabriel Ryan. Educator, software engineer, and curriculum architect.
              </p>
            </div>
          </div>
        </div>

      </div>

      {/* BOTTOM: Editorial Colophon & Entry Point */}
      <footer className="relative z-10 w-full pt-3 border-t border-navy/20 flex items-center justify-between text-[9px] sm:text-[10px] md:text-xs font-mono tracking-[0.2em] uppercase text-navy/70">
        <div>
          <span>EST. 2020 // FIRST EDITION</span>
        </div>
        <button 
          onClick={() => handleScrollClick('about-me')}
          className="flex items-center gap-2 hover:text-navy cursor-pointer group"
          aria-label="Scroll to enter Chapter 01"
        >
          <span className="group-hover:underline">OPEN MONOGRAPH</span>
          <span className="group-hover:translate-y-0.5 transition-transform">↓</span>
        </button>
      </footer>

    </section>
  );
}

export function HomeOriginal() {
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
    <section id="home" className="relative w-full h-[100svh] min-h-[600px] overflow-hidden bg-cream text-navy font-sans select-none">
      
      {/* 
        CANVAS LINING: Fine archival border & corner registration marks
      */}
      <div className="absolute inset-3 sm:inset-5 md:inset-8 border border-navy/15 pointer-events-none z-0">
        <div className="absolute -top-1.5 -left-1.5 font-mono text-[9px] text-navy/40 leading-none select-none">+</div>
        <div className="absolute -top-1.5 -right-1.5 font-mono text-[9px] text-navy/40 leading-none select-none">+</div>
        <div className="absolute -bottom-1.5 -left-1.5 font-mono text-[9px] text-navy/40 leading-none select-none">+</div>
        <div className="absolute -bottom-1.5 -right-1.5 font-mono text-[9px] text-navy/40 leading-none select-none">+</div>
      </div>

      {/* Subtle archival watermark rings */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[75vw] h-[75vw] max-w-[850px] max-h-[850px] rounded-full border border-navy/[0.04] pointer-events-none z-0"></div>
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[50vw] h-[50vw] max-w-[550px] max-h-[550px] rounded-full border border-navy/[0.03] pointer-events-none z-0"></div>

      {/* LAYER 1: MASTHEAD BACKGROUND TYPOGRAPHY */}
      <div className="absolute inset-0 z-10">
        <HomeBackgroundTypography variants={heroVariants} />
      </div>

      {/* LAYER 2: PORTRAIT (Center Subject - completely unsevered by vertical seam) */}
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

      {/* LAYER 3: FRONT EDITORIAL METADATA & UI (Elevated in front of portrait) */}
      <div className="absolute inset-0 z-30 pointer-events-none">
        
        {/* Top Left Meta */}
        <motion.div 
          variants={heroVariants.metaTopLeft}
          initial="hidden"
          animate="visible"
          className="absolute top-6 left-6 sm:top-8 sm:left-8 md:top-12 md:left-12 flex flex-col gap-1 text-[10px] md:text-xs font-bold tracking-[0.2em] uppercase text-navy"
        >
          <div className="flex items-center gap-2">
            <span className="w-1.5 h-1.5 rounded-full bg-navy/60 inline-block"></span>
            <span>VOL. 01</span>
          </div>
          <span className="opacity-60 pl-3.5">OCT / 2026</span>
        </motion.div>

        {/* Top Right Meta */}
        <motion.div 
          variants={heroVariants.metaTopRight}
          initial="hidden"
          animate="visible"
          className="absolute top-6 right-6 sm:top-8 sm:right-8 md:top-12 md:right-12 flex flex-col gap-1 text-[10px] md:text-xs font-bold tracking-[0.2em] uppercase text-right text-navy"
        >
          <span>VISUAL STUDY</span>
          <span className="opacity-60">BY GABRIEL RYAN</span>
        </motion.div>

        {/* Bottom Left Meta (Role & Est. - 2-line vertical stack, never occluded by portrait) */}
        <motion.div 
          variants={heroVariants.metaBottom}
          initial="hidden"
          animate="visible"
          className="absolute bottom-8 left-6 sm:bottom-10 sm:left-8 md:bottom-16 md:left-12 flex flex-col gap-2.5 sm:gap-3 md:gap-4 text-[10px] md:text-xs font-bold tracking-[0.15em] uppercase text-navy max-w-[200px] sm:max-w-[240px] md:max-w-xs"
        >
          <span className="opacity-60 tracking-[0.2em] text-[9px] sm:text-[10px] md:text-xs font-mono">ROLE //</span>
          <div className="flex flex-col text-xs sm:text-sm md:text-base font-black tracking-[0.08em] leading-tight">
            <span className="whitespace-nowrap text-navy">EDUCATOR &amp;</span>
            <span className="relative inline-grid [grid-template-areas:'stack'] overflow-hidden h-[1.3em]">
              <AnimatePresence mode="popLayout" initial={false}>
                <motion.span
                  key={roleIndex}
                  initial={{ y: "100%", opacity: 0 }}
                  animate={{ y: "0%", opacity: 1 }}
                  exit={{ y: "-100%", opacity: 0 }}
                  transition={{ duration: 0.5, ease: heroEase }}
                  className="[grid-area:stack] inline-block whitespace-nowrap text-navy"
                >
                  {ROLES[roleIndex]}
                </motion.span>
              </AnimatePresence>
            </span>
          </div>
          <div className="w-10 sm:w-12 h-[1px] bg-navy/30"></div>
          <span className="tracking-[0.2em] text-[9px] sm:text-[10px] md:text-xs opacity-60 font-mono">EST. 2020</span>
        </motion.div>

        {/* Middle Right Stamp (Aged paper card with navy framing) */}
        <motion.div 
          variants={heroVariants.stamp}
          initial="hidden"
          animate="visible"
          className="absolute top-[48%] md:top-1/2 -translate-y-1/2 right-6 sm:right-10 md:right-20 flex items-center pointer-events-auto"
        >
          <div className="relative w-16 h-16 sm:w-20 sm:h-20 md:w-28 md:h-28 z-10">
            <div className="absolute inset-0 bg-navy/10 transform translate-x-2 translate-y-2 md:translate-x-2.5 md:translate-y-2.5"></div>
            <div className="absolute inset-0 bg-[#F5F0E6] p-2 shadow-sm border border-navy/30 flex items-center justify-center">
              <img 
                src="/favicon.jpg" 
                alt="Author" 
                className="w-full h-full object-cover grayscale contrast-125 bg-gray-200" 
                onError={(e) => { e.target.src = 'https://api.dicebear.com/7.x/notionists/svg?seed=Gabriel&backgroundColor=e5e5e5'; }} 
              />
            </div>
          </div>
          <div className="absolute right-[-3.8rem] sm:right-[-4.5rem] md:right-[-5.5rem] top-1/2 -translate-y-1/2 origin-center rotate-90 text-[8px] md:text-[9px] font-bold tracking-[0.25em] uppercase text-navy/70 whitespace-nowrap font-mono">
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
  const handleScrollClick = () => {
    const el = document.getElementById('about-me');
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <div className="absolute bottom-8 right-6 sm:bottom-10 sm:right-8 md:bottom-16 md:right-12 flex flex-col items-end pointer-events-auto select-none z-30">
      <button 
        onClick={handleScrollClick}
        className="flex flex-col items-end gap-2 text-navy group cursor-pointer"
        aria-label="Scroll to explore"
      >
        <span className="text-[9px] sm:text-[10px] md:text-xs font-bold tracking-[0.25em] uppercase whitespace-nowrap opacity-70 group-hover:opacity-100 transition-opacity font-mono">
          Scroll to explore
        </span>
        <div className="flex items-center gap-2.5">
          <span className="text-[9px] font-mono opacity-40 group-hover:opacity-80 transition-opacity">CHAPTER 01</span>
          <div className="w-10 sm:w-14 h-[1px] bg-navy/30 group-hover:bg-navy/70 transition-colors"></div>
          <div className="w-[1px] h-5 sm:h-6 bg-navy/30 overflow-hidden relative">
            <motion.div 
              className="absolute top-0 left-0 w-full h-[60%] bg-navy"
              animate={{ y: ["-100%", "200%"] }}
              transition={{ duration: 1.4, repeat: Infinity, ease: "easeInOut" }}
            />
          </div>
        </div>
      </button>
    </div>
  );
}

function HomeBackgroundTypography({ variants }) {
  return (
    <div className="absolute inset-0 flex flex-col pointer-events-none">
      {/* Center Masthead Typography */}
      <div className="absolute top-[25%] md:top-[12%] left-0 w-full flex flex-col items-center justify-start">
        <motion.h1 
          variants={variants?.title}
          initial="hidden"
          animate="visible"
          className="font-serif text-[26vw] md:text-[17vw] font-black tracking-[-0.04em] leading-[0.8] uppercase z-10 relative text-navy selection:bg-navy selection:text-cream drop-shadow-sm"
        >
          GABRIEL
        </motion.h1>
        {/* Cursive text overlapping */}
        <motion.div 
          variants={variants?.cursive}
          initial="hidden"
          animate="visible"
          className="absolute top-[60%] md:top-[40%] left-1/2 -translate-x-1/2 mt-[2vw] ml-[6vw] z-20 opacity-90 text-[#8C6D46]"
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
