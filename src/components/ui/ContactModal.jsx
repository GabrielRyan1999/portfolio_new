import React, { useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { X, CheckCircle2 } from 'lucide-react';
import { useForm, ValidationError } from "@formspree/react";

export function ContactModal({ isOpen, onClose }) {
  const [state, handleFormSubmit] = useForm("xgaekynq");
  const [showSuccess, setShowSuccess] = React.useState(false);

  useEffect(() => {
    if (state.succeeded) {
      setShowSuccess(true);
      const timer = setTimeout(() => {
        setShowSuccess(false);
        onClose();
      }, 2500);
      return () => clearTimeout(timer);
    }
  }, [state.succeeded, onClose]);

  // Prevent background scrolling when open
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = 'unset';
    }
    return () => { document.body.style.overflow = 'unset'; };
  }, [isOpen]);

  return (
    <AnimatePresence>
      {isOpen && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          className="fixed inset-0 z-[9999] flex items-center justify-center bg-white/90 dark:bg-[#09090b]/90 backdrop-blur-md p-4"
        >
          <motion.div
            initial={{ scale: 0.95, y: 20, opacity: 0 }}
            animate={{ scale: 1, y: 0, opacity: 1 }}
            exit={{ scale: 0.95, y: 20, opacity: 0 }}
            transition={{ type: "spring", bounce: 0.3, duration: 0.6 }}
            className="w-full max-w-lg bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800 rounded-3xl p-6 md:p-10 shadow-2xl relative"
          >
            <button 
              onClick={onClose}
              className="absolute top-6 right-6 p-2 rounded-full hover:bg-slate-100 dark:hover:bg-zinc-800 text-slate-500 transition-colors"
            >
              <X className="w-5 h-5" />
            </button>

            {showSuccess ? (
              <motion.div 
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                className="flex flex-col items-center justify-center py-10 text-center space-y-4"
              >
                <div className="w-16 h-16 bg-green-100 dark:bg-green-900/30 text-green-600 dark:text-green-400 rounded-full flex items-center justify-center mb-2">
                  <CheckCircle2 className="w-8 h-8" />
                </div>
                <h3 className="text-2xl font-bold text-slate-900 dark:text-zinc-100">Message Sent!</h3>
                <p className="text-slate-500 dark:text-zinc-400">Thanks for reaching out. I'll get back to you shortly.</p>
              </motion.div>
            ) : (
              <>
                <div className="mb-8">
                  <h2 className="text-3xl font-black text-slate-900 dark:text-zinc-100 tracking-tight mb-2">Get in touch</h2>
                  <p className="text-slate-500 dark:text-zinc-400">Send me a quick message and let's talk about your project.</p>
                </div>

                <form onSubmit={handleFormSubmit} className="space-y-4 w-full">
                  <div>
                    <label className="block text-sm font-medium text-slate-700 dark:text-zinc-300 mb-1.5">Email Address</label>
                    <input 
                      type="email" 
                      name="email" 
                      placeholder="hello@example.com"
                      required 
                      className="w-full bg-slate-50 dark:bg-zinc-800/50 border border-slate-200 dark:border-zinc-700 text-slate-900 dark:text-zinc-100 text-sm rounded-xl px-4 py-3 outline-none focus:border-blue-500 focus:bg-white dark:focus:bg-zinc-900 transition-all"
                    />
                    <ValidationError field="email" prefix="Email" errors={state.errors} className="text-red-500 text-xs mt-1" />
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-slate-700 dark:text-zinc-300 mb-1.5">Message</label>
                    <textarea 
                      name="message" 
                      placeholder="How can we work together?"
                      required 
                      rows="4"
                      className="w-full bg-slate-50 dark:bg-zinc-800/50 border border-slate-200 dark:border-zinc-700 text-slate-900 dark:text-zinc-100 text-sm rounded-xl px-4 py-3 outline-none focus:border-blue-500 focus:bg-white dark:focus:bg-zinc-900 transition-all resize-none"
                    />
                    <ValidationError field="message" prefix="Message" errors={state.errors} className="text-red-500 text-xs mt-1" />
                  </div>
                  
                  <button 
                    type="submit" 
                    disabled={state.submitting}
                    className="w-full bg-blue-600 hover:bg-blue-700 text-white rounded-xl px-4 py-3.5 mt-2 flex items-center justify-center gap-2 text-sm font-bold transition-all disabled:opacity-70 disabled:cursor-not-allowed shadow-lg shadow-blue-600/20"
                  >
                    {state.submitting ? "Sending..." : "Send Message"}
                  </button>
                </form>
              </>
            )}
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
