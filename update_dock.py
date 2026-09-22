import re

with open('src/components/ui/dock.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Imports
content = content.replace("from 'framer-motion';", "from 'framer-motion';\nimport { Link, useLocation } from 'react-router-dom';")

# 2. Nav Items
nav_old = """  const myNavItems = [
    { id: 'about', label: 'Home', icon: Home },
    { id: 'about-me', label: 'About', icon: User },
    { id: 'work', label: 'Work', icon: Briefcase },
    { id: 'service', label: 'Service', icon: Layers },
    { id: 'experience', label: 'Experience', icon: Star },
  ];"""

nav_new = """  const myNavItems = [
    { path: '/', label: 'Home', icon: Home },
    { path: '/about', label: 'About', icon: User },
    { path: '/work', label: 'Work', icon: Briefcase },
    { path: '/service', label: 'Service', icon: Layers },
    { path: '/experience', label: 'Experience', icon: Star },
    { path: '/contact', label: 'Contact', icon: Mail },
  ];
  
  const location = useLocation();"""
content = content.replace(nav_old, nav_new)

# 3. Replace the map function
map_old = """            {myNavItems.map((item) => (
              <div key={item.id} className="relative group/tooltip flex items-center justify-center">
                <button
                  onClick={() => scrollTo(item.id)}
                  onMouseEnter={() => setHovered(item.id)}
                  onMouseLeave={() => setHovered(null)}
                  className="w-10 h-10 md:w-12 md:h-12 rounded-full flex items-center justify-center transition-all bg-slate-100/80 dark:bg-zinc-800/80 text-slate-500 dark:text-zinc-400 hover:bg-blue-100 dark:hover:bg-zinc-700 hover:text-blue-600 dark:hover:text-blue-400 hover:scale-110 active:scale-95"
                >
                  <item.icon className="w-5 h-5 md:w-6 md:h-6" />
                </button>
                <AnimatePresence>
                  {hovered === item.id && (
                    <motion.div
                      initial={{ opacity: 0, y: isScrolled ? -10 : 20, scale: 0.8 }}
                      animate={{ opacity: 1, y: isScrolled ? -45 : 45, scale: 1 }}
                      exit={{ opacity: 0, y: isScrolled ? -10 : 20, scale: 0.8 }}
                      className="absolute whitespace-nowrap px-3 py-1.5 bg-slate-900 dark:bg-zinc-100 text-white dark:text-zinc-900 text-sm rounded-md font-medium z-50 shadow-xl pointer-events-none"
                    >
                      {item.label}
                    </motion.div>
                  )}
                </AnimatePresence>
              </div>
            ))}"""

map_new = """            {myNavItems.map((item) => {
              const isActive = location.pathname === item.path;
              return (
              <div key={item.path} className="relative group/tooltip flex items-center justify-center">
                <Link
                  to={item.path}
                  onClick={() => setIsExpanded(false)}
                  onMouseEnter={() => setHovered(item.path)}
                  onMouseLeave={() => setHovered(null)}
                  className={`w-10 h-10 md:w-12 md:h-12 rounded-full flex items-center justify-center transition-all hover:scale-110 active:scale-95 ${
                    isActive 
                      ? 'bg-blue-600 text-white shadow-lg shadow-blue-500/30' 
                      : 'bg-slate-100/80 dark:bg-zinc-800/80 text-slate-500 dark:text-zinc-400 hover:bg-blue-100 dark:hover:bg-zinc-700 hover:text-blue-600 dark:hover:text-blue-400'
                  }`}
                >
                  <item.icon className="w-5 h-5 md:w-6 md:h-6" />
                </Link>
                <AnimatePresence>
                  {hovered === item.path && (
                    <motion.div
                      initial={{ opacity: 0, y: isScrolled ? -10 : 20, scale: 0.8 }}
                      animate={{ opacity: 1, y: isScrolled ? -45 : 45, scale: 1 }}
                      exit={{ opacity: 0, y: isScrolled ? -10 : 20, scale: 0.8 }}
                      className="absolute whitespace-nowrap px-3 py-1.5 bg-slate-900 dark:bg-zinc-100 text-white dark:text-zinc-900 text-sm rounded-md font-medium z-50 shadow-xl pointer-events-none"
                    >
                      {item.label}
                    </motion.div>
                  )}
                </AnimatePresence>
              </div>
            )})}"""
content = content.replace(map_old, map_new)

with open('src/components/ui/dock.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Dock updated")
