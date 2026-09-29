import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

experience_regex = r'export function Experience\(\) \{[\s\S]*?(?=export function Contact\(\) \{)'

new_experience = '''export function Experience() {
    return (
      <PageTransition>
        <section id="experience" className="relative w-full min-h-[100svh] bg-[#1A365D] py-24 md:py-32 flex flex-col border-t-2 border-[#F5F2EB] overflow-hidden text-[#F5F2EB]">
          
          {/* Header */}
          <div className="w-full max-w-7xl mx-auto px-6 mb-16 md:mb-24 flex flex-col md:flex-row md:items-end justify-between gap-8 z-10">
             <div>
                <span className="text-xs font-bold tracking-widest uppercase text-[#F5F2EB]/50 font-mono mb-4 block">Chapter 04</span>
                <h2 className="font-serif text-5xl md:text-7xl lg:text-8xl font-black tracking-tighter leading-[0.85]">PROFESSIONAL<br/>RECORD</h2>
             </div>
             <div className="max-w-md text-[#F5F2EB]/80 font-serif text-lg leading-relaxed border-l-2 border-[#F5F2EB] pl-6 flex flex-col gap-4">
                <p>A chronological ledger of roles and responsibilities.</p>
                <div className="flex items-center gap-3">
                   <span className="w-2 h-2 bg-rose-500 rounded-none animate-pulse"></span>
                   <span className="text-xs font-mono tracking-widest uppercase opacity-70">Indicates Current Role</span>
                </div>
             </div>
          </div>

          {/* Brutalist Ledger Table */}
          <div className="w-full flex flex-col z-10 border-b-2 border-[#F5F2EB]">
            {experienceJobs.map((job, i) => (
              <div key={i} className="flex flex-col md:flex-row border-t-2 border-[#F5F2EB] group hover:bg-[#F5F2EB] hover:text-[#1A365D] transition-colors duration-300">
                 
                 {/* Year Cell */}
                 <div className="w-full md:w-1/4 py-6 md:py-10 px-6 border-b-2 md:border-b-0 md:border-r-2 border-[#F5F2EB] group-hover:border-[#1A365D] transition-colors flex items-center justify-between md:justify-start">
                     <span className="font-mono text-sm md:text-base tracking-widest font-bold opacity-70 group-hover:opacity-100">{job.date}</span>
                     {job.isActive && <span className="w-2 h-2 bg-rose-500 rounded-none animate-pulse md:ml-6"></span>}
                 </div>
                 
                 {/* Company & Title Cell */}
                 <div className="w-full md:w-1/2 py-6 md:py-10 px-6 border-b-2 md:border-b-0 md:border-r-2 border-[#F5F2EB] group-hover:border-[#1A365D] transition-colors flex flex-col justify-center">
                     <h3 className="font-serif text-3xl md:text-5xl lg:text-6xl font-black tracking-tighter mb-2">{job.company}</h3>
                     <p className="font-sans text-xs md:text-sm font-bold tracking-widest uppercase opacity-70 group-hover:opacity-100">{job.title}</p>
                 </div>
                 
                 {/* Description Cell */}
                 <div className="w-full md:w-1/4 py-6 md:py-10 px-6 flex items-center">
                     <p className="font-serif text-base md:text-lg leading-relaxed opacity-80 group-hover:opacity-100">
                        {job.desc}
                     </p>
                 </div>
              </div>
            ))}
          </div>

        </section>

        {/* Testimonials Wrapper */}
        <section className="relative w-full bg-[#F5F2EB] py-32 border-t-2 border-[#1A365D] overflow-hidden">
           <div className="w-full max-w-7xl mx-auto px-6 mb-16">
              <span className="text-xs font-bold tracking-widest uppercase text-[#1A365D]/50 font-mono mb-4 block text-center">Chapter 05 // Endorsements</span>
           </div>
           <Testimonials />
        </section>

      </PageTransition>
    );
}
'''

content = re.sub(experience_regex, new_experience, content, flags=re.DOTALL)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Redesigned Experience section.')
