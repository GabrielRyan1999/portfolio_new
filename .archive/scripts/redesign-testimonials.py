import re

with open('src/components/ui/unique-testimonial.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

regex = r'export function Testimonials\(\) \{[\s\S]*'

new_component = '''export function Testimonials() {
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
    <div className="w-full flex flex-col items-center justify-center py-10 px-4 relative z-10">
      
      {/* Card Stack Container */}
      <div className="relative w-full max-w-5xl h-[450px] md:h-[400px] lg:h-[450px] flex justify-center items-center perspective-1000 mt-4">
        <AnimatePresence initial={false}>
          {cards.map((card, index) => {
            const isTop3 = index < 3;
            if (!isTop3) return null;

            return (
              <motion.div
                key={card.id}
                initial={{ opacity: 0, scale: 0.95, y: 30 }}
                animate={{
                  y: index * -20, // Stack cards slightly upwards
                  scale: 1, // Keep scale consistent for a hard brutalist stack
                  zIndex: cards.length - index,
                  opacity: 1, 
                  x: index * 10, // Slight offset to the right to see the stack
                }}
                exit={{ opacity: 0, scale: 0.95, y: 50 }}
                transition={{
                  duration: 0.4,
                  ease: "easeOut",
                }}
                className="absolute w-full h-full bg-[#1A365D] border-2 border-[#1A365D] rounded-none p-8 md:p-12 lg:p-16 flex flex-col justify-between cursor-grab active:cursor-grabbing shadow-[8px_8px_0px_0px_rgba(26,54,93,0.15)]"
                style={{
                  transformOrigin: "bottom right",
                }}
                drag={index === 0 ? "x" : false}
                dragConstraints={{ left: 0, right: 0 }}
                onDragEnd={(e, { offset, velocity }) => {
                  const swipe = Math.abs(offset.x);
                  if (swipe > 50) {
                    handleNext(); 
                  }
                }}
              >
                <div className="relative z-10 pointer-events-none flex-1 flex flex-col justify-center">
                  <div className="absolute -top-12 -left-4 md:-left-8 text-8xl md:text-[10rem] font-serif font-black text-[#F5F2EB]/10 leading-none">
                    "
                  </div>
                  <p className="font-serif text-2xl md:text-3xl lg:text-5xl text-[#F5F2EB] font-bold leading-[1.1] tracking-tighter relative z-10">
                    {card.quote}
                  </p>
                </div>

                <div className="mt-12 flex flex-col md:flex-row md:items-end justify-between border-t border-[#F5F2EB]/20 pt-6 pointer-events-none gap-4">
                  <div>
                     <p className="text-[#F5F2EB] font-black text-xl md:text-2xl uppercase tracking-tighter">{card.author}</p>
                     <p className="text-[#F5F2EB]/60 font-mono text-xs md:text-sm uppercase tracking-widest mt-1">{card.role}</p>
                  </div>
                  <div className="font-mono text-[10px] text-[#F5F2EB]/40 uppercase tracking-widest">
                     Record No. 0{card.id}
                  </div>
                </div>
              </motion.div>
            );
          })}
        </AnimatePresence>
      </div>

      {/* Brutalist Controls */}
      <div className="flex items-center gap-4 mt-16 md:mt-20 z-20">
        <button
          onClick={handlePrev}
          aria-label="Previous Testimonial"
          className="px-8 py-3 border-2 border-[#1A365D] text-[#1A365D] font-mono font-bold text-xs uppercase tracking-widest hover:bg-[#1A365D] hover:text-[#F5F2EB] transition-colors active:scale-95"
        >
          Previous
        </button>
        <button
          onClick={handleNext}
          aria-label="Next Testimonial"
          className="px-8 py-3 border-2 border-[#1A365D] text-[#1A365D] font-mono font-bold text-xs uppercase tracking-widest hover:bg-[#1A365D] hover:text-[#F5F2EB] transition-colors active:scale-95"
        >
          Next
        </button>
      </div>

    </div>
  );
}
'''

content = re.sub(regex, new_component, content, flags=re.DOTALL)

with open('src/components/ui/unique-testimonial.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Redesigned Testimonials component.')
