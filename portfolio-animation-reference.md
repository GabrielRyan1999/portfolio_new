# Animation Reference — Portfolio Revamp

Kasih file ini utuh ke Antigravity sebagai context tambahan. Root cause animasi ga smooth biasanya:

1. Coba animate `height: auto` pakai CSS transition biasa. Ini gak jalan smooth secara native, browser gak bisa interpolate ke `auto`.
2. Transition di-apply ke property yang bikin layout reflow (height, top, margin) alih-alih `transform` dan `opacity` (yang GPU-accelerated).
3. Easing default linear/ease, bukan custom easing yang bikin gerakan terasa natural.
4. Gak ada `AnimatePresence` buat handle exit animation pas accordion nutup, jadi konten hilang mendadak.

Solusinya: pakai Framer Motion (`npm i motion`), bukan CSS transition manual, untuk semua interactive animation di bawah.

---

## 1. Service Accordion (paling sering bikin bingung)

```tsx
"use client";
import { useState } from "react";
import { motion, AnimatePresence } from "motion/react";

const services = [
  {
    title: "UIUX DESIGN",
    desc: "Designing clear and scalable interfaces for dashboards, mobile apps, and websites.",
    images: ["/mock1.png", "/mock2.png", "/mock3.png"],
  },
  { title: "WEB DESIGN & DEV", desc: "...", images: [] },
  { title: "BRANDING", desc: "...", images: [] },
];

export default function ServiceAccordion() {
  const [activeIndex, setActiveIndex] = useState<number | null>(0);

  return (
    <div className="divide-y divide-gray-200">
      {services.map((service, index) => {
        const isOpen = activeIndex === index;
        return (
          <motion.div key={service.title} layout className="overflow-hidden">
            <motion.button
              layout
              onClick={() => setActiveIndex(isOpen ? null : index)}
              className={`w-full flex items-center justify-between p-8 rounded-3xl transition-colors duration-300 ${
                isOpen ? "bg-black text-white" : "bg-transparent text-black"
              }`}
            >
              <motion.span layout="position" className="text-4xl font-bold">
                {service.title}
              </motion.span>
              <motion.span
                animate={{ rotate: isOpen ? 135 : 0 }}
                transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
              >
                {/* icon arrow-up-right, rotate 135deg jadi keliatan kayak X */}
                <ArrowIcon />
              </motion.span>
            </motion.button>

            <AnimatePresence initial={false}>
              {isOpen && (
                <motion.div
                  key="content"
                  initial={{ height: 0, opacity: 0 }}
                  animate={{ height: "auto", opacity: 1 }}
                  exit={{ height: 0, opacity: 0 }}
                  transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
                  className="bg-black rounded-b-3xl px-8"
                >
                  <div className="pb-8 flex items-center justify-between">
                    <p className="text-gray-300 max-w-md">{service.desc}</p>
                    <div className="flex -space-x-8">
                      {service.images.map((src, i) => (
                        <motion.img
                          key={src}
                          src={src}
                          initial={{ opacity: 0, y: 10 }}
                          animate={{
                            opacity: 1,
                            y: 0,
                            rotate: (i - 1) * 8, // -8deg, 0deg, 8deg
                          }}
                          transition={{ delay: 0.15 + i * 0.08, duration: 0.4 }}
                          className="w-24 rounded-xl shadow-lg"
                        />
                      ))}
                    </div>
                  </div>
                </motion.div>
              )}
            </AnimatePresence>
          </motion.div>
        );
      })}
    </div>
  );
}
```

**Poin kritis biar smooth:**
- `layout` prop di parent `motion.div` dan `motion.button` itu wajib. Ini yang bikin Framer Motion otomatis hitung perubahan posisi/ukuran dan animate-in dengan smooth, tanpa kamu manual hitung height.
- `AnimatePresence` wajib bungkus konten yang conditional render, kalau enggak, pas ditutup dia hilang instan tanpa exit animation.
- `height: "auto"` DI DALAM Framer Motion (bukan CSS) itu jalan, karena Framer Motion measure elemen dulu baru interpolate. Ini beda sama CSS transition biasa.
- Easing `[0.16, 1, 0.3, 1]` itu custom cubic-bezier ("ease-out-expo"), lebih natural dari `ease-out` bawaan. Dipakai konsisten di semua animasi biar berasa satu design system.
- Cuma satu `activeIndex` di state, bukan array of booleans, biar behavior-nya accordion (nutup yang lain otomatis).

---

## 2. Hero Entrance (stagger on load)

```tsx
const container = {
  hidden: {},
  show: {
    transition: { staggerChildren: 0.12, delayChildren: 0.1 },
  },
};

const item = {
  hidden: { opacity: 0, y: 20 },
  show: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.6, ease: [0.16, 1, 0.3, 1] },
  },
};

<motion.div variants={container} initial="hidden" animate="show">
  <motion.div variants={item}>{/* navbar pill */}</motion.div>
  <motion.h1 variants={item}>{/* nama */}</motion.h1>
  <motion.div variants={item}>{/* foto */}</motion.div>
  <motion.div variants={item}>{/* role + desc + CTA */}</motion.div>
  <motion.div variants={item}>{/* social pills */}</motion.div>
</motion.div>
```

`staggerChildren` di parent otomatis kasih delay berurutan ke semua `variants={item}` di dalamnya. Ini jauh lebih gampang daripada manual kasih `delay` satu-satu, dan Antigravity sering salah pas disuruh manual.

---

## 3. Scroll Reveal (Work / Service / Experience watermark)

```tsx
<motion.div
  initial={{ opacity: 0, y: 30 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true, amount: 0.3 }}
  transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
>
  {/* section content */}
</motion.div>

{/* watermark text, delay dikit dan opacity target rendah */}
<motion.span
  initial={{ opacity: 0 }}
  whileInView={{ opacity: 0.05 }}
  viewport={{ once: true }}
  transition={{ duration: 1, delay: 0.2 }}
  className="absolute text-[10rem] font-bold text-black pointer-events-none select-none"
>
  SERVICE
</motion.span>
```

`viewport={{ once: true }}` penting, biar animasi cuma jalan sekali pas pertama masuk layar, gak re-trigger tiap scroll naik-turun (ini salah satu penyebab kesan "gak smooth", karena animasi keulang-ulang random).

---

## 4. Work Card Hover

```tsx
<motion.div
  whileHover={{ y: -4 }}
  transition={{ duration: 0.3, ease: [0.16, 1, 0.3, 1] }}
  className="rounded-3xl overflow-hidden shadow-md hover:shadow-xl"
>
  <div className="overflow-hidden">
    <motion.img
      src={thumbnail}
      whileHover={{ scale: 1.05 }}
      transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
    />
  </div>
  {/* title, tags */}
</motion.div>
```

Zoom gambar harus di child `motion.img`, bukan di parent card, dan parent-nya wajib `overflow-hidden`. Kalau scale di-apply ke card langsung, seluruh card ikut membesar (termasuk teks di bawahnya), itu juga penyebab umum kesan "kasar".

---

## Cara pakai ke Antigravity

Paste seluruh isi file ini ke prompt, bilang:

> "Ini reference code animasi yang harus kamu ikuti persis (library, struktur komponen, easing value, dan teknik height animation-nya). Jangan pakai CSS transition manual untuk accordion, harus pakai Framer Motion `layout` + `AnimatePresence` seperti contoh."

Kasih instruksi eksplisit "ikuti persis" itu penting, karena kalau cuma dikasih deskripsi behavior, AI coding agent cenderung improvisasi pakai teknik yang dia familiar (biasanya CSS transition biasa yang gak smooth buat height).
