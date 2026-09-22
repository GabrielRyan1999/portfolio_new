import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Quote, ChevronLeft, ChevronRight } from "lucide-react";

const TESTIMONIALS = [
  {
    id: 1,
    quote: "This interactive metaverse session completely changed how our students learn. The engagement was off the charts and the students loved every second.",
    author: "Sekolah Bintang Mayantara",
    role: "School Partner",
  },
  {
    id: 2,
    quote: "The programming curriculum was so easy to follow and incredibly engaging. Our teachers feel so much more confident delivering this material now.",
    author: "Krya Global",
    role: "EdTech Partner",
  },
  {
    id: 3,
    quote: "Ryan's approach to game development mentorship is outstanding. He breaks down complex logic perfectly for absolute beginners.",
    author: "Teman Belajar Krya",
    role: "Mentorship Platform",
  },
  {
    id: 4,
    quote: "Great attention to detail and patience with beginners. Highly recommend him for any youth coding events or workshops.",
    author: "Xingzhong School",
    role: "School Partner",
  },
];

export function Testimonials() {
  const [cards, setCards] = useState(TESTIMONIALS);

  // Auto-play the stack
  useEffect(() => {
    const interval = setInterval(() => {
      handleNext();
    }, 5000);
    return () => clearInterval(interval);
  }, [cards]);

  const handleNext = () => {
    setCards((prevCards) => {
      const newCards = [...prevCards];
      const first = newCards.shift();
      newCards.push(first);
      return newCards;
    });
  };

  const handlePrev = () => {
    setCards((prevCards) => {
      const newCards = [...prevCards];
      const last = newCards.pop();
      newCards.unshift(last);
      return newCards;
    });
  };

  return (
    <div className="w-full flex flex-col items-center justify-center py-20 px-4 relative z-10">
      
      {/* Card Stack Container */}
      <div className="relative w-full max-w-xl h-[320px] md:h-[280px] flex justify-center items-center perspective-1000 mt-10">
        <AnimatePresence initial={false}>
          {cards.map((card, index) => {
            const isTop3 = index < 3;
            if (!isTop3) return null;

            return (
              <motion.div
                key={card.id}
                initial={{ opacity: 0, scale: 0.8, y: 50 }}
                animate={{
                  y: index * -25, // Stack cards upwards
                  scale: 1 - index * 0.06, // Cards in back get smaller
                  zIndex: cards.length - index,
                  opacity: 1 - index * 0.25, // Cards in back fade out
                  x: 0, // ensure card snaps back to center
                }}
                exit={{ opacity: 0, scale: 0.8, y: 50 }}
                transition={{
                  duration: 0.5,
                  ease: "easeInOut",
                }}
                className="absolute w-full h-full bg-[#0a0f1e] border border-white/10 dark:bg-zinc-900/90 dark:border-white/10 rounded-3xl p-8 md:p-10 shadow-2xl flex flex-col justify-between backdrop-blur-sm cursor-grab active:cursor-grabbing"
                style={{
                  transformOrigin: "top center",
                }}
                drag={index === 0 ? "x" : false}
                dragConstraints={{ left: 0, right: 0 }}
                onDragEnd={(e, { offset, velocity }) => {
                  const swipe = Math.abs(offset.x);
                  if (swipe > 50) {
                    handleNext(); // swipe left or right discards the front card
                  }
                }}
              >
                <div className="relative z-10 pointer-events-none">
                  <Quote className="w-12 h-12 text-blue-600/30 absolute -top-4 -left-4 md:-top-2 md:-left-2 rotate-180" />
                  <p className="text-lg md:text-xl text-slate-200 dark:text-zinc-200 font-medium leading-relaxed mt-6 relative z-10">
                    "{card.quote}"
                  </p>
                </div>

                <div className="mt-8 flex flex-col pointer-events-none">
                  <p className="text-white dark:text-white font-bold text-lg md:text-xl">{card.author}</p>
                  <p className="text-blue-400 dark:text-blue-400 font-mono text-sm uppercase tracking-wider mt-1">{card.role}</p>
                </div>
              </motion.div>
            );
          })}
        </AnimatePresence>
      </div>

      {/* Controls */}
      <div className="flex items-center gap-4 mt-8 md:mt-12 z-20">
        <button
          onClick={handlePrev}
          className="w-12 h-12 rounded-full border border-white/10 flex items-center justify-center text-slate-400 hover:text-white hover:bg-white/5 transition-all active:scale-95"
        >
          <ChevronLeft className="w-6 h-6" />
        </button>
        <button
          onClick={handleNext}
          className="w-12 h-12 rounded-full border border-white/10 flex items-center justify-center text-slate-400 hover:text-white hover:bg-white/5 transition-all active:scale-95"
        >
          <ChevronRight className="w-6 h-6" />
        </button>
      </div>

    </div>
  );
}
