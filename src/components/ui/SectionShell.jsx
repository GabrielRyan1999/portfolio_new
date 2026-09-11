import React from 'react';

export function SectionShell({
  id,
  header,
  label,
  watermark,
  children,
  footer,
  dark = false,
  className = ''
}) {
  return (
    <section
      id={id}
      className={`w-full min-h-[100dvh] h-auto relative overflow-hidden snap-start snap-always flex flex-col ${dark ? 'bg-[var(--background-secondary)]' : 'bg-[var(--background)]'} text-[var(--foreground)] ${className}`}
    >
      {/* Header layer */}
      {header ? (
         header
      ) : (label || watermark) ? (
         <div className="relative shrink-0 px-6 md:px-8 lg:px-12 pt-10 md:pt-16 max-w-7xl w-full mx-auto">
            {watermark && (
              <span className={`absolute top-0 left-6 md:left-8 lg:left-12 text-7xl md:text-[10rem] font-bold opacity-[0.04] leading-none pointer-events-none select-none text-[var(--foreground)]`}>
                {watermark}
              </span>
            )}
            {label && (
              <h2 className="relative text-4xl md:text-6xl font-black tracking-tighter z-10 uppercase">
                {label}
              </h2>
            )}
         </div>
      ) : null}

      {/* Main content layer */}
      <div className="flex-1 flex flex-col items-center justify-center px-6 md:px-8 lg:px-12 min-h-0 w-full max-w-7xl mx-auto relative z-10 py-8">
        {children}
      </div>

      {/* Footer layer */}
      {footer && (
        <div className="shrink-0 px-6 md:px-8 lg:px-12 pb-8 md:pb-12 w-full max-w-7xl mx-auto">
           {footer}
        </div>
      )}
    </section>
  );
}
