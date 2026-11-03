# Tallyboard (public site)

The public site of Tallyboard: landing page, privacy policy and support page in 5 languages
(`en` at the root, `pl/`, `de/`, `es/`, `it/`). Published at `https://ideaapps.io/Tallyboard/` (GitHub Pages of `idea-apps/Tallyboard`).

Everything is generated; do not edit the HTML by hand.

```bash
python3 -m pip install Pillow
python3 tools/build.py                   # pages, stylesheet, icon, og image and screenshots
python3 tools/build.py --no-images       # only the pages and the stylesheet
python3 tools/build.py --shots <dir>     # screenshots from another folder (default ../judgebook-ios/fastlane/screenshots)
```

- Texts: `tools/content.py` (one dict per language, same structure). Bump `UPDATED` in `tools/build.py` when the privacy policy changes.
- Layout and styles: `tools/build.py` (the "Medal Pro" look of the app: paper, navy, rust). Fonts: `assets/fonts`.
- Screenshots come from the app repo: `fastlane/screenshots/<lang>/{iphone,ipad}-NN-*.png` and `fastlane/screenshots_mac/<lang>/NN-*.png` (made by `fastlane create_assets`). German, Spanish and Italian use the English Mac screenshots. Run the build again after new screenshots.
- The privacy policy must stay in step with the app (Firebase Analytics and Crashlytics, optional iCloud, tips) and the App Privacy answers in App Store Connect. The app also bundles its own short policy and terms (`Tallyboard/Resources/Legal`).
- `BASE` in `tools/build.py` sets canonical URLs; the App Store listing (`fastlane/metadata/*/support_url.txt`, `privacy_url.txt`, `marketing_url.txt` in judgebook-ios) points at the same addresses.
