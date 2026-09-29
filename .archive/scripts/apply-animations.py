import re

with open('src/pages/Pages.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Inject ParallaxImage component
injection_point = r'const fadeUp = \{'
parallax_component = '''export function ParallaxImage({ src, alt, className = "" }) {
  const ref = React.useRef(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start end", "end start"]
  });
  const y = useTransform(scrollYProgress, [0, 1], ["-15%", "15%"]);

  return (
    <div ref={ref} className="relative w-full h-full overflow-hidden">
      <motion.img 
        style={{ y, scale: 1.25 }}
        src={src} 
        alt={alt}
        className={`absolute inset-0 w-full h-full object-cover ${className}`}
      />
    </div>
  );
}

const fadeUp = {'''
content = re.sub(injection_point, parallax_component, content)

# 2. Apply RevealLine to Services
old_service_heading = r'<h2 className="font-serif text-5xl md:text-7xl lg:text-8xl font-black text-\[#1A365D\] tracking-tighter leading-\[0\.85\]">SERVICES<br\/>& EXPERTISE<\/h2>'
new_service_heading = '''<h2 className="font-serif text-5xl md:text-7xl lg:text-8xl font-black text-[#1A365D] tracking-tighter leading-[0.85] flex flex-col">
  <RevealLine>SERVICES</RevealLine>
  <RevealLine delay={0.1}>& EXPERTISE</RevealLine>
</h2>'''
content = re.sub(old_service_heading, new_service_heading, content)

# 3. Apply RevealLine to Experience
old_exp_heading = r'<h2 className="font-serif text-5xl md:text-7xl lg:text-8xl font-black tracking-tighter leading-\[0\.85\]">PROFESSIONAL<br\/>RECORD<\/h2>'
new_exp_heading = '''<h2 className="font-serif text-5xl md:text-7xl lg:text-8xl font-black tracking-tighter leading-[0.85] flex flex-col">
  <RevealLine>PROFESSIONAL</RevealLine>
  <RevealLine delay={0.1}>RECORD</RevealLine>
</h2>'''
content = re.sub(old_exp_heading, new_exp_heading, content)

# 4. Apply Parallax to Work section
old_work_img = r'<img\s+src=\{workProjects\[workIndex\]\.img\}\s+alt=\{workProjects\[workIndex\]\.title\}\s+className="w-full h-full object-cover object-center grayscale contrast-125 mix-blend-luminosity opacity-80 group-hover:grayscale-0 group-hover:mix-blend-normal group-hover:opacity-100 transition-all duration-700"\s+\/>'
new_work_img = '''<ParallaxImage 
  src={workProjects[workIndex].img} 
  alt={workProjects[workIndex].title}
  className="grayscale contrast-125 mix-blend-luminosity opacity-80 group-hover:grayscale-0 group-hover:mix-blend-normal group-hover:opacity-100 transition-all duration-700" 
/>'''
content = re.sub(old_work_img, new_work_img, content)

with open('src/pages/Pages.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Applied animations to headings and images.')
