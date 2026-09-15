
import { createRoot } from 'react-dom/client'
import './index.css'
import 'lenis/dist/lenis.css'
import App from './App.jsx'
import { Analytics } from '@vercel/analytics/react'
import { ReactLenis } from 'lenis/react'

createRoot(document.getElementById('root')).render(
  <ReactLenis root options={{ lerp: 0.05, duration: 1.5, smoothWheel: true, syncTouch: true, touchMultiplier: 2 }}>
    <App />
    <Analytics />
  </ReactLenis>
)
