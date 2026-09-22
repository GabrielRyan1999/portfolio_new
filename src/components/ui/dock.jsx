import React, { useState, useEffect } from 'react';
import { Home, Briefcase, Layers, User, Moon, Sun, Star, Mail, Menu, X } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import { Link, useLocation } from 'react-router-dom';

export function FloatingDock() {
  const [hovered, setHovered] = useState(null);
  const [isDark, setIsDark] = useState(false);
  const location = useLocation();
  
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

  const myNavItems = [
    { path: '/', label: 'Home', icon: Home },
    { path: '/about', label: 'About', icon: User },
    { path: '/work', label: 'Work', icon: Briefcase },
    { path: '/service', label: 'Service', icon: Layers },
    { path: '/experience', label: 'Experience', icon: Star },
    { path: '/contact', label: 'Contact', icon: Mail },
  ];

  const showFullMenu = !isScrolled || isExpanded;

  return (
    <div className="fixed bottom-6 md:bottom-auto md:top-5 left-1/2 -translate-x-1/2 z-[100] flex flex-col items-center">
      <AnimatePresence mode="wait">
        {!showFullMenu ? (
          // Collapsed State (Dynamic Island)
          <motion.button
            key="collapsed"
            initial={{ opacity: 0, scale: 0.8, y: 20 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.8, y: 20 }}
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
            className={`flex items-center gap-1 md:gap-3 ${isScrolled ? 'px-4 py-3 bg-[#111111]/80 backdrop-blur-xl border border-white/10 rounded-full shadow-2xl' : ''}`}
          >
            {myNavItems.map((item) => {
              const Icon = item.icon;
              const isHovered = hovered === item.path;
              const isActive = location.pathname === item.path;

              return (
                <div 
                  key={item.path} 
                  className="relative"
                  onMouseEnter={() => setHovered(item.path)}
                  onMouseLeave={() => setHovered(null)}
                >
                  <AnimatePresence>
                    {isHovered && (
                      <motion.div
                        initial={{ opacity: 0, y: -10, scale: 0.8 }}
                        animate={{ opacity: 1, y: 0, scale: 1 }}
                        exit={{ opacity: 0, y: -10, scale: 0.8 }}
                        className="absolute -top-10 md:top-14 left-1/2 -translate-x-1/2 px-3 py-1.5 bg-[#1a1a1a] border border-white/10 text-white text-xs font-medium rounded-lg whitespace-nowrap shadow-xl z-50 pointer-events-none"
                      >
                        {item.label}
                      </motion.div>
                    )}
                  </AnimatePresence>

                  <Link
                    to={item.path}
                    onClick={() => {
                        if (isScrolled) setIsExpanded(false);
                        window.scrollTo(0, 0); // Ensure top of page when changing routes
                    }}
                    className={`relative flex items-center justify-center w-9 h-9 md:w-12 md:h-12 rounded-full ${isScrolled ? 'hover:bg-white/10' : 'bg-[#111111] border border-white/5'} transition-all duration-300 ${isActive ? 'text-blue-500' : 'text-slate-300'}`}
                  >
                    {!isScrolled && isHovered && (
                      <motion.div 
                        layoutId="dock-hover"
                        className="absolute inset-0 bg-white/10 rounded-full shadow-[0_0_20px_rgba(255,255,255,0.2)] border border-white/20"
                        transition={{ type: "spring", stiffness: 300, damping: 25 }}
                      />
                    )}
                    <Icon className={`w-4 h-4 md:w-5 md:h-5 relative z-10 ${isHovered || isActive ? 'text-white' : 'text-slate-300'}`} />
                  </Link>
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
                    className="absolute -top-10 md:top-14 left-1/2 -translate-x-1/2 px-3 py-1.5 bg-[#1a1a1a] border border-white/10 text-white text-xs font-medium rounded-lg whitespace-nowrap shadow-xl z-50 pointer-events-none"
                  >
                    {isDark ? 'Light Mode' : 'Dark Mode'}
                  </motion.div>
                )}
              </AnimatePresence>
              <button
                onClick={() => setIsDark(!isDark)}
                className={`relative flex items-center justify-center w-9 h-9 md:w-12 md:h-12 rounded-full ${isScrolled ? 'hover:bg-white/10' : 'bg-[#111111] border border-white/5'} transition-all duration-300 text-slate-300`}
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
