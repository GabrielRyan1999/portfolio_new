"use client"

import { useState } from "react"
import { cn } from "../../lib/utils"

const testimonials = [
  {
    id: 1,
    quote: "This interactive metaverse session completely changed how our students learn.",
    author: "Sekolah Bintang Mayantara",
    role: "School Partner",
    screenshot: "https://images.unsplash.com/photo-1517048676732-d65bc937f952?q=80&w=800",
  },
  {
    id: 2,
    quote: "The programming curriculum was so easy to follow and incredibly engaging.",
    author: "Krya Global",
    role: "EdTech Partner",
    screenshot: "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=800",
  },
  {
    id: 3,
    quote: "Ryan's approach to game development mentorship is outstanding.",
    author: "Teman Belajar Krya",
    role: "Mentorship Platform",
    screenshot: "https://images.unsplash.com/photo-1542831371-29b0f74f9713?q=80&w=800",
  },
  {
    id: 4,
    quote: "Great attention to detail and patience with beginners.",
    author: "Dharma Mulya",
    role: "Educational Institution",
    screenshot: "https://images.unsplash.com/photo-1509062522246-3755977927d7?q=80&w=800",
  },
  {
    id: 5,
    quote: "Highly recommend for any kids coding events.",
    author: "Xingzhong School",
    role: "School Partner",
    screenshot: "https://images.unsplash.com/photo-1516321497487-e288fb19713f?q=80&w=800",
  },
  {
    id: 6,
    quote: "The 3D modeling class was a huge hit with the students.",
    author: "Parent A",
    role: "Student Parent",
    screenshot: "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?q=80&w=800",
  },
  {
    id: 7,
    quote: "We saw an immediate improvement in logical thinking.",
    author: "Parent B",
    role: "Student Parent",
    screenshot: "https://images.unsplash.com/photo-1427504494785-3a9ca7044f45?q=80&w=800",
  },
  {
    id: 8,
    quote: "Very professional and always brings fresh ideas to the table.",
    author: "Tech Edu",
    role: "Collaborator",
    screenshot: "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?q=80&w=800",
  },
  {
    id: 9,
    quote: "Managed our IT systems flawlessly during the online transition.",
    author: "Krya Operations",
    role: "Internal Team",
    screenshot: "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=800",
  },
  {
    id: 10,
    quote: "Our students successfully built their first games in just 4 weeks!",
    author: "Coding Bootcamp",
    role: "Event Partner",
    screenshot: "https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=800",
  }
]

export function Testimonials() {
  const [activeIndex, setActiveIndex] = useState(0)
  const [isAnimating, setIsAnimating] = useState(false)
  
  const activeTestimonial = testimonials[activeIndex];

  const handleSelect = (index) => {
    if (index === activeIndex || isAnimating) return
    setIsAnimating(true)
    setTimeout(() => {
      setActiveIndex(index)
      setTimeout(() => setIsAnimating(false), 300)
    }, 150)
  }

  return (
    <div className="flex flex-col items-center gap-6 w-full py-0">
      {/* Screenshot & Text Container */}
      <div className="relative w-full max-w-4xl px-2 flex flex-col items-center gap-6 md:gap-10">
        <div 
           className={cn(
            "w-full aspect-[16/9] md:aspect-[21/9] rounded-3xl overflow-hidden shadow-2xl border border-[var(--color-brand)]/20 bg-muted transition-all duration-300 ease-out",
            isAnimating ? "opacity-0 blur-sm scale-[0.98]" : "opacity-100 blur-0 scale-100"
          )}
        >
          <img 
            src={activeTestimonial.screenshot} 
            alt={`Screenshot from ${activeTestimonial.author}`} 
            className="w-full h-full object-cover"
          />
        </div>

        <div className="relative px-6">
            <span className="absolute -left-4 md:-left-8 -top-6 md:-top-10 text-6xl md:text-8xl font-serif text-black/10 dark:text-white/10 select-none pointer-events-none">
              "
            </span>
            <p
              className={cn(
                "text-xl md:text-3xl font-light text-[var(--foreground)] text-center max-w-3xl leading-relaxed transition-all duration-300 ease-out",
                isAnimating ? "opacity-0 blur-sm scale-[0.98]" : "opacity-100 blur-0 scale-100",
              )}
            >
              {activeTestimonial.quote}
            </p>
            <span className="absolute -right-4 md:-right-8 -bottom-8 md:-bottom-12 text-6xl md:text-8xl font-serif text-black/10 dark:text-white/10 select-none pointer-events-none">
              "
            </span>
        </div>
      </div>

      <div className="flex flex-col items-center gap-4 mt-2 w-full">
        <p
          className={cn(
            "text-xs md:text-sm text-blue-600 dark:text-blue-400 font-bold tracking-[0.2em] uppercase transition-all duration-400 ease-out",
            isAnimating ? "opacity-0 translate-y-1" : "opacity-100 translate-y-0",
          )}
        >
          {activeTestimonial.role}
        </p>

        {/* Auto-scrolling buttons container */}
        <div className="w-full overflow-hidden relative mt-4 md:mt-8 rounded-full">
          {/* Fading edges to blend with the card background */}
          <div className="absolute left-0 top-0 bottom-0 w-8 bg-gradient-to-r from-[var(--card)] to-transparent z-10 pointer-events-none" />
          <div className="absolute right-0 top-0 bottom-0 w-8 bg-gradient-to-l from-[var(--card)] to-transparent z-10 pointer-events-none" />
          
          <div className="flex items-center gap-2 w-max animate-slide-left pause-on-hover px-4">
            {/* Render list twice for infinite scrolling illusion */}
            {[...testimonials, ...testimonials].map((testimonial, index) => {
              const actualIndex = index % testimonials.length;
              const isActive = activeIndex === actualIndex;

              return (
                <button
                  key={`${testimonial.id}-${index}`}
                  onClick={() => handleSelect(actualIndex)}
                  className={cn(
                    "relative flex items-center shrink-0 px-6 py-2.5 md:py-3 md:px-8 rounded-full cursor-pointer",
                    "transition-all duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] font-bold text-sm md:text-base border",
                    isActive ? "bg-[var(--color-brand)] text-white border-[var(--color-brand)] shadow-[0_0_10px_rgba(37,99,235,0.4)]" : "bg-[var(--background)] border-[var(--card-border)] text-foreground hover:bg-[var(--card)] hover:border-[var(--color-brand)]/50",
                  )}
                >
                  {testimonial.author}
                </button>
              )
            })}
          </div>
        </div>
      </div>
    </div>
  )
}
