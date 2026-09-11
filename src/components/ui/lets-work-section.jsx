import React, { useState } from "react"
import { ArrowUpRight, Calendar, Send } from "lucide-react"
import { Linkedin, Github, Instagram } from "./brand-icons"
import { SectionShell } from "./SectionShell"
import { useForm, ValidationError } from "@formspree/react"

export function LetsWorkTogether() {
  const [isHovered, setIsHovered] = useState(false)
  const [isClicked, setIsClicked] = useState(false)
  const [showSuccess, setShowSuccess] = useState(false)
  const [isButtonHovered, setIsButtonHovered] = useState(false)
  const [state, handleFormSubmit] = useForm("xgaekynq")

  const handleClick = (e) => {
    e.preventDefault()
    setIsClicked(true)

    setTimeout(() => {
      setShowSuccess(true)
    }, 500)
  }

  const handleBookCall = () => {
    window.open("https://cal.com/jatin-yadav05/15min", "_blank")
  }

  return (
    <SectionShell dark={false} footer={
        <div className="flex flex-col md:flex-row items-center justify-between w-full border-t border-slate-200 pt-6 mt-8 text-slate-500 dark:text-zinc-500 dark:text-zinc-400">
          <div className="text-sm font-medium text-center md:text-left">
            &copy; {new Date().getFullYear()} Gabriel Ryan.<br className="block md:hidden"/> All rights reserved.
          </div>
          <div className="flex flex-row gap-6 my-4 md:my-0">
            <a href="https://www.linkedin.com/in/gabrielryan1999/" target="_blank" rel="noreferrer" aria-label="LinkedIn" className="hover:text-blue-600 transition-colors"><Linkedin className="w-5 h-5" /></a>
            <a href="https://github.com/GabrielRyan1999" target="_blank" rel="noreferrer" aria-label="GitHub" className="hover:text-slate-900 dark:hover:text-zinc-100 transition-colors"><Github className="w-5 h-5" /></a>
            <a href="https://www.instagram.com/heyitsgabrielryan/" target="_blank" rel="noreferrer" aria-label="Instagram" className="hover:text-pink-600 transition-colors"><Instagram className="w-5 h-5" /></a>
          </div>
          <div className="text-sm text-center md:text-right hidden md:block">
            Created with 💙 by Ryan
          </div>
        </div>
      }>
      <div className="relative flex flex-col items-center gap-12">
        <div
          className="absolute inset-0 z-10 flex flex-col items-center justify-center gap-8 transition-all duration-700 ease-[cubic-bezier(0.16,1,0.3,1)]"
          style={{
            opacity: showSuccess ? 1 : 0,
            transform: showSuccess ? "translateY(0) scale(1)" : "translateY(20px) scale(0.95)",
            pointerEvents: showSuccess ? "auto" : "none",
          }}
        >
          {/* Elegant heading */}
          <div className="flex flex-col items-center gap-2">
            <span
              className="text-xs font-medium tracking-[0.3em] uppercase text-slate-500 dark:text-zinc-500 dark:text-zinc-400 transition-all duration-500"
              style={{
                transform: showSuccess ? "translateY(0)" : "translateY(10px)",
                opacity: showSuccess ? 1 : 0,
                transitionDelay: "100ms",
              }}
            >
              Perfect
            </span>
            <h3
              className="text-3xl font-light tracking-tight text-slate-900 dark:text-zinc-100 transition-all duration-500 sm:text-4xl"
              style={{
                transform: showSuccess ? "translateY(0)" : "translateY(10px)",
                opacity: showSuccess ? 1 : 0,
                transitionDelay: "200ms",
              }}
            >
              Let's talk
            </h3>
          </div>

          
          {/* Formspree Form */}
          <div 
             className="w-full max-w-sm mt-2 transition-all duration-500"
             style={{
                transform: showSuccess ? "translateY(0)" : "translateY(15px)",
                opacity: showSuccess ? 1 : 0,
                transitionDelay: "150ms",
             }}
          >
            {state.succeeded ? (
               <div className="text-center bg-slate-50 dark:bg-zinc-800/50 border border-slate-200 rounded-2xl p-6 shadow-sm">
                  <p className="text-emerald-600 font-medium text-lg">Message sent!</p>
                  <p className="text-slate-500 dark:text-zinc-500 dark:text-zinc-400 text-sm mt-2">I'll get back to you as soon as possible.</p>
               </div>
            ) : (
               <form onSubmit={handleFormSubmit} className="flex flex-col gap-4 w-full text-left">
                 <div>
                   <input 
                     type="email" 
                     name="email" 
                     placeholder="Your email address"
                     required 
                     className="w-full bg-slate-50 dark:bg-zinc-800/50 border border-slate-200 text-slate-900 dark:text-zinc-100 text-sm rounded-xl px-4 py-3 outline-none focus:border-slate-400 focus:bg-white dark:focus:bg-zinc-900 transition-all"
                   />
                   <ValidationError field="email" prefix="Email" errors={state.errors} className="text-red-500 text-xs mt-1" />
                 </div>
                 
                 <div>
                   <textarea 
                     name="message" 
                     placeholder="How can we work together?"
                     required 
                     rows="3"
                     className="w-full bg-slate-50 dark:bg-zinc-800/50 border border-slate-200 text-slate-900 dark:text-zinc-100 text-sm rounded-xl px-4 py-3 outline-none focus:border-slate-400 focus:bg-white dark:focus:bg-zinc-900 transition-all resize-none"
                   />
                   <ValidationError field="message" prefix="Message" errors={state.errors} className="text-red-500 text-xs mt-1" />
                 </div>
                 
                 <button 
                   type="submit" 
                   disabled={state.submitting}
                   className="w-full bg-slate-900 text-white rounded-xl px-4 py-3 flex items-center justify-center gap-2 text-sm font-medium hover:bg-slate-800 focus:scale-[0.98] transition-all disabled:opacity-70 disabled:cursor-not-allowed"
                 >
                   {state.submitting ? "Sending..." : "Send Message"}
                 </button>
               </form>
            )}
          </div>

          {/* Subtle subtext */}
          <span
            className="text-xs tracking-widest uppercase text-slate-400 transition-all duration-500"
            style={{
              transform: showSuccess ? "translateY(0)" : "translateY(10px)",
              opacity: showSuccess ? 1 : 0,
              transitionDelay: "450ms",
            }}
          >
            Will reply asap
          </span>
        </div>

        

        <div
          className="group relative cursor-pointer"
          onMouseEnter={() => setIsHovered(true)}
          onMouseLeave={() => setIsHovered(false)}
          onClick={handleClick}
          style={{
            pointerEvents: isClicked ? "none" : "auto",
          }}
        >
          <div className="flex flex-col items-center gap-6">
            <h2
              className="relative text-center text-5xl font-black tracking-tighter uppercase text-slate-900 dark:text-zinc-100 sm:text-6xl md:text-7xl lg:text-8xl transition-all duration-700 ease-[cubic-bezier(0.16,1,0.3,1)]"
              style={{
                opacity: isClicked ? 0 : 1,
                transform: isClicked ? "translateY(-40px) scale(0.95)" : "translateY(0) scale(1)",
              }}
            >
              <span className="block overflow-hidden pb-4 -mb-4">
                <span
                  className="block transition-transform duration-700 ease-[cubic-bezier(0.16,1,0.3,1)]"
                  style={{
                    transform: isHovered && !isClicked ? "translateY(-8%)" : "translateY(0)",
                  }}
                >
                  Let's work
                </span>
              </span>
              <span className="block overflow-hidden pb-4 -mb-4">
                <span
                  className="block transition-transform duration-700 ease-[cubic-bezier(0.16,1,0.3,1)] delay-75"
                  style={{
                    transform: isHovered && !isClicked ? "translateY(-8%)" : "translateY(0)",
                  }}
                >
                  <span className="text-slate-400 dark:text-zinc-400">together</span>
                </span>
              </span>
            </h2>

            <div className="relative mt-4 flex w-16 h-16 items-center justify-center sm:w-20 sm:h-20">
              <div
                className="pointer-events-none absolute inset-0 rounded-full border transition-all ease-out"
                style={{
                  borderColor: isClicked ? "var(--foreground)" : isHovered ? "var(--foreground)" : "var(--card-border)",
                  backgroundColor: isClicked ? "transparent" : isHovered ? "var(--foreground)" : "transparent",
                  transform: isClicked ? "scale(3)" : isHovered ? "scale(1.1)" : "scale(1)",
                  opacity: isClicked ? 0 : 1,
                  transitionDuration: isClicked ? "700ms" : "500ms",
                }}
              />
              <ArrowUpRight
                className="w-6 h-6 transition-all ease-[cubic-bezier(0.16,1,0.3,1)] sm:w-7 sm:h-7"
                style={{
                  transform: isClicked
                    ? "translate(100px, -100px) scale(0.5)"
                    : isHovered
                      ? "translate(2px, -2px)"
                      : "translate(0, 0)",
                  opacity: isClicked ? 0 : 1,
                  color: isHovered && !isClicked ? "var(--background)" : "var(--foreground)",
                  transitionDuration: isClicked ? "600ms" : "500ms",
                }}
              />
            </div>
          </div>

          <div className="absolute -left-8 top-1/2 -translate-y-1/2 sm:-left-16">
            <div
              className="h-px w-8 bg-slate-200 transition-all duration-500 sm:w-12"
              style={{
                transform: isClicked ? "scaleX(0) translateX(-20px)" : isHovered ? "scaleX(1.5)" : "scaleX(1)",
                opacity: isClicked ? 0 : isHovered ? 1 : 0.5,
              }}
            />
          </div>
          <div className="absolute -right-8 top-1/2 -translate-y-1/2 sm:-right-16">
            <div
              className="h-px w-8 bg-slate-200 transition-all duration-500 sm:w-12"
              style={{
                transform: isClicked ? "scaleX(0) translateX(20px)" : isHovered ? "scaleX(1.5)" : "scaleX(1)",
                opacity: isClicked ? 0 : isHovered ? 1 : 0.5,
              }}
            />
          </div>
        </div>

        <div
          className="mt-8 flex flex-col items-center gap-4 text-center transition-all duration-500 delay-100"
          style={{
            opacity: isClicked ? 0 : 1,
            transform: isClicked ? "translateY(20px)" : "translateY(0)",
            pointerEvents: isClicked ? "none" : "auto",
          }}
        >
          <p className="max-w-md text-sm leading-relaxed text-slate-500 dark:text-zinc-500 dark:text-zinc-400">
            Have a project in mind? I'd love to hear about it. Let's create something exceptional together.
          </p>
          
          
        </div>
      </div>
    </SectionShell>
  )
}
