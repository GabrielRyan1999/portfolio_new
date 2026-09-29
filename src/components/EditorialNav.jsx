import React, { useState, useEffect } from 'react';

const CHAPTERS = [
  { id: 'about-me', num: '01', label: 'ABOUT' },
  { id: 'work', num: '02', label: 'WORK' },
  { id: 'service', num: '03', label: 'SERVICES' },
  { id: 'experience', num: '04', label: 'RECORD' },
  { id: 'testimonials', num: '05', label: 'ARCHIVES' },
  { id: 'contact', num: '06', label: 'CONTACT' },
];

export function EditorialNav() {
  const [activeChapter, setActiveChapter] = useState('');
  const [isScrolled, setIsScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 80);

      const scrollPos = window.scrollY + 250;
      for (let i = CHAPTERS.length - 1; i >= 0; i--) {
        const el = document.getElementById(CHAPTERS[i].id);
        if (el && el.offsetTop <= scrollPos) {
          setActiveChapter(CHAPTERS[i].id);
          break;
        }
      }
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollTo = (id) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <header 
      className={`fixed top-0 left-0 w-full z-40 transition-all duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] ${
        isScrolled 
          ? 'translate-y-0 opacity-100 pointer-events-auto bg-[#EBE5D8]/95 backdrop-blur-md border-b-2 border-navy py-2 px-4 md:px-8 shadow-sm text-navy' 
          : '-translate-y-full opacity-0 pointer-events-none py-2 px-4 md:px-8 text-navy'
      }`}
    >
      <div className="max-w-7xl mx-auto flex items-center justify-between pointer-events-auto">
        <button 
          onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
          className="font-mono text-[10px] md:text-xs font-bold tracking-widest uppercase hover:underline cursor-pointer flex items-center gap-2"
        >
          <span>GABRIEL RYAN</span>
          <span className="opacity-50 hidden sm:inline">// INDEX</span>
        </button>

        <nav className="flex items-center gap-1 sm:gap-3 md:gap-6 overflow-x-auto scrollbar-hide py-1">
          {CHAPTERS.map((ch) => {
            const isActive = activeChapter === ch.id;
            return (
              <button
                key={ch.id}
                onClick={() => scrollTo(ch.id)}
                className={`font-mono text-[10px] md:text-xs tracking-widest uppercase whitespace-nowrap transition-all cursor-pointer py-1 px-2 border ${
                  isActive 
                    ? 'border-navy bg-navy text-cream font-bold shadow-[2px_2px_0px_0px_#1E4E8C]' 
                    : 'border-transparent opacity-70 hover:opacity-100 hover:border-navy/30'
                }`}
              >
                <span className="hidden sm:inline opacity-70 mr-1">{ch.num}</span>
                {ch.label}
              </button>
            );
          })}
        </nav>

        <button
          onClick={() => scrollTo('contact')}
          className="hidden md:inline-block border-2 border-navy bg-cream text-navy px-3 py-1 font-mono text-[10px] font-bold tracking-widest uppercase hover:bg-navy hover:text-cream transition-colors cursor-pointer shadow-[2px_2px_0px_0px_#1E4E8C] active:translate-x-0.5 active:translate-y-0.5 active:shadow-none"
        >
          CONTACT
        </button>
      </div>
    </header>
  );
}
