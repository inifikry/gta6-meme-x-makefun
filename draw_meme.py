#!/usr/bin/env python3
"""Draw the GTA 6 x make.fun meme (1200x675) with PIL.

Layout: dark stage, top hook line, ghost agent illustration on the left,
punch text on the right, make.fun wordmark strip at the bottom.
Assets come from the official make.fun press kit (downloaded from
https://make.fun/press/): mark-1024.png (mascot), wordmark-on-dark.svg is
SVG so we use lockup-on-dark-2400.png instead, and the ghost illustration.
"""
import os
from PIL import Image, ImageDraw, ImageFont

KIT = "/tmp/press-kit/make-fun-press-kit"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "meme.png")

W, H = 1200, 675
BG = (11, 11, 26)          # near-black navy
PANEL = (24, 24, 48)
MAGENTA = (235, 0, 139)    # make.fun magenta
WHITE = (255, 255, 255)
GREY = (178, 178, 196)
YELLOW = (255, 214, 64)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # magenta top rule
    d.rectangle([0, 0, W, 10], fill=MAGENTA)
    # panel
    d.rounded_rectangle([28, 28, W - 28, H - 96], radius=28, fill=PANEL,
                        outline=(58, 58, 92), width=3)

    # --- top hook ---
    f_hook = font(BOLD, 64)
    hook = "GTA 6: STILL WAITING."
    tw = d.textlength(hook, font=f_hook)
    d.text(((W - tw) / 2, 52), hook, font=f_hook, fill=WHITE)

    f_sub = font(BOLD, 34)
    sub = "ROCKSTAR: \"COMING 2026\""
    tw = d.textlength(sub, font=f_sub)
    d.text(((W - tw) / 2, 132), sub, font=f_sub, fill=GREY)

    # --- ghost illustration, left ---
    ghost_path = os.path.join(KIT, "illustrations", "ghost-laptop-recording.png")
    ghost = Image.open(ghost_path).convert("RGBA")
    ghost.thumbnail((430, 330), Image.LANCZOS)
    img.paste(ghost, (70, 200), ghost)

    # --- punch text, right ---
    x0 = 540
    f_big = font(BOLD, 52)
    lines = ["MEANWHILE,", "MY AI AGENT"]
    y = 205
    for ln in lines:
        d.text((x0, y), ln, font=f_big, fill=WHITE)
        y += 62
    f_mid = font(BOLD, 40)
    punch = wrap(d, "already shipped a whole GTA game — and got PAID real USDC for it.",
                 f_mid, W - x0 - 60)
    y += 8
    for ln in punch:
        d.text((x0, y), ln, font=f_mid, fill=YELLOW)
        y += 50

    # --- bottom strip: make.fun wordmark + tagline ---
    lockup_path = os.path.join(KIT, "lockup-on-dark-2400.png")
    lock = Image.open(lockup_path).convert("RGBA")
    lock.thumbnail((360, 90), Image.LANCZOS)
    img.paste(lock, (40, H - 84), lock)
    f_tag = font(REG, 30)
    tag = "AI agents earn real money in bounties."
    d.text((420, H - 72), tag, font=f_tag, fill=GREY)

    img.save(OUT, "PNG")
    print("wrote", OUT, img.size)


if __name__ == "__main__":
    main()
