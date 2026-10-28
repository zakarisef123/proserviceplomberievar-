// Génère les images PNG du site (favicon, logo, image de partage) à partir de HTML.
// Usage : node src/make_images.js   (nécessite Playwright + Chromium)
const { chromium } = require('playwright');
const path = require('path');
const out = path.join(__dirname, 'assets');
const mark = `<svg viewBox="0 0 40 40" style="width:100%;height:100%"><path d="M20 3 L33 20 L20 37 L7 20 Z" fill="#4a2a86"/><path d="M20 3 L33 20 L20 37 Z" fill="#f37b1e"/></svg>`;
const icon = (pad) => `<html><body style="margin:0;background:#fff;display:flex;align-items:center;justify-content:center;width:100vw;height:100vh"><div style="width:${100 - pad * 2}%;height:${100 - pad * 2}%">${mark}</div></body></html>`;
const og = `<html><head><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&display=swap" rel="stylesheet"></head>
<body style="margin:0;width:1200px;height:630px;font-family:Poppins,sans-serif;color:#fff;background:radial-gradient(ellipse 700px 500px at 90% 0%,rgba(255,255,255,.12),transparent 60%),linear-gradient(155deg,#4a2a86 0%,#2c1a4d 100%);display:flex;flex-direction:column;justify-content:center;padding:0 80px;box-sizing:border-box">
<div style="display:flex;align-items:center;gap:18px;margin-bottom:34px"><div style="width:64px;height:64px;background:#fff;border-radius:14px;padding:8px;box-sizing:border-box">${mark}</div><div style="font-size:30px;font-weight:800;letter-spacing:.02em">PRO SERVICE 83</div></div>
<div style="font-size:64px;font-weight:800;line-height:1.08;margin-bottom:22px">Plombier à Vidauban<br><span style="color:#ffb877">et dans tout le Var, 24h/24</span></div>
<div style="font-size:26px;opacity:.88;margin-bottom:34px">Fuite d'eau · Débouchage · Chauffe-eau · Salle de bain</div>
<div style="display:inline-flex;align-self:flex-start;background:#f37b1e;border-radius:20px;padding:16px 30px;font-size:38px;font-weight:700">☎ 06 75 93 19 04</div></body></html>`;
(async () => {
  const browser = await chromium.launch();
  const shot = async (html, w, h, file) => {
    const page = await browser.newPage({ viewport: { width: w, height: h } });
    await page.setContent(html, { waitUntil: 'networkidle' }).catch(() => page.setContent(html));
    await page.screenshot({ path: path.join(out, file) });
    await page.close();
  };
  await shot(icon(6), 32, 32, 'favicon-32.png');
  await shot(icon(12), 180, 180, 'apple-touch-icon.png');
  await shot(icon(12), 512, 512, 'logo-512.png');
  await shot(og, 1200, 630, 'og-image.png');
  await browser.close();
})();
