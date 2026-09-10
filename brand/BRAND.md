# EZ AI Academy brand

The product brand is **locked**. Do not invent a new name, mark, palette, or tagline.

## Name

**EZ AI Academy**

Never write “Easy AI Academy” in learner-facing or public copy (README, `dist/`, adapter start phrases, acceptance prompts, commercial-readiness, GitHub Pages).

The canonical skill folder id remains `ai-academy` (`$ai-academy`, `/ai-academy`). Do not rename technical paths, git repo name, or progress schema to match the wordmark. Cursor checkout aliases `/ez-ai-academy` and `/start` are allowed; they must load the same root `SKILL.md` and must not fork curriculum.

## Message

| Role | Line |
|---|---|
| Primary | **Learn AI where you work.** |
| Supporting pillars | **WORK / LEARN / PROGRESS** |
| Secondary | Small steps. Bigger opportunities. |

The site is discovery and setup only. Teaching stays inside the harness.

## Color

| Token | Hex | Use |
|---|---|---|
| Navy | `#0B1730` | Primary brand, headlines, bubble outline, “EZ” / “Academy” |
| Cyan | `#72E0D1` | Energy, progress, staircase, “AI”, highlights |
| Dark Cyan | `#0B766D` | Buttons, deeper interactive accents |
| Paper | `#F5F8FB` | Light page background |
| White | `#FFFFFF` | Cards, contrast |
| Slate | `#4A5568` | Secondary text |

## Type

- **Inter** — UI, headlines, body. Bold for headlines; Regular for body; Medium for labels.
- **JetBrains Mono** — code, commands, copy-paste install blocks.

## Logo

Source files live in [`assets/`](assets/).

| File | Use |
|---|---|
| `logo-icon.png` / `logo-icon.svg` | Favicon, app icon, header mark |
| `logo-primary.png` | Horizontal lockup (icon + wordmark) |

The mark is a navy chat-bubble outline with a bottom-left tail and six cyan rounded squares in a **1-2-3** staircase (progress). Do not distort it, recolor it, or replace it with a lettermark.

On paper or navy UI, prefer the SVG icon plus an HTML wordmark (**EZ** navy, **AI** cyan, **Academy** navy). Dark-background PNGs match the presentation lockup.

Clear space: keep the mark simple and give it room. No heavy shadows or gradients on the logo.

`scripts/render-brand-logos.py` rebuilds the PNGs from this geometry if the rasters need regenerating. Do not generate a different symbol.

## Voice

Practical, clear, encouraging, progress-oriented. Jargon-free for nontechnical enterprise employees.

Do:

- Keep the mark simple and the navy/cyan palette consistent.
- Leave whitespace.
- Reuse the pixel staircase, rounded cards, and thin connector lines when a layout needs a motif.
- Stay honest about harness status (Pass / To run / parked).

Don’t:

- Write “Easy AI Academy” or “working name / brand still open.”
- Distort the icon or switch illustration styles.
- Clutter frames with shadows, gradients, or off-brand color.
- Put lessons, quizzes, or progress on the website.

## Pages landing

`dist/` is discovery and setup only. Favicon is `logo-icon.png`. Header uses the icon and wordmark. Asset paths stay relative so GitHub Pages at `/ez-ai-academy/` resolves them.
