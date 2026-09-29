import React, { useEffect } from 'react';
import { BrowserRouter, Routes, Route, useLocation } from 'react-router-dom';
import { AnimatePresence, motion, useScroll, useSpring } from 'framer-motion';
import { Home, About, Work, Service, Experience, Contact } from './pages/Pages';
import { EditorialNav } from './components/EditorialNav';

// Component to handle scroll restoration and hash scrolling
function ScrollHandler() {
  const { pathname, hash } = useLocation();

  useEffect(() => {
    if (hash) {
      // Small delay to ensure the page has rendered before scrolling
      setTimeout(() => {
        const id = hash.replace('#', '');
        const element = document.getElementById(id);
        if (element) {
          element.scrollIntoView({ behavior: 'smooth' });
        }
      }, 100);
    } else {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }, [pathname, hash]);

  return null;
}

function IndexPage() {
  return (
    <div className="flex flex-col w-full">
      <Home />
      <About />
      <Work />
      <Service />
      <Experience />
      <Contact />
    </div>
  );
}

function AnimatedRoutes() {
  const location = useLocation();
  
  return (
    <AnimatePresence mode="wait">
      <Routes location={location} key={location.pathname}>
        <Route path="/" element={<IndexPage />} />
      </Routes>
    </AnimatePresence>
  );
}

function App() {
  const { scrollYProgress } = useScroll();
  const scaleX = useSpring(scrollYProgress, {
    stiffness: 100,
    damping: 30,
    restDelta: 0.001
  });

  return (
    <BrowserRouter>
      <ScrollHandler />
      <motion.div
        className="fixed top-0 left-0 right-0 h-1 md:h-1.5 bg-[#1E4E8C] origin-left z-[9999]"
        style={{ scaleX }}
      />
      <EditorialNav />
      
      {/* Authentic Vintage Paper Grain Overlay (matches editorial zine texture) */}
      <div 
        className="fixed inset-0 z-[9990] pointer-events-none opacity-30 mix-blend-multiply"
        style={{
          backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.4'/%3E%3C/svg%3E")`
        }}
      />
      
      <div className="relative z-10 w-full min-h-screen">
        <AnimatedRoutes />
      </div>
    </BrowserRouter>
  );
}

export default App;
