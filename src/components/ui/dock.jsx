import React, { useState, useEffect } from 'react';
import { Home, Briefcase, Layers, User, Moon, Sun, Star, Mail, Menu, X } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

export function FloatingDock() {
  const [hovered, setHovered] = useState(null);
  const [isDark, setIsDark] = useState(false);
  
  // Collapse state
  const [isScrolled, setIsScrolled] = useState(false);
  const [isExpanded, setIsExpanded] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 100) {
        setIsScrolled(true);
      } else {
        setIsScrolled(false);
        setIsExpanded(false);
      }
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  useEffect(() => {
    if (isDark) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [isDark]);

  const scrollTo = (id) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
    // Auto collapse after clicking a link if we are scrolled down
    if (isScrolled) {
      setIsExpanded(false);
    }
  };

  const myNavItems = [
    { id: 'about', label: 'Home', icon: Home },
    { id: 'about-me', label: 'About', icon: User },
    { id: 'work', label: 'Work', icon: Briefcase },
    { id: 'service', label: 'Service', icon: Layers },
    { id: 'experience', label: 'Experience', icon: Star },
    { id: 'contact', label: 'Contact', icon: Mail },
  ];

  const showFullMenu = !isScrolled || isExpanded;

  return (
    <div className="fixed top-8 md:top-12 left-1/2 -translate-x-1/2 z-[100] flex flex-col items-center">
      <AnimatePresence mode="wait">
        {!showFullMenu ? (
          // Collapsed State (Dynamic Island)
          <motion.button
            key="collapsed"
            initial={{ opacity: 0, scale: 0.8, y: -20 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.8, y: -20 }}
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={() => setIsExpanded(true)}
            className="flex items-center gap-2 px-5 py-3 rounded-full bg-[#111111]/90 backdrop-blur-md border border-white/10 shadow-[0_8px_30px_rgb(0,0,0,0.5)] text-white group"
          >
            <Menu className="w-5 h-5 text-slate-300 group-hover:text-white transition-colors" />
            <span className="text-sm font-semibold tracking-wide pr-1">Menu</span>
          </motion.button>
        ) : (
          // Expanded / Default State
          <motion.div 
            key="expanded"
            initial={{ opacity: 0, scale: 0.9, y: -10 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.9, y: -10 }}
            className={`flex items-center gap-2 md:gap-3 ${isScrolled ? 'px-4 py-3 bg-[#111111]/80 backdrop-blur-xl border border-white/10 rounded-full shadow-2xl' : ''}`}
          >
            {myNavItems.map((item) => {
              const Icon = item.icon;
              const isHovered = hovered === item.id;

              return (
                <div 
                  key={item.id} 
                  className="relative"
                  onMouseEnter={() => setHovered(item.id)}
                  onMouseLeave={() => setHovered(null)}
                >
                  <AnimatePresence>
                    {isHovered && (
                      <motion.div
                        initial={{ opacity: 0, y: -10, scale: 0.8 }}
                        animate={{ opacity: 1, y: 0, scale: 1 }}
                        exit={{ opacity: 0, y: -10, scale: 0.8 }}
                        className="absolute top-14 left-1/2 -translate-x-1/2 px-3 py-1.5 bg-[#1a1a1a] border border-white/10 text-white text-xs font-medium rounded-lg whitespace-nowrap shadow-xl z-50"
                      >
                        {item.label}
                      </motion.div>
                    )}
                  </AnimatePresence>

                  <button
                    onClick={() => scrollTo(item.id)}
                    className={`relative flex items-center justify-center w-10 h-10 md:w-12 md:h-12 rounded-full ${isScrolled ? 'hover:bg-white/10' : 'bg-[#111111] border border-white/5'} transition-all duration-300 text-slate-300`}
                  >
                    {!isScrolled && isHovered && (
                      <motion.div 
                        layoutId="dock-hover"
                        className="absolute inset-0 bg-white/10 rounded-full shadow-[0_0_20px_rgba(255,255,255,0.2)] border border-white/20"
                        transition={{ type: "spring", stiffness: 300, damping: 25 }}
                      />
                    )}
                    <Icon className={`w-4 h-4 md:w-5 md:h-5 relative z-10 ${isHovered ? 'text-white' : 'text-slate-300'}`} />
                  </button>
                </div>
              );
            })}

            {/* Separator */}
            <div className="w-[1px] h-6 bg-slate-300 dark:bg-white/20 mx-1 md:mx-2"></div>

            {/* Theme Toggle Button */}
            <div 
              className="relative"
              onMouseEnter={() => setHovered('theme')}
              onMouseLeave={() => setHovered(null)}
            >
              <AnimatePresence>
                {hovered === 'theme' && (
                  <motion.div
                    initial={{ opacity: 0, y: -10, scale: 0.8 }}
                    animate={{ opacity: 1, y: 0, scale: 1 }}
                    exit={{ opacity: 0, y: -10, scale: 0.8 }}
                    className="absolute top-14 left-1/2 -translate-x-1/2 px-3 py-1.5 bg-[#1a1a1a] border border-white/10 text-white text-xs font-medium rounded-lg whitespace-nowrap shadow-xl z-50"
                  >
                    {isDark ? 'Light Mode' : 'Dark Mode'}
                  </motion.div>
                )}
              </AnimatePresence>
              <button
                onClick={() => setIsDark(!isDark)}
                className={`relative flex items-center justify-center w-10 h-10 md:w-12 md:h-12 rounded-full ${isScrolled ? 'hover:bg-white/10' : 'bg-[#111111] border border-white/5'} transition-all duration-300 text-slate-300`}
              >
                {!isScrolled && hovered === 'theme' && (
                  <motion.div 
                    layoutId="dock-hover"
                    className="absolute inset-0 bg-white/10 rounded-full shadow-[0_0_20px_rgba(255,255,255,0.2)] border border-white/20"
                    transition={{ type: "spring", stiffness: 300, damping: 25 }}
                  />
                )}
                {isDark ? (
                  <Sun className={`w-4 h-4 md:w-5 md:h-5 relative z-10 ${hovered === 'theme' ? 'text-white' : 'text-slate-300'}`} />
                ) : (
                  <Moon className={`w-4 h-4 md:w-5 md:h-5 relative z-10 ${hovered === 'theme' ? 'text-white' : 'text-slate-300'}`} />
                )}
              </button>
            </div>

            {/* Close Button when Expanded */}
            {isScrolled && (
              <button 
                onClick={() => setIsExpanded(false)}
                className="ml-1 flex items-center justify-center w-8 h-8 rounded-full bg-red-500/20 hover:bg-red-500/40 text-red-300 hover:text-red-100 transition-colors"
              >
                <X className="w-4 h-4" />
              </button>
            )}

          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
