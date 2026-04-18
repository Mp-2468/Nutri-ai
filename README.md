# 🥗 NutriAI — Smart Calorie Tracker

> AI-powered nutrition tracking with food scanning (Claude AI), BMI calculator, water & exercise logging, and an intelligent chatbot (Gemini 1.5).

---

## 📁 Project Structure

```
nutri-ai/
├── index.html              ← The entire app (single file)
├── manifest.json           ← PWA manifest (installable as mobile app)
├── sw.js                   ← Service worker (offline support)
├── vercel.json             ← Vercel deployment config
├── netlify.toml            ← Netlify deployment config
├── generate_icons.py       ← Icon generator script
├── .github/
│   └── workflows/
│       └── deploy.yml      ← GitHub Pages auto-deploy
└── icons/                  ← (Generate with generate_icons.py)
    ├── icon-72.png
    ├── icon-96.png
    ├── icon-128.png
    ├── icon-144.png
    ├── icon-152.png
    ├── icon-192.png
    ├── icon-384.png
    └── icon-512.png
```

---

## 🔑 API Keys

The app uses two AI services. Update them in `index.html` inside the `CONFIG` object at the top:

```javascript
const CONFIG = {
  GEMINI_API_KEY: "YOUR_GEMINI_KEY_HERE",       // For NutriBot chatbot
  ANTHROPIC_API_KEY: "YOUR_ANTHROPIC_KEY_HERE", // For food image scanning (outside Claude.ai)
};
```

### Getting Your API Keys

#### Gemini API Key (for chatbot)
1. Go to → https://aistudio.google.com/app/apikey
2. Click **"Create API Key"**
3. Select a project (or create one)
4. Copy the key → paste into `CONFIG.GEMINI_API_KEY`
5. Free tier: 15 requests/min, 1 million tokens/day ✅

#### Anthropic API Key (for food scanning — only needed outside Claude.ai)
1. Go to → https://console.anthropic.com/settings/keys
2. Click **"Create Key"**
3. Copy the key → paste into `CONFIG.ANTHROPIC_API_KEY`
4. Also uncomment the headers block in the `analyzeFood()` function:
   ```javascript
   // Uncomment these lines in analyzeFood():
   headers["x-api-key"] = CONFIG.ANTHROPIC_API_KEY;
   headers["anthropic-version"] = "2023-06-01";
   ```
5. Pricing: ~$0.003 per food scan (claude-sonnet-4)

> ⚠️ **Security Note**: For production apps, never expose API keys in client-side code.
> Use a backend proxy (see "Production Security" section below).

---

## 🚀 Deployment Options

---

### Option 1: Vercel (Recommended — Free, Fastest)

**Time: ~3 minutes**

#### Method A: Vercel CLI
```bash
# 1. Install Vercel CLI
npm install -g vercel

# 2. Navigate to your project folder
cd nutri-ai

# 3. Deploy (follow prompts)
vercel

# 4. For production deployment:
vercel --prod
```
Your app will be live at: `https://nutri-ai-xxx.vercel.app`

#### Method B: Drag & Drop (No CLI needed)
1. Go to → https://vercel.com/new
2. Sign up / log in (free)
3. Click **"Deploy"** then drag your entire `nutri-ai/` folder into the upload zone
4. Done! Live in ~30 seconds

#### Method C: GitHub Integration (Auto-deploys on every push)
1. Push your code to a GitHub repository
2. Go to → https://vercel.com/new
3. Click **"Import Git Repository"** → select your repo
4. Click **Deploy** → it's live!

---

### Option 2: Netlify (Free, Great for PWAs)

**Time: ~3 minutes**

#### Method A: Drag & Drop
1. Go to → https://app.netlify.com/drop
2. Drag your entire `nutri-ai/` folder into the page
3. Done! Your app is live instantly

#### Method B: Netlify CLI
```bash
# 1. Install Netlify CLI
npm install -g netlify-cli

# 2. Login
netlify login

# 3. Deploy
cd nutri-ai
netlify deploy

# 4. When ready, deploy to production
netlify deploy --prod
```

#### Method C: GitHub Integration
1. Push code to GitHub
2. Go to → https://app.netlify.com
3. Click **"Add new site"** → **"Import an existing project"**
4. Connect GitHub → select your repo
5. Build settings: leave all blank (static site)
6. Click **Deploy site**

---

### Option 3: GitHub Pages (Free, Good for open source)

**Time: ~5 minutes**

```bash
# 1. Create a GitHub repository
# Go to https://github.com/new

# 2. Push your code
git init
git add .
git commit -m "Initial commit: NutriAI app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/nutri-ai.git
git push -u origin main

# 3. Enable GitHub Pages
# Go to your repo → Settings → Pages
# Source: "GitHub Actions"
# The .github/workflows/deploy.yml file handles auto-deployment

# 4. Your app will be live at:
# https://YOUR_USERNAME.github.io/nutri-ai/
```

---

### Option 4: Firebase Hosting (Free, Google CDN)

**Time: ~5 minutes**

```bash
# 1. Install Firebase CLI
npm install -g firebase-tools

# 2. Login
firebase login

# 3. Initialize (from your project folder)
cd nutri-ai
firebase init hosting
# → Select "Use an existing project" or create new
# → Public directory: . (current directory)
# → Single-page app: Yes
# → Overwrite index.html: No

# 4. Deploy
firebase deploy

# Your app is live at: https://YOUR-PROJECT.web.app
```

---

### Option 5: Local Development Server

**Test locally before deploying:**

```bash
# Option A: Python (built-in, no install needed)
cd nutri-ai
python3 -m http.server 8080
# Open: http://localhost:8080

# Option B: Node.js
npx serve .
# Open: http://localhost:3000

# Option C: VS Code
# Install "Live Server" extension → right-click index.html → "Open with Live Server"
```

> ⚠️ Opening `index.html` directly via `file://` won't work due to browser security
> restrictions on camera access and service workers. Always use a server.

---

## 📱 Installing as a Mobile App (PWA)

Once deployed, users can install NutriAI directly to their home screen:

### iPhone / iPad (Safari)
1. Open the deployed URL in **Safari**
2. Tap the **Share** button (box with arrow)
3. Scroll down → tap **"Add to Home Screen"**
4. Tap **"Add"**
5. The app icon appears on your home screen!

### Android (Chrome)
1. Open the deployed URL in **Chrome**
2. A banner may appear: **"Add NutriAI to home screen"** → tap it
3. Or: tap the **⋮ menu** → **"Add to Home Screen"** / **"Install App"**

### Desktop (Chrome / Edge)
1. Open the URL
2. Click the **install icon** (➕) in the address bar
3. Click **"Install"**

---

## 🖼️ Generating App Icons

The `manifest.json` requires PNG icons. Generate them with:

```bash
# Install Pillow first
pip install Pillow

# Run the generator
python generate_icons.py

# Icons will be created in ./icons/
```

**Alternative (no Python needed):**
1. Create a 512×512 PNG of your logo
2. Go to → https://realfavicongenerator.net
3. Upload your image
4. Download the icon pack → extract into `icons/` folder

---

## 🔒 Production Security

**Important:** Exposing API keys in client-side JavaScript is a security risk for production apps. Here's how to secure them:

### Option A: Vercel Edge Functions (Recommended)

Create `api/analyze.js` in your project:

```javascript
// api/analyze.js — Vercel serverless function
export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).end();

  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': process.env.ANTHROPIC_API_KEY,      // Set in Vercel dashboard
      'anthropic-version': '2023-06-01'
    },
    body: JSON.stringify(req.body)
  });

  const data = await response.json();
  res.json(data);
}
```

Then set environment variables in Vercel Dashboard:
1. Go to your project → **Settings** → **Environment Variables**
2. Add: `ANTHROPIC_API_KEY` = your key
3. Add: `GEMINI_API_KEY` = your key

Update `index.html` to call `/api/analyze` instead of directly calling Anthropic.

### Option B: Netlify Functions

```bash
mkdir netlify/functions
```

Create `netlify/functions/analyze.js`:
```javascript
const fetch = require('node-fetch');
exports.handler = async (event) => {
  const body = JSON.parse(event.body);
  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': process.env.ANTHROPIC_API_KEY,
      'anthropic-version': '2023-06-01'
    },
    body: JSON.stringify(body)
  });
  const data = await response.json();
  return { statusCode: 200, body: JSON.stringify(data) };
};
```

Set env vars in **Netlify Dashboard → Site settings → Environment variables**.

---

## 🌐 Custom Domain Setup

### Vercel
1. Go to your project → **Settings** → **Domains**
2. Add your domain (e.g., `nutriai.yourdomain.com`)
3. Add the DNS records shown to your domain registrar
4. SSL is automatic ✅

### Netlify
1. Go to your site → **Domain management** → **Add custom domain**
2. Follow the DNS setup instructions
3. SSL is automatic ✅

---

## 🐛 Troubleshooting

| Problem | Solution |
|---|---|
| Camera not working | Must be served over HTTPS or localhost. Deploy first. |
| "API key invalid" error | Check your Gemini/Anthropic keys in `CONFIG` at the top of `index.html` |
| Food scan fails outside Claude.ai | Uncomment the API key headers in `analyzeFood()` and add your Anthropic key |
| App not installing as PWA | Requires HTTPS. Use Vercel/Netlify (both provide free SSL) |
| Icons not showing | Run `generate_icons.py` and make sure `icons/` folder is in the same directory as `index.html` |
| Service worker not registering | Must be served from root path `/`. Check your deployment URL |
| Data not persisting | App uses localStorage as fallback. Make sure cookies/storage is not blocked in browser settings |

---

## 📊 Features Overview

| Feature | Technology |
|---|---|
| Food image scanning | Claude claude-sonnet-4 Vision API |
| AI nutrition chatbot | Google Gemini 1.5 Flash |
| BMI calculator | Mifflin-St Jeor equation |
| TDEE estimation | Harris-Benedict activity multipliers |
| Calorie targets | Cut (−20%), Maintain, Bulk (+15%) |
| Data persistence | localStorage / Claude.ai storage API |
| Offline support | Service Worker + Cache API |
| Installable app | Progressive Web App (PWA) |
| Camera capture | MediaDevices.getUserMedia() |

---

## 📜 License

MIT License — free to use, modify, and deploy for personal or commercial projects.

---

## 🙏 Credits

Built with Claude AI (Anthropic) + Gemini (Google) + vanilla HTML/CSS/JS.
