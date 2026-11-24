// Génère les images PNG du site (favicon, logo, image de partage) à partir de HTML.
// Usage : node src/make_images.js   (nécessite Playwright + Chromium)
const { chromium } = require('playwright');
const path = require('path');
const out = path.join(__dirname, 'assets');
const mark = `<svg style="width:100%;height:100%" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="30" fill="#ffd400"/><circle cx="32" cy="32" r="24.5" fill="none" stroke="#111" stroke-width="2.2"/><g transform="translate(20 9.5)"><path d="M12 3.2c0 0-6.2 7.1-6.2 11.4a6.2 6.2 0 0 0 12.4 0C18.2 10.3 12 3.2 12 3.2Z" fill="#111"/></g><text x="32" y="47" text-anchor="middle" font-family="Space Grotesk, Arial, sans-serif" font-weight="700" font-size="12.5" fill="#111">24/7</text></svg>`;
const iconSvg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="31" fill="#ffd400"/><circle cx="32" cy="32" r="25" fill="none" stroke="#111" stroke-width="3"/><g transform="translate(14 13) scale(1.5)"><path d="M12 3.2c0 0-6.2 7.1-6.2 11.4a6.2 6.2 0 0 0 12.4 0C18.2 10.3 12 3.2 12 3.2Z" fill="#111"/></g></svg>`;
const icon = (pad) => `<html><body style="margin:0;background:#111;display:flex;align-items:center;justify-content:center;width:100vw;height:100vh"><div style="width:${100 - pad * 2}%;height:${100 - pad * 2}%">${iconSvg.replace('<svg ', '<svg style="width:100%;height:100%" ')}</div></body></html>`;
const og = `<html><head><link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet"></head>
<body style="margin:0;width:1200px;height:630px;font-family:'Space Grotesk',sans-serif;color:#fff;background:#111;border-bottom:18px solid #ffd400;display:flex;flex-direction:column;justify-content:center;padding:0 80px;box-sizing:border-box">
<div style="display:flex;align-items:center;gap:18px;margin-bottom:34px"><div style="width:72px;height:72px">${mark}</div><div><div style="font-size:36px;font-weight:700;letter-spacing:-.02em">Proservice</div><div style="font-size:15px;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:#ffd400">Plomberie · Var</div></div></div>
<div style="font-size:64px;font-weight:800;line-height:1.08;margin-bottom:22px">Votre plombier<br><span style="color:#ffd400">dans tout le Var, 24h/24</span></div>
<div style="font-size:26px;opacity:.88;margin-bottom:34px">Fuite d'eau · Débouchage · Chauffe-eau · Salle de bain</div>
<div style="display:inline-flex;align-self:flex-start;background:#ffd400;color:#111;border-radius:10px;padding:16px 30px;font-size:38px;font-weight:700">☎ 06 75 93 19 04</div></body></html>`;
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
