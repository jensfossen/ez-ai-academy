#!/usr/bin/env python3
"""Render locked EZ AI Academy logo PNGs from the geometric mark.

The chat-bubble + 1-2-3 cyan staircase is the locked mark. This script
reconstructs it; it does not invent a new symbol.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


NAVY = (11, 23, 48, 255)
CYAN = (114, 224, 209, 255)
BLACK = (0, 0, 0, 255)
PAPER = (245, 248, 251, 255)

ROOT = Path(__file__).resolve().parents[1]
BRAND_ASSETS = ROOT / "brand" / "assets"
DIST_ASSETS = ROOT / "dist" / "assets"
INTER_BOLD = Path("/usr/share/fonts/truetype/macos/Inter-Bold.ttf")


def rounded_rect(draw: ImageDraw.ImageDraw, box, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def draw_mark(draw: ImageDraw.ImageDraw, origin, size, stroke, block, gap, fill_inside):
    """Draw the chat-bubble outline and 1-2-3 staircase into `draw`."""
    x, y = origin
    # Bubble body
    body = (x, y, x + size, y + int(size * 0.82))
    radius = int(size * 0.22)
    rounded_rect(draw, body, radius, fill=fill_inside, outline=NAVY, width=stroke)

    # Bottom-left tail (outline look: navy fill, then punch inner with fill_inside)
    tip = (x - int(size * 0.06), y + int(size * 1.02))
    left = (x + int(size * 0.10), y + int(size * 0.70))
    right = (x + int(size * 0.36), y + int(size * 0.78))
    draw.polygon([left, tip, right], fill=NAVY)
    # Inner tail cut so the bubble stays hollow
    inset = max(2, stroke // 2)
    inner_tip = (tip[0] + int(stroke * 0.55), tip[1] - int(stroke * 0.35))
    inner_left = (left[0] + inset, left[1] + inset // 2)
    inner_right = (right[0] - inset, right[1] - inset)
    draw.polygon([inner_left, inner_tip, inner_right], fill=fill_inside)

    # 1-2-3 cyan blocks, bottom-aligned inside the bubble
    inner_left_x = x + int(size * 0.22)
    inner_bottom = y + int(size * 0.70)
    cols = 3
    total_w = cols * block + (cols - 1) * gap
    start_x = x + (size - total_w) // 2
    heights = (1, 2, 3)
    for col, count in enumerate(heights):
        for row in range(count):
            bx = start_x + col * (block + gap)
            by = inner_bottom - (row + 1) * block - row * gap
            br = max(4, block // 5)
            rounded_rect(draw, (bx, by, bx + block, by + block), br, fill=CYAN)


def render_icon(path: Path, canvas=1024, background=BLACK):
    im = Image.new("RGBA", (canvas, canvas), background)
    draw = ImageDraw.Draw(im)
    size = int(canvas * 0.70)
    origin = ((canvas - size) // 2, int(canvas * 0.10))
    stroke = max(8, int(size * 0.11))
    block = int(size * 0.13)
    gap = max(4, int(block * 0.22))
    draw_mark(draw, origin, size, stroke, block, gap, fill_inside=background)
    path.parent.mkdir(parents=True, exist_ok=True)
    im.save(path, "PNG")
    return im


def render_primary(path: Path, canvas_h=720, background=BLACK):
    # Wide lockup: mark + Inter wordmark
    icon_box = int(canvas_h * 0.78)
    pad = int(canvas_h * 0.12)
    font_size = int(canvas_h * 0.22)
    font = ImageFont.truetype(str(INTER_BOLD), font_size)

    scratch = Image.new("RGBA", (8, 8), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(scratch)
    ez_w = sdraw.textlength("EZ ", font=font)
    ai_w = sdraw.textlength("AI ", font=font)
    ac_w = sdraw.textlength("Academy", font=font)
    text_w = ez_w + ai_w + ac_w

    gap = int(canvas_h * 0.10)
    width = pad + icon_box + gap + int(text_w) + pad
    im = Image.new("RGBA", (width, canvas_h), background)
    draw = ImageDraw.Draw(im)

    size = int(icon_box * 0.88)
    origin = (pad + (icon_box - size) // 2, (canvas_h - int(size * 1.02)) // 2)
    stroke = max(8, int(size * 0.11))
    block = int(size * 0.13)
    gap_b = max(4, int(block * 0.22))
    draw_mark(draw, origin, size, stroke, block, gap_b, fill_inside=background)

    text_x = pad + icon_box + gap
    bbox = font.getbbox("Academy")
    text_h = bbox[3] - bbox[1]
    text_y = (canvas_h - text_h) // 2 - bbox[1]
    draw.text((text_x, text_y), "EZ ", font=font, fill=NAVY)
    draw.text((text_x + ez_w, text_y), "AI ", font=font, fill=CYAN)
    draw.text((text_x + ez_w + ai_w, text_y), "Academy", font=font, fill=NAVY)

    path.parent.mkdir(parents=True, exist_ok=True)
    im.save(path, "PNG")
    return im


def main() -> None:
    icon = BRAND_ASSETS / "logo-icon.png"
    primary = BRAND_ASSETS / "logo-primary.png"
    render_icon(icon)
    render_primary(primary)
    DIST_ASSETS.mkdir(parents=True, exist_ok=True)
    Image.open(icon).save(DIST_ASSETS / "logo-icon.png", "PNG")
    Image.open(primary).save(DIST_ASSETS / "logo-primary.png", "PNG")
    print(f"Wrote {icon.relative_to(ROOT)} and {primary.relative_to(ROOT)}")
    print(f"Copied into {DIST_ASSETS.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
