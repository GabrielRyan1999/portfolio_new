import React from 'react'
import { Card, CardContent, CardHeader } from './card'
import { AlertTriangle, Cog, TrendingUp } from 'lucide-react'

const caseStudySteps = [
  {
    number: 1,
    title: "Problem",
    icon: <AlertTriangle className="w-6 h-6" aria-hidden />,
    description:
      "The previous process of logging study sessions and creating monthly reports was done manually, making it highly time-consuming and prone to human error. Scattered mentoring data made it difficult for management to comprehensively monitor student progress and mentor performance. Additionally, the manual delivery of reports to parents hindered the institution from maintaining a maximum standard of professionalism.",
    image: "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=800",
  },
  {
    number: 2,
    title: "Process",
    icon: <Cog className="w-6 h-6" aria-hidden />,
    description:
      "Built a full-stack LMS web application using Next.js and MySQL to centralize all mentor, student, and session data into a single unified dashboard. Engineered an automation pipeline that instantly compiles daily mentor logs and formats them into beautifully designed PDF documents. Integrated an SMTP service, allowing administrators to email customized PDF reports directly to parents with just a single click.",
    image: "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=800",
  },
  {
    number: 3,
    title: "Impact",
    icon: <TrendingUp className="w-6 h-6" aria-hidden />,
    description:
      "This automation slashed the administrative workload of generating monthly reports from hours to mere seconds per student. The consistent, fast, and neat delivery of customized emails and reports drastically elevated the institution's professional image and credibility among parents. Furthermore, the mobile-optimized interface empowered mentors to log data on-the-go directly from their phones, making business operations highly efficient and ready to scale.",
    image: "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800",
  },
];

const CardDecorator = ({ image, icon }) => (
    <div className="relative mx-auto w-full h-[240px] md:h-[320px] lg:h-[360px] shrink-0 rounded-2xl overflow-hidden mb-6 group-hover:scale-[1.02] transition-transform duration-500">
        <img src={image} alt="" loading="lazy" className="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity" />
        <div className="absolute inset-0 bg-slate-900/10 mix-blend-multiply" />
        <div className="absolute inset-0 bg-[linear-gradient(to_right,rgba(255,255,255,0.2)_1px,transparent_1px),linear-gradient(to_bottom,rgba(255,255,255,0.2)_1px,transparent_1px)] bg-[size:24px_24px] opacity-30"/>
        
        {/* Floating icon */}
        <div className="absolute bottom-4 left-4 bg-white dark:bg-zinc-900/90 backdrop-blur text-slate-900 dark:text-zinc-100 p-3 rounded-xl shadow-lg">
           {icon}
        </div>
    </div>
)

export function MentorReportingFeatures() {
    return (
        <div className="w-full max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-6 items-stretch text-center md:text-left z-10">
            {caseStudySteps.map((step) => (
                <Card key={step.title} className="group border border-slate-100 bg-white dark:bg-zinc-900/50 hover:bg-slate-50 dark:hover:bg-zinc-800/50 transition-colors shadow-xl shadow-slate-200/50 h-full flex flex-col overflow-hidden rounded-[2rem]">
                    <CardHeader className="pb-5 md:pb-6 shrink-0 flex flex-col">
                        <CardDecorator image={step.image} icon={step.icon} />
                        <div className="flex items-center gap-3 justify-start shrink-0">
                            <span className="w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-zinc-400 text-xs font-bold flex items-center justify-center shrink-0">
                                {step.number}
                            </span>
                            <h3 className="text-xl font-bold text-slate-900 dark:text-zinc-100">{step.title}</h3>
                        </div>
                    </CardHeader>
                    <CardContent className="flex-1">
                        <p className="text-sm text-slate-600 dark:text-zinc-300 leading-relaxed text-center md:text-left">
                            {step.description}
                        </p>
                    </CardContent>
                </Card>
            ))}
        </div>
    )
}
