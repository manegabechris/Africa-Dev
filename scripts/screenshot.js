/*
Simple Puppeteer script to capture screenshots of key pages.
Usage:
  1. Serve the project locally (from repo root):
       python -m http.server 8000
  2. Install puppeteer locally (recommended):
       npm install puppeteer --no-save
     (If you run into interactive postinstall hooks in your environment, use a machine without the Wix postinstall blocker or use npx)
  3. Run the script:
       node scripts/screenshot.js --baseUrl=http://localhost:8000 --out=screenshots

The script will visit a list of pages and save PNG files in the output directory.
*/

const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer');

const pages = [
  { url: '/', name: 'index' },
  { url: '/option.html', name: 'option' },
  { url: '/inscription.html', name: 'inscription' },
  { url: '/transformation%20digital.html', name: 'transformation' },
  { url: '/developement%20web.html', name: 'developpement-web' },
  { url: '/marketing%20digital.html', name: 'marketing' },
  { url: '/groupe%20chat.html', name: 'groupe-chat' }
];

async function run() {
  const argv = require('yargs').option('baseUrl', { type: 'string', demandOption: true }).option('out', { type: 'string', default: 'screenshots' }).argv;
  const baseUrl = argv.baseUrl.replace(/\/$/, '');
  const outDir = path.resolve(process.cwd(), argv.out);
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  page.setViewport({ width: 1280, height: 900 });

  for (const p of pages) {
    const url = baseUrl + p.url;
    console.log('Visiting', url);
    await page.goto(url, { waitUntil: 'networkidle2' });
    // If the page is inscription and modal should open automatically for ?from=privacy
    if (p.name === 'inscription') {
      // wait a bit and try to open policy modal if not open
      await page.waitForTimeout(400);
    }
    const file = path.join(outDir, `${p.name}.png`);
    await page.screenshot({ path: file, fullPage: true });
    console.log('Saved', file);
  }

  await browser.close();
}

run().catch(err => { console.error(err); process.exit(1); });
