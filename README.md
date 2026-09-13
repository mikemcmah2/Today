# Daybreak — Morning & Evening Routine Tracker

One file to deploy: `index.html`. Icons included for browser tab + iOS home screen.

## What's inside

- `index.html` — the whole app. React and ReactDOM are embedded directly in the file (no CDN, no build step), so it works offline and isn't dependent on any external script loading.
- `apple-touch-icon.png` (180×180) — used when someone adds the app to their iOS home screen.
- `favicon-32.png` — browser tab icon.
- `icon-1024.png` — large master copy of the icon, kept in case you want to generate other sizes later.

## Deploy on GitHub Pages

1. Put all four files at the **root** of the repo (same folder).
2. Repo **Settings → Pages** → **Source: Deploy from a branch** → branch `main`, folder `/ (root)`.
3. Wait ~30–60 seconds, then visit your Pages URL.
4. On iPhone, open that URL in Safari → Share → **Add to Home Screen** for a proper app icon and full-screen launch.

## Notes

- Routines and daily progress are stored in `localStorage` in whatever browser you use — no sync between devices.
- Streaks (current + best) are tracked per section based on your local history, kept for the last 90 days.
- If anything ever fails to load, the page shows the exact error as readable text instead of staying blank.
