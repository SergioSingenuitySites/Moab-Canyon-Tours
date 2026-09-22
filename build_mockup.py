from pathlib import Path
import re


ROOT = Path(__file__).parent
OUT = ROOT / "dist" / "index.html"
HERO = Path("/Users/sergiosanchez/.codex/generated_images/01a0cacc-da7a-70c2-83b2-b6a8ee0ab734/exec-f790470e-74a6-4127-8747-316adccd21bf.png")
CANYON = Path("/Users/sergiosanchez/.codex/generated_images/01a0cacc-da7a-70c2-83b2-b6a8ee0ab734/exec-04ce8d47-22d9-4d5c-8d61-fa459e28ba56.png")
CANONICAL = Path("/Users/sergiosanchez/Documents/Claude : Singenuity/outputs/automation-mockups/posh-pottery-franklin/index.html")


def data_uri(path: Path) -> str:
    import base64

    mime = "image/webp" if path.suffix.lower() == ".webp" else "image/png"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode("ascii")


def embedded_asset(class_name: str) -> str:
    html = CANONICAL.read_text(encoding="utf-8")
    match = re.search(rf'<img class="{re.escape(class_name)}" src="([^"]+)"', html)
    if not match:
        raise RuntimeError(f"Could not find canonical asset: {class_name}")
    return match.group(1)


TEMPLATE = r'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Concept landing page for Moab Canyon Tours with an interactive Singenuity booking popup demo.">
  <title>Moab Canyon Tours — Adventure, Made Personal</title>
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%2324211f'/%3E%3Cpath d='M14 48 29 17l6 13 5-9 10 27Z' fill='%23ef6035'/%3E%3Cpath d='M31 16c-6 11-8 21-3 32' fill='none' stroke='%23fff4e8' stroke-width='4' stroke-linecap='round'/%3E%3C/svg%3E">
  <style>
    :root {
      --ink: #211f1d;
      --ink-2: #302b27;
      --paper: #f6f0e6;
      --paper-2: #fffaf2;
      --orange: #ef6035;
      --orange-dark: #c94423;
      --sky: #b9d9e8;
      --blue: #175f7a;
      --sand: #d9b28d;
      --muted: #6e665f;
      --line: rgba(33,31,29,.14);
      --max: 1180px;
      --shadow: 0 28px 80px rgba(35, 24, 17, .18);
    }
    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0;
      color: var(--ink);
      background: var(--paper);
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      overflow-x: hidden;
    }
    body.modal-open { overflow: hidden; }
    a { color: inherit; text-decoration: none; }
    button, input, select { font: inherit; }
    button, a { -webkit-tap-highlight-color: transparent; }
    img { display: block; max-width: 100%; }
    .eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      text-transform: uppercase;
      letter-spacing: .16em;
      font-size: .78rem;
      font-weight: 900;
    }
    .eyebrow::before { content: ""; width: 30px; height: 2px; background: currentColor; }
    .nav-wrap {
      position: absolute;
      inset: 0 0 auto;
      z-index: 20;
      border-bottom: 1px solid rgba(255,255,255,.18);
      background: linear-gradient(180deg, rgba(18,17,16,.8), rgba(18,17,16,.15));
    }
    .nav {
      width: min(var(--max), calc(100% - 36px));
      height: 92px;
      margin: auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
      color: white;
    }
    .brand { display: flex; align-items: center; gap: 12px; min-width: 225px; }
    .brand-mark {
      width: 48px;
      height: 48px;
      border: 2px solid rgba(255,255,255,.8);
      border-radius: 50%;
      position: relative;
      flex: 0 0 48px;
    }
    .brand-mark::before {
      content: "";
      position: absolute;
      inset: 8px 16px 7px;
      border: 3px solid var(--orange);
      border-top: 0;
      border-radius: 0 0 12px 12px;
      transform: rotate(18deg);
    }
    .brand-mark::after {
      content: "";
      position: absolute;
      width: 7px;
      height: 7px;
      border: 3px solid var(--orange);
      border-radius: 50%;
      left: 17px;
      bottom: 6px;
    }
    .brand strong { display: block; font-size: 1.06rem; letter-spacing: .075em; line-height: 1; }
    .brand small { display: block; margin-top: 5px; color: rgba(255,255,255,.68); font-size: .71rem; letter-spacing: .12em; text-transform: uppercase; }
    .nav-links { display: flex; align-items: center; gap: 28px; font-size: .88rem; font-weight: 800; }
    .nav-links a { opacity: .86; }
    .nav-links a:hover { opacity: 1; color: #ff9b73; }
    .button {
      appearance: none;
      border: 0;
      border-radius: 3px;
      min-height: 50px;
      padding: 0 22px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      cursor: pointer;
      font-weight: 900;
      letter-spacing: .03em;
      transition: transform .2s ease, background .2s ease, color .2s ease;
    }
    .button:hover { transform: translateY(-2px); }
    .button.primary { background: var(--orange); color: white; box-shadow: 0 14px 34px rgba(239,96,53,.3); }
    .button.primary:hover { background: #ff7047; }
    .button.dark { background: var(--ink); color: white; }
    .button.light { background: white; color: var(--ink); border: 1px solid rgba(33,31,29,.12); }
    .button.outline { background: transparent; color: white; border: 1px solid rgba(255,255,255,.55); }
    .hero {
      min-height: 790px;
      display: flex;
      align-items: flex-end;
      position: relative;
      overflow: hidden;
      color: white;
      background-image:
        linear-gradient(90deg, rgba(16,14,13,.9) 0%, rgba(16,14,13,.63) 37%, rgba(16,14,13,.1) 68%),
        linear-gradient(0deg, rgba(16,14,13,.75) 0%, transparent 38%),
        url("__HERO__");
      background-size: cover;
      background-position: center;
    }
    .hero::after {
      content: "";
      position: absolute;
      right: -100px;
      bottom: -170px;
      width: 420px;
      height: 420px;
      border: 1px solid rgba(255,255,255,.22);
      border-radius: 50%;
      box-shadow: 0 0 0 70px rgba(255,255,255,.035), 0 0 0 140px rgba(255,255,255,.025);
    }
    .hero-inner {
      width: min(var(--max), calc(100% - 36px));
      margin: 0 auto;
      padding: 180px 0 86px;
      position: relative;
      z-index: 2;
      display: grid;
      grid-template-columns: minmax(0, 720px) 1fr;
      gap: 60px;
      align-items: end;
    }
    .hero h1 {
      margin: 24px 0 22px;
      max-width: 760px;
      font-family: Georgia, "Times New Roman", serif;
      font-size: clamp(4rem, 8.4vw, 8.4rem);
      font-weight: 500;
      letter-spacing: -.065em;
      line-height: .82;
    }
    .hero h1 em { color: #ff7549; font-style: italic; }
    .hero-copy { max-width: 610px; color: rgba(255,255,255,.82); font-size: 1.12rem; line-height: 1.62; }
    .hero-actions { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 30px; }
    .hero-note {
      align-self: end;
      justify-self: end;
      width: min(300px, 100%);
      padding: 22px;
      border-left: 3px solid var(--orange);
      background: rgba(20,18,17,.55);
      backdrop-filter: blur(12px);
    }
    .hero-note strong { display: block; font-family: Georgia, serif; font-size: 1.9rem; font-weight: 500; }
    .hero-note span { display: block; margin-top: 8px; color: rgba(255,255,255,.72); line-height: 1.5; }
    .proof-strip { background: var(--orange); color: white; }
    .proof-inner {
      width: min(var(--max), calc(100% - 36px));
      margin: auto;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
    }
    .proof-item { padding: 25px 26px; border-right: 1px solid rgba(255,255,255,.22); }
    .proof-item:first-child { border-left: 1px solid rgba(255,255,255,.22); }
    .proof-item strong { display: block; font-size: 1.2rem; }
    .proof-item span { display: block; margin-top: 4px; color: rgba(255,255,255,.74); font-size: .84rem; }
    .section { padding: 108px 18px; }
    .section-inner { width: min(var(--max), 100%); margin: auto; }
    .section-head {
      display: grid;
      grid-template-columns: minmax(0, 1.25fr) minmax(260px, .75fr);
      gap: 60px;
      align-items: end;
      margin-bottom: 46px;
    }
    .section-head h2 {
      margin: 16px 0 0;
      font-family: Georgia, "Times New Roman", serif;
      font-size: clamp(3rem, 6vw, 6rem);
      font-weight: 500;
      line-height: .93;
      letter-spacing: -.055em;
    }
    .section-head p { margin: 0; color: var(--muted); font-size: 1.05rem; line-height: 1.65; }
    .tour-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
    .tour-card {
      min-height: 430px;
      padding: 28px;
      border: 1px solid var(--line);
      background: var(--paper-2);
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
      transition: transform .25s ease, box-shadow .25s ease;
    }
    .tour-card:hover { transform: translateY(-7px); box-shadow: var(--shadow); }
    .tour-card::before {
      content: attr(data-number);
      position: absolute;
      right: 14px;
      top: 4px;
      font-family: Georgia, serif;
      font-size: 8rem;
      color: rgba(33,31,29,.045);
      line-height: 1;
    }
    .tour-card.featured { color: white; background: var(--ink); border-color: var(--ink); }
    .tour-card.featured::before { color: rgba(255,255,255,.06); }
    .tour-card .tag { align-self: flex-start; padding: 7px 9px; background: rgba(239,96,53,.12); color: var(--orange-dark); font-size: .72rem; font-weight: 900; text-transform: uppercase; letter-spacing: .1em; }
    .tour-card.featured .tag { color: #ff9a77; background: rgba(239,96,53,.13); }
    .tour-card h3 { margin: auto 0 14px; font-family: Georgia, serif; font-size: 2.35rem; font-weight: 500; line-height: .98; letter-spacing: -.035em; }
    .tour-card p { margin: 0; color: var(--muted); line-height: 1.56; }
    .tour-card.featured p { color: rgba(255,255,255,.68); }
    .tour-meta { display: flex; flex-wrap: wrap; gap: 7px; margin: 20px 0 24px; }
    .tour-meta span { padding: 7px 9px; border: 1px solid currentColor; opacity: .74; font-size: .74rem; font-weight: 800; }
    .card-link { display: flex; align-items: center; justify-content: space-between; border-top: 1px solid currentColor; padding-top: 17px; font-weight: 900; }
    .card-link span:last-child { font-size: 1.4rem; color: var(--orange); }
    .split {
      background: var(--ink);
      color: white;
      padding: 0 18px;
    }
    .split-inner { width: min(1380px, 100%); margin: auto; display: grid; grid-template-columns: 1fr 1fr; }
    .split-photo { min-height: 720px; background: url("__CANYON__") center/cover; }
    .split-copy { padding: clamp(70px, 9vw, 130px); display: flex; flex-direction: column; justify-content: center; }
    .split-copy h2 { margin: 18px 0 22px; font-family: Georgia, serif; font-size: clamp(3rem, 5.3vw, 5.7rem); font-weight: 500; line-height: .92; letter-spacing: -.055em; }
    .split-copy > p { color: rgba(255,255,255,.7); line-height: 1.68; font-size: 1.05rem; }
    .guide-points { display: grid; gap: 18px; margin-top: 28px; }
    .guide-point { display: grid; grid-template-columns: 46px 1fr; gap: 15px; align-items: start; }
    .guide-icon { width: 42px; height: 42px; border: 1px solid rgba(255,255,255,.3); border-radius: 50%; display: grid; place-items: center; color: #ff8b64; font-weight: 900; }
    .guide-point strong { display: block; }
    .guide-point span { display: block; margin-top: 4px; color: rgba(255,255,255,.6); line-height: 1.45; }
    .flow { background: #dfeaf0; }
    .flow-layout { display: grid; grid-template-columns: .78fr 1.22fr; gap: 74px; align-items: start; }
    .flow-copy { position: sticky; top: 34px; }
    .flow-copy h2 { margin: 18px 0; font-family: Georgia, serif; font-size: clamp(3rem, 5vw, 5.4rem); font-weight: 500; line-height: .92; letter-spacing: -.055em; }
    .flow-copy p { color: #4c626d; line-height: 1.65; }
    .steps-list { display: grid; }
    .flow-step { display: grid; grid-template-columns: 70px 1fr; gap: 24px; padding: 30px 0; border-top: 1px solid rgba(23,95,122,.22); }
    .flow-step:last-child { border-bottom: 1px solid rgba(23,95,122,.22); }
    .flow-step b { font-family: Georgia, serif; font-size: 2.2rem; color: var(--blue); }
    .flow-step h3 { margin: 0 0 8px; font-size: 1.2rem; }
    .flow-step p { margin: 0; color: #536770; line-height: 1.55; }
    .review-section { background: var(--paper-2); }
    .reviews { display: grid; grid-template-columns: 1.2fr .8fr; gap: 16px; }
    .review-main { padding: clamp(34px, 6vw, 76px); background: var(--orange); color: white; }
    .review-main .stars { letter-spacing: .2em; }
    .review-main blockquote { margin: 28px 0 34px; font-family: Georgia, serif; font-size: clamp(2.3rem, 4.8vw, 4.8rem); font-weight: 500; line-height: 1.02; letter-spacing: -.045em; }
    .review-main p { margin: 0; color: rgba(255,255,255,.78); line-height: 1.55; }
    .review-stats { padding: 44px; background: var(--ink); color: white; display: flex; flex-direction: column; justify-content: space-between; }
    .review-stats strong { display: block; font-family: Georgia, serif; font-size: 5.4rem; font-weight: 500; color: #ff8a63; line-height: 1; }
    .review-stats span { color: rgba(255,255,255,.62); line-height: 1.5; }
    .review-themes { display: grid; gap: 12px; margin-top: 34px; }
    .review-theme { padding: 15px 0; border-top: 1px solid rgba(255,255,255,.18); font-weight: 800; }
    .faq { display: grid; grid-template-columns: .75fr 1.25fr; gap: 70px; }
    .faq h2 { margin: 16px 0 0; font-family: Georgia, serif; font-size: clamp(3rem, 5vw, 5.2rem); font-weight: 500; line-height: .92; letter-spacing: -.05em; }
    .faq-list { border-top: 1px solid var(--line); }
    .faq-item { border-bottom: 1px solid var(--line); }
    .faq-q { width: 100%; padding: 24px 0; border: 0; background: transparent; display: flex; justify-content: space-between; gap: 20px; text-align: left; font-weight: 900; cursor: pointer; color: var(--ink); }
    .faq-q span:last-child { color: var(--orange); font-size: 1.3rem; transition: transform .2s ease; }
    .faq-a { max-height: 0; overflow: hidden; color: var(--muted); line-height: 1.65; transition: max-height .28s ease, padding .28s ease; }
    .faq-item.open .faq-a { max-height: 180px; padding: 0 0 24px; }
    .faq-item.open .faq-q span:last-child { transform: rotate(45deg); }
    .final-cta { padding: 0 18px 22px; background: var(--paper); }
    .final-inner {
      width: min(1380px, 100%);
      margin: auto;
      min-height: 520px;
      padding: clamp(44px, 7vw, 100px);
      position: relative;
      overflow: hidden;
      background:
        radial-gradient(circle at 83% 18%, rgba(255,255,255,.14), transparent 18rem),
        linear-gradient(135deg, #c94a28, #f16b3d 56%, #d95731);
      color: white;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: center;
    }
    .final-inner::after { content: "MOAB"; position: absolute; right: -25px; bottom: -48px; color: rgba(255,255,255,.09); font-family: Georgia, serif; font-size: clamp(8rem, 21vw, 21rem); line-height: .8; }
    .final-inner h2 { max-width: 850px; margin: 18px 0 28px; font-family: Georgia, serif; font-size: clamp(3.2rem, 7vw, 7rem); font-weight: 500; line-height: .9; letter-spacing: -.06em; position: relative; z-index: 1; }
    .final-inner .button { position: relative; z-index: 1; }
    footer { background: var(--ink); color: white; padding: 44px 18px; }
    .footer-inner { width: min(var(--max), 100%); margin: auto; display: flex; align-items: center; justify-content: space-between; gap: 24px; }
    .footer-inner small { color: rgba(255,255,255,.56); }
    .footer-links { display: flex; gap: 20px; font-size: .86rem; font-weight: 800; }

    .modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(10,12,14,.72);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 200;
      padding: 18px;
      backdrop-filter: blur(10px);
    }
    .modal-backdrop.open { display: flex; }
    .modal {
      width: min(1050px, 100%);
      max-height: min(760px, 94vh);
      overflow: auto;
      border-radius: 34px;
      background: #f8f2e8;
      box-shadow: 0 32px 110px rgba(0,0,0,.42);
      display: grid;
      grid-template-columns: .72fr 1.28fr;
      position: relative;
    }
    .modal-aside {
      background:
        linear-gradient(180deg, rgba(25,22,20,.10), rgba(25,22,20,.84)),
        url("__CANYON__") center/cover;
      color: white;
      padding: 30px;
      min-height: 620px;
      display: flex;
      flex-direction: column;
      justify-content: end;
    }
    .modal-aside h2 { font-family: Georgia, serif; font-size: clamp(2.2rem, 4vw, 4.1rem); line-height: .94; margin: 0; letter-spacing: -.055em; font-weight: 500; }
    .modal-aside p { font-weight: 700; line-height: 1.5; color: rgba(255,255,255,.82); }
    .modal-main { padding: 28px; }
    .modal-top { display: flex; justify-content: space-between; gap: 18px; align-items: flex-start; }
    .modal-top h3 { margin: 0; font-size: 1.74rem; letter-spacing: -.035em; }
    .modal-top p { margin: .35rem 0 0; color: var(--muted); font-weight: 700; }
    .close {
      width: 44px;
      height: 44px;
      min-width: 44px;
      flex: 0 0 44px;
      aspect-ratio: 1 / 1;
      border: 0;
      border-radius: 50%;
      background: #eaded2;
      color: var(--ink);
      font-size: 1.4rem;
      cursor: pointer;
      display: grid;
      place-items: center;
      line-height: 1;
    }
    .steps { display: flex; gap: 8px; margin: 18px 0 20px; }
    .steps span { flex: 1; height: 8px; border-radius: 999px; background: #e5d8cb; }
    .steps span:nth-child(-n+3) { background: linear-gradient(90deg, var(--orange), #ffb067); }
    .booking-options { display: grid; grid-template-columns: repeat(3, 1fr); gap: 9px; }
    .booking-options button { text-align: left; border: 1px solid rgba(33,31,29,.11); background: white; border-radius: 16px; padding: 13px; cursor: pointer; font-weight: 900; color: var(--ink); }
    .booking-options button.active { border-color: var(--orange); box-shadow: inset 0 0 0 2px rgba(239,96,53,.18); }
    .booking-options span { display: block; color: var(--muted); font-size: .78rem; margin-top: 3px; font-weight: 700; }
    .modal-fields { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin-top: 14px; }
    .field { border: 1px solid rgba(33,31,29,.1); border-radius: 15px; background: white; padding: 11px; }
    .field label { display: block; color: var(--muted); font-size: .75rem; font-weight: 900; margin-bottom: 6px; }
    .field input, .field select { width: 100%; border: 0; outline: 0; color: var(--ink); background: transparent; font-weight: 800; }
    .wide { grid-column: 1 / -1; }
    .insight { margin-top: 14px; border-radius: 18px; padding: 14px; background: #e9f3f6; border: 1px solid rgba(23,95,122,.16); color: #315d6c; font-weight: 750; line-height: 1.42; font-size: .9rem; }
    .insight strong { color: var(--blue); }
    .modal-actions { display: flex; align-items: center; gap: 10px; margin-top: 16px; flex-wrap: wrap; }
    .modal-actions .button { min-height: 46px; padding: 0 17px; font-size: .88rem; }
    .mode-panel { display: none; }
    .mode-panel.active { display: block; }
    .modal.singenuity-mode {
      background:
        radial-gradient(circle at 6% 8%, rgba(41,180,226,.24), transparent 19rem),
        radial-gradient(circle at 94% 22%, rgba(32,216,166,.18), transparent 21rem),
        #07141c;
      color: white;
    }
    .modal.singenuity-mode .modal-aside {
      background:
        radial-gradient(circle at 50% 19%, rgba(255,255,255,.94), rgba(255,255,255,.66) 9rem, transparent 14rem),
        linear-gradient(180deg, #ffffff 0%, #ffffff 22%, #dff4fb 34%, #0d2635 63%, #07141c 100%);
      justify-content: center;
      align-items: center;
      overflow: hidden;
      min-height: 620px;
      gap: 16px;
    }
    .singenuity-logo { width: min(78%, 390px); height: auto; object-fit: contain; filter: drop-shadow(0 10px 20px rgba(0,0,0,.12)); }
    .singenuity-device { width: min(112%, 580px); height: auto; object-fit: contain; filter: drop-shadow(0 28px 42px rgba(0,0,0,.42)); transform: translateX(-8px); }
    .singenuity-left-copy { width: min(94%, 460px); text-align: center; margin-top: -4px; }
    .singenuity-left-copy h2 { margin: 0; font-family: Inter, ui-sans-serif, system-ui, sans-serif; font-size: clamp(1.55rem, 3vw, 2.75rem); line-height: 1; letter-spacing: -.055em; font-weight: 850; }
    .modal.singenuity-mode .modal-main { color: white; background: linear-gradient(145deg, rgba(255,255,255,.08), rgba(255,255,255,.02)); display: flex; flex-direction: column; justify-content: center; padding: 34px; }
    .modal.singenuity-mode .close { background: rgba(255,255,255,.14); color: white; }
    .singenuity-headline { font-size: clamp(2.35rem, 4.45vw, 4.45rem) !important; line-height: .94; letter-spacing: -.06em; margin: 0; }
    .singenuity-copy { color: rgba(255,255,255,.76); font-weight: 750; line-height: 1.55; font-size: 1.08rem; margin: 18px 0 20px; }
    .singenuity-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; margin: 18px 0 20px; }
    .singenuity-card { border: 1px solid rgba(94,209,239,.34); background: linear-gradient(145deg, rgba(255,255,255,.98), rgba(235,249,255,.94)); border-radius: 21px; padding: 18px; box-shadow: 0 18px 36px rgba(0,0,0,.16), inset 0 1px 0 rgba(255,255,255,.8); }
    .singenuity-card strong { display: block; color: #0a3048; font-size: 1.04rem; }
    .singenuity-card p { margin: 6px 0 0; font-size: .92rem; line-height: 1.42; font-weight: 700; color: #41596b; }
    .text-sergio { display: inline-flex; align-items: center; justify-content: center; border-radius: 999px; padding: 14px 20px; background: linear-gradient(135deg,#2ab6f0,#65dce8); color: #062033; font-weight: 950; box-shadow: 0 18px 42px rgba(42,182,240,.26); }
    .ghost-action { border: 1px solid rgba(255,255,255,.16); background: rgba(255,255,255,.07); color: white; border-radius: 999px; padding: 13px 18px; font-weight: 900; cursor: pointer; }
    @media (max-width: 960px) {
      .nav-links { display: none; }
      .hero-inner { grid-template-columns: 1fr; }
      .hero-note { justify-self: start; }
      .tour-grid { grid-template-columns: 1fr; }
      .tour-card { min-height: 340px; }
      .split-inner, .flow-layout, .reviews, .faq, .modal { grid-template-columns: 1fr; }
      .split-photo { min-height: 560px; }
      .flow-copy { position: static; }
      .modal-aside { min-height: 300px; }
      .section-head { grid-template-columns: 1fr; gap: 22px; }
    }
    @media (max-width: 680px) {
      .nav { height: 78px; }
      .brand small { display: none; }
      .brand { min-width: 0; }
      .brand strong { font-size: .88rem; }
      .nav .button { min-height: 44px; padding: 0 15px; font-size: .82rem; }
      .hero { min-height: 740px; background-position: 58% center; }
      .hero-inner { padding-top: 140px; padding-bottom: 54px; }
      .hero h1 { font-size: clamp(3.8rem, 19vw, 6rem); }
      .hero-note { display: none; }
      .proof-inner { grid-template-columns: repeat(2, 1fr); }
      .proof-item { border-bottom: 1px solid rgba(255,255,255,.22); }
      .section { padding: 76px 18px; }
      .split { padding: 0; }
      .split-photo { min-height: 470px; }
      .split-copy { padding: 68px 24px; }
      .footer-inner { align-items: flex-start; flex-direction: column; }
      .booking-options, .modal-fields, .singenuity-grid { grid-template-columns: 1fr; }
      .wide { grid-column: auto; }
      .modal { max-height: 96vh; border-radius: 24px; }
      .modal-main { padding: 22px; }
      .modal.singenuity-mode .modal-aside { min-height: 420px; }
      .singenuity-device { width: min(88%, 430px); }
    }
    @media (prefers-reduced-motion: reduce) {
      html { scroll-behavior: auto; }
      *, *::before, *::after { transition-duration: .01ms !important; }
    }
  </style>
</head>
<body>
  <header class="nav-wrap">
    <nav class="nav" aria-label="Main navigation">
      <a class="brand" href="#top" aria-label="Moab Canyon Tours home">
        <span class="brand-mark" aria-hidden="true"></span>
        <span><strong>MOAB CANYON TOURS</strong><small>Private desert adventures</small></span>
      </a>
      <div class="nav-links">
        <a href="#adventures">Adventures</a>
        <a href="#guides">Why MCT</a>
        <a href="#reviews">Reviews</a>
        <a href="#planning">Plan Your Day</a>
      </div>
      <button class="button primary js-open-booking" type="button">Find a tour <span aria-hidden="true">↗</span></button>
    </nav>
  </header>

  <main id="top">
    <section class="hero" aria-labelledby="hero-title">
      <div class="hero-inner">
        <div>
          <span class="eyebrow">Private guided adventures · Moab, Utah</span>
          <h1 id="hero-title">Go beyond the <em>overlook.</em></h1>
          <p class="hero-copy">Rappel, climb, scramble, and hike into Moab’s hidden terrain with a private guide who matches the day to your crew.</p>
          <div class="hero-actions">
            <button class="button primary js-open-booking" type="button">Choose your adventure</button>
            <a class="button outline" href="#adventures">Explore tours</a>
          </div>
        </div>
        <aside class="hero-note" aria-label="Private tour highlight">
          <strong>Your canyon. Your pace.</strong>
          <span>Private departures built around your experience level, goals, and sense of adventure.</span>
        </aside>
      </div>
    </section>

    <section class="proof-strip" aria-label="Tour highlights">
      <div class="proof-inner">
        <div class="proof-item"><strong>Private tours</strong><span>Your group, your guide</span></div>
        <div class="proof-item"><strong>Ages 7+</strong><span>Beginner-friendly options</span></div>
        <div class="proof-item"><strong>Safety first</strong><span>Experienced local guides</span></div>
        <div class="proof-item"><strong>5-star favorite</strong><span>Hundreds of traveler reviews</span></div>
      </div>
    </section>

    <section class="section" id="adventures">
      <div class="section-inner">
        <div class="section-head">
          <div>
            <span class="eyebrow" style="color:var(--orange-dark)">Choose your line</span>
            <h2>Three ways into the wild.</h2>
          </div>
          <p>Start with the time you have and the kind of challenge you want. Every option includes a private guide and a route selected for the group.</p>
        </div>
        <div class="tour-grid">
          <article class="tour-card featured" data-number="01">
            <span class="tag">Best first canyon</span>
            <h3>Bow &amp; Arrow Canyon</h3>
            <p>A lively half-day introduction with hiking, scrambling, and a memorable rappel through classic Moab sandstone.</p>
            <div class="tour-meta"><span>From $169</span><span>4 hours</span><span>Ages 7+</span></div>
            <button class="card-link js-open-booking" type="button"><span>Check this tour</span><span>↗</span></button>
          </article>
          <article class="tour-card" data-number="02">
            <span class="tag">Mix it up</span>
            <h3>Cable Arch</h3>
            <p>Part canyon, part climb, and all fun — an active half day for guests who want variety without committing a full day.</p>
            <div class="tour-meta"><span>From $139</span><span>4 hours</span><span>Ages 7+</span></div>
            <button class="card-link js-open-booking" type="button"><span>Check this tour</span><span>↗</span></button>
          </article>
          <article class="tour-card" data-number="03">
            <span class="tag">Go farther</span>
            <h3>Irish Canyons</h3>
            <p>A full-day slot-canyon mission with remote terrain, deeper challenge, and the satisfaction of a true desert objective.</p>
            <div class="tour-meta"><span>From $349</span><span>7–12 hours</span><span>Ages 7+</span></div>
            <button class="card-link js-open-booking" type="button"><span>Check this tour</span><span>↗</span></button>
          </article>
        </div>
      </div>
    </section>

    <section class="split" id="guides">
      <div class="split-inner">
        <div class="split-photo" role="img" aria-label="A guide and two adult guests walking through a sculpted red-rock slot canyon"></div>
        <div class="split-copy">
          <span class="eyebrow" style="color:#ff8b64">Guided, not generic</span>
          <h2>Big adventure. Calm confidence.</h2>
          <p>You do not need prior rope experience to have an unforgettable day. A great guide makes the terrain feel approachable, teaches as you go, and keeps the focus on the experience.</p>
          <div class="guide-points">
            <div class="guide-point"><span class="guide-icon">01</span><div><strong>Matched to your crew</strong><span>Routes are chosen around fitness, comfort, age, and ambition.</span></div></div>
            <div class="guide-point"><span class="guide-icon">02</span><div><strong>Hands-on instruction</strong><span>Learn the movement, systems, and desert know-how behind the adventure.</span></div></div>
            <div class="guide-point"><span class="guide-icon">03</span><div><strong>Private by design</strong><span>Move at your pace without being folded into a large mixed group.</span></div></div>
          </div>
        </div>
      </div>
    </section>

    <section class="section flow" id="planning">
      <div class="section-inner flow-layout">
        <div class="flow-copy">
          <span class="eyebrow" style="color:var(--blue)">Book with clarity</span>
          <h2>Your day, mapped in minutes.</h2>
          <p>A cleaner online flow lets guests choose the right experience, see practical details, and reserve without bouncing between tour pages and a separate checkout.</p>
          <button class="button dark js-open-booking" type="button" style="margin-top:20px">Try the booking demo</button>
        </div>
        <div class="steps-list">
          <article class="flow-step"><b>01</b><div><h3>Choose your adventure</h3><p>Compare duration, price, minimum age, and challenge at a glance.</p></div></article>
          <article class="flow-step"><b>02</b><div><h3>Pick a date</h3><p>See a straightforward calendar and departure options for your group.</p></div></article>
          <article class="flow-step"><b>03</b><div><h3>Tell us about the crew</h3><p>Share guest count and experience level so the team can prepare well.</p></div></article>
          <article class="flow-step"><b>04</b><div><h3>Reserve with confidence</h3><p>Keep the booking experience visually connected to the adventure that inspired it.</p></div></article>
        </div>
      </div>
    </section>

    <section class="section review-section" id="reviews">
      <div class="section-inner">
        <div class="reviews">
          <div class="review-main">
            <div class="stars" aria-label="Five stars">★★★★★</div>
            <blockquote>“I felt safe, capable, and completely in the moment.”</blockquote>
            <p>That is the pattern across traveler feedback: patient guides, clear instruction, thoughtful pacing, and days people remember long after the ropes are packed.</p>
          </div>
          <aside class="review-stats">
            <div><strong>5.0</strong><span>Traveler rating on TripAdvisor, with more than 800 reviews.</span></div>
            <div class="review-themes">
              <div class="review-theme">First-timer friendly</div>
              <div class="review-theme">Safety-minded guides</div>
              <div class="review-theme">Private, personal days</div>
            </div>
          </aside>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="section-inner faq">
        <div><span class="eyebrow" style="color:var(--orange-dark)">Good to know</span><h2>Plan the adventure.</h2></div>
        <div class="faq-list">
          <div class="faq-item open"><button class="faq-q" type="button"><span>Do I need canyoneering experience?</span><span>+</span></button><div class="faq-a">No. Several half-day routes are designed for adventurous first-timers. Your guide handles the systems and teaches what you need along the way.</div></div>
          <div class="faq-item"><button class="faq-q" type="button"><span>Are these private tours?</span><span>+</span></button><div class="faq-a">Yes. The experience is built around your own party, which gives your group more flexibility and personal instruction.</div></div>
          <div class="faq-item"><button class="faq-q" type="button"><span>What should I bring?</span><span>+</span></button><div class="faq-a">Wear active layers and sturdy footwear, bring water and sun protection, and follow the specific packing guidance sent with your reservation.</div></div>
          <div class="faq-item"><button class="faq-q" type="button"><span>Which tour is right for my family?</span><span>+</span></button><div class="faq-a">Start with your youngest guest, available time, fitness, and comfort with heights. The booking flow can collect those details so the team can guide you to a strong fit.</div></div>
        </div>
      </div>
    </section>

    <section class="final-cta">
      <div class="final-inner">
        <span class="eyebrow">Ready when you are</span>
        <h2>Meet the Moab most visitors never see.</h2>
        <button class="button dark js-open-booking" type="button">Find your tour</button>
      </div>
    </section>
  </main>

  <footer>
    <div class="footer-inner">
      <div class="brand"><span class="brand-mark" aria-hidden="true"></span><span><strong>MOAB CANYON TOURS</strong><small>Concept website mockup</small></span></div>
      <div class="footer-links"><a href="tel:4352601822">(435) 260-1822</a><a href="mailto:info@moabcanyontours.com">Email</a></div>
      <small>Moab, Utah · Daily 7am–7pm</small>
    </div>
  </footer>

  <div class="modal-backdrop" id="bookingModal" aria-hidden="true" role="dialog" aria-modal="true" aria-label="Singenuity booking popup demo">
    <div class="modal" id="modalShell">
      <aside class="modal-aside">
        <div class="mode-panel active" data-panel="booking">
          <h2>From inspired to reserved — without leaving the moment.</h2>
          <p>A focused booking path keeps the adventure, group details, and next step in one connected experience.</p>
        </div>
        <div class="mode-panel" data-panel="singenuity">
          <img class="singenuity-logo" src="__SINGENUITY_LOGO__" alt="Singenuity">
          <img class="singenuity-device" src="__SINGENUITY_DEVICE__" alt="Singenuity running across point of sale, mobile, and operations screens">
          <div class="singenuity-left-copy"><h2>One simplified platform for booking, POS, waivers, memberships, gift cards, and more.</h2></div>
        </div>
      </aside>
      <section class="modal-main">
        <div class="mode-panel active" data-panel="booking">
          <div class="modal-top">
            <div><h3>Reserve a private adventure</h3><p>Start with the experience that fits your crew.</p></div>
            <button class="close js-close-booking" aria-label="Close booking popup" type="button">×</button>
          </div>
          <div class="steps" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
          <div class="booking-options">
            <button class="active" type="button">Bow &amp; Arrow <span>Beginner · 4 hours</span></button>
            <button type="button">Cable Arch <span>Mixed adventure · 4 hours</span></button>
            <button type="button">Irish Canyons <span>Full day · 7–12 hours</span></button>
          </div>
          <div class="modal-fields">
            <div class="field"><label for="date">Preferred date</label><select id="date"><option>Thursday, October 8</option><option>Friday, October 9</option><option>Saturday, October 10</option></select></div>
            <div class="field"><label for="departure">Departure</label><select id="departure"><option>8:00 AM</option><option>9:00 AM</option><option>Contact me about options</option></select></div>
            <div class="field"><label for="guests">Guests</label><select id="guests"><option>2 guests</option><option>3 guests</option><option>4 guests</option><option>5+ guests</option></select></div>
            <div class="field"><label for="level">Experience level</label><select id="level"><option>First time</option><option>Some climbing or rappelling</option><option>Experienced</option></select></div>
            <div class="field wide"><label for="notes">Anything we should know?</label><input id="notes" value="Two adults — excited, but new to rappelling"></div>
          </div>
          <div class="insight"><strong>Connected guest journey:</strong> The opportunity is not just taking bookings online. It is improving the guest flow, reducing abandoned intent, and giving the operator clearer visibility into which marketing efforts create revenue.</div>
          <div class="modal-actions">
            <a class="button primary" href="https://singenuity.com" target="_blank" rel="noopener">Visit Singenuity.com</a>
            <button class="button light js-show-singenuity" type="button">See how Singenuity helps</button>
          </div>
        </div>

        <div class="mode-panel" data-panel="singenuity">
          <div class="modal-top"><div><h3 class="singenuity-headline">Booking software that works like an operating system.</h3></div><button class="close js-close-booking" aria-label="Close booking popup" type="button">×</button></div>
          <p class="singenuity-copy">Singenuity helps experience businesses sell online, simplify operations, and see which marketing efforts actually turn into bookings.</p>
          <div class="singenuity-grid">
            <div class="singenuity-card"><strong>Better booking flow</strong><p>Guide guests to the right experience, date, capacity, add-ons, and checkout without making them hunt.</p></div>
            <div class="singenuity-card"><strong>POS + online together</strong><p>Online booking and in-person POS in one connected system instead of scattered tools.</p></div>
            <div class="singenuity-card"><strong>Complete guest toolkit</strong><p>Waivers, memberships, gift cards, staff tools, communication, mobile check-in, and reporting.</p></div>
            <div class="singenuity-card"><strong>Marketing that connects</strong><p>Follow the guest journey from ad click or email to completed booking and revenue.</p></div>
          </div>
          <div class="modal-actions"><a class="text-sergio" href="sms:+18018670934">Text Sergio</a><a class="ghost-action" href="https://www.climbworks.com/" target="_blank" rel="noopener">See Live Flow</a><button class="ghost-action js-show-booking" type="button">Back to booking demo</button></div>
        </div>
      </section>
    </div>
  </div>

  <script>
    const modal = document.getElementById('bookingModal');
    const modalShell = document.getElementById('modalShell');
    const openers = document.querySelectorAll('.js-open-booking');
    const closeButtons = document.querySelectorAll('.js-close-booking');
    const optionButtons = document.querySelectorAll('.booking-options button');
    const showSingenuityButtons = document.querySelectorAll('.js-show-singenuity');
    const showBookingButtons = document.querySelectorAll('.js-show-booking');
    let lastOpener = null;

    function showMode(mode) {
      document.querySelectorAll('.mode-panel').forEach(panel => panel.classList.toggle('active', panel.dataset.panel === mode));
      modalShell.classList.toggle('singenuity-mode', mode === 'singenuity');
      const close = modal.querySelector('.mode-panel.active .js-close-booking');
      if (close) close.focus();
    }
    function openBooking(event) {
      lastOpener = event.currentTarget;
      showMode('booking');
      modal.classList.add('open');
      modal.setAttribute('aria-hidden', 'false');
      document.body.classList.add('modal-open');
    }
    function closeBooking() {
      modal.classList.remove('open');
      modal.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('modal-open');
      if (lastOpener) lastOpener.focus();
    }
    openers.forEach(button => button.addEventListener('click', openBooking));
    closeButtons.forEach(button => button.addEventListener('click', closeBooking));
    showSingenuityButtons.forEach(button => button.addEventListener('click', () => showMode('singenuity')));
    showBookingButtons.forEach(button => button.addEventListener('click', () => showMode('booking')));
    modal.addEventListener('click', event => { if (event.target === modal) closeBooking(); });
    window.addEventListener('keydown', event => { if (event.key === 'Escape' && modal.classList.contains('open')) closeBooking(); });
    optionButtons.forEach(button => button.addEventListener('click', () => { optionButtons.forEach(item => item.classList.remove('active')); button.classList.add('active'); }));
    document.querySelectorAll('.faq-q').forEach(button => button.addEventListener('click', () => button.closest('.faq-item').classList.toggle('open')));
  </script>
</body>
</html>
'''


html = (TEMPLATE
        .replace("__HERO__", data_uri(HERO))
        .replace("__CANYON__", data_uri(CANYON))
        .replace("__SINGENUITY_LOGO__", embedded_asset("singenuity-logo"))
        .replace("__SINGENUITY_DEVICE__", embedded_asset("singenuity-device")))

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(html, encoding="utf-8")
print(OUT)
print(f"{OUT.stat().st_size / (1024 * 1024):.2f} MB")
