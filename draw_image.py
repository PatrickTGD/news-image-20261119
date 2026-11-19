#!/usr/bin/env python3
"""Draw the 'Day in One Picture' front page for Thursday, November 19, 2026.

Original vector-style artwork drawn with Pillow only -- no copied photos,
artwork or characters. Output: entry.png (1024x1024) next to this script.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math

W = H = 1024
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

INK = (20, 24, 31)
PAPER = (247, 243, 234)
NAVY = (18, 32, 54)
RED = (179, 35, 42)
WHITE = (255, 255, 255)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def font(path, size):
    return ImageFont.truetype(path, size)


def fit(text, path, max_w, start, min_size=14):
    """Largest font size <= start that fits text in max_w."""
    s = start
    while s > min_size:
        f = font(path, s)
        if d.textlength(text, font=f) <= max_w:
            return f
        s -= 2
    return font(path, min_size)


def center(text, cx, y, f, fill=INK):
    w = d.textlength(text, font=f)
    d.text((cx - w / 2, y), text, font=f, fill=fill)
    return y + f.size


def left(text, x, y, f, fill=INK):
    d.text((x, y), text, font=f, fill=fill)
    return y + f.size


# ---------------------------------------------------------------- masthead
d.rectangle([0, 0, W, 10], fill=RED)
center("THE DAY IN ONE PICTURE", W // 2, 30, fit("THE DAY IN ONE PICTURE", SERIF, 940, 66))
d.rectangle([36, 118, W - 36, 124], fill=INK)
# date band
d.rectangle([36, 140, W - 36, 228], fill=NAVY)
center("THURSDAY, NOVEMBER 19, 2026", W // 2, 158,
       fit("THURSDAY, NOVEMBER 19, 2026", SANS, 900, 56), fill=WHITE)
center("THE WORLD'S NEWS · ONE FRONT PAGE", W // 2, 240,
       fit("THE WORLD'S NEWS · ONE FRONT PAGE", SANS, 900, 24), fill=(90, 96, 105))

# ---------------------------------------------------------------- helpers
def panel(x0, y0, x1, y1, bg):
    d.rectangle([x0, y0, x1, y1], fill=bg, outline=INK, width=3)


def headline_lines(lines, cx, y, max_w, start=44, fill=INK, gap=6):
    for ln in lines:
        f = fit(ln, SANS, max_w, start)
        center(ln, cx, y, f, fill=fill)
        y += f.size + gap
    return y


def subline(text, cx, y, max_w, start=26, fill=(52, 58, 66)):
    f = fit(text, SANS, max_w, start)
    center(text, cx, y, f, fill=fill)
    return y + f.size


# ---------------------------------------------------------------- lead: summit
panel(36, 284, W - 36, 512, (222, 232, 242))
# three overlapping circles: US / CN / RU
cy = 368
for cx, col, tag in [(150, (38, 74, 140), "US"), (232, (196, 42, 42), "CN"), (191, (90, 110, 150), "RU")]:
    pass
# draw in order so the middle (RU) sits behind: simpler -- side by side overlap
d.ellipse([86, cy - 52, 190, cy + 52], fill=(38, 74, 140), outline=WHITE, width=4)
d.ellipse([248, cy - 52, 352, cy + 52], fill=(196, 42, 42), outline=WHITE, width=4)
d.ellipse([167, cy - 62, 271, cy + 42], fill=(96, 116, 156), outline=WHITE, width=4)
for cx, tag in [(138, "US"), (219, "RU"), (300, "CN")]:
    f = font(SANS, 30)
    w = d.textlength(tag, font=f)
    d.text((cx - w / 2, cy - 20), tag, font=f, fill=WHITE)
center("SHENZHEN, CHINA", 219, cy + 66, font(SANS, 22), fill=(52, 58, 66))

lx = 560  # text centre for lead panel
y = headline_lines(["TRUMP, XI & PUTIN", "MEET IN SHENZHEN"], lx, 306, 400, start=45)
y = subline("FIRST TRILATERAL SUMMIT", lx, y + 8, 400, start=27, fill=RED)
y = subline("NUCLEAR TALKS · UKRAINE", lx, y + 6, 400, start=25)
subline("AT THE CENTER", lx, y + 4, 400, start=25)

# ---------------------------------------------------------------- row 2
panel(36, 528, 504, 748, (244, 231, 199))     # Anthropic (left)
panel(520, 528, 988, 748, (222, 214, 240))    # GTA VI (right)

# Anthropic: ticker chip + rising line
d.rounded_rectangle([66, 556, 226, 616], radius=12, fill=NAVY)
center("ANT", 146, 570, font(SANS, 34), fill=WHITE)
pts = [(250, 606), (300, 588), (348, 596), (404, 562), (452, 548)]
d.line(pts, fill=(22, 128, 57), width=7, joint="curve")
d.polygon([(452, 548), (428, 550), (446, 568)], fill=(22, 128, 57))
center("NASDAQ", 146, 626, font(SANS, 20), fill=(52, 58, 66))
y = headline_lines(["ANTHROPIC DEBUTS", "ON NASDAQ TODAY"], 270, 646, 440, start=33)
subline("IPO $83 · $81.3B RAISED · LARGEST EVER", 270, y + 2, 440, start=21)

# GTA VI: sun + palm + VI
d.ellipse([838, 548, 922, 632], fill=(244, 164, 40))
# palm: trunk + drooping fronds, kept above the headline
tx, ty_top, ty_bot = 752, 560, 640
d.line([(tx - 6, ty_bot), (tx + 4, ty_top)], fill=(46, 64, 48), width=8)
for dx, droop in [(-58, 26), (-34, 12), (0, 6), (36, 12), (60, 28)]:
    pts = []
    for t in range(11):
        u = t / 10
        px = tx + 4 + dx * u
        py = ty_top - 14 * u + (droop + 16) * u * u
        pts.append((px, py))
    d.line(pts, fill=(46, 64, 48), width=6)
center("VI", 610, 552, font(SERIF, 64), fill=(70, 40, 110))
y = headline_lines(["GTA VI LAUNCH DAY"], 754, 646, 440, start=33)
subline("13-YEAR WAIT ENDS · 99/100 REVIEWS", 754, y + 2, 440, start=21)
subline("2.3M WATCHING ON TWITCH", 754, y + 28, 440, start=21)

# ---------------------------------------------------------------- row 3
panel(36, 764, 504, 956, (226, 236, 219))     # ICJ (left)
panel(520, 764, 988, 956, (214, 234, 234))    # Cyclone (right)

# ICJ: scales of justice (compact, kept clear of the text block)
sx, sy = 104, 800
d.line([(sx, sy), (sx, sy + 62)], fill=INK, width=5)
d.line([(sx - 38, sy + 7), (sx + 38, sy + 7)], fill=INK, width=5)
for px in (sx - 38, sx + 38):
    d.line([(px, sy + 7), (px - 13, sy + 36)], fill=INK, width=3)
    d.line([(px, sy + 7), (px + 13, sy + 36)], fill=INK, width=3)
    d.arc([px - 17, sy + 26, px + 17, sy + 46], 0, 180, fill=INK, width=4)
d.line([(sx - 18, sy + 64), (sx + 18, sy + 64)], fill=INK, width=5)
y = headline_lines(["WORLD COURT RULES", "ON ROHINGYA CASE"], 336, 786, 320, start=30)
subline("ICJ GENOCIDE RULING", 336, y + 4, 320, start=22, fill=RED)
subline("GAMBIA v. MYANMAR · THE HAGUE", 336, y + 32, 320, start=20)

# Cyclone: spiral
cx, cyy = 610, 838
for r, a0 in [(52, 300), (40, 255), (28, 210), (16, 165)]:
    d.arc([cx - r, cyy - r, cx + r, cyy + r], a0, a0 + 290, fill=(16, 96, 120), width=7)
d.ellipse([cx - 7, cyy - 7, cx + 7, cyy + 7], fill=(16, 96, 120))
y = headline_lines(["CYCLONE AKVAN", "HITS INDIA"], 806, 786, 350, start=30)
subline("100,000+ EVACUATED", 806, y + 4, 350, start=22, fill=RED)
subline("ODISHA · RED ALERT", 806, y + 32, 350, start=20)

# ---------------------------------------------------------------- footer
d.rectangle([0, 972, W, H], fill=INK)
center("ALSO TODAY: COP31 CLIMATE TALKS IN ANTALYA · CRIMEAN BRIDGE ATTACKED AGAIN · GOLD $3,740",
       W // 2, 986, fit("ALSO TODAY: COP31 CLIMATE TALKS IN ANTALYA · CRIMEAN BRIDGE ATTACKED AGAIN · GOLD $3,740",
                        SANS, 980, 24), fill=WHITE)

out = Path(__file__).resolve().parent / "entry.png"
img.save(out, "PNG", optimize=True)
print("wrote", out, out.stat().st_size, "bytes")
