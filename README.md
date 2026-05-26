# 🏦 CBS Core Knowledge Quiz

A quiz app to help you master the **CBS Core Knowledge Book** — built around
a pool of **360 multiple-choice questions** covering Tables, the Registry,
Lifecycle Spaces (LIV/NAU/HIS/DEL/SIM), Standard Operations, the Dynamic
Data Dictionary, Projections, Plugins, Enquiries, and the Product Factory.
The pool now includes **60 business/scenario questions** that test
understanding through realistic banking situations, not just memorization.

Every quiz round picks **30 random questions** from the pool. Pass it. Fail
it. Take it again until you nail it.

Comes in two flavors:

- **Web app** (`index.html`) — runs in any browser, hosts on GitHub Pages,
  has a shared leaderboard.
- **Python CLI** (`quiz.py`) — runs in your terminal, no install needed.

---

## 📁 Files

| File | What it is |
|---|---|
| `index.html` | The web app — open in any browser |
| `questions.js` | The 300-question bank (used by the browser) |
| `questions.json` | Same 300 questions in JSON (used by Python) |
| `config.js` | Optional shared-leaderboard configuration |
| `quiz.py` | Python CLI version (no dependencies) |
| `README.md` | This file |

---

## 🐍 Option 1 — Run the Python CLI locally

You just need Python 3.8+ installed. No `pip install` needed.

```bash
cd cbs-quiz
python quiz.py
```

You'll see a menu:

1. Take the quiz
2. View leaderboard
3. Quit

Your scores save to `scores.json` next to the script. Colors work on
macOS, Linux, and modern Windows terminals.

---

## 🌐 Option 2 — Host the web app on GitHub Pages

### Step 1 — Create the GitHub repo

1. Go to https://github.com/Adrien-Monthe and click **New repository**.
2. Name it **`cbs-quiz`** (or anything you like).
3. Keep it **Public** (required for free GitHub Pages).
4. Don't add a README, .gitignore, or license — we already have files.
5. Click **Create repository**.

### Step 2 — Push the files

Open a terminal in the `cbs-quiz` folder and run:

```bash
git init
git add .
git commit -m "Initial commit — CBS quiz app"
git branch -M main
git remote add origin https://github.com/Adrien-Monthe/cbs-quiz.git
git push -u origin main
```

If you don't have git installed, you can also drag-and-drop the files
into the GitHub web UI ("Add file" → "Upload files").

### Step 3 — Turn on GitHub Pages

1. In the new repo, click **Settings** → **Pages** (left sidebar).
2. Under **Build and deployment** → **Source**, select **Deploy from a branch**.
3. Branch: **main**, folder: **`/ (root)`**. Click **Save**.
4. Wait ~30 seconds. GitHub will publish to:

   ```
   https://adrien-monthe.github.io/cbs-quiz/
   ```

That's it! Open the link in any browser. Share with friends.

---

## 🏆 Option 3 (Optional) — Enable the shared global leaderboard

By default the leaderboard works **locally per browser** (each visitor sees
their own scores). To make it **truly shared** (everyone sees everyone's
scores worldwide), pick **one** of the two backends below and fill in
`config.js`.

### 🅰️ Option A — Firebase Realtime Database (recommended, most reliable)

This is Google infrastructure — rock-solid, free tier is huge.

1. Go to **https://console.firebase.google.com** and sign in with Google.
2. Click **Add project** → give it any name → skip Analytics → **Create project**.
3. In the left sidebar click **Build** → **Realtime Database**.
4. Click **Create Database** → pick any location → choose **Start in test mode**
   (that's fine for a quiz app) → **Enable**.
5. At the top of the database page, copy the URL — it looks like:
   ```
   https://your-project-default-rtdb.firebaseio.com
   ```
6. Open `config.js` and paste:
   ```js
   const CONFIG = {
     FIREBASE_URL: "https://your-project-default-rtdb.firebaseio.com",
     PANTRY_ID:    "",
   };
   ```
7. Commit and push. Done — leaderboard is global.

> ℹ️ Test-mode rules expire after 30 days. To keep it open longer, in the
> Firebase console go to **Realtime Database → Rules** and paste:
> ```json
> { "rules": { ".read": true, ".write": true } }
> ```
> Click **Publish**. (Public read/write is fine for a personal study app.)

### 🅱️ Option B — Pantry (simplest, no Google account)

If you don't want to use Google, **Pantry** is dead simple — just an email.

1. Go to **https://getpantry.cloud**.
2. Enter any email address → click **Get Started**.
3. The site will show you a **Pantry ID** — a UUID like
   `12345678-90ab-cdef-1234-567890abcdef`. Copy it.
4. Open `config.js` and paste:
   ```js
   const CONFIG = {
     FIREBASE_URL: "",
     PANTRY_ID:    "12345678-90ab-cdef-1234-567890abcdef",
   };
   ```
5. Commit and push. Done — leaderboard is global.

That's it: no API key, no console, no rules to configure.

### Either way, commit and deploy:

```bash
git add config.js
git commit -m "Enable shared leaderboard"
git push
```

> If you leave both fields empty, the app silently falls back to
> per-browser localStorage — still totally functional, just not shared
> across devices.

---

## 📚 What the questions cover

The 300 questions are organized across 10 topics drawn from the source book:

| Topic | Range | What it covers |
|---|---|---|
| Table Entity | 1-25 | Tables, CUSTOMER, ACCOUNT, USER, TELLER, FUNDS.TRANSFER, etc. |
| Anatomy | 26-50 | PROGRAM/FILE registries, classification, audit fields |
| File Types | 51-90 | LIV, NAU, HIS, DEL, SIM — cardinality and behavior |
| Operations | 91-140 | SEE, INPUT, HOLD, VALIDATE, AUTH, REVERSE, DELETE, HISTORY.RESTORE |
| DDD | 141-175 | Dynamic Data Dictionary, D/I/J fields, Non-1NF, hot-swap |
| Projections | 176-220 | SDUI, Resolution Waterfall, Diff Engine, Hot Fields, hooks |
| Plugins | 221-245 | Hooks, gateway model, jBase/Java, Hot Field plugins |
| Enquiries | 246-275 | Soft Links, Virtual Merging, Fast Path, Designer |
| Compare | 276-290 | Projection vs Enquiry side-by-side |
| Product Factory | 291-300 | PRODUCT.CLASS hierarchy, lifecycle stages, versioning |

Every question includes a **tip / explanation** so each round is also a
mini lesson.

---

## 🛠 Adding more questions later

Open `questions.js`, add new entries to the array (pick fresh IDs after 300),
and rerun:

```bash
node -e "require('fs').writeFileSync('questions.json', JSON.stringify(require('./questions.js'), null, 2))"
```

That regenerates `questions.json` for the Python CLI. Commit and push and
you're done.

---

## 💡 Tips for mastering CBS

- Don't memorize — pay attention to the **tip after each question**.
  That's where the real learning is.
- If you keep missing the same topic, search the Core Knowledge Book for
  that section.
- Aim for 90%+ on three consecutive runs before you call it mastered.

Good luck! 🚀
