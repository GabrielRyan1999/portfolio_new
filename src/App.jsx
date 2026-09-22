import React from 'react';
import { BrowserRouter, Routes, Route, useLocation } from 'react-router-dom';
import { AnimatePresence } from 'framer-motion';
import { FloatingDock } from './components/ui/dock';
import { Home, About, Work, Service, Experience, Contact } from './pages/Pages';

function AnimatedRoutes() {
  const location = useLocation();
  
  return (
    <AnimatePresence mode="wait">
      <Routes location={location} key={location.pathname}>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/work" element={<Work />} />
        <Route path="/service" element={<Service />} />
        <Route path="/experience" element={<Experience />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </AnimatePresence>
  );
}

function App() {
  return (
    <BrowserRouter>
      {/* Background Elements (fixed so they stay behind everything) */}
      <div className="fixed inset-0 z-0 pointer-events-none">
        <div className="absolute inset-0 bg-grid opacity-50 dark:opacity-30"></div>
        <div className="absolute top-0 -left-4 w-96 h-96 bg-indigo-600 rounded-full filter blur-[100px] opacity-20 animate-blob"></div>
        <div className="absolute top-0 -right-4 w-96 h-96 bg-blue-600 rounded-full filter blur-[100px] opacity-20 animate-blob animation-delay-2000"></div>
        <div className="absolute -bottom-8 left-20 w-96 h-96 bg-cyan-600 rounded-full filter blur-[100px] opacity-20 animate-blob animation-delay-4000"></div>
      </div>
      
      <div className="relative z-10 w-full min-h-screen">
        <FloatingDock />
        <AnimatedRoutes />
      </div>
    </BrowserRouter>
  );
}

export default App;
