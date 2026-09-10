#!/usr/bin/env python3
"""Render the Module 4 Agents and Harness Engineering explainer (SVG + compact PNG).

Locked kit only: navy, cyan, dark cyan, paper, white, slate.
Official mark only: navy chat-bubble outline + cyan 1-2-3 pixel staircase.
No gold, no lightning, no invented symbols.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


NAVY = (11, 23, 48, 255)
CYAN = (114, 224, 209, 255)
DARK_CYAN = (11, 118, 109, 255)
PAPER = (245, 248, 251, 255)
WHITE = (255, 255, 255, 255)
SLATE = (74, 85, 104, 255)

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
BRAND_ICON = ROOT / "brand" / "assets" / "logo-icon.png"
NOTO_BOLD = Path("/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf")
NOTO_REG = Path("/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf")

STEPS = (
    ("1", "AGENT", "A goal-seeking helper that can take steps — not only answer one question."),
    ("2", "HARNESS", "The workplace setup around the model. A chat box with no tools is still a harness."),
    ("3", "TOOLS", "Give only the tools and permissions the job needs. More access is not safer."),
    ("4", "RULES", "Must-follow limits that stay on. Not the same as this request’s wording."),
    ("5", "NOTICE", "Check memory, files, and how you talk to it. If the result is weak, inspect the setup."),
)


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, max_w: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = word if not current else f"{current} {word}"
        if draw.textlength(trial, font=fnt) <= max_w:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def render_png(path: Path) -> Image.Image:
    w, h = 900, 1200
    im = Image.new("RGBA", (w, h), PAPER)
    draw = ImageDraw.Draw(im)

    title_f = font(NOTO_BOLD, 34)
    sub_f = font(NOTO_REG, 20)
    step_f = font(NOTO_BOLD, 22)
    body_f = font(NOTO_REG, 18)
    num_f = font(NOTO_BOLD, 20)
    foot_f = font(NOTO_BOLD, 16)

    draw.rectangle((0, 0, w, 168), fill=NAVY)

    chip_box = (28, 28, 140, 140)
    draw.rounded_rectangle(chip_box, radius=20, fill=PAPER)
    mark = Image.open(BRAND_ICON).convert("RGBA")
    mark.thumbnail((100, 100), Image.Resampling.LANCZOS)
    chip = Image.new("RGBA", (112, 112), (0, 0, 0, 0))
    chip.paste(mark, ((112 - mark.width) // 2, (112 - mark.height) // 2), mark)
    im.paste(chip, (28, 28), chip)

    title = "AGENTS AND HARNESS"
    draw.text((168, 48), title, font=title_f, fill=WHITE)
    draw.text((168, 98), "Shape the setup around a goal-seeking helper", font=sub_f, fill=CYAN)
    draw.rectangle((168, 142, w - 40, 148), fill=CYAN)

    top = 196
    card_h = 168
    gap = 18
    left, right = 40, w - 40
    for i, (num, name, blurb) in enumerate(STEPS):
        y = top + i * (card_h + gap)
        draw.rounded_rectangle((left, y, right, y + card_h), radius=18, fill=WHITE)
        draw.rounded_rectangle((left, y, right, y + card_h), radius=18, outline=DARK_CYAN, width=2)
        cx, cy = left + 46, y + 44
        draw.ellipse((cx - 22, cy - 22, cx + 22, cy + 22), fill=CYAN)
        nw = draw.textlength(num, font=num_f)
        draw.text((cx - nw / 2, cy - 14), num, font=num_f, fill=NAVY)
        draw.text((left + 86, y + 26), name, font=step_f, fill=NAVY)
        for li, line in enumerate(wrap(draw, blurb, body_f, right - left - 108)):
            draw.text((left + 86, y + 68 + li * 28), line, font=body_f, fill=SLATE)

    draw.rectangle((0, h - 92, w, h), fill=NAVY)
    footer = "Name the helper, shape the setup, notice when the setup caused the miss."
    fw = draw.textlength(footer, font=foot_f)
    draw.text(((w - fw) / 2, h - 58), footer, font=foot_f, fill=WHITE)

    path.parent.mkdir(parents=True, exist_ok=True)
    im.convert("P", palette=Image.Palette.ADAPTIVE, colors=16).save(path, "PNG", optimize=True)
    return im


def wrap_svg_lines(text: str, width: int = 58) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = word if not current else f"{current} {word}"
        if len(trial) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def official_mark_svg(ox: float, oy: float, view: float) -> str:
    s = view / 256.0
    return f"""  <g transform="translate({ox},{oy}) scale({s:.4f})">
    <rect x="36" y="28" width="184" height="152" rx="40" fill="none" stroke="#0B1730" stroke-width="22"/>
    <path d="M58 168 L28 232 L104 180" fill="none" stroke="#0B1730" stroke-width="22" stroke-linejoin="round" stroke-linecap="round"/>
    <g fill="#72E0D1">
      <rect x="86" y="128" width="22" height="22" rx="5"/>
      <rect x="117" y="128" width="22" height="22" rx="5"/>
      <rect x="117" y="97" width="22" height="22" rx="5"/>
      <rect x="148" y="128" width="22" height="22" rx="5"/>
      <rect x="148" y="97" width="22" height="22" rx="5"/>
      <rect x="148" y="66" width="22" height="22" rx="5"/>
    </g>
  </g>"""


def render_svg(path: Path) -> None:
    steps_svg = []
    y = 196
    for num, name, blurb in STEPS:
        lines = wrap_svg_lines(blurb)
        tspans = []
        for i, line in enumerate(lines):
            dy = 0 if i == 0 else 28
            tspans.append(f'<tspan x="126" dy="{dy}">{line}</tspan>')
        steps_svg.append(
            f"""  <g>
    <rect x="40" y="{y}" width="820" height="168" rx="18" fill="#FFFFFF" stroke="#0B766D" stroke-width="2"/>
    <circle cx="86" cy="{y + 44}" r="22" fill="#72E0D1"/>
    <text x="86" y="{y + 51}" text-anchor="middle" font-family="Inter, Noto Sans, sans-serif" font-size="20" font-weight="700" fill="#0B1730">{num}</text>
    <text x="126" y="{y + 48}" font-family="Inter, Noto Sans, sans-serif" font-size="22" font-weight="700" fill="#0B1730">{name}</text>
    <text y="{y + 86}" font-family="Inter, Noto Sans, sans-serif" font-size="18" fill="#4A5568">{''.join(tspans)}</text>
  </g>"""
        )
        y += 186

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 1200" role="img" aria-label="Agents and harness map. Shape the setup around a goal-seeking helper. Agent, harness, tools, rules, then notice.">
  <rect width="900" height="1200" fill="#F5F8FB"/>
  <rect width="900" height="168" fill="#0B1730"/>
  <rect x="28" y="28" width="112" height="112" rx="20" fill="#F5F8FB"/>
{official_mark_svg(30, 22, 116)}
  <text x="168" y="78" font-family="Inter, Noto Sans, sans-serif" font-size="34" font-weight="700" fill="#FFFFFF">AGENTS AND HARNESS</text>
  <text x="168" y="118" font-family="Inter, Noto Sans, sans-serif" font-size="20" fill="#72E0D1">Shape the setup around a goal-seeking helper</text>
  <rect x="168" y="142" width="692" height="6" fill="#72E0D1"/>
{chr(10).join(steps_svg)}
  <rect y="1108" width="900" height="92" fill="#0B1730"/>
  <text x="450" y="1162" text-anchor="middle" font-family="Inter, Noto Sans, sans-serif" font-size="16" font-weight="700" fill="#FFFFFF">Name the helper, shape the setup, notice when the setup caused the miss.</text>
</svg>
"""
    path.write_text(svg, encoding="utf-8")


def main() -> None:
    png = ASSETS / "agents-harness-engineering-map.png"
    svg = ASSETS / "agents-harness-engineering-map.svg"
    render_png(png)
    render_svg(svg)
    print(f"Wrote {svg.relative_to(ROOT)} ({svg.stat().st_size} bytes)")
    print(f"Wrote {png.relative_to(ROOT)} ({png.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
