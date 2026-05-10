#!/usr/bin/env python3
"""Generate 128x128 icon.png for Spring Bloom in Vancouver theme."""

from __future__ import annotations

import math
from pathlib import Path

try:
    from PIL import Image, ImageDraw
except ImportError:
    raise SystemExit("Install Pillow: pip install pillow") from None

SIZE = 128
BG = "#FDF8F5"
BRANCH = "#5C3A1E"
BLOSSOM_DEEP = "#C4527A"
BLOSSOM_SOFT = "#F2C4D4"


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "icon.png"

    im = Image.new("RGBA", (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(im)

    # Curved branch from lower-left toward upper-right
    points: list[tuple[float, float]] = []
    for t in range(0, 65):
        u = t / 64.0
        x = 8 + u * 95
        y = 100 - 55 * math.sin(u * math.pi * 0.85) - 15 * u
        points.append((x, y))
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        draw.line([(x0, y0), (x1, y1)], fill=BRANCH, width=5)

    # Small twigs
    draw.line([(55, 38), (68, 28)], fill=BRANCH, width=3)
    draw.line([(72, 52), (82, 42)], fill=BRANCH, width=3)

    def blossom(cx: float, cy: float, r: float, deep: bool) -> None:
        fill = BLOSSOM_DEEP if deep else BLOSSOM_SOFT
        for k in range(5):
            ang = k * 2 * math.pi / 5 - math.pi / 2
            ox = r * 0.55 * math.cos(ang)
            oy = r * 0.55 * math.sin(ang)
            draw.ellipse(
                [cx + ox - r, cy + oy - r, cx + ox + r, cy + oy + r],
                fill=fill,
                outline=BLOSSOM_DEEP if not deep else BLOSSOM_SOFT,
                width=1,
            )
        draw.ellipse([cx - r * 0.35, cy - r * 0.35, cx + r * 0.35, cy + r * 0.35], fill="#FDF8F5")

    blossom(78, 32, 11, True)
    blossom(62, 48, 9, False)
    blossom(88, 48, 8, True)
    blossom(48, 58, 7, False)
    blossom(95, 62, 6, False)

    im.save(out, "PNG")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
