import React, { useState, useEffect, useCallback } from "react";
import { motion, AnimatePresence } from "framer-motion";

const TESTIMONIALS = [
  {
    id: 1,
    quote: "This interactive metaverse session completely changed how our students learn. The engagement was off the charts and the students loved every second.",
    author: "Sekolah Bintang Mayantara",
    role: "School Partner",
    year: "2024",
  },
  {
    id: 2,
    quote: "The programming curriculum was so easy to follow and incredibly engaging. Our teachers feel so much more confident delivering this material now.",
    author: "Krya Global",
    role: "EdTech Partner",
    year: "2023",
  },
  {
    id: 3,
    quote: "Ryan's approach to game development mentorship is outstanding. He breaks down complex logic perfectly for absolute beginners.",
    author: "Teman Belajar Krya",
    role: "Mentorship Platform",
    year: "2023",
  },
  {
    id: 4,
    quote: "Great attention to detail and patience with beginners. Highly recommend him for any youth coding events or workshops.",
    author: "Xingzhong School",
    role: "School Partner",
    year: "2022",
  },
];

export function Testimonials() {
  const [cards, setCards] = useState(TESTIMONIALS);
  const [isPaused, setIsPaused] = useState(false);

  const handleNext = useCallback(() => {
    setCards((prevCards) => {
      const newCards = [...prevCards];
      const first = newCards.shift();
      newCards.push(first);
      return newCards;
    });
  }, []);

  const handlePrev = useCallback(() => {
    setCards((prevCards) => {
      const newCards = [...prevCards];
      const last = newCards.pop();
      newCards.unshift(last);
      return newCards;
    });
  }, []);

  // Auto-play the stack with pause-on-hover support
  useEffect(() => {
    if (isPaused) return;
    const interval = setInterval(() => {
      handleNext();
    }, 6000);
    return () => clearInterval(interval);
  }, [isPaused, handleNext]);

  return (
    <div 
      className="w-full flex flex-col items-center justify-center px-4 relative z-10"
      onMouseEnter={() => setIsPaused(true)}
      onMouseLeave={() => setIsPaused(false)}
    >
      {/* Editorial Card Stack Container */}
      <div className="relative w-full max-w-4xl h-[420px] sm:h-[390px] md:h-[400px] flex justify-center items-center mt-6 md:mt-10">
        <AnimatePresence initial={false} mode="popLayout">
          {cards.map((card, index) => {
            const isTop3 = index < 3;
            if (!isTop3) return null;

            const isFront = index === 0;

            return (
              <motion.div
                key={card.id}
                layout
                initial={{ opacity: 0, scale: 0.88, y: 30 }}
                animate={{
                  y: index * -20,
                  scale: 1 - index * 0.04,
                  zIndex: cards.length - index,
                  opacity: 1 - index * 0.22,
                  x: 0,
                }}
                exit={{ opacity: 0, scale: 0.9, y: 40, transition: { duration: 0.3 } }}
                transition={{
                  duration: 0.5,
                  ease: [0.16, 1, 0.3, 1],
                }}
                className={`absolute w-full h-full bg-cream border-2 border-navy p-0 flex flex-col justify-between select-none ${
                  isFront 
                    ? "shadow-[8px_8px_0px_0px_#1E4E8C] md:shadow-[12px_12px_0px_0px_#1E4E8C] cursor-grab active:cursor-grabbing" 
                    : "shadow-[6px_6px_0px_0px_rgba(30,78,140,0.3)] pointer-events-none"
                }`}
                style={{
                  transformOrigin: "top center",
                }}
                drag={isFront ? "x" : false}
                dragConstraints={{ left: 0, right: 0 }}
                onDragEnd={(e, { offset }) => {
                  const swipe = Math.abs(offset.x);
                  if (swipe > 60) {
                    if (offset.x < 0) {
                      handleNext();
                    } else {
                      handlePrev();
                    }
                  }
                }}
              >
                {/* Dossier Header Bar */}
                <div className="flex items-center justify-between border-b-2 border-navy px-5 md:px-8 py-3 bg-navy/5 font-mono text-[10px] md:text-xs uppercase tracking-widest text-navy shrink-0">
                  <span className="font-bold">
                    ARCHIVE RECORD // 0{card.id}
                  </span>
                  <span className="hidden sm:inline-block font-semibold opacity-70">
                    EST. {card.year}
                  </span>
                  <span className="font-bold border border-navy px-2 py-0.5 bg-cream">
                    FIG. 0{index + 1}
                  </span>
                </div>

                {/* Main Quote Area */}
                <div className="flex-1 p-6 sm:p-8 md:p-10 flex flex-col justify-center relative overflow-hidden">
                  <span className="absolute -top-4 -left-1 font-serif text-8xl md:text-9xl text-navy/10 pointer-events-none select-none leading-none -z-0">
                    “
                  </span>
                  <p className="font-serif italic text-xl sm:text-2xl md:text-3xl lg:text-4xl text-navy font-bold leading-snug tracking-tight relative z-10 text-left">
                    "{card.quote}"
                  </p>
                </div>

                {/* Dossier Footer / Attribution Bar */}
                <div className="flex flex-col sm:flex-row sm:items-center justify-between border-t-2 border-navy px-5 md:px-8 py-4 bg-navy/5 gap-2 shrink-0">
                  <div>
                    <h3 className="font-sans font-black text-lg md:text-xl uppercase tracking-tight text-navy leading-tight">
                      {card.author}
                    </h3>
                    <p className="font-mono text-[11px] md:text-xs font-bold tracking-widest uppercase text-navy/70 mt-0.5">
                      ROLE // {card.role}
                    </p>
                  </div>
                  <div className="flex items-center gap-2 text-[10px] md:text-xs font-mono font-bold tracking-widest uppercase text-navy/60">
                    <span className="hidden md:inline-block">VERIFIED ENDORSEMENT</span>
                  </div>
                </div>
              </motion.div>
            );
          })}
        </AnimatePresence>
      </div>

      {/* Editorial Brutalist Controls */}
      <div className="flex items-center justify-between w-full max-w-4xl mt-8 md:mt-12 z-20 px-2 gap-4">
        <button
          onClick={handlePrev}
          aria-label="Previous Testimonial"
          className="border-2 border-navy bg-cream text-navy px-4 md:px-8 py-3 font-mono text-xs md:text-sm font-bold tracking-widest uppercase hover:bg-navy hover:text-cream transition-all shadow-[4px_4px_0px_0px_#1E4E8C] active:translate-x-0.5 active:translate-y-0.5 active:shadow-none flex items-center gap-2 cursor-pointer"
        >
          <span>PREV</span>
          <span className="hidden sm:inline">RECORD</span>
        </button>

        <div className="flex items-center gap-2 md:gap-3 font-mono text-xs md:text-sm font-bold tracking-widest uppercase text-navy bg-cream border-2 border-navy px-4 py-2.5 shadow-[4px_4px_0px_0px_rgba(30,78,140,0.3)]">
          <span>0{cards[0].id} / 0{TESTIMONIALS.length}</span>
        </div>

        <button
          onClick={handleNext}
          aria-label="Next Testimonial"
          className="border-2 border-navy bg-cream text-navy px-4 md:px-8 py-3 font-mono text-xs md:text-sm font-bold tracking-widest uppercase hover:bg-navy hover:text-cream transition-all shadow-[4px_4px_0px_0px_#1E4E8C] active:translate-x-0.5 active:translate-y-0.5 active:shadow-none flex items-center gap-2 cursor-pointer"
        >
          <span>NEXT</span>
          <span className="hidden sm:inline">RECORD</span>
        </button>
      </div>
    </div>
  );
}
