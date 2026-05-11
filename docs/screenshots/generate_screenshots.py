#!/usr/bin/env python3
"""Generate demo screenshots using the Spring Bloom in Vancouver palette."""

from __future__ import annotations

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent

# Palette (same as theme)
BG = "#FDF8F5"
GUTTER_BG = "#F7F0EB"
LINE_HL = "#F1E6DF"
GUTTER_FG = "#B89888"
TEXT = "#2D1A0E"
MUTED = "#7A5A48"
KEYWORD = "#C4527A"
STRING = "#4A8C2A"
ESCAPE = "#5FAE35"
TYPE = "#3A8CC4"
FUNC = "#5C3A1E"
PARAM = "#7A5A48"
NUMBER = "#B07A10"
COMMENT = "#B8909A"
OP = "#C4608A"
TAG_PUNCT = "#B89888"

WIDTH = 1200
HEIGHT = 720
GUTTER_W = 56
PAD_X = 14
LINE_H = 28
FONT_SIZE = 17


def load_fonts(size: int) -> dict[str, ImageFont.FreeTypeFont | ImageFont.ImageFont]:
    fonts_dir = Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts"
    candidates = {
        "regular": ["consola.ttf", "cascadiamonospace.ttf", "lucon.ttf"],
        "bold": ["consolab.ttf", "CascadiaMono-Bold.ttf"],
        "italic": ["consolai.ttf", "CascadiaMono-Italic.ttf"],
        "bolditalic": ["consolaz.ttf", "CascadiaMono-BoldItalic.ttf"],
    }
    out: dict[str, ImageFont.FreeTypeFont | ImageFont.ImageFont] = {}
    for kind, names in candidates.items():
        path = next((fonts_dir / n for n in names if (fonts_dir / n).is_file()), None)
        if path:
            try:
                out[kind] = ImageFont.truetype(str(path), size)
                continue
            except OSError:
                pass
        out[kind] = ImageFont.load_default()
    return out


def pick_font(fonts: dict[str, ImageFont.ImageFont], bold: bool, italic: bool) -> ImageFont.ImageFont:
    if bold and italic:
        return fonts.get("bolditalic") or fonts["bold"]
    if bold:
        return fonts["bold"]
    if italic:
        return fonts["italic"]
    return fonts["regular"]


def text_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> float:
    if hasattr(draw, "textlength"):
        return float(draw.textlength(text, font=font))
    bbox = draw.textbbox((0, 0), text, font=font)
    return float(bbox[2] - bbox[0])


def draw_segments(
    draw: ImageDraw.ImageDraw,
    fonts: dict[str, ImageFont.ImageFont],
    x: float,
    y: float,
    segments: list[tuple[str, str, bool, bool]],
) -> None:
    cx = x
    for text, color, bold, italic in segments:
        font = pick_font(fonts, bold, italic)
        draw.text((cx, y), text, fill=color, font=font)
        cx += text_width(draw, text, font)


def editor_canvas(highlight_line: int | None, num_lines: int) -> Image.Image:
    im = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(im)
    draw.rectangle([0, 0, GUTTER_W - 1, HEIGHT - 1], fill=GUTTER_BG)
    fonts = load_fonts(FONT_SIZE)
    content_top = 48
    for i in range(num_lines):
        y = content_top + i * LINE_H
        if highlight_line is not None and i == highlight_line:
            draw.rectangle([GUTTER_W, y - 2, WIDTH - 1, y + LINE_H - 4], fill=LINE_HL)
        num = str(i + 1).rjust(3)
        fn = pick_font(fonts, False, False)
        tw = text_width(draw, num, fn)
        draw.text((GUTTER_W - PAD_X - tw, y), num, fill=GUTTER_FG, font=fn)
    return im


def typescript_shot() -> None:
    fonts = load_fonts(FONT_SIZE)
    lines: list[list[tuple[str, str, bool, bool]]] = [
        [
            ("import ", KEYWORD, True, False),
            ("{ ", TEXT, False, False),
            ("walkUnderCherries", FUNC, False, False),
            (" } ", TEXT, False, False),
            ("from ", KEYWORD, True, False),
            ('"', STRING, False, False),
            ("@spring/vancouver", TYPE, False, False),
            ('"', STRING, False, False),
            (";", TEXT, False, False),
        ],
        [],
        [
            ("export ", KEYWORD, True, False),
            ("async ", KEYWORD, True, False),
            ("function ", KEYWORD, True, False),
            ("petalCount", FUNC, False, False),
            ("(", TEXT, False, False),
            ("lane", PARAM, False, True),
            (": ", TEXT, False, False),
            ("string", TYPE, False, False),
            ("): ", TEXT, False, False),
            ("Promise", TYPE, False, False),
            ("<", OP, False, False),
            ("boolean", TYPE, False, False),
            ("> ", TEXT, False, False),
            ("{", TEXT, False, False),
        ],
        [
            ("  ", TEXT, False, False),
            ("const ", KEYWORD, True, False),
            ("depth ", TEXT, False, False),
            ("= ", OP, False, False),
            ("3", NUMBER, True, False),
            (";", TEXT, False, False),
            ("  ", TEXT, False, False),
            ("// canopy layers", COMMENT, False, True),
        ],
        [
            ("  ", TEXT, False, False),
            ("if ", KEYWORD, True, False),
            ("(", TEXT, False, False),
            ("lane", PARAM, False, True),
            (".", OP, False, False),
            ("length ", TEXT, False, False),
            ("=== ", OP, False, False),
            ("0", NUMBER, False, False),
            (") ", TEXT, False, False),
            ("return ", KEYWORD, True, False),
            ("false", KEYWORD, True, False),
            (";", TEXT, False, False),
        ],
        [
            ("  ", TEXT, False, False),
            ("return ", KEYWORD, True, False),
            ("lane", PARAM, False, True),
            (".", OP, False, False),
            ("includes", FUNC, False, False),
            ("(", TEXT, False, False),
            ('"', STRING, False, False),
            ("blossom", STRING, False, False),
            ('"', STRING, False, False),
            (");", TEXT, False, False),
        ],
        [
            ("}", TEXT, False, False),
        ],
    ]
    im = editor_canvas(highlight_line=3, num_lines=max(10, len(lines) + 2))
    draw = ImageDraw.Draw(im)
    content_top = 48
    x0 = float(GUTTER_W + PAD_X)
    for i, segs in enumerate(lines):
        if not segs:
            continue
        y = content_top + i * LINE_H
        draw_segments(draw, fonts, x0, float(y), segs)
    title = ImageFont.truetype(
        str(Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts" / "segoeui.ttf"), 13
    )
    try:
        draw.text((PAD_X, 14), "TypeScript — Spring Bloom in Vancouver", fill=MUTED, font=title)
    except OSError:
        draw.text((PAD_X, 14), "TypeScript — Spring Bloom in Vancouver", fill=MUTED)
    im.save(ROOT / "typescript.png", "PNG")


def markdown_shot() -> None:
    fonts = load_fonts(FONT_SIZE)
    lines: list[list[tuple[str, str, bool, bool]]] = [
        [
            ("# ", KEYWORD, False, False),
            ("West End stroll", TEXT, True, False),
        ],
        [
            ("Soft ", TEXT, False, False),
            ("*petals*", FUNC, False, True),
            (" and ", TEXT, False, False),
            ("**clear sky**", TEXT, True, False),
            (".", TEXT, False, False),
        ],
        [
            ("See ", TEXT, False, False),
            ("[season notes]", TYPE, False, False),
            ("(", TEXT, False, False),
            ("https://mrait.ca/spring-bloom", TYPE, False, False),
            (")", TEXT, False, False),
        ],
        [],
        [
            ("```", FUNC, False, False),
            ("ts", STRING, False, False),
        ],
        [
            ("const ", KEYWORD, True, False),
            ("season ", TEXT, False, False),
            ("= ", OP, False, False),
            ('"', STRING, False, False),
            ("spring", STRING, False, False),
            ('"', STRING, False, False),
            (";", TEXT, False, False),
        ],
        [
            ("```", FUNC, False, False),
        ],
    ]
    im = editor_canvas(highlight_line=None, num_lines=10)
    draw = ImageDraw.Draw(im)
    content_top = 48
    x0 = float(GUTTER_W + PAD_X)
    for i, segs in enumerate(lines):
        if not segs:
            continue
        y = content_top + i * LINE_H
        draw_segments(draw, fonts, x0, float(y), segs)
    try:
        title = ImageFont.truetype(
            str(Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts" / "segoeui.ttf"), 13
        )
        draw.text((PAD_X, 14), "Markdown — Spring Bloom in Vancouver", fill=MUTED, font=title)
    except OSError:
        draw.text((PAD_X, 14), "Markdown — Spring Bloom in Vancouver", fill=MUTED)
    im.save(ROOT / "markdown.png", "PNG")


def html_shot() -> None:
    fonts = load_fonts(FONT_SIZE)
    lines: list[list[tuple[str, str, bool, bool]]] = [
        [
            ("<!DOCTYPE ", KEYWORD, True, False),
            ("html", STRING, False, False),
            (">", TAG_PUNCT, False, False),
        ],
        [
            ("<", TAG_PUNCT, False, False),
            ("section", KEYWORD, False, False),
            (" ", TEXT, False, False),
            ("class", FUNC, False, False),
            ('="', TAG_PUNCT, False, False),
            ("canopy", STRING, False, False),
            ('"', TAG_PUNCT, False, False),
            (">", TAG_PUNCT, False, False),
        ],
        [
            ("  ", TEXT, False, False),
            ("<", TAG_PUNCT, False, False),
            ("p", KEYWORD, False, False),
            (" ", TEXT, False, False),
            ("id", FUNC, False, False),
            ('="', TAG_PUNCT, False, False),
            ("lane", STRING, False, False),
            ('"', TAG_PUNCT, False, False),
            (">", TAG_PUNCT, False, False),
            ("Cherry shade along Nelson.", TEXT, False, False),
            ("</", TAG_PUNCT, False, False),
            ("p", KEYWORD, False, False),
            (">", TAG_PUNCT, False, False),
        ],
        [
            ("</", TAG_PUNCT, False, False),
            ("section", KEYWORD, False, False),
            (">", TAG_PUNCT, False, False),
        ],
    ]
    im = editor_canvas(highlight_line=1, num_lines=8)
    draw = ImageDraw.Draw(im)
    content_top = 48
    x0 = float(GUTTER_W + PAD_X)
    for i, segs in enumerate(lines):
        y = content_top + i * LINE_H
        draw_segments(draw, fonts, x0, float(y), segs)
    try:
        title = ImageFont.truetype(
            str(Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts" / "segoeui.ttf"), 13
        )
        draw.text((PAD_X, 14), "HTML — Spring Bloom in Vancouver", fill=MUTED, font=title)
    except OSError:
        draw.text((PAD_X, 14), "HTML — Spring Bloom in Vancouver", fill=MUTED)
    im.save(ROOT / "html.png", "PNG")


def main() -> None:
    typescript_shot()
    markdown_shot()
    html_shot()
    print(f"Wrote PNGs to {ROOT}")


if __name__ == "__main__":
    main()
