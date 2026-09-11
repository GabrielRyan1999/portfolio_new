import React, { useState, useEffect } from 'react';
import { X, ChevronLeft, ChevronRight } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

export function HoverExpandGallery({ images }) {
  const [lightboxIndex, setLightboxIndex] = useState(null);

  // Close lightbox on escape key
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape') setLightboxIndex(null);
      if (e.key === 'ArrowRight' && lightboxIndex !== null) {
        setLightboxIndex((prev) => (prev + 1) % images.length);
      }
      if (e.key === 'ArrowLeft' && lightboxIndex !== null) {
        setLightboxIndex((prev) => (prev - 1 + images.length) % images.length);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [lightboxIndex, images.length]);

  return (
    <>
      <div className="w-full h-[55vh] md:h-[65vh] flex gap-2 md:gap-4 overflow-hidden rounded-3xl">
        {images.map((img, i) => (
          <div
            key={i}
            className="group relative h-full flex-1 hover:flex-[3] transition-[flex] duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] overflow-hidden rounded-2xl cursor-pointer"
            onClick={() => setLightboxIndex(i)}
          >
            <img
              src={img.image || img.src}
              alt={img.title || img.alt || ''}
              className="w-full h-full object-cover"
            />
            {/* caption muncul on hover, overlay gradient bawah */}
            <div className="absolute inset-x-0 bottom-0 p-4 md:p-6 bg-gradient-to-t from-black/90 via-black/40 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300">
              <h4 className="text-white font-bold text-lg">{img.title}</h4>
              <p className="text-slate-300 text-sm mt-1">{img.description || img.caption}</p>
            </div>
          </div>
        ))}
      </div>

      <AnimatePresence>
        {lightboxIndex !== null && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 z-[100] bg-black/95 backdrop-blur-sm flex items-center justify-center"
            onClick={() => setLightboxIndex(null)}
          >
            <button
              onClick={() => setLightboxIndex(null)}
              className="absolute top-6 right-6 p-2 text-white/70 hover:text-white bg-white/10 hover:bg-white/20 rounded-full transition-colors z-[110]"
            >
              <X className="w-8 h-8" />
            </button>

            <button
              onClick={(e) => {
                e.stopPropagation();
                setLightboxIndex((prev) => (prev - 1 + images.length) % images.length);
              }}
              className="absolute left-4 md:left-8 top-1/2 -translate-y-1/2 p-3 text-white/70 hover:text-white bg-white/10 hover:bg-white/20 rounded-full transition-colors z-[110]"
            >
              <ChevronLeft className="w-6 h-6 md:w-8 md:h-8" />
            </button>

            <button
              onClick={(e) => {
                e.stopPropagation();
                setLightboxIndex((prev) => (prev + 1) % images.length);
              }}
              className="absolute right-4 md:right-8 top-1/2 -translate-y-1/2 p-3 text-white/70 hover:text-white bg-white/10 hover:bg-white/20 rounded-full transition-colors z-[110]"
            >
              <ChevronRight className="w-6 h-6 md:w-8 md:h-8" />
            </button>

            <motion.div
              key={lightboxIndex}
              initial={{ scale: 0.9, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              exit={{ scale: 0.9, opacity: 0 }}
              transition={{ type: "spring", damping: 25, stiffness: 300 }}
              className="relative max-w-5xl w-full max-h-[85vh] p-4 md:p-8 flex flex-col items-center justify-center pointer-events-none"
            >
              <img
                src={images[lightboxIndex].image || images[lightboxIndex].src}
                alt={images[lightboxIndex].title || images[lightboxIndex].alt}
                className="max-w-full max-h-[70vh] object-contain rounded-lg shadow-2xl pointer-events-auto"
                onClick={(e) => e.stopPropagation()}
              />
              <div className="mt-6 text-center pointer-events-auto">
                 <h3 className="text-white text-xl md:text-2xl font-bold">{images[lightboxIndex].title}</h3>
                 <p className="text-slate-400 mt-2 text-sm md:text-base max-w-2xl mx-auto">{images[lightboxIndex].description || images[lightboxIndex].caption}</p>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  );
}
