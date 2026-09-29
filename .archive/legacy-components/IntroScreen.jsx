import { motion } from 'framer-motion';
import Magnetic from './Magnetic';
import { ArrowRight } from 'lucide-react';

export function IntroScreen({ onEnter }) {
  return (
    <motion.div
      className="fixed inset-0 z-[200] flex items-center justify-center overflow-hidden"
      initial={{ opacity: 1 }}
      exit={{ y: "-100%", transition: { duration: 1, ease: [0.76, 0, 0.24, 1] } }} // Smooth slide up exit
    >
      {/* Solid Background */}
      <div className="absolute inset-0 flex">
        <div className="w-full h-full bg-[var(--background)]" />
      </div>

      {/* Background Graphic (Orbital System Theme) */}
      <div className="absolute inset-0 flex items-center justify-center pointer-events-none overflow-hidden">
        {/* Outer orbital track */}
        <motion.div 
          className="absolute w-[400px] h-[400px] md:w-[700px] md:h-[700px] rounded-full border border-[var(--color-brand)]/20 border-dashed"
          animate={{ rotate: 360 }}
          transition={{ duration: 100, repeat: Infinity, ease: "linear" }}
        >
          {/* Orbital Nodes */}
          <div className="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-1/2 w-3 h-3 bg-cyan-400/80 rounded-full shadow-[0_0_15px_rgba(34,211,238,0.6)]" />
          <div className="absolute bottom-1/4 left-[10%] w-2 h-2 bg-blue-500/40 rounded-full" />
        </motion.div>

        {/* Inner orbital track */}
        <motion.div 
          className="absolute w-[250px] h-[250px] md:w-[450px] md:h-[450px] rounded-full border border-[var(--color-brand)]/30"
          animate={{ rotate: -360 }}
          transition={{ duration: 60, repeat: Infinity, ease: "linear" }}
        >
          <div className="absolute bottom-0 left-1/2 -translate-x-1/2 translate-y-1/2 w-4 h-4 bg-[var(--color-brand)]/60 rounded-full shadow-[0_0_20px_rgba(37,99,235,0.6)]" />
        </motion.div>
        
        {/* Core segment ring */}
        <motion.div 
          className="absolute w-[150px] h-[150px] md:w-[250px] md:h-[250px] rounded-full border-[20px] border-[var(--color-brand)]/5 border-t-[var(--color-brand)]/30 border-r-cyan-400/20"
          animate={{ rotate: 360 }}
          transition={{ duration: 40, repeat: Infinity, ease: "linear" }}
        />

        {/* Center Glow */}
        <div className="absolute w-[40vw] h-[40vw] md:w-[30vw] md:h-[30vw] rounded-full bg-[var(--color-brand)]/15 blur-[120px]" />
      </div>

      {/* Main Content */}
      <div className="relative z-10 flex flex-col items-center text-center px-4">
        <motion.div
          initial={{ scale: 0.9, opacity: 0, y: 20 }}
          animate={{ scale: 1, opacity: 1, y: 0 }}
          transition={{ duration: 1.2, delay: 0.3, ease: [0.16, 1, 0.3, 1] }}
          className="mb-10"
        >

          
          <h1 className="text-5xl md:text-7xl lg:text-8xl font-bold tracking-tight mb-6 leading-[1.1] text-[var(--foreground)]">
            Teaching Minds. <br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-cyan-300">
               Building Systems.
            </span>
          </h1>
          
          <p className="text-[var(--foreground-muted)] text-lg max-w-lg mx-auto">
            Educator at heart, developer by trade. Exploring the intersection of curriculum, code, and human potential.
          </p>
        </motion.div>

        <motion.div
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ duration: 0.8, delay: 0.8, ease: "easeOut" }}
        >
          <Magnetic>
            <button 
              onClick={onEnter}
              className="group relative flex items-center gap-3 px-8 py-4 bg-[var(--color-brand)] text-white rounded-full font-bold text-lg hover:shadow-[0_0_40px_rgba(37,99,235,0.4)] transition-all overflow-hidden"
            >
              <div className="absolute inset-0 bg-white/20 translate-y-[100%] group-hover:translate-y-0 transition-transform duration-300" />
              <span className="relative z-10">Enter Portfolio</span>
              <ArrowRight className="relative z-10 w-5 h-5 group-hover:translate-x-1 transition-transform" />
            </button>
          </Magnetic>
        </motion.div>
      </div>
    </motion.div>
  );
}
