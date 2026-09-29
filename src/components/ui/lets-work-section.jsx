import React, { useState } from "react";
import { Copy, Check } from "lucide-react";
import { Linkedin, Github, Instagram } from "./brand-icons";
import { useForm, ValidationError } from "@formspree/react";

export function LetsWorkTogether() {
  const [copied, setCopied] = useState(false);
  const [state, handleFormSubmit] = useForm("xgaekynq");

  const copyEmail = () => {
    navigator.clipboard.writeText("gabrielryan1999@gmail.com");
    setCopied(true);
    setTimeout(() => setCopied(false), 2500);
  };

  return (
    <section className="relative w-full min-h-[100svh] bg-navy text-cream flex flex-col justify-between border-t-2 border-cream overflow-hidden">
      
      {/* Header Row */}
      <div className="w-full flex items-center justify-between px-6 md:px-12 py-4 border-b border-cream/30 shrink-0 z-20 relative">
        <span className="text-xs font-bold tracking-widest uppercase">Chapter 06 // Contact & Inquiries</span>
        <span className="text-xs font-bold tracking-widest uppercase hidden md:inline-block">Yogyakarta, ID</span>
      </div>

      {/* Main 2-Column Editorial Spread */}
      <div className="flex-1 flex flex-col lg:flex-row w-full h-full relative">
        
        {/* Left Column: Direct Info & Editorial Pitch */}
        <div className="w-full lg:w-1/2 p-6 sm:p-10 md:p-12 lg:p-14 border-b lg:border-b-0 lg:border-r border-cream/30 flex flex-col justify-between">
          <div>
            <span className="text-xs font-mono font-bold tracking-[0.25em] uppercase opacity-70 block mb-3">
              01 // DIRECT INQUIRIES
            </span>
            <h2 className="font-serif text-5xl sm:text-6xl md:text-7xl lg:text-8xl font-black tracking-tighter leading-[0.85] mb-6">
              LET'S WORK<br />TOGETHER.
            </h2>
            <p className="font-serif text-lg md:text-xl leading-relaxed text-cream/90 max-w-lg mb-8">
              Available for curriculum development, tech mentorship, web platforms, and engineering collaborations with forward-thinking schools and edtech platforms.
            </p>
          </div>

          {/* Directory Ledger Table */}
          <div className="w-full border-t border-cream/30 pt-6 flex flex-col gap-4 mt-8 lg:mt-0">
            
            {/* Email Row */}
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-4 border-b border-cream/20">
              <span className="text-xs font-mono tracking-widest uppercase opacity-70">
                EMAIL //
              </span>
              <div className="flex items-center gap-3">
                <a
                  href="mailto:gabrielryan1999@gmail.com"
                  className="font-mono text-sm md:text-base font-bold underline decoration-cream/40 underline-offset-4 hover:decoration-cream text-cream transition-colors"
                >
                  gabrielryan1999@gmail.com
                </a>
                <button
                  onClick={copyEmail}
                  type="button"
                  aria-label="Copy email address"
                  className="border border-cream/40 px-2.5 py-1 text-[10px] font-mono tracking-widest uppercase hover:bg-cream hover:text-navy transition-colors flex items-center gap-1.5 cursor-pointer"
                >
                  {copied ? (
                    <>
                      <Check className="w-3 h-3" />
                      <span>COPIED</span>
                    </>
                  ) : (
                    <>
                      <Copy className="w-3 h-3" />
                      <span>COPY</span>
                    </>
                  )}
                </button>
              </div>
            </div>

            {/* Location Row */}
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-4 border-b border-cream/20">
              <span className="text-xs font-mono tracking-widest uppercase opacity-70">
                LOCATION //
              </span>
              <span className="font-mono text-sm font-bold text-cream">
                Yogyakarta, Indonesia (WIB · UTC+7)
              </span>
            </div>

            {/* Availability Row */}
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-4 border-b border-cream/20">
              <span className="text-xs font-mono tracking-widest uppercase opacity-70">
                STATUS //
              </span>
              <div className="flex items-center gap-2">
                <span className="w-2 h-2 bg-emerald-400 rounded-none animate-pulse"></span>
                <span className="font-mono text-sm font-bold text-cream">
                  Available for Select Projects
                </span>
              </div>
            </div>

            {/* Social Channels Row */}
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pt-1">
              <span className="text-xs font-mono tracking-widest uppercase opacity-70">
                PROFILES //
              </span>
              <div className="flex items-center gap-6">
                <a
                  href="https://www.linkedin.com/in/gabrielryan1999/"
                  target="_blank"
                  rel="noreferrer"
                  className="flex items-center gap-2 text-xs font-mono tracking-widest uppercase hover:opacity-70 transition-opacity"
                >
                  <Linkedin className="w-4 h-4" />
                  <span>LinkedIn</span>
                </a>
                <a
                  href="https://github.com/GabrielRyan1999"
                  target="_blank"
                  rel="noreferrer"
                  className="flex items-center gap-2 text-xs font-mono tracking-widest uppercase hover:opacity-70 transition-opacity"
                >
                  <Github className="w-4 h-4" />
                  <span>GitHub</span>
                </a>
                <a
                  href="https://www.instagram.com/heyitsgabrielryan/"
                  target="_blank"
                  rel="noreferrer"
                  className="flex items-center gap-2 text-xs font-mono tracking-widest uppercase hover:opacity-70 transition-opacity"
                >
                  <Instagram className="w-4 h-4" />
                  <span>Instagram</span>
                </a>
              </div>
            </div>

          </div>
        </div>

        {/* Right Column: Clean, Perfectly Aligned Brutalist Form */}
        <div className="w-full lg:w-1/2 p-6 sm:p-10 md:p-12 lg:p-14 flex flex-col justify-between bg-navy/30">
          
          <div>
            {/* Header matches left column baseline */}
            <span className="text-xs font-mono font-bold tracking-[0.25em] uppercase opacity-70 block mb-3">
              02 // DIRECT DISPATCH
            </span>
            <h3 className="font-serif text-4xl sm:text-5xl md:text-6xl font-black tracking-tighter leading-[0.85] text-cream mb-4">
              START A<br />CONVERSATION.
            </h3>
            <p className="font-serif text-base md:text-lg text-cream/80 mb-8 max-w-lg">
              Send a note directly. I review inquiries personally and will get back to your email within 24 to 48 hours.
            </p>
          </div>

          <div className="w-full my-auto">
            {state.succeeded ? (
              <div className="bg-cream text-navy p-8 md:p-10 border-2 border-cream shadow-[8px_8px_0px_0px_rgba(235,229,216,0.3)] text-left">
                <span className="font-mono text-xs font-bold tracking-widest uppercase opacity-70 block mb-2">
                  RECORD // TRANSMITTED
                </span>
                <h4 className="font-serif text-4xl md:text-5xl font-black tracking-tight mb-3">
                  MESSAGE RECEIVED.
                </h4>
                <p className="font-serif text-base md:text-lg leading-relaxed opacity-90 mb-4">
                  Thank you for reaching out. Your note has been logged directly to my inbox and I will reply within 24 to 48 hours.
                </p>
                <div className="font-mono text-xs font-bold tracking-widest uppercase opacity-60">
                  DISPATCH CONFIRMATION // GR-{new Date().getFullYear()}
                </div>
              </div>
            ) : (
              <form onSubmit={handleFormSubmit} className="flex flex-col gap-6">
                <input type="text" name="_gotcha" style={{ display: "none" }} />

                {/* Field 01: Name */}
                <div className="flex flex-col border-b-2 border-cream/30 focus-within:border-cream transition-colors pb-2">
                  <label htmlFor="contact-name" className="text-[11px] font-mono font-bold tracking-widest uppercase opacity-70 mb-1">
                    01 // YOUR NAME OR ORGANIZATION *
                  </label>
                  <input
                    id="contact-name"
                    type="text"
                    name="name"
                    required
                    placeholder="e.g. Alex Morgan / Studio Partner"
                    className="w-full bg-transparent text-cream font-serif text-xl md:text-2xl outline-none placeholder:text-cream/30 py-1"
                  />
                </div>

                {/* Field 02: Email */}
                <div className="flex flex-col border-b-2 border-cream/30 focus-within:border-cream transition-colors pb-2">
                  <label htmlFor="contact-email" className="text-[11px] font-mono font-bold tracking-widest uppercase opacity-70 mb-1">
                    02 // EMAIL ADDRESS *
                  </label>
                  <input
                    id="contact-email"
                    type="email"
                    name="email"
                    required
                    placeholder="name@organization.com"
                    className="w-full bg-transparent text-cream font-serif text-xl md:text-2xl outline-none placeholder:text-cream/30 py-1"
                  />
                  <ValidationError field="email" prefix="Email" errors={state.errors} className="text-rose-400 font-mono text-xs mt-1" />
                </div>

                {/* Field 03: Message */}
                <div className="flex flex-col border-b-2 border-cream/30 focus-within:border-cream transition-colors pb-2">
                  <label htmlFor="contact-message" className="text-[11px] font-mono font-bold tracking-widest uppercase opacity-70 mb-1">
                    03 // PROJECT SCOPE OR INQUIRY *
                  </label>
                  <textarea
                    id="contact-message"
                    name="message"
                    required
                    rows={3}
                    placeholder="Briefly describe your goals, timeline, or curriculum requirements..."
                    className="w-full bg-transparent text-cream font-serif text-lg md:text-xl outline-none placeholder:text-cream/30 py-1 resize-none leading-relaxed"
                  />
                  <ValidationError field="message" prefix="Message" errors={state.errors} className="text-rose-400 font-mono text-xs mt-1" />
                </div>

                {/* Submit Button */}
                <div className="pt-2">
                  <button
                    type="submit"
                    disabled={state.submitting}
                    className="w-full bg-cream text-navy border-2 border-cream py-4 md:py-4.5 font-mono text-xs md:text-sm font-black tracking-widest uppercase hover:bg-transparent hover:text-cream transition-all disabled:opacity-50 disabled:cursor-not-allowed cursor-pointer shadow-[6px_6px_0px_0px_rgba(235,229,216,0.25)] hover:shadow-none active:translate-x-1 active:translate-y-1 flex items-center justify-center"
                  >
                    <span>{state.submitting ? "SENDING DISPATCH..." : "SEND MESSAGE"}</span>
                  </button>
                </div>
              </form>
            )}
          </div>

          <div className="hidden lg:block h-6"></div>

        </div>

      </div>

      {/* Editorial Footer */}
      <footer className="w-full flex flex-col md:flex-row items-center justify-between border-t-2 border-cream/30 py-5 px-6 md:px-12 text-cream/70 font-mono text-xs tracking-widest uppercase shrink-0 bg-navy">
        <div className="text-center md:text-left mb-2 md:mb-0">
          &copy; {new Date().getFullYear()} GABRIEL RYAN PRIMA. ALL RIGHTS RESERVED.
        </div>
        <div className="text-center md:text-right">
          YOGYAKARTA, ID // ARCHITECTED WITH CARE
        </div>
      </footer>

    </section>
  );
}
