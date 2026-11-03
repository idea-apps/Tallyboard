#!/usr/bin/env python3
"""Generates the Tallyboard site: en at the root, pl/ de/ es/ it/ in folders, plus assets.

    python3 tools/build.py                 # pages and stylesheet
    python3 tools/build.py --shots <dir>   # also icon, og image and screenshots (default: the app repo's fastlane/screenshots)
"""
import argparse
import html
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from content import APP_ID, LANGS  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
APP_REPO = ROOT.parent / "judgebook-ios"
BASE = "https://ideaapps.io/Tallyboard/"
STORE = f"https://apps.apple.com/app/id{APP_ID}"
UPDATED = {"en": "3 November 2026", "pl": "3 listopada 2026", "de": "3. November 2026", "es": "3 de noviembre de 2026", "it": "3 novembre 2026"}
UPDATED_LABEL = {"en": "Last updated", "pl": "Ostatnia aktualizacja", "de": "Zuletzt aktualisiert", "es": "Última actualización", "it": "Ultimo aggiornamento"}
APP_NAME_LINE = {"en": "Tallyboard app", "pl": "Aplikacja Tallyboard", "de": "App Tallyboard", "es": "App Tallyboard", "it": "App Tallyboard"}
ICONS = [
    "M12 3v3M5 7l2 2M19 7l-2 2M4 14a8 8 0 0116 0M12 14l3-4",
    "M3 7h7v6H3zM14 7h7v6h-7zM8 17h8M12 13v4",
    "M12 7v5l3 2M12 3a9 9 0 100 18 9 9 0 000-18z",
    "M4 6h16M4 12h16M4 18h10",
    "M5 20V10M12 20V4M19 20v-7",
    "M5 4v17M5 5h12l-2 4 2 4H5",
    "M6 3h9l4 4v14H6zM14 3v5h5M9 13h6M9 17h6",
    "M12 3l8 3v6c0 4.500-3.200 7.800-8 9-4.800-1.200-8-4.500-8-9V6zM9 12l2 2 4-4",
]
CSS = """:root{--bg:#F7F3EC;--bg2:#EFE7DA;--card:#fff;--line:#E4DDD0;--ink:#17203A;--soft:#4A5068;--mute:#6B6F80;--acc:#E4572E;--wash:#FFF3EE;--navy:#17203A}
@font-face{font-family:"Plus Jakarta Sans";font-weight:500;src:url(fonts/PlusJakartaSans-Medium.ttf)}
@font-face{font-family:"Plus Jakarta Sans";font-weight:700;src:url(fonts/PlusJakartaSans-Bold.ttf)}
@font-face{font-family:"Plus Jakarta Sans";font-weight:800;src:url(fonts/PlusJakartaSans-ExtraBold.ttf)}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:"Plus Jakarta Sans",-apple-system,BlinkMacSystemFont,"Helvetica Neue",Arial,sans-serif;font-size:17px;line-height:1.6;-webkit-text-size-adjust:100%;overflow-x:hidden}
body:before{content:"";position:fixed;inset:0;z-index:-1;background:radial-gradient(900px 600px at 90% -10%,rgba(228,87,46,.12),transparent 60%),linear-gradient(180deg,#FBF8F2 0,#F7F3EC 50%,#EFE7DA 100%)}
a{color:var(--acc)}img{max-width:100%;display:block}
.wrap{max-width:1120px;margin:0 auto;padding:0 22px}
nav.top{position:sticky;top:0;z-index:20;backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);background:rgba(247,243,236,.82);border-bottom:1px solid var(--line)}
nav.top .wrap{display:flex;align-items:center;gap:22px;height:64px}
.brand{display:flex;align-items:center;gap:10px;font-weight:800;font-size:20px;color:var(--ink);text-decoration:none;margin-right:auto}
.brand img{width:34px;height:34px;border-radius:9px}
nav.top a.l{color:var(--soft);text-decoration:none;font-weight:700;font-size:15px}nav.top a.l:hover{color:var(--ink)}
.btn{display:inline-flex;align-items:center;gap:10px;padding:15px 28px;border-radius:999px;background:var(--navy);color:#fff;font-weight:800;text-decoration:none;box-shadow:0 12px 28px -10px rgba(23,32,58,.6);transition:transform .2s}
.btn:hover{transform:translateY(-2px)}.btn.ghost{background:var(--card);color:var(--ink);box-shadow:none;border:1px solid var(--line)}
.btn svg{width:20px;height:20px}
.eyebrow{display:inline-flex;gap:8px;align-items:center;font-size:13px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--acc)}
.eyebrow:before{content:"";width:26px;height:4px;border-radius:2px;background:var(--acc)}
h1,h2,h3{line-height:1.12;margin:0;letter-spacing:-.02em;text-wrap:balance}
h1{font-size:clamp(38px,6.2vw,66px);font-weight:800}h1 em{font-style:normal;color:var(--acc)}
h2{font-size:clamp(28px,4.2vw,44px);font-weight:800}h3{font-size:20px;font-weight:800}
.lead{font-size:clamp(18px,2.2vw,21px);color:var(--soft);max-width:34em}
.hero{padding:72px 0 40px}.hero .wrap{display:grid;grid-template-columns:1.05fr .95fr;gap:40px;align-items:center}
.hero h1{margin:16px 0 22px}.hero .btns{display:flex;gap:14px;flex-wrap:wrap;margin:30px 0 18px}
.dev{color:var(--mute);font-weight:700;font-size:14px}
.shot{height:auto;border-radius:28px;border:1px solid var(--line);box-shadow:0 36px 70px -30px rgba(23,32,58,.45);background:var(--card)}
.phones{position:relative;height:640px}
.phones .shot{position:absolute;width:270px}
.phones .p1{left:48%;top:0;transform:rotate(5deg);animation:float 7s ease-in-out infinite}
.phones .p2{left:4%;top:70px;transform:rotate(-6deg) scale(.92);animation:float 8s ease-in-out -2s infinite}
@keyframes float{50%{translate:0 -14px}}
section{padding:90px 0}.head{max-width:720px;margin:0 auto 52px;text-align:center}.head p{color:var(--soft);font-size:19px;margin:16px 0 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:28px;padding:26px}
.step{display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center;margin:0 0 80px}.step:nth-child(even) .txt{order:2}
.num{display:inline-grid;place-items:center;width:46px;height:46px;border-radius:14px;background:var(--acc);color:#fff;font-weight:800;font-size:22px;margin-bottom:18px}
.step p{color:var(--soft);font-size:19px;margin:14px 0 0;max-width:28em}
.step .shot{width:300px;margin:0 auto;transform:rotate(-2deg);transition:transform .5s}.step:nth-child(even) .shot{transform:rotate(2deg)}.step .shot:hover{transform:none}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.feat{background:var(--card);border:1px solid var(--line);border-radius:26px;padding:24px;transition:transform .25s,border-color .25s}.feat:hover{transform:translateY(-4px);border-color:rgba(228,87,46,.5)}
.feat .ic{width:48px;height:48px;border-radius:15px;display:grid;place-items:center;margin-bottom:16px;background:var(--wash);color:var(--acc)}.feat .ic svg{width:26px;height:26px}
.feat p{color:var(--soft);margin:8px 0 0;font-size:15.5px}
.gallery{display:flex;gap:26px;overflow-x:auto;padding:10px 22px 40px;scroll-snap-type:x mandatory;justify-content:safe center}
.gallery figure{margin:0;flex:0 0 auto;scroll-snap-align:center;text-align:center}.gallery figcaption{margin-top:14px;font-weight:700;color:var(--soft)}
.gallery img{height:480px;width:auto;max-width:none}.gallery.dev img{height:400px}
.plans{display:grid;grid-template-columns:1fr 1fr;gap:20px;max-width:820px;margin:0 auto}
.plan{position:relative;background:var(--card);border:1px solid var(--line);border-radius:28px;padding:30px}.plan.pro{border-color:rgba(228,87,46,.6);background:var(--wash)}
.plan ul{list-style:none;padding:0;margin:18px 0 0}.plan li{padding:8px 0 8px 30px;position:relative;color:var(--soft)}
.plan li:before{content:"";position:absolute;left:0;top:15px;width:16px;height:8px;border-left:3px solid var(--acc);border-bottom:3px solid var(--acc);transform:rotate(-45deg) scale(.8)}
.badge{position:absolute;top:-13px;right:22px;background:var(--acc);color:#fff;font-weight:800;font-size:13px;padding:5px 14px;border-radius:999px}
.note{text-align:center;color:var(--mute);margin:26px 0 0}
.legal{display:flex;gap:18px;align-items:flex-start;max-width:820px;margin:0 auto}.legal svg{flex:0 0 34px;width:34px;color:var(--acc)}.legal p{margin:6px 0 0;color:var(--soft)}
.faq{max-width:760px;margin:0 auto}details{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:4px 20px;margin:0 0 12px}
summary{cursor:pointer;font-weight:700;padding:14px 0}details p{margin:0 0 16px;color:var(--soft)}
.cta{padding:30px 0 90px}.cta .box{text-align:center;background:var(--navy);color:#fff;border-radius:36px;padding:56px 22px}
.cta p{color:rgba(255,255,255,.75);font-size:19px;margin:12px 0 26px}.cta .btn{background:var(--acc);box-shadow:0 12px 28px -10px rgba(228,87,46,.7)}
footer{border-top:1px solid var(--line);padding:30px 0 40px;color:var(--mute);font-size:15px}footer .wrap{display:flex;gap:22px;flex-wrap:wrap;align-items:center}
footer a{color:var(--soft);text-decoration:none;font-weight:700}footer .sp{margin-left:auto;display:flex;gap:16px;flex-wrap:wrap}
.page{max-width:780px;margin:0 auto;padding:64px 22px 80px}.page h1{font-size:clamp(34px,5vw,52px)}.page h2{font-size:22px;margin:34px 0 8px}
.page p{color:var(--soft)}.sub{color:var(--mute)!important;margin:10px 0 24px}.short{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:18px 22px;color:var(--ink)!important}
.page .btns{display:flex;gap:14px;flex-wrap:wrap;margin-top:24px}
.reveal{opacity:0;transform:translateY(22px);transition:opacity .7s,transform .7s}.reveal.in{opacity:1;transform:none}
@media(max-width:860px){nav.top a.l{display:none}.hero .wrap,.step{grid-template-columns:1fr;gap:30px}.step:nth-child(even) .txt{order:0}.phones{height:560px}.phones .p1{left:40%}.grid{grid-template-columns:1fr 1fr}.plans{grid-template-columns:1fr}section{padding:60px 0}}
@media(max-width:520px){.grid{grid-template-columns:1fr}.phones .shot{width:220px}.phones .p2{left:0}.gallery img{height:420px}.gallery.dev img{height:300px}}
@media(prefers-reduced-motion:reduce){.phones .shot{animation:none}.reveal{opacity:1;transform:none;transition:none}}
"""
JS = """(function(){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12});document.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});})();
"""
DL_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v11M7 11l5 5 5-5M5 20h14"/></svg>'
MAIL_LINK_SKIP = None


def e(s):
    return html.escape(s, quote=True)


def svg(path):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="{path}"/></svg>'


def pre(L):
    return "" if L["code"] == "en" else "../"


def url(L, name):
    folder = "" if L["code"] == "en" else L["code"] + "/"
    return f"{BASE}{folder}{'' if name == 'index.html' else name}"


def shot(L, device, n, alt, cls="", width=None):
    d = L["mac"] if device == "mac" else L["shots"]
    dims = {"iphone": (660, 1434), "ipad": (900, 1200), "mac": (1400, 875)}[device]
    return (f'<img class="shot {cls}" src="{pre(L)}assets/shots/{d}-{device}-{n}.webp" alt="{e(alt)}" loading="lazy" '
            f'width="{dims[0]}" height="{dims[1]}">')


def head(L, name, title, desc):
    p = pre(L)
    alts = "".join(f'<link rel="alternate" hreflang="{M["code"]}" href="{url(M, name)}">' for M in LANGS)
    alts += f'<link rel="alternate" hreflang="x-default" href="{url(LANGS[0], name)}">'
    return f"""<!doctype html>
<html lang="{L['lang']}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#F7F3EC">
<meta name="apple-itunes-app" content="app-id={APP_ID}">
<link rel="canonical" href="{url(L, name)}">
{alts}
<meta property="og:type" content="website"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{BASE}assets/og.png"><meta property="og:url" content="{url(L, name)}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{p}assets/icon.png"><link rel="apple-touch-icon" href="{p}assets/icon.png">
<link rel="stylesheet" href="{p}assets/style.css">
</head>
<body>
"""


def nav(L):
    p = pre(L)
    n = L["nav"]
    links = (f'<a class="l" href="./#how">{n["how"]}</a><a class="l" href="./#features">{n["features"]}</a>'
             f'<a class="l" href="./#devices">{n["devices"]}</a>')
    return (f'<nav class="top"><div class="wrap"><a class="brand" href="./"><img src="{p}assets/icon.png" alt="" width="34" height="34">Tallyboard</a>'
            f'{links}<a class="l" href="support.html">{n["support"]}</a>'
            f'<a class="btn" style="padding:10px 20px" href="{STORE}">{n["download"]}</a></div></nav>\n')


def footer(L, name):
    n = L["nav"]
    here = L["code"]
    links = []
    for M in LANGS:
        if M["code"] == here:
            href = "./" if name == "index.html" else name
        else:
            href = (pre(L) + ("" if M["code"] == "en" else M["code"] + "/")) + ("" if name == "index.html" else name)
            href = href or "./"
        links.append(f'<a href="{href}" hreflang="{M["code"]}">{M["label"]}</a>')
    return (f'<footer><div class="wrap"><span>Tallyboard · IdeaApps</span><a href="privacy.html">{n["privacy"]}</a>'
            f'<a href="support.html">{n["support"]}</a><span class="sp">{"".join(links)}</span></div></footer>\n'
            f'<script src="{pre(L)}assets/app.js" defer></script>\n</body></html>\n')


def index_page(L):
    t = L["idx"]
    n = L["nav"]
    out = [head(L, "index.html", t["title"], t["desc"]), nav(L)]
    out.append(f'<header class="hero"><div class="wrap"><div><span class="eyebrow">{t["eyebrow"]}</span><h1>{t["h1"]}</h1>'
               f'<p class="lead">{t["lead"]}</p><div class="btns"><a class="btn" href="{STORE}">{DL_SVG}{n["store"]}</a>'
               f'<a class="btn ghost" href="#how">{t["see"]}</a></div><span class="dev">{t["devices"]}</span></div>'
               f'<div class="phones">{shot(L, "iphone", "01", t["shots"][0], "p2")}{shot(L, "iphone", "03", t["shots"][2], "p1")}</div></div></header>')
    out.append(f'<section id="how"><div class="wrap"><div class="head reveal"><h2>{t["how"]}</h2></div>')
    step_shots = [("06", 5), ("02", 1), ("03", 2)]
    for i, (h, p) in enumerate(t["steps"]):
        n_, si = step_shots[i]
        out.append(f'<div class="step reveal"><div class="txt"><span class="num">{i + 1}</span><h2 style="font-size:clamp(26px,3.6vw,38px)">{h}</h2><p>{p}</p></div>'
                   f'<div>{shot(L, "iphone", n_, t["shots"][si])}</div></div>')
    out.append('</div></section>')
    out.append(f'<section id="features"><div class="wrap"><div class="head reveal"><h2>{t["featuresH"]}</h2></div><div class="grid">')
    for i, (h, p) in enumerate(t["feats"]):
        out.append(f'<div class="feat reveal"><div class="ic">{svg(ICONS[i])}</div><h3>{h}</h3><p>{p}</p></div>')
    out.append('</div></div></section>')
    out.append(f'<section id="devices" style="padding-top:20px"><div class="wrap"><div class="head reveal"><h2>{t["devicesH"]}</h2><p>{t["devicesP"]}</p></div></div><div class="gallery dev">')
    for device, n_, label in [("mac", "01", "Mac"), ("ipad", "03", "iPad"), ("iphone", "02", "iPhone"), ("mac", "03", "Mac")]:
        out.append(f'<figure>{shot(L, device, n_, label + " · Tallyboard")}<figcaption>{label}</figcaption></figure>')
    out.append('</div></section>')
    out.append(f'<section style="padding-top:20px"><div class="head reveal"><h2>{t["galleryH"]}</h2></div><div class="gallery">')
    for i, cap in enumerate(t["shots"]):
        out.append(f'<figure>{shot(L, "iphone", f"{i + 1:02d}", cap)}<figcaption>{cap}</figcaption></figure>')
    out.append('</div></section>')
    fh, fl = t["free"]
    gh, gb, gl = t["tips"]
    out.append(f'<section id="pricing"><div class="wrap"><div class="head reveal"><h2>{t["tipsH"]}</h2><p>{t["tipsP"]}</p></div>'
               f'<div class="plans reveal"><div class="plan"><h3>{fh}</h3><ul>{"".join(f"<li>{x}</li>" for x in fl)}</ul></div>'
               f'<div class="plan pro"><span class="badge">{gb}</span><h3>{gh}</h3><ul>{"".join(f"<li>{x}</li>" for x in gl)}</ul></div></div>'
               f'<p class="note">{t["tipsNote"]}</p></div></section>')
    lh, lp = t["legal"]
    out.append(f'<section style="padding:20px 0 60px"><div class="wrap"><div class="card legal reveal">{svg("M12 3l9 16H3zM12 10v4M12 17h.01")}'
               f'<div><h3>{lh}</h3><p>{lp}</p></div></div></div></section>')
    out.append(f'<section style="padding-top:20px"><div class="wrap"><div class="head reveal"><h2>{t["faqH"]}</h2></div><div class="faq reveal">'
               + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"]) + '</div></div></section>')
    out.append(f'<div class="cta"><div class="wrap"><div class="box reveal"><h2>{t["ctaH"]}</h2><p>{t["ctaP"]}</p>'
               f'<a class="btn" href="{STORE}">{DL_SVG}{n["store"]}</a></div></div></div>')
    out.append(footer(L, "index.html"))
    return "".join(out)


def privacy_page(L):
    t = L["privacy"]
    from content import MAIL
    body = "".join(f"<h2>{h}</h2><p>{p.format(mail=MAIL)}</p>" for h, p in t["secs"])
    return (head(L, "privacy.html", f'{t["title"]} · Tallyboard', t["desc"]) + nav(L)
            + f'<main class="page"><h1>{t["title"]}</h1><p class="sub">{APP_NAME_LINE[L["code"]]}. {UPDATED_LABEL[L["code"]]}: {UPDATED[L["code"]]}</p>'
              f'<p class="short">{t["short"]}</p>{body}</main>' + footer(L, "privacy.html"))


def support_page(L):
    t = L["support"]
    from content import MAIL
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"])
    return (head(L, "support.html", f'{t["title"]} · Tallyboard', t["desc"]) + nav(L)
            + f'<main class="page"><h1>{t["title"]}</h1><p class="sub">{APP_NAME_LINE[L["code"]]}</p><p class="short">{t["short"]}</p>'
              f'<div class="btns"><a class="btn" href="mailto:{MAIL}">{t["mail"]}</a></div>'
              f'<div style="margin-top:34px">{faq}</div><p class="sub" style="margin-top:30px">{t["note"]}</p></main>'
            + footer(L, "support.html"))


def make_images(shots_root):
    from PIL import Image, ImageDraw, ImageFont
    sdir = ROOT / "assets" / "shots"
    sdir.mkdir(parents=True, exist_ok=True)
    root = Path(shots_root)
    mac_root = root.parent / (root.name + "_mac")
    done = set()
    for L in LANGS:
        for dirname, device in ((L["shots"], "iphone"), (L["shots"], "ipad"), (L["mac"], "mac")):
            if (dirname, device) in done:
                continue
            done.add((dirname, device))
            folder = (mac_root if device == "mac" else root) / dirname
            width = {"iphone": 660, "ipad": 900, "mac": 1400}[device]
            for src in sorted(folder.glob("*.png")):
                if device != "mac" and not src.name.startswith(device):
                    continue
                n = src.name.split("-")[1] if device != "mac" else src.name.split("-")[0]
                im = Image.open(src).convert("RGB")
                im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
                im.save(sdir / f"{dirname}-{device}-{n}.webp", "WEBP", quality=84, method=6)
    icon = Image.open(APP_REPO / "Tallyboard/Resources/Assets.xcassets/AppIcon.appiconset/icon-1024.png").convert("RGB")
    icon.resize((256, 256), Image.LANCZOS).save(ROOT / "assets" / "icon.png")
    og = Image.new("RGB", (1200, 630), "#F7F3EC")
    d = ImageDraw.Draw(og)
    for y in range(630):
        k = y / 630
        d.line([(0, y), (1200, y)], fill=(int(251 * (1 - k) + 239 * k), int(248 * (1 - k) + 231 * k), int(242 * (1 - k) + 218 * k)))
    og.paste(icon.resize((200, 200), Image.LANCZOS), (80, 110))
    big = ImageFont.truetype(str(ROOT / "assets/fonts/PlusJakartaSans-ExtraBold.ttf"), 92)
    small = ImageFont.truetype(str(ROOT / "assets/fonts/PlusJakartaSans-Bold.ttf"), 36)
    d.text((310, 130), "Tallyboard", font=big, fill="#17203A")
    d.text((310, 250), "Scoring for amateur contests", font=small, fill="#E4572E")
    d.text((310, 305), "iPhone · iPad · Mac", font=small, fill="#6B6F80")
    ph = Image.open(sdir / "en-US-iphone-03.webp").convert("RGB")
    ph = ph.resize((330, round(ph.height * 330 / ph.width)))
    og.paste(ph, (830, 60))
    og.save(ROOT / "assets" / "og.png", optimize=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default=str(APP_REPO / "fastlane/screenshots"))
    ap.add_argument("--no-images", action="store_true")
    args = ap.parse_args()
    (ROOT / "assets").mkdir(exist_ok=True)
    if not args.no_images:
        make_images(args.shots)
    (ROOT / "assets" / "style.css").write_text(CSS)
    (ROOT / "assets" / "app.js").write_text(JS)
    (ROOT / ".nojekyll").write_text("")
    for L in LANGS:
        d = ROOT if L["code"] == "en" else ROOT / L["code"]
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(index_page(L))
        (d / "privacy.html").write_text(privacy_page(L))
        (d / "support.html").write_text(support_page(L))
    print("ok")


if __name__ == "__main__":
    main()
