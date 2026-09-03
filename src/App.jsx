  {
    title: "IT Specialist",
    company: "Krya Global",
    date: "Apr 2021-Present",
    isActive: true,
    desc: "Provided technical support to internal teams, managed a virtual admin system for parent/client communication, and supported EdTech systems implementation."
  },
  {
    title: "Coding Coach",
    company: "Krya Global",
    date: "Jul 2021-Present",
    isActive: true,
    desc: "Taught coding to children in online seminars, hackathons, and extracurricular classes at Dharma Mulya School and Xingzhong School. Developed curriculum and mentored students in the virtual environment."
  },
  {
    title: "Online Mentor",
    company: "Teman Belajar Krya",
    date: "Dec 2021-Present",
    isActive: true,
    desc: "Guided students in programming, 3D modeling, and game development. Built metaverse-based learning methods using Firestorm to boost engagement, and created scalable learning materials for online/hybrid environments."
  },
  {
    title: "Metaverse Coach",
    company: "Sekolah Bintang Mayantara",
    date: "Feb 2024-Present",
    isActive: true,
    desc: "Delivering interactive curriculum inside the Firestorm 3D metaverse platform."
  },
  {
    title: "Web Developer",
  }, []);

  return (
    <>
      <AnimatePresence>
        {!hasEntered && <IntroScreen key="intro" onEnter={() => setHasEntered(true)} />}
      </AnimatePresence>

      <div className="relative min-h-screen overflow-x-hidden" id="about">
        {/* Background Elements */}
      <div className="fixed inset-0 z-0 pointer-events-none">
        <div className="absolute inset-0 bg-grid opacity-50"></div>
        <div className="absolute top-0 -left-4 w-96 h-96 bg-indigo-600 rounded-full filter blur-[100px] opacity-20 animate-blob"></div>
        <div className="absolute top-0 -right-4 w-96 h-96 bg-blue-600 rounded-full filter blur-[100px] opacity-20 animate-blob animation-delay-2000"></div>
        <div className="absolute -bottom-8 left-20 w-96 h-96 bg-cyan-600 rounded-full filter blur-[100px] opacity-20 animate-blob animation-delay-4000"></div>
        <div className="absolute -bottom-8 right-20 w-96 h-96 bg-blue-400 rounded-full filter blur-[100px] opacity-10 animate-blob animation-delay-2000"></div>
      </div>

      <div className="relative z-10 w-full">
        {/* 1. Hero Card */}
        <StackedSection zIndex={10}>
        <BentoCard className="w-full h-full flex flex-col gap-8" delay={0.1}>
          <div className="flex flex-col-reverse md:flex-row gap-8 items-center w-full h-full">
            <div className="flex-1 w-full flex flex-col justify-center">
              <motion.h1 
                className="text-5xl md:text-6xl lg:text-8xl font-black tracking-tight mb-6 leading-[1.1] flex flex-wrap gap-x-4 text-white"
                initial="hidden"
                animate="visible"
                variants={{
                  visible: { transition: { staggerChildren: 0.1 } }
                }}
              >
                <motion.span 
                  variants={{ hidden: { opacity: 0, y: 20 }, visible: { opacity: 1, y: 0 } }} 
                  className="text-transparent" 
                  style={{ WebkitTextStroke: '2px rgba(255,255,255,0.9)' }}
                >
                  Educator
                </motion.span>
                <motion.span variants={{ hidden: { opacity: 0, y: 20 }, visible: { opacity: 1, y: 0 } }} className="text-cyan-400">&</motion.span>
                <motion.div variants={{ hidden: { opacity: 0, y: 20 }, visible: { opacity: 1, y: 0 } }} className="w-max min-w-full h-[1.3em] relative overflow-hidden pr-8">
                  <AnimatePresence>
                    <motion.span
                      key={roleIndex}
                      initial={{ y: 50, opacity: 0 }}
                      animate={{ y: 0, opacity: 1 }}
                      exit={{ y: -50, opacity: 0 }}
                      transition={{ type: "spring", stiffness: 300, damping: 20 }}
                      className="absolute inset-0 whitespace-nowrap bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-cyan-300 pb-2"
                  >
                    {roles[roleIndex]}
                  </motion.span>
                </AnimatePresence>
              </motion.div>
            </motion.h1>
            <p className="text-xl text-muted max-w-lg leading-relaxed">
              Guiding the next generation of tech talent, and engineering systems that make digital learning seamless.
            </p>
          </div>
          <div className="w-full md:w-1/3 aspect-square flex items-center justify-center relative">
            <OrbitalNav />
          </div>
        </div>
      </BentoCard>
        </StackedSection>

      {/* 2. Who Am I Card */}
      <StackedSection zIndex={20}>
        <BentoCard id="about" className="w-full h-full flex flex-col" delay={0.2}>
        <div className="flex flex-col md:flex-row h-full w-full items-center justify-center gap-8 md:gap-16">
          {/* 1. Large Prominent Portrait Photo */}
          <div className="w-56 sm:w-64 md:w-72 aspect-[3/4] rounded-3xl overflow-hidden border-4 border-[var(--background)] shadow-xl relative group shrink-0 md:mb-0">
            <div className="absolute inset-0 bg-brand/10 mix-blend-overlay group-hover:opacity-0 transition-opacity duration-300 z-10 pointer-events-none" />
            <img src="/ryan.jpg" alt="Gabriel Ryan Prima" className="w-full h-full object-cover object-top transform group-hover:scale-105 transition-transform duration-700" />
          </div>

          {/* 2. Name Header */}
          <div className="text-center mb-8">
            <h2 className="text-3xl font-black text-white tracking-tight">Gabriel Ryan Prima</h2>
          </div>

          {/* 3. Stat badges */}
          <div className="flex flex-wrap justify-center gap-3 mb-8">
            <div className="glass-badge bg-[var(--background)]/50">
              <span className="text-xl font-bold mr-1"><CountUp end={5} duration={3} enableScrollSpy scrollSpyOnce />+</span>
              <span className="text-xs uppercase tracking-wider opacity-80">Years</span>
            </div>
            <div className="glass-badge bg-[var(--background)]/50">
              <span className="text-xl font-bold mr-1"><CountUp end={500} duration={3} enableScrollSpy scrollSpyOnce />+</span>
              <span className="text-xs uppercase tracking-wider opacity-80">Sessions</span>
            </div>
            <div className="glass-badge bg-[var(--background)]/50">
              <span className="text-xl font-bold mr-1"><CountUp end={10} duration={3} enableScrollSpy scrollSpyOnce />+</span>
              <span className="text-xs uppercase tracking-wider opacity-80">Programs</span>
            </div>
          </div>

          {/* 4. About-me Paragraph */}
          <p className="text-muted leading-relaxed text-sm text-justify">
            I am an educator first, and a developer second. By stepping into the virtual classroom every day, I understand exactly where students struggle and where EdTech systems fail. I use my engineering background not just to teach code, but to build the tools that make teaching it better.
          </p>
        </div>
      </BentoCard>
        </StackedSection>

      {/* 3. Experience Card */}
      <StackedSection zIndex={30}>
        <BentoCard delay={0.3} className="w-full h-full flex flex-col">
        <div className="mb-6 flex items-center gap-2">
          <motion.div whileHover={{ scale: 1.2, rotate: 15 }} transition={{ type: "spring", stiffness: 260, damping: 20 }}>
            <Terminal className="w-5 h-5 text-brand cursor-pointer" />
          </motion.div>
          <h2 className="text-2xl font-bold">Experience</h2>
        </div>
          <div className="flex-1 relative overflow-hidden rounded-xl">
            {/* Fade overlays for smooth scrolling effect */}
            <div className="absolute top-0 left-0 right-0 h-10 bg-gradient-to-b from-[#09122c] to-transparent z-20 pointer-events-none" />
            <div className="absolute bottom-0 left-0 right-0 h-10 bg-gradient-to-t from-[#09122c] to-transparent z-20 pointer-events-none" />
            
            {/* Static Background Timeline Line */}
            <div className="absolute left-[23px] top-0 bottom-0 w-px bg-gradient-to-b from-brand/10 via-brand/50 to-brand/10 z-0" />

            <div className="absolute inset-0 pt-4">
              <div className="animate-slide-up pause-on-hover flex flex-col gap-4">
                {[...experienceJobs, ...experienceJobs].map((job, i) => (
                  <div key={i} className="relative pl-14 group">
                    {/* Timeline Dot */}
                    <div className={`absolute left-[17px] top-7 w-3 h-3 rounded-full ring-4 ring-[#09122c] transition-all duration-300 z-10 ${
                      job.isActive 
                        ? 'bg-brand shadow-[0_0_10px_rgba(59,130,246,0.6)] animate-pulse group-hover:scale-150 group-hover:bg-cyan-400 group-hover:shadow-[0_0_15px_rgba(34,211,238,0.8)]' 
                        : 'bg-slate-600 group-hover:bg-slate-400 group-hover:scale-125'
                    }`} />
                    
                    {/* Card Container */}
                    <div className={`border rounded-2xl p-5 transition-all duration-500 relative overflow-hidden ${
                      job.isActive
                        ? 'bg-white/[0.03] border-white/[0.08] hover:bg-white/[0.05] hover:border-brand/40'
                        : 'bg-white/[0.01] border-white/[0.03] hover:bg-white/[0.02] hover:border-slate-600/50'
                    }`}>
                      {/* Subtle Hover Gradient */}
                      <div className={`absolute inset-0 bg-gradient-to-r to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 ${
                        job.isActive ? 'from-brand/10' : 'from-slate-600/10'
                      }`} />
                      
                      <div className="relative z-10">
                        <div className="flex flex-col xl:flex-row xl:items-center xl:justify-between gap-2 mb-2">
                          <h3 className={`font-bold text-lg transition-colors ${
                            job.isActive ? 'text-white group-hover:text-cyan-300' : 'text-slate-300 group-hover:text-white'
                          }`}>{job.title}</h3>
                          <span className={`text-xs font-mono shrink-0 px-2.5 py-1 rounded-full border ${
                            job.isActive 
                              ? 'text-cyan-300 bg-blue-500/20 border-blue-500/30' 
                              : 'text-slate-400 bg-slate-800/50 border-slate-700/50'
                          }`}>{job.date}</span>
                        </div>
                        <div className="flex items-center gap-2 mb-3">
                          <span className={`w-1.5 h-1.5 rounded-full ${job.isActive ? 'bg-brand/60' : 'bg-slate-500'}`} />
                          <p className={`text-sm font-semibold tracking-wide uppercase ${job.isActive ? 'text-brand' : 'text-slate-400'}`}>{job.company}</p>
                        </div>
                        <p className={`text-sm leading-relaxed text-justify transition-colors ${
                          job.isActive ? 'text-slate-300 group-hover:text-white' : 'text-slate-400 group-hover:text-slate-300'
                        }`}>{job.desc}</p>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </BentoCard>
        </StackedSection>

      {/* Teaching Sessions Squeeze Carousel Card */}
      <StackedSection zIndex={40}>
        <BentoCard className="w-full h-full flex flex-col overflow-hidden" delay={0.35} noPadding>
        <div className="p-6 md:p-8 pb-0">
          <div className=" mb-2 flex items-center gap-2">
            <motion.div whileHover={{ scale: 1.2, rotate: 15 }} transition={{ type: "spring", stiffness: 260, damping: 20 }}>
              <Users className="w-5 h-5 text-brand cursor-pointer" />
            </motion.div>
            <h2 className="text-2xl font-bold">In The Classroom</h2>
          </div>
          <p className="text-muted mb-6 md:mb-8 pr-24 md:pr-0">Moments from mentoring, coaching, and virtual sessions.</p>
        </div>
        
        <div className="flex-1 min-h-0 w-full px-4 md:px-8 pb-6 md:pb-8">
          <SqueezeCarousel height="100%" slides={[
              {
                id: "coding",
                title: "Online Seminars",
                description: "Teaching coding fundamentals to eager students across the country.",
                image: "https://images.unsplash.com/photo-1571260899304-42507011bb6b?q=80&w=800",
                imageAlt: "Student looking at code",
              },
              {
                id: "mentorship",
                title: "1-on-1 Mentorship",
                description: "Guiding students through complex programming logic and game development.",
                image: "https://images.unsplash.com/photo-1531482615713-2afd69097998?q=80&w=800",
                imageAlt: "Team working on laptops",
              },
              {
                id: "metaverse",
                title: "Metaverse Classes",
                description: "Interactive virtual learning sessions built on top of the Firestorm engine.",
                image: "https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=800",
                imageAlt: "Collaborative learning",
              },
              {
                id: "curriculum",
                title: "Curriculum Design",
                description: "Developing scalable, hands-on learning materials for hybrid environments.",
                image: "https://images.unsplash.com/photo-1509062522246-3755977927d7?q=80&w=800",
                imageAlt: "Education tools",
              }
            ]}
            height={260}
            gap={16}
            slatGap={8}
            slatWidth={12}
            radius={16}
            duration={800}
            hoverGrow={true}
            autoplay={false}
            accent="var(--color-brand)"
            accentForeground="white"
            label="Classroom Moments"
            panelClassName="border border-brand/20 shadow-md"
          />
        </div>
      </BentoCard>
        </StackedSection>

      {/* 4. Projects Card */}
      <StackedSection zIndex={50}>
        <BentoCard id="projects" className="w-full h-full flex flex-col" delay={0.4}>
        <div className=" mb-8 flex items-center gap-2">
          <motion.div whileHover={{ scale: 1.2, rotate: 15 }} transition={{ type: "spring", stiffness: 260, damping: 20 }}>
            <Code className="w-5 h-5 text-brand cursor-pointer" />
          </motion.div>
          <h2 className="text-3xl font-bold">Selected Projects</h2>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {[
            {
              title: "Automated Mentor Reporting",
              hook: "Cut reporting from multi-hour manual process to auto-generated PDFs.",
              tags: ["Next.js", "Prisma", "Tailwind", "Puppeteer"]
            },
            {
              title: "Privacy-First PDF Toolkit",
              hook: "Client-side only OCR & tools for sensitive documents.",
              tags: ["React", "Vite", "WebAssembly"],
              url: "#"
            },
            {
              title: "Metaverse Curriculum",
              hook: "Full-year history curriculum replacing lectures with 3D interactive roleplay.",
              tags: ["Firestorm", "Instructional Design"],
              url: "#"
            }
          ].map((project, i) => (
            <motion.div 
              key={i}
              whileHover={{ y: -8 }}
              className="h-full"
            >
              <a href={project.url} target="_blank" rel="noopener noreferrer" className="group cursor-pointer flex flex-col bg-[var(--background)]/40 rounded-3xl border border-card-border overflow-hidden hover:border-cyan-400/40 transition-colors shadow-sm h-full">
                <div className="w-full aspect-[4/3] bg-slate-800/50 border-b border-card-border flex items-center justify-center relative overflow-hidden">
                  <div className="absolute inset-0 bg-brand/5 group-hover:bg-cyan-500/10 transition-colors duration-500 z-10" />
                  
                  {/* Mockup Window Effect */}
                  <div className="absolute top-8 left-8 right-8 bottom-0 bg-[var(--card)] rounded-t-xl border-t border-l border-r border-blue-400/20 shadow-2xl flex items-center justify-center transform origin-bottom group-hover:scale-105 transition-transform duration-500 overflow-hidden">
                    <div className="absolute top-0 left-0 right-0 h-6 bg-blue-900/30 border-b border-blue-400/10 flex items-center px-3 gap-1.5">
                      <div className="w-2 h-2 rounded-full bg-blue-400/30"></div>
                      <div className="w-2 h-2 rounded-full bg-blue-400/50"></div>
                      <div className="w-2 h-2 rounded-full bg-cyan-400/50"></div>
                    </div>
                    <p className="text-muted font-mono text-xs text-center px-4 text-blue-200">Screenshot:<br/>{project.title}</p>
                  </div>

                  <div className="absolute top-4 right-4 z-20 opacity-0 group-hover:opacity-100 transition-opacity bg-cyan-500 text-white p-2 rounded-full transform translate-x-2 -translate-y-2 group-hover:translate-x-0 group-hover:translate-y-0 duration-300 shadow-lg shadow-cyan-500/20">
                    <ArrowUpRight className="w-4 h-4" />
                  </div>
                </div>
                
                <div className="p-6 md:p-8 flex flex-col flex-1">
                  <h3 className="font-bold text-xl mb-3 group-hover:text-cyan-300 transition-colors text-white">{project.title}</h3>
                  <p className="text-sm text-muted mb-8 flex-1 leading-relaxed">{project.hook}</p>
                  <div className="flex flex-wrap gap-2 mt-auto">
                    {project.tags.map(tag => (
                      <span key={tag} className="text-xs px-3 py-1 bg-blue-500/20 text-cyan-300 rounded-md font-semibold tracking-wide">
                        {tag}
                      </span>
                    ))}
                  </div>
                </div>
              </a>
            </motion.div>
          ))}
        </div>
      </BentoCard>
        </StackedSection>

      {/* 5. Case Study Card */}
      <StackedSection zIndex={60}>
        <BentoCard className="w-full h-full flex flex-col" delay={0.5}>
        <div className=" mb-8 flex items-center gap-2">
          <motion.div whileHover={{ scale: 1.2, rotate: 15 }} transition={{ type: "spring", stiffness: 260, damping: 20 }}>
            <Star className="w-5 h-5 text-brand cursor-pointer fill-brand/20" />
          </motion.div>
          <h2 className="text-3xl font-bold">Case Study: Mentor Reporting System</h2>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div className="flex flex-col gap-4 h-full">
            <h3 className="text-xl font-bold text-brand flex items-center gap-2"><span className="w-6 h-6 rounded-full bg-brand/20 flex items-center justify-center text-sm">1</span> Problem</h3>
            <p className="text-muted text-sm leading-relaxed">
              Generating monthly reports was a manual, multi-hour nightmare for the entire EdTech mentoring org. Mentors struggled with formatting, tracking sessions, and bilingual requirements.
            </p>
            <div className="w-full aspect-video bg-slate-200 dark:bg-slate-800 rounded-xl border border-card-border flex items-center justify-center relative mt-auto">
               <p className="text-muted font-mono text-xs">Screenshot: Old Process</p>
            </div>
          </div>
          
          <div className="flex flex-col gap-4 h-full">
            <h3 className="text-xl font-bold text-brand flex items-center gap-2"><span className="w-6 h-6 rounded-full bg-brand/20 flex items-center justify-center text-sm">2</span> Process</h3>
            <p className="text-muted text-sm leading-relaxed">
              Built an internal platform to track mentor lifecycles and session recaps. Used Puppeteer to automatically generate perfectly formatted bilingual PDFs from the database.
            </p>
            <div className="w-full aspect-video bg-slate-200 dark:bg-slate-800 rounded-xl border border-card-border flex items-center justify-center relative mt-auto">
               <p className="text-muted font-mono text-xs">Screenshot: Dashboard UI</p>
            </div>
          </div>

          <div className="flex flex-col gap-4 h-full">
            <h3 className="text-xl font-bold text-brand flex items-center gap-2"><span className="w-6 h-6 rounded-full bg-brand/20 flex items-center justify-center text-sm">3</span> Impact</h3>
            <p className="text-muted text-sm leading-relaxed">
              Reduced reporting time from hours to minutes. Standardized the output quality across the organization and eliminated formatting errors entirely.
            </p>
            <div className="w-full aspect-video bg-slate-200 dark:bg-slate-800 rounded-xl border border-card-border flex items-center justify-center relative mt-auto">
               <p className="text-muted font-mono text-xs">Screenshot: Generated PDF</p>
            </div>
          </div>
        </div>
      </BentoCard>
        </StackedSection>

      {/* Testimonials Card */}
      <StackedSection zIndex={70}>
        <BentoCard className="w-full h-full flex flex-col" delay={0.55}>
        <div className=" mb-6 flex items-center gap-2">
          <motion.div whileHover={{ scale: 1.2, rotate: 15 }} transition={{ type: "spring", stiffness: 260, damping: 20 }}>
            <MessageSquareQuote className="w-5 h-5 text-brand cursor-pointer" />
          </motion.div>
          <h2 className="text-3xl font-bold">Testimonials</h2>
        </div>
        
        <Testimonials />
      </BentoCard>
        </StackedSection>

      {/* 6. Contact Card */}
      <StackedSection zIndex={80}>
        <BentoCard id="contact" className="w-full h-full flex flex-col" innerClassName="bg-brand text-white border-none" delay={0.6} noPadding>
        <div className="p-10 md:p-16 flex flex-col items-center text-center">
          <h2 className="text-4xl md:text-5xl font-bold mb-4 text-white">Let's build together.</h2>
          <p className="text-white/80 max-w-xl mx-auto mb-10 text-lg">
            Whether you need an educator to shape a curriculum, or a developer to engineer an EdTech solution—I'm open for new opportunities.
          </p>
          <div className="flex gap-4 mt-4">
            <Magnetic>
              <a href="mailto:hello@example.com" className="bg-white text-blue-700 px-8 py-4 rounded-full font-bold hover:shadow-lg hover:bg-cyan-400 hover:text-white hover:scale-105 transition-all flex items-center gap-2">
                <Mail className="w-5 h-5" /> Get In Touch
              </a>
            </Magnetic>
            <a href="https://github.com" className="bg-blue-900/50 text-white p-4 rounded-full hover:bg-cyan-500 hover:text-white transition-colors flex items-center justify-center">
              <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0112 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/></svg>
            </a>
            <a href="https://linkedin.com" className="bg-blue-900/50 text-white p-4 rounded-full hover:bg-cyan-500 hover:text-white transition-colors flex items-center justify-center">
              <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
            </a>
          </div>
        </div>
      </BentoCard>
        </StackedSection>
      
      {/* Footer */}
      <footer className="col-span-1 md:col-span-2 mt-8 flex flex-col sm:flex-row justify-between items-center text-sm text-muted opacity-60 hover:opacity-100 transition-opacity">
        <p>© {new Date().getFullYear()} Gabriel Ryan Prima. All rights reserved.</p>
        <button 
          onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
          className="mt-4 sm:mt-0 hover:text-cyan-400 transition-colors flex items-center gap-1 group"
        >
          Back to top <ArrowUp className="w-4 h-4 group-hover:-translate-y-1 transition-transform" />
        </button>
      </footer>

      </div>
      </div>
    </>
  );
}

export default App;
