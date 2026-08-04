# Today

A one-tap nightly check-in. Tap green for a good day, red for a rough one — it
tracks the ratio in a ring chart and keeps the running totals below.

Everything is saved on your phone only (in the browser's local storage), never
sent anywhere.

## Put it on GitHub Pages

1. Create a new GitHub repo (public).
2. Upload every file in this folder to the **root** of that repo (not a
   subfolder) — `index.html`, `manifest.json`, and the icon PNGs should all
   sit next to each other.
3. In the repo, go to **Settings → Pages**, set "Source" to the `main`
   branch, root folder, and save.
4. GitHub gives you a URL like `https://yourname.github.io/repo-name/`.
   Open that on your phone.

## Add it to your Home Screen

**iPhone (Safari):** open the URL → Share icon → "Add to Home Screen."
**Android (Chrome):** open the URL → ⋮ menu → "Add to Home screen" /
"Install app."

It'll launch full-screen with its own icon, no browser bar.

## Notes

- One tap per day: tapping the other button later the same day just changes
  today's entry instead of double-counting.
- `make_icons.py` is just the script used to generate the icon PNGs — not
  needed for the app to run, safe to delete or keep.
