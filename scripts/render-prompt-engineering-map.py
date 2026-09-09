#!/usr/bin/env python3
"""Render the Module 2 Prompt Engineering explainer (SVG + compact PNG).

Chat-first, pixel-progress motif. Brand navy / cyan / paper. No robots or brains.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


NAVY = (11, 23, 48, 255)
CYAN = (114, 224, 209, 255)
PAPER = (245, 248, 251, 255)
WHITE = (255, 255, 255, 255)
SLATE = (74, 85, 104, 255)
AMBER = (196, 163, 90, 255)

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
NOTO_BOLD = Path("/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf")
NOTO_REG = Path("/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf")

STEPS = (
    ("1", "OUTCOME", "Name the useful result, who it is for, and what they will do next."),
    ("2", "INPUTS", "Give the information the job needs. Leave out decoration."),
    ("3", "BOUNDARIES", "Say what to include, avoid, or put first. Keep unknowns visible."),
    ("4", "SHAPE", "Choose a format the next person can actually use."),
    ("5", "CHECK", "Inspect the result. Improve the instruction from what you see."),
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


def draw_bubble(draw: ImageDraw.ImageDraw, x: int, y: int, size: int) -> None:
    body = (x, y, x + size, y + int(size * 0.72))
    draw.rounded_rectangle(body, radius=int(size * 0.22), outline=NAVY, width=max(3, size // 14))
    tip = (x + int(size * 0.08), y + int(size * 1.02))
    left = (x + int(size * 0.16), y + int(size * 0.64))
    right = (x + int(size * 0.42), y + int(size * 0.72))
    draw.polygon([left, tip, right], fill=NAVY)
    inset = max(2, size // 16)
    draw.polygon(
        [
            (left[0] + inset, left[1] + inset // 2),
            (tip[0] + inset, tip[1] - inset),
            (right[0] - inset, right[1] - inset),
        ],
        fill=PAPER,
    )
    block = max(5, size // 7)
    gap = max(2, block // 4)
    start_x = x + int(size * 0.28)
    bottom = y + int(size * 0.58)
    for col, count in enumerate((1, 2, 3)):
        for row in range(count):
            bx = start_x + col * (block + gap)
            by = bottom - (row + 1) * block - row * gap
            draw.rounded_rectangle((bx, by, bx + block, by + block), radius=2, fill=CYAN)


def render_png(path: Path) -> Image.Image:
    w, h = 900, 1200
    im = Image.new("RGBA", (w, h), PAPER)
    draw = ImageDraw.Draw(im)

    title_f = font(NOTO_BOLD, 36)
    sub_f = font(NOTO_REG, 20)
    step_f = font(NOTO_BOLD, 22)
    body_f = font(NOTO_REG, 18)
    num_f = font(NOTO_BOLD, 20)
    foot_f = font(NOTO_BOLD, 18)

    # Header
    draw.rectangle((0, 0, w, 168), fill=NAVY)
    draw_bubble(draw, 36, 28, 88)
    title = "PROMPT ENGINEERING"
    tw = draw.textlength(title, font=title_f)
    draw.text(((w - tw) / 2 + 28, 38), title, font=title_f, fill=WHITE)
    subtitle = "Direct AI toward useful work"
    sw = draw.textlength(subtitle, font=sub_f)
    draw.text(((w - sw) / 2 + 28, 92), subtitle, font=sub_f, fill=CYAN)
    draw.rectangle((72, 148, w - 72, 154), fill=AMBER)

    # Step cards
    top = 196
    card_h = 168
    gap = 18
    left, right = 40, w - 40
    for i, (num, name, blurb) in enumerate(STEPS):
        y = top + i * (card_h + gap)
        draw.rounded_rectangle((left, y, right, y + card_h), radius=18, fill=WHITE)
        draw.rounded_rectangle((left, y, right, y + card_h), radius=18, outline=(197, 208, 220, 255), width=2)
        cx, cy = left + 46, y + 44
        draw.ellipse((cx - 22, cy - 22, cx + 22, cy + 22), fill=CYAN)
        nw = draw.textlength(num, font=num_f)
        draw.text((cx - nw / 2, cy - 14), num, font=num_f, fill=NAVY)
        draw.text((left + 86, y + 26), name, font=step_f, fill=NAVY)
        lines = wrap(draw, blurb, body_f, right - left - 108)
        for li, line in enumerate(lines):
            draw.text((left + 86, y + 68 + li * 28), line, font=body_f, fill=SLATE)

    # Footer
    draw.rectangle((0, h - 92, w, h), fill=NAVY)
    footer = "Clear direction, then inspect the result — not a longer prompt."
    fw = draw.textlength(footer, font=foot_f)
    draw.text(((w - fw) / 2, h - 58), footer, font=foot_f, fill=WHITE)

    path.parent.mkdir(parents=True, exist_ok=True)
    rgb = im.convert("P", palette=Image.Palette.ADAPTIVE, colors=32)
    rgb.save(path, "PNG", optimize=True)
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
    <rect x="40" y="{y}" width="820" height="168" rx="18" fill="#FFFFFF" stroke="#C5D0DC" stroke-width="2"/>
    <circle cx="86" cy="{y + 44}" r="22" fill="#72E0D1"/>
    <text x="86" y="{y + 51}" text-anchor="middle" font-family="Inter, Noto Sans, sans-serif" font-size="20" font-weight="700" fill="#0B1730">{num}</text>
    <text x="126" y="{y + 48}" font-family="Inter, Noto Sans, sans-serif" font-size="22" font-weight="700" fill="#0B1730">{name}</text>
    <text y="{y + 86}" font-family="Inter, Noto Sans, sans-serif" font-size="18" fill="#4A5568">{''.join(tspans)}</text>
  </g>"""
        )
        y += 186

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 1200" role="img" aria-label="Prompt engineering map. Direct AI toward useful work. Outcome, inputs, boundaries, shape, then check.">
  <rect width="900" height="1200" fill="#F5F8FB"/>
  <rect width="900" height="168" fill="#0B1730"/>
  <rect x="36" y="28" width="88" height="64" rx="18" fill="none" stroke="#F5F8FB" stroke-width="6"/>
  <path d="M48 88 L40 118 L72 94" fill="none" stroke="#F5F8FB" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <g fill="#72E0D1">
    <rect x="58" y="68" width="10" height="10" rx="2"/>
    <rect x="72" y="68" width="10" height="10" rx="2"/>
    <rect x="72" y="54" width="10" height="10" rx="2"/>
    <rect x="86" y="68" width="10" height="10" rx="2"/>
    <rect x="86" y="54" width="10" height="10" rx="2"/>
    <rect x="86" y="40" width="10" height="10" rx="2"/>
  </g>
  <text x="500" y="72" text-anchor="middle" font-family="Inter, Noto Sans, sans-serif" font-size="36" font-weight="700" fill="#FFFFFF">PROMPT ENGINEERING</text>
  <text x="500" y="112" text-anchor="middle" font-family="Inter, Noto Sans, sans-serif" font-size="20" fill="#72E0D1">Direct AI toward useful work</text>
  <rect x="72" y="148" width="756" height="6" fill="#C4A35A"/>
{chr(10).join(steps_svg)}
  <rect y="1108" width="900" height="92" fill="#0B1730"/>
  <text x="450" y="1162" text-anchor="middle" font-family="Inter, Noto Sans, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">Clear direction, then inspect the result — not a longer prompt.</text>
</svg>
"""
    path.write_text(svg, encoding="utf-8")


def main() -> None:
    png = ASSETS / "prompt-engineering-map.png"
    svg = ASSETS / "prompt-engineering-map.svg"
    render_png(png)
    render_svg(svg)
    print(f"Wrote {svg.relative_to(ROOT)} ({svg.stat().st_size} bytes)")
    print(f"Wrote {png.relative_to(ROOT)} ({png.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
