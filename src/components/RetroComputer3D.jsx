import React, { useEffect, useRef, useState, useCallback } from 'react';
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';

export default function RetroComputer3D({ 
  projects = [], 
  selectedIndex = 0, 
  onSelectProject,
  onPrev,
  onNext 
}) {
  const mountRef = useRef(null);
  const sceneRef = useRef(null);
  const rendererRef = useRef(null);
  const controlsRef = useRef(null);
  const cameraRef = useRef(null);
  const screenMeshRef = useRef(null);
  const textureRef = useRef(null);
  const canvasRef = useRef(null);
  const isAutoRotatingRef = useRef(false);
  const loadedImagesRef = useRef({});

  // Keep latest callbacks & props in ref for event handlers without stale closures
  const stateRef = useRef({
    projects,
    selectedIndex,
    onSelectProject,
    onPrev,
    onNext
  });

  useEffect(() => {
    stateRef.current = {
      projects,
      selectedIndex,
      onSelectProject,
      onPrev,
      onNext
    };
  }, [projects, selectedIndex, onSelectProject, onPrev, onNext]);

  const [isAutoSpin, setIsAutoSpin] = useState(false);
  const [hintVisible, setHintVisible] = useState(true);

  // Helper function to draw the retro broadsheet LCD screen onto a 2D canvas texture
  const drawScreen = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    const W = canvas.width;
    const H = canvas.height;
    const curr = projects[selectedIndex] || {
      title: 'SELECTED PROJECT',
      tag: 'SYSTEM',
      desc: 'No description available.',
      tech: ['REACT'],
      url: '#'
    };

    // 1. Clean Deep Navy LCD Canvas
    ctx.fillStyle = '#081424';
    ctx.fillRect(0, 0, W, H);

    // Subtle ambient lighting gradient across screen
    const radGlow = ctx.createRadialGradient(W / 2, H / 2, 40, W / 2, H / 2, W / 1.05);
    radGlow.addColorStop(0, 'rgba(20, 48, 82, 0.5)');
    radGlow.addColorStop(1, 'rgba(5, 12, 22, 0.98)');
    ctx.fillStyle = radGlow;
    ctx.fillRect(0, 0, W, H);

    // 2. Top Masthead & Tab Navigation Strip
    ctx.fillStyle = '#040B14';
    ctx.fillRect(0, 0, W, 72);

    ctx.strokeStyle = 'rgba(235, 229, 216, 0.35)';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(0, 72);
    ctx.lineTo(W, 72);
    ctx.stroke();

    // Tabs
    const tabW = 246;
    const tabH = 48;
    const startX = 24;
    const tabY = 24;

    projects.forEach((p, idx) => {
      const isCurrent = idx === selectedIndex;
      const x = startX + idx * (tabW + 12);

      if (isCurrent) {
        ctx.fillStyle = '#EBE5D8';
        ctx.fillRect(x, tabY, tabW, tabH);
        ctx.strokeStyle = '#EBE5D8';
        ctx.lineWidth = 2;
        ctx.strokeRect(x, tabY, tabW, tabH);

        ctx.fillStyle = '#153966';
        ctx.font = 'bold 15px "Courier New", monospace';
        ctx.fillText(`0${idx + 1}. ${p.title.toUpperCase().slice(0, 16)}`, x + 14, tabY + 29);
      } else {
        ctx.fillStyle = '#0B1B30';
        ctx.fillRect(x, tabY, tabW, tabH);
        ctx.strokeStyle = 'rgba(235, 229, 216, 0.3)';
        ctx.lineWidth = 1;
        ctx.strokeRect(x, tabY, tabW, tabH);

        ctx.fillStyle = 'rgba(235, 229, 216, 0.75)';
        ctx.font = '14px "Courier New", monospace';
        ctx.fillText(`0${idx + 1}. ${p.title.toUpperCase().slice(0, 16)}`, x + 14, tabY + 29);
      }
    });

    // Right Status on Header
    ctx.fillStyle = '#22C55E';
    ctx.beginPath();
    ctx.arc(W - 160, 48, 5.5, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = 'rgba(235, 229, 216, 0.85)';
    ctx.font = 'bold 13px "Courier New", monospace';
    ctx.fillText('LCD DISPLAY // 3D', W - 146, 52);

    // 3. Left Section: Visual Preview / Slideshow Frame
    const previewX = 36;
    const previewY = 102;
    const previewW = 460;
    const previewH = 416;

    // Image background box
    ctx.fillStyle = '#0B1728';
    ctx.fillRect(previewX, previewY, previewW, previewH);
    ctx.strokeStyle = '#EBE5D8';
    ctx.lineWidth = 2;
    ctx.strokeRect(previewX, previewY, previewW, previewH);

    // Subtle technical grid
    ctx.strokeStyle = 'rgba(235, 229, 216, 0.08)';
    ctx.lineWidth = 1;
    for (let gx = previewX + 40; gx < previewX + previewW; gx += 40) {
      ctx.beginPath(); ctx.moveTo(gx, previewY); ctx.lineTo(gx, previewY + previewH); ctx.stroke();
    }
    for (let gy = previewY + 40; gy < previewY + previewH; gy += 40) {
      ctx.beginPath(); ctx.moveTo(previewX, gy); ctx.lineTo(previewX + previewW, gy); ctx.stroke();
    }

    // Registration crosshairs on preview corners
    const drawCross = (cx, cy) => {
      ctx.strokeStyle = 'rgba(235, 229, 216, 0.6)';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(cx - 6, cy); ctx.lineTo(cx + 6, cy);
      ctx.moveTo(cx, cy - 6); ctx.lineTo(cx, cy + 6);
      ctx.stroke();
    };
    drawCross(previewX + 14, previewY + 14);
    drawCross(previewX + previewW - 14, previewY + 14);
    drawCross(previewX + 14, previewY + previewH - 14);
    drawCross(previewX + previewW - 14, previewY + previewH - 14);

    // Draw project image if loaded
    const loadedImg = loadedImagesRef.current[curr.img];
    let imageDrawn = false;
    if (loadedImg && loadedImg.complete && loadedImg.naturalWidth !== 0) {
      try {
        const padding = 24;
        ctx.drawImage(
          loadedImg, 
          previewX + padding, 
          previewY + padding, 
          previewW - padding * 2, 
          previewH - padding * 2
        );
        imageDrawn = true;
      } catch {
        imageDrawn = false;
      }
    }

    if (!imageDrawn) {
      // Technical schematic fallback illustration
      ctx.fillStyle = 'rgba(235, 229, 216, 0.1)';
      ctx.fillRect(previewX + 30, previewY + 70, previewW - 60, previewH - 140);
      ctx.strokeStyle = 'rgba(235, 229, 216, 0.3)';
      ctx.strokeRect(previewX + 30, previewY + 70, previewW - 60, previewH - 140);

      ctx.fillStyle = '#EBE5D8';
      ctx.font = 'bold 24px "Georgia", serif';
      ctx.textAlign = 'center';
      ctx.fillText(curr.title.toUpperCase(), previewX + previewW / 2, previewY + previewH / 2 - 10);

      ctx.fillStyle = 'rgba(235, 229, 216, 0.7)';
      ctx.font = '13px "Courier New", monospace';
      ctx.fillText(`// PROJECT 0${selectedIndex + 1} ARCHIVE //`, previewX + previewW / 2, previewY + previewH / 2 + 20);
      ctx.textAlign = 'left';
    }

    // Slideshow control bar below preview (from Aline's sketch: 'SLIDESHOW')
    const slideBarY = previewY + previewH + 16;
    const slideBarH = 46;
    ctx.fillStyle = '#050D18';
    ctx.fillRect(previewX, slideBarY, previewW, slideBarH);
    ctx.strokeStyle = 'rgba(235, 229, 216, 0.4)';
    ctx.strokeRect(previewX, slideBarY, previewW, slideBarH);

    // Left button
    ctx.fillStyle = 'rgba(235, 229, 216, 0.15)';
    ctx.fillRect(previewX + 8, slideBarY + 8, 80, slideBarH - 16);
    ctx.fillStyle = '#EBE5D8';
    ctx.font = 'bold 12px "Courier New", monospace';
    ctx.textAlign = 'center';
    ctx.fillText('PREV', previewX + 48, slideBarY + 28);
    ctx.textAlign = 'left';

    // Center text
    ctx.fillStyle = 'rgba(235, 229, 216, 0.85)';
    ctx.font = 'bold 12px "Courier New", monospace';
    ctx.textAlign = 'center';
    ctx.fillText(`SLIDESHOW // 0${selectedIndex + 1} OF 0${projects.length}`, previewX + previewW / 2, slideBarY + 28);
    ctx.textAlign = 'left';

    // Right button
    ctx.fillStyle = 'rgba(235, 229, 216, 0.15)';
    ctx.fillRect(previewX + previewW - 88, slideBarY + 8, 80, slideBarH - 16);
    ctx.fillStyle = '#EBE5D8';
    ctx.font = 'bold 12px "Courier New", monospace';
    ctx.textAlign = 'center';
    ctx.fillText('NEXT', previewX + previewW - 48, slideBarY + 28);
    ctx.textAlign = 'left';

    // 4. Right Section: Project Metadata & Dossier
    const infoX = 525;
    const infoY = 102;
    const infoW = 465;

    // Classification tag
    ctx.fillStyle = '#EBE5D8';
    ctx.font = 'bold 13px "Courier New", monospace';
    ctx.fillText(`INDEX: PROJECT 0${selectedIndex + 1}  //  TAG: ${curr.tag?.toUpperCase() || 'SYSTEM'}`, infoX, infoY + 20);

    ctx.strokeStyle = 'rgba(235, 229, 216, 0.35)';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(infoX, infoY + 34);
    ctx.lineTo(infoX + infoW, infoY + 34);
    ctx.stroke();

    // Large Title
    ctx.fillStyle = '#FFFFFF';
    ctx.font = 'bold 32px "Georgia", serif';
    const words = curr.title.split(' ');
    if (words.length > 2) {
      ctx.fillText(words.slice(0, 2).join(' ').toUpperCase(), infoX, infoY + 76);
      ctx.fillText(words.slice(2).join(' ').toUpperCase(), infoX, infoY + 116);
    } else {
      ctx.fillText(curr.title.toUpperCase(), infoX, infoY + 80);
    }

    // Description (Wrap lines)
    ctx.fillStyle = '#EBE5D8';
    ctx.font = '17px "Arial", sans-serif';
    const descText = curr.desc || '';
    const descWords = descText.split(' ');
    let line = '';
    let lineY = infoY + 160;
    for (let n = 0; n < descWords.length; n++) {
      const testLine = line + descWords[n] + ' ';
      const metrics = ctx.measureText(testLine);
      if (metrics.width > infoW - 10 && n > 0) {
        ctx.fillText(line, infoX, lineY);
        line = descWords[n] + ' ';
        lineY += 28;
      } else {
        line = testLine;
      }
    }
    ctx.fillText(line, infoX, lineY);

    // Tech Stack Chips
    const techY = lineY + 38;
    ctx.fillStyle = 'rgba(235, 229, 216, 0.7)';
    ctx.font = 'bold 13px "Courier New", monospace';
    ctx.fillText('ENGINEERING SPECIFICATIONS //', infoX, techY);

    let chipX = infoX;
    let chipY = techY + 14;
    (curr.tech || []).forEach((t) => {
      const chipPad = 12;
      ctx.font = 'bold 13px "Courier New", monospace';
      const chipTextW = ctx.measureText(t.toUpperCase()).width;
      const chipTotalW = chipTextW + chipPad * 2;

      if (chipX + chipTotalW > infoX + infoW) {
        chipX = infoX;
        chipY += 34;
      }

      ctx.fillStyle = 'rgba(235, 229, 216, 0.15)';
      ctx.fillRect(chipX, chipY, chipTotalW, 26);
      ctx.strokeStyle = '#EBE5D8';
      ctx.lineWidth = 1;
      ctx.strokeRect(chipX, chipY, chipTotalW, 26);

      ctx.fillStyle = '#FFFFFF';
      ctx.fillText(t.toUpperCase(), chipX + chipPad, chipY + 18);

      chipX += chipTotalW + 10;
    });

    // Launch Dispatch Button (High Contrast Cream background with Navy text)
    const btnY = 510;
    const btnW = infoW;
    const btnH = 52;
    ctx.fillStyle = '#EBE5D8';
    ctx.fillRect(infoX, btnY, btnW, btnH);
    ctx.strokeStyle = '#153966';
    ctx.lineWidth = 2;
    ctx.strokeRect(infoX, btnY, btnW, btnH);

    ctx.fillStyle = '#153966';
    ctx.font = 'bold 16px "Courier New", monospace';
    ctx.textAlign = 'center';
    ctx.fillText('OPEN LIVE PROJECT DISPATCH', infoX + btnW / 2, btnY + 32);
    ctx.textAlign = 'left';

    if (textureRef.current) {
      textureRef.current.needsUpdate = true;
    }
  }, [projects, selectedIndex]);

  // Keep ref to drawScreen for mount initialization without recreating Three.js scene
  const drawScreenRef = useRef(drawScreen);
  useEffect(() => {
    drawScreenRef.current = drawScreen;
  }, [drawScreen]);

  // Update canvas texture whenever projects or selectedIndex changes (WITHOUT resetting camera!)
  useEffect(() => {
    drawScreen();
  }, [drawScreen]);

  // Pre-load project images for high-res drawing on the 3D LCD screen
  useEffect(() => {
    projects.forEach((p, idx) => {
      if (p.img && !loadedImagesRef.current[p.img]) {
        const img = new Image();
        img.src = p.img;
        img.onload = () => {
          loadedImagesRef.current[p.img] = img;
          if (idx === stateRef.current.selectedIndex) {
            drawScreen();
          }
        };
      }
    });
  }, [projects, drawScreen]);

  // Three.js Scene Setup with Procedural 3D Broadsheet LCD Workstation
  // RUNS ONLY ON MOUNT [] so camera angle and user rotation are NEVER reset on tab switch!
  useEffect(() => {
    const container = mountRef.current;
    if (!container) return;

    // Dimensions
    const width = container.clientWidth;
    const height = container.clientHeight || 640;

    // 1. Scene & Background
    const scene = new THREE.Scene();
    sceneRef.current = scene;

    // 2. Camera with Spacious Framing for Full Workstation (Monitor, Keyboard & Mouse)
    const camera = new THREE.PerspectiveCamera(36, width / height, 0.1, 100);
    // Elevated 3/4 isometric desk viewpoint with workstation filling canvas from top to bottom
    camera.position.set(0.9, 2.2, 4.3);
    cameraRef.current = camera;

    // 3. WebGL Renderer
    const renderer = new THREE.WebGLRenderer({ 
      antialias: true, 
      alpha: true,
      powerPreference: 'high-performance' 
    });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFShadowMap;
    rendererRef.current = renderer;
    container.innerHTML = '';
    container.appendChild(renderer.domElement);

    // 4. OrbitControls
    const controls = new OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.08;
    controls.enableZoom = false; // Disable scroll zoom so portfolio page scrolling is completely natural
    // Target aimed at workstation focal center so keyboard/mouse reach down flush to the bottom HUD line
    controls.target.set(0, 0.96, 0.45);
    controls.maxPolarAngle = Math.PI / 2 - 0.08; // Keep above desk
    controls.minPolarAngle = 0.3; // Prevent flipping over top
    controlsRef.current = controls;

    // 5. Lighting
    const ambientLight = new THREE.AmbientLight(0xFFFFFF, 1.35);
    scene.add(ambientLight);

    const dirLight = new THREE.DirectionalLight(0xFFFBF0, 1.8);
    dirLight.position.set(4, 7, 5);
    dirLight.castShadow = true;
    dirLight.shadow.mapSize.width = 2048;
    dirLight.shadow.mapSize.height = 2048;
    dirLight.shadow.camera.near = 0.5;
    dirLight.shadow.camera.far = 20;
    dirLight.shadow.camera.left = -4;
    dirLight.shadow.camera.right = 4;
    dirLight.shadow.camera.top = 4;
    dirLight.shadow.camera.bottom = -4;
    dirLight.shadow.bias = -0.0005;
    scene.add(dirLight);

    const fillLight = new THREE.DirectionalLight(0xD8E2EE, 0.7);
    fillLight.position.set(-5, 3, -2);
    scene.add(fillLight);

    // 6. Materials & Line-art helper
    const navyLineColor = 0x153966;
    const creamColor = 0xE6DECC;
    const creamDarkColor = 0xD8CFBD;

    const lineMat = new THREE.LineBasicMaterial({ color: navyLineColor, linewidth: 2 });

    const createMeshWithOutlines = (geometry, material) => {
      const mesh = new THREE.Mesh(geometry, material);
      const edges = new THREE.EdgesGeometry(geometry, 28);
      const line = new THREE.LineSegments(edges, lineMat);
      mesh.add(line);
      mesh.castShadow = true;
      mesh.receiveShadow = true;
      return mesh;
    };

    const creamMat = new THREE.MeshStandardMaterial({ 
      color: creamColor, 
      roughness: 0.85, 
      metalness: 0.05 
    });
    const creamDarkMat = new THREE.MeshStandardMaterial({ 
      color: creamDarkColor, 
      roughness: 0.9, 
      metalness: 0.05 
    });

    // 7. Workstation Group
    const workstationGroup = new THREE.Group();
    scene.add(workstationGroup);

    // --- SLEEK MODERN LCD MONITOR (Thin Profile & Clean Flat Back) ---
    const monitorGroup = new THREE.Group();
    monitorGroup.position.set(0, 1.02, 0);
    // Slight ergonomic tilt: tilted back 3 degrees, turned slightly toward viewer
    monitorGroup.rotation.x = -0.05;
    monitorGroup.rotation.y = -0.06;
    workstationGroup.add(monitorGroup);

    // Slim LCD Main Panel (Thickness is only 0.12, no giant cone!)
    const panelW = 3.08;
    const panelH = 1.96;
    const panelD = 0.12;
    const panelGeo = new THREE.BoxGeometry(panelW, panelH, panelD);
    const panelMesh = createMeshWithOutlines(panelGeo, creamMat);
    monitorGroup.add(panelMesh);

    // Elegant Inset Rear Backplate
    const backPlateGeo = new THREE.BoxGeometry(panelW - 0.2, panelH - 0.2, 0.02);
    const backPlateMesh = createMeshWithOutlines(backPlateGeo, creamDarkMat);
    backPlateMesh.position.set(0, 0, -panelD / 2 - 0.01);
    monitorGroup.add(backPlateMesh);

    // Central VESA Mount / Stand Hinge Hub on the rear
    const vesaGeo = new THREE.BoxGeometry(0.48, 0.48, 0.04);
    const vesaMesh = createMeshWithOutlines(vesaGeo, new THREE.MeshStandardMaterial({ color: 0x153966, roughness: 0.5 }));
    vesaMesh.position.set(0, 0.04, -panelD / 2 - 0.03);
    monitorGroup.add(vesaMesh);

    // Discreet Rear Ventilation Slots across the top back
    for (let i = 0; i < 3; i++) {
      const ventGeo = new THREE.BoxGeometry(1.6, 0.02, 0.01);
      const ventMesh = new THREE.Mesh(ventGeo, new THREE.MeshBasicMaterial({ color: 0x153966 }));
      ventMesh.position.set(0, 0.55 + i * 0.06, -panelD / 2 - 0.022);
      monitorGroup.add(ventMesh);
    }

    // Broadsheet Spec Tag on the rear
    const backTagGeo = new THREE.PlaneGeometry(0.85, 0.2);
    const backTagMat = new THREE.MeshBasicMaterial({ color: 0x153966 });
    const backTagMesh = new THREE.Mesh(backTagGeo, backTagMat);
    backTagMesh.rotation.y = Math.PI; // faces backwards
    backTagMesh.position.set(0, -0.45, -panelD / 2 - 0.022);
    monitorGroup.add(backTagMesh);

    // Front Bottom Bezel Brand Plate
    const frontLogoGeo = new THREE.PlaneGeometry(0.7, 0.06);
    const frontLogoMesh = new THREE.Mesh(frontLogoGeo, new THREE.MeshBasicMaterial({ color: 0x153966 }));
    frontLogoMesh.position.set(0, -panelH / 2 + 0.065, panelD / 2 + 0.002);
    monitorGroup.add(frontLogoMesh);

    // Power LED (Glowing green dot on bottom right of bezel)
    const ledGeo = new THREE.SphereGeometry(0.02, 12, 12);
    const ledMat = new THREE.MeshBasicMaterial({ color: 0x22C55E });
    const ledMesh = new THREE.Mesh(ledGeo, ledMat);
    ledMesh.position.set(panelW / 2 - 0.12, -panelH / 2 + 0.065, panelD / 2 + 0.005);
    monitorGroup.add(ledMesh);

    // --- LCD DISPLAY SCREEN (CANVAS TEXTURE) ---
    const screenCanvas = document.createElement('canvas');
    screenCanvas.width = 1024;
    screenCanvas.height = 680;
    canvasRef.current = screenCanvas;

    const screenTexture = new THREE.CanvasTexture(screenCanvas);
    screenTexture.generateMipmaps = true;
    screenTexture.minFilter = THREE.LinearMipmapLinearFilter;
    screenTexture.colorSpace = THREE.SRGBColorSpace;
    textureRef.current = screenTexture;

    const screenW = 2.84;
    const screenH = 1.74;
    const screenGeo = new THREE.PlaneGeometry(screenW, screenH);
    const screenMat = new THREE.MeshBasicMaterial({ 
      map: screenTexture,
      toneMapped: false,
      side: THREE.FrontSide
    });
    const screenMesh = new THREE.Mesh(screenGeo, screenMat);
    
    // Positioned proudly on the front face of panel (+0.006) to ensure zero clipping or Z-fighting
    screenMesh.position.set(0, 0.045, panelD / 2 + 0.006);
    
    // Add thin navy contour around the screen boundary
    const screenEdges = new THREE.EdgesGeometry(screenGeo);
    const screenEdgeLines = new THREE.LineSegments(screenEdges, new THREE.LineBasicMaterial({ color: 0x153966, linewidth: 2 }));
    screenMesh.add(screenEdgeLines);

    screenMeshRef.current = screenMesh;
    monitorGroup.add(screenMesh);

    // --- ARTICULATED SLENDER LCD STAND (Matching Aline's sketch!) ---
    // Angled Arm Strut: reaches up from desk base to back VESA mount
    const armGeo = new THREE.BoxGeometry(0.18, 0.88, 0.07);
    const armMesh = createMeshWithOutlines(armGeo, creamMat);
    armMesh.position.set(0, 0.48, -0.22);
    armMesh.rotation.x = 0.22; // angled backward elegantly
    workstationGroup.add(armMesh);

    // Swivel Tilt Hinge (joins top of arm to rear of LCD monitor)
    const hingeGeo = new THREE.CylinderGeometry(0.09, 0.09, 0.22, 16);
    hingeGeo.rotateZ(Math.PI / 2);
    const hingeMesh = createMeshWithOutlines(hingeGeo, new THREE.MeshStandardMaterial({ color: 0x153966, roughness: 0.5 }));
    hingeMesh.position.set(0, 0.96, -panelD / 2 - 0.05);
    workstationGroup.add(hingeMesh);

    // Sleek Flat Base Pedestal on the desk
    const baseGeo = new THREE.BoxGeometry(1.25, 0.04, 0.95);
    const baseMesh = createMeshWithOutlines(baseGeo, creamMat);
    baseMesh.position.set(0, 0.02, -0.05);
    workstationGroup.add(baseMesh);

    // Base Neck Foot
    const baseRingGeo = new THREE.BoxGeometry(0.32, 0.04, 0.22);
    const baseRingMesh = createMeshWithOutlines(baseRingGeo, creamDarkMat);
    baseRingMesh.position.set(0, 0.05, -0.15);
    workstationGroup.add(baseRingMesh);

    // --- MECHANICAL KEYBOARD ---
    const kbdGroup = new THREE.Group();
    kbdGroup.position.set(-0.15, 0.04, 0.98);
    kbdGroup.rotation.y = -0.03;
    workstationGroup.add(kbdGroup);

    // Keyboard Base Wedge
    const kbdBaseGeo = new THREE.BoxGeometry(2.1, 0.07, 0.75);
    const kbdBaseMesh = createMeshWithOutlines(kbdBaseGeo, creamMat);
    kbdGroup.add(kbdBaseMesh);

    // Keyboard Keybed Inset
    const keybedGeo = new THREE.BoxGeometry(1.98, 0.02, 0.65);
    const keybedMesh = createMeshWithOutlines(keybedGeo, creamDarkMat);
    keybedMesh.position.set(0, 0.04, 0);
    kbdGroup.add(keybedMesh);

    // Key Rows
    const keyRows = 4;
    const keyCols = 14;
    const keyW = 0.11;
    const keyH = 0.035;
    const keyD = 0.11;
    const keyMat = new THREE.MeshStandardMaterial({ color: 0xF2ECE0, roughness: 0.7 });
    const keyLineMat = new THREE.LineBasicMaterial({ color: 0x153966, linewidth: 1 });

    for (let r = 0; r < keyRows; r++) {
      for (let c = 0; c < keyCols; c++) {
        if (r === keyRows - 1 && c >= 4 && c <= 9) continue;

        const kGeo = new THREE.BoxGeometry(keyW, keyH, keyD);
        const kMesh = new THREE.Mesh(kGeo, keyMat);
        const kEdges = new THREE.EdgesGeometry(kGeo);
        kMesh.add(new THREE.LineSegments(kEdges, keyLineMat));

        const kX = (c - keyCols / 2 + 0.5) * (keyW + 0.025);
        const kZ = (r - keyRows / 2 + 0.5) * (keyD + 0.035);
        kMesh.position.set(kX, 0.065, kZ);
        kbdGroup.add(kMesh);
      }
    }

    // Spacebar
    const spaceGeo = new THREE.BoxGeometry(0.75, keyH, keyD);
    const spaceMesh = new THREE.Mesh(spaceGeo, keyMat);
    const spaceEdges = new THREE.EdgesGeometry(spaceGeo);
    spaceMesh.add(new THREE.LineSegments(spaceEdges, keyLineMat));
    spaceMesh.position.set(0.04, 0.065, (keyRows - 1 - keyRows / 2 + 0.5) * (keyD + 0.035));
    kbdGroup.add(spaceMesh);

    // --- VINTAGE TWO-BUTTON MOUSE WITH CURVED WIRE (On the RIGHT side) ---
    const mouseGroup = new THREE.Group();
    mouseGroup.position.set(1.30, 0.04, 0.76);
    mouseGroup.rotation.y = -0.18;
    workstationGroup.add(mouseGroup);

    // Mouse Body
    const mouseGeo = new THREE.BoxGeometry(0.36, 0.11, 0.55);
    const mouseMesh = createMeshWithOutlines(mouseGeo, creamMat);
    mouseGroup.add(mouseMesh);

    // Mouse Button Split Groove
    const seamGeo = new THREE.BoxGeometry(0.015, 0.02, 0.25);
    const seamMesh = new THREE.Mesh(seamGeo, new THREE.MeshBasicMaterial({ color: 0x153966 }));
    seamMesh.position.set(0, 0.06, -0.14);
    mouseGroup.add(seamMesh);

    // Mouse Wire: Extends from front tip of mouse, curving across desk to behind monitor
    const curvePoints = [
      new THREE.Vector3(1.30, 0.05, 0.48),
      new THREE.Vector3(1.22, 0.02, 0.28),
      new THREE.Vector3(0.92, 0.02, 0.12),
      new THREE.Vector3(0.48, 0.02, -0.05),
      new THREE.Vector3(0.1, 0.12, -0.22)
    ];
    const wireCurve = new THREE.CatmullRomCurve3(curvePoints);
    const wireGeo = new THREE.TubeGeometry(wireCurve, 32, 0.018, 8, false);
    const wireMat = new THREE.MeshStandardMaterial({ color: 0x153966, roughness: 0.6 });
    const wireMesh = new THREE.Mesh(wireGeo, wireMat);
    wireMesh.castShadow = true;
    workstationGroup.add(wireMesh);

    // --- DESK ARCHITECTURAL BLOTTER ---
    const deskGeo = new THREE.PlaneGeometry(16, 12);
    const deskMat = new THREE.MeshStandardMaterial({ 
      color: 0x0B1B30, 
      roughness: 0.9,
      metalness: 0.05
    });
    const deskMesh = new THREE.Mesh(deskGeo, deskMat);
    deskMesh.rotation.x = -Math.PI / 2;
    deskMesh.position.set(0, 0, 0.8);
    deskMesh.receiveShadow = true;
    workstationGroup.add(deskMesh);

    // Blotter Outline
    const blotterGeo = new THREE.PlaneGeometry(6.6, 4.4);
    const blotterMat = new THREE.MeshBasicMaterial({ 
      color: 0x153966, 
      wireframe: true 
    });
    const blotterMesh = new THREE.Mesh(blotterGeo, blotterMat);
    blotterMesh.rotation.x = -Math.PI / 2;
    blotterMesh.position.set(0, 0.005, 0.6);
    workstationGroup.add(blotterMesh);

    // 8. Raycasting on 3D LCD Screen for direct in-world interaction
    const raycaster = new THREE.Raycaster();
    const mouseVec = new THREE.Vector2();

    const handleCanvasClick = (event) => {
      const rect = renderer.domElement.getBoundingClientRect();
      mouseVec.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
      mouseVec.y = -(((event.clientY - rect.top) / rect.height) * 2 - 1);

      raycaster.setFromCamera(mouseVec, camera);
      const intersects = raycaster.intersectObject(screenMeshRef.current);

      if (intersects.length > 0) {
        const uv = intersects[0].uv;
        if (uv) {
          const clickX = uv.x * 1024;
          const clickY = (1 - uv.y) * 680;

          const { projects: currentProjects, selectedIndex: currentIdx, onSelectProject: cbSelect, onPrev: cbPrev, onNext: cbNext } = stateRef.current;

          // Check if top tabs clicked
          if (clickY >= 20 && clickY <= 72) {
            const tabW = 246;
            const startX = 24;
            currentProjects.forEach((_, idx) => {
              const x = startX + idx * (tabW + 12);
              if (clickX >= x && clickX <= x + tabW) {
                if (cbSelect) cbSelect(idx);
              }
            });
          }

          // Check if Slideshow PREV clicked
          if (clickY >= 530 && clickY <= 585 && clickX >= 36 && clickX <= 130) {
            if (cbPrev) cbPrev();
          }

          // Check if Slideshow NEXT clicked
          if (clickY >= 530 && clickY <= 585 && clickX >= 400 && clickX <= 500) {
            if (cbNext) cbNext();
          }

          // Check if Open Dispatch Button clicked
          if (clickY >= 510 && clickY <= 565 && clickX >= 525 && clickX <= 990) {
            const curr = currentProjects[currentIdx];
            if (curr?.url) {
              window.open(curr.url, '_blank', 'noopener,noreferrer');
            }
          }
        }
      }
    };

    renderer.domElement.addEventListener('click', handleCanvasClick);

    // Initial Screen Draw & immediate GPU upload
    drawScreenRef.current();
    screenTexture.needsUpdate = true;

    // 9. Animation & Render Loop
    let animationFrameId;
    let lastTime = performance.now();

    const animate = (currentTime) => {
      animationFrameId = requestAnimationFrame(animate);
      const delta = (currentTime - lastTime) / 1000;
      lastTime = currentTime;

      if (isAutoRotatingRef.current && delta < 0.2) {
        workstationGroup.rotation.y += delta * 0.45;
      }

      controls.update();
      renderer.render(scene, camera);
    };
    animate(performance.now());

    // 10. Responsive Resize Handler
    const handleResize = () => {
      if (!container || !renderer || !camera) return;
      const newW = container.clientWidth;
      const newH = container.clientHeight || 640;
      camera.aspect = newW / newH;
      camera.updateProjectionMatrix();
      renderer.setSize(newW, newH);
    };
    window.addEventListener('resize', handleResize);

    return () => {
      window.removeEventListener('resize', handleResize);
      renderer.domElement.removeEventListener('click', handleCanvasClick);
      cancelAnimationFrame(animationFrameId);
      controls.dispose();
      renderer.dispose();
      scene.clear();
    };
  }, []); // Run only once on mount: NEVER reset user camera angle on tab clicks!

  // Update auto-spin state ref
  useEffect(() => {
    isAutoRotatingRef.current = isAutoSpin;
  }, [isAutoSpin]);

  // Reset Camera View to Aline's exact 3/4 isometric sketch (showing monitor, keyboard, and mouse)
  const handleResetCamera = () => {
    if (!cameraRef.current || !controlsRef.current) return;
    cameraRef.current.position.set(0.9, 2.2, 4.3);
    controlsRef.current.target.set(0, 0.96, 0.45);
    controlsRef.current.update();
  };

  return (
    <div className="relative w-full h-full flex-1 flex flex-col items-stretch justify-start select-none min-h-0">
      {/* 3D WebGL Canvas Container: Expands fully down to the top of the HUD control line */}
      <div 
        ref={mountRef} 
        onMouseDown={() => setHintVisible(false)}
        onTouchStart={() => setHintVisible(false)}
        className="w-full flex-1 min-h-[520px] cursor-grab active:cursor-grabbing relative rounded-sm overflow-hidden"
      />

      {/* Floating 3D Interaction Control HUD */}
      <div className="w-full flex flex-wrap items-center justify-between gap-2 pt-1.5 pb-1 border-t border-cream/20 font-mono text-[9px] sm:text-[10px] md:text-xs uppercase tracking-wider text-cream/70 shrink-0">
        
        {/* Left: 3D Scene Controls */}
        <div className="flex items-center gap-2">
          <button
            onClick={handleResetCamera}
            className="px-2.5 py-1 border border-cream/30 hover:bg-cream hover:text-navy transition-colors font-bold cursor-pointer"
          >
            RESET 3D VIEW
          </button>
          <button
            onClick={() => setIsAutoSpin(!isAutoSpin)}
            className={`px-2.5 py-1 border transition-colors font-bold cursor-pointer ${
              isAutoSpin 
                ? 'bg-cream text-navy border-cream' 
                : 'border-cream/30 hover:bg-cream hover:text-navy'
            }`}
          >
            {isAutoSpin ? 'PAUSE 360° SPIN' : 'AUTO 360° SPIN'}
          </button>
        </div>

        {/* Center: Instruction Prompt */}
        {hintVisible && (
          <div className="hidden md:flex items-center gap-2 text-cream/60">
            <span className="animate-pulse">●</span>
            <span>DRAG TO ROTATE 360° // CLICK SCREEN TABS</span>
          </div>
        )}

        {/* Right: Quick Launch Live Site Button */}
        {projects[selectedIndex]?.url && (
          <a
            href={projects[selectedIndex].url}
            target="_blank"
            rel="noopener noreferrer"
            className="px-3 py-1 bg-cream text-navy font-bold hover:bg-cream/90 transition-colors cursor-pointer flex items-center"
          >
            <span>LAUNCH PROJECT 0{selectedIndex + 1}</span>
          </a>
        )}
      </div>
    </div>
  );
}
