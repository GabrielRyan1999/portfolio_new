import re

with open('src/components/ui/lets-work-section.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the entire LetsWorkTogether function
regex = r'export function LetsWorkTogether\(\) \{[\s\S]*'

new_component = '''export function LetsWorkTogether() {
    const [isHovered, setIsHovered] = useState(false)
    const [isClicked, setIsClicked] = useState(false)
    const [showSuccess, setShowSuccess] = useState(false)
    
    const [state, handleFormSubmit] = useForm("xgaekynq")
  
    const handleClick = (e) => {
      e.preventDefault()
      setIsClicked(true)
  
      setTimeout(() => {
        setShowSuccess(true)
      }, 500)
    }
  
    return (
      <section className="relative w-full min-h-[100svh] bg-[#1A365D] flex flex-col justify-center items-center py-32 px-6 border-t-2 border-[#F5F2EB] text-[#F5F2EB] overflow-hidden">
        
        <div className="absolute top-8 left-8">
           <span className="font-mono text-xs tracking-widest uppercase opacity-50">Chapter 06 // Initiate</span>
        </div>

        <div className="relative flex flex-col items-center gap-12 w-full max-w-4xl z-10">
          <div
            className="absolute inset-0 z-10 flex flex-col items-center justify-center gap-12 transition-all duration-700 ease-[cubic-bezier(0.16,1,0.3,1)]"
            style={{
              opacity: showSuccess ? 1 : 0,
              transform: showSuccess ? "translateY(0) scale(1)" : "translateY(20px) scale(0.95)",
              pointerEvents: showSuccess ? "auto" : "none",
            }}
          >
            {/* Elegant heading */}
            <div className="flex flex-col items-center gap-4">
              <span
                className="text-xs font-mono tracking-[0.3em] uppercase text-[#F5F2EB]/50 transition-all duration-500"
                style={{
                  transform: showSuccess ? "translateY(0)" : "translateY(10px)",
                  opacity: showSuccess ? 1 : 0,
                  transitionDelay: "100ms",
                }}
              >
                Transmission
              </span>
              <h3
                className="font-serif text-5xl md:text-7xl font-black tracking-tighter text-[#F5F2EB] transition-all duration-500"
                style={{
                  transform: showSuccess ? "translateY(0)" : "translateY(10px)",
                  opacity: showSuccess ? 1 : 0,
                  transitionDelay: "200ms",
                }}
              >
                ESTABLISH CONTACT
              </h3>
            </div>
  
            
            {/* Formspree Form */}
            <div 
               className="w-full max-w-2xl mt-4 transition-all duration-500"
               style={{
                  transform: showSuccess ? "translateY(0)" : "translateY(15px)",
                  opacity: showSuccess ? 1 : 0,
                  transitionDelay: "150ms",
               }}
            >
              {state.succeeded ? (
                 <div className="text-center bg-[#F5F2EB] border-2 border-[#1A365D] p-12 shadow-[8px_8px_0px_0px_rgba(245,242,235,0.3)]">
                    <p className="text-[#1A365D] font-black font-serif text-4xl mb-4">RECEIVED.</p>
                    <p className="text-[#1A365D]/80 font-mono text-sm uppercase tracking-widest">I will respond shortly.</p>
                 </div>
              ) : (
                 <form onSubmit={handleFormSubmit} className="flex flex-col gap-8 w-full text-left">
                   <input type="text" name="_gotcha" style={{ display: 'none' }} />
                   
                   <div>
                     <input 
                       type="email" 
                       name="email" 
                       aria-label="Email address"
                       placeholder="Enter your email address..."
                       required 
                       className="w-full bg-transparent border-b-2 border-[#F5F2EB]/30 text-[#F5F2EB] font-serif text-2xl md:text-4xl py-4 outline-none focus:border-[#F5F2EB] placeholder:text-[#F5F2EB]/20 transition-all rounded-none"
                     />
                     <ValidationError field="email" prefix="Email" errors={state.errors} className="text-rose-400 font-mono text-xs mt-2" />
                   </div>
                   
                   <div>
                     <textarea 
                       name="message" 
                       aria-label="Message content"
                       placeholder="How can we collaborate?"
                       required 
                       rows="2"
                       className="w-full bg-transparent border-b-2 border-[#F5F2EB]/30 text-[#F5F2EB] font-serif text-2xl md:text-4xl py-4 outline-none focus:border-[#F5F2EB] placeholder:text-[#F5F2EB]/20 transition-all resize-none rounded-none"
                     />
                     <ValidationError field="message" prefix="Message" errors={state.errors} className="text-rose-400 font-mono text-xs mt-2" />
                   </div>
                   
                   <button 
                     type="submit" 
                     disabled={state.submitting}
                     className="w-full bg-[#F5F2EB] text-[#1A365D] border-2 border-[#F5F2EB] mt-8 py-6 flex items-center justify-center font-mono font-bold tracking-widest uppercase hover:bg-transparent hover:text-[#F5F2EB] transition-all disabled:opacity-50 disabled:cursor-not-allowed group"
                   >
                     {state.submitting ? "Transmitting..." : "Send Transmission"}
                   </button>
                 </form>
              )}
            </div>
          </div>
  
          <button
            type="button"
            aria-label="Open contact form"
            aria-expanded={isClicked}
            className="group relative cursor-pointer appearance-none bg-transparent border-none p-0 outline-none w-full flex justify-center"
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
            onFocus={() => setIsHovered(true)}
            onBlur={() => setIsHovered(false)}
            onClick={handleClick}
            style={{ pointerEvents: isClicked ? "none" : "auto" }}
          >
            <div className="flex flex-col items-center gap-0">
              <h2
                className="relative text-center text-[12vw] leading-[0.8] font-black tracking-tighter uppercase font-serif text-[#F5F2EB] transition-all duration-700 ease-[cubic-bezier(0.16,1,0.3,1)]"
                style={{
                  opacity: isClicked ? 0 : 1,
                  transform: isClicked ? "translateY(-40px) scale(0.95)" : "translateY(0) scale(1)",
                }}
              >
                <span className="block overflow-hidden">
                  <span
                    className="block transition-transform duration-700 ease-[cubic-bezier(0.16,1,0.3,1)] group-hover:italic"
                    style={{ transform: isHovered && !isClicked ? "scale(1.05)" : "scale(1)" }}
                  >
                    INITIATE
                  </span>
                </span>
                <span className="block overflow-hidden">
                  <span
                    className="block transition-transform duration-700 ease-[cubic-bezier(0.16,1,0.3,1)] delay-75 opacity-70 group-hover:opacity-100"
                    style={{ transform: isHovered && !isClicked ? "scale(1.05)" : "scale(1)" }}
                  >
                    CONTACT
                  </span>
                </span>
              </h2>

              <div className="relative mt-12 flex w-24 h-24 items-center justify-center">
                <div
                  className="pointer-events-none absolute inset-0 rounded-full border-2 transition-all ease-out"
                  style={{
                    borderColor: isClicked ? "transparent" : isHovered ? "#F5F2EB" : "rgba(245,242,235,0.3)",
                    backgroundColor: isClicked ? "transparent" : isHovered ? "#F5F2EB" : "transparent",
                    transform: isClicked ? "scale(3)" : isHovered ? "scale(1.1)" : "scale(1)",
                    opacity: isClicked ? 0 : 1,
                    transitionDuration: isClicked ? "700ms" : "500ms",
                  }}
                />
                <ArrowUpRight
                  className="w-10 h-10 transition-all ease-[cubic-bezier(0.16,1,0.3,1)]"
                  style={{
                    transform: isClicked
                      ? "translate(100px, -100px) scale(0.5)"
                      : isHovered
                        ? "translate(4px, -4px)"
                        : "translate(0, 0)",
                    opacity: isClicked ? 0 : 1,
                    color: isHovered && !isClicked ? "#1A365D" : "#F5F2EB",
                    transitionDuration: isClicked ? "600ms" : "500ms",
                  }}
                />
              </div>
            </div>
          </button>
        </div>
        
        {/* Footer */}
        <div className="absolute bottom-0 left-0 w-full flex flex-col md:flex-row items-center justify-between border-t-2 border-[#F5F2EB]/30 py-6 px-6 md:px-12 text-[#F5F2EB]/70 font-mono text-xs tracking-widest uppercase">
          <div className="text-center md:text-left mb-4 md:mb-0">
            &copy; {new Date().getFullYear()} Gabriel Ryan. All rights reserved.
          </div>
          <div className="flex flex-row gap-8 my-4 md:my-0">
            <a href="https://www.linkedin.com/in/gabrielryan1999/" target="_blank" rel="noreferrer" className="hover:text-[#F5F2EB] transition-colors">LinkedIn</a>
            <a href="https://github.com/GabrielRyan1999" target="_blank" rel="noreferrer" className="hover:text-[#F5F2EB] transition-colors">GitHub</a>
            <a href="https://www.instagram.com/heyitsgabrielryan/" target="_blank" rel="noreferrer" className="hover:text-[#F5F2EB] transition-colors">Instagram</a>
          </div>
          <div className="text-center md:text-right hidden md:block">
            ARCHITECTED BY RYAN
          </div>
        </div>

      </section>
    )
}
'''

content = re.sub(regex, new_component, content, flags=re.DOTALL)

with open('src/components/ui/lets-work-section.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Redesigned Contact section.')
