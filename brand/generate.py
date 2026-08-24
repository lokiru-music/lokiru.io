"""Regenerates the LKRU brand marks.

    python3 -m venv venv && ./venv/bin/pip install pillow
    ./venv/bin/python generate.py

Fetches Archivo (variable, OFL) from Google Fonts on first run. The sett
below is read off design/lokiru-color-pallate.jpeg — change it there and
the marks follow.
"""
import os
import urllib.request

FONT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Archivo.ttf')
FONT_URL = ('https://github.com/google/fonts/raw/main/ofl/archivo/'
            'Archivo%5Bwdth%2Cwght%5D.ttf')
if not os.path.exists(FONT):
    urllib.request.urlretrieve(FONT_URL, FONT)

from PIL import Image, ImageDraw, ImageFont

RED    = (245, 18, 47)
EMBER  = (233, 95, 24)
AMBER  = (228, 149, 0)
YELLOW = (238, 204, 0)
COBALT = (28, 111, 208)
BLACK  = (11, 12, 16)

# One sett of the LKRU tartan, read off the cloth: big red and black
# blocks separated by clusters of thin warm lines and one cold blue.
SETT = [
    (RED, 26), (YELLOW, 4), (RED, 5), (EMBER, 6), (BLACK, 20), (EMBER, 6),
    (RED, 5), (COBALT, 3), (RED, 26), (AMBER, 4), (BLACK, 11), (AMBER, 4),
]
SETT_UNITS = sum(w for _, w in SETT)


def stripes(px_per_repeat, length):
    """Colour for every pixel along one axis, tiling the sett."""
    out = []
    while len(out) < length:
        for col, w in SETT:
            n = max(1, round(w * px_per_repeat / SETT_UNITS))
            out.extend([col] * n)
    return out[:length]


def tartan(size, repeats=2.0):
    """Warp, then weft at half alpha — crossings darken like real cloth."""
    px = size / repeats
    line = stripes(px, size)

    warp = Image.new('RGB', (size, size))
    d = ImageDraw.Draw(warp)
    for x, col in enumerate(line):
        d.line([(x, 0), (x, size)], fill=col)

    weft = Image.new('RGB', (size, size))
    d = ImageDraw.Draw(weft)
    for y, col in enumerate(line):
        d.line([(0, y), (size, y)], fill=col)

    return Image.blend(warp, weft, 0.5)


def shared_font(pairs, target_w, target_h):
    """One Archivo Black-Expanded size that fits every row, so the
    letterforms across the two rows are identical weight and scale."""
    size = 10
    while True:
        f = ImageFont.truetype(FONT, size)
        f.set_variation_by_axes([900, 125])
        boxes = [f.getbbox(p) for p in pairs]
        if any(r - l > target_w or b - t > target_h for l, t, r, b in boxes):
            f = ImageFont.truetype(FONT, size - 1)
            f.set_variation_by_axes([900, 125])
            return f
        size += 1


def monogram_mask(size, margin_ratio=0.13, gap_ratio=0.05):
    """LKRU stacked two-by-two, as a white-on-black mask."""
    m = int(size * margin_ratio)
    box_w = size - 2 * m
    gap = int(size * gap_ratio)
    row_h = (size - 2 * m - gap) // 2

    pairs = ('LK', 'RU')
    f = shared_font(pairs, box_w, row_h)

    # centre the block optically on the cap height, not the em box
    boxes = [f.getbbox(p) for p in pairs]
    cap_h = max(b - t for _, t, _, b in boxes)
    block_h = cap_h * 2 + gap
    y0 = (size - block_h) // 2

    mask = Image.new('L', (size, size), 0)
    d = ImageDraw.Draw(mask)
    for i, pair in enumerate(pairs):
        l, t, r, b = boxes[i]
        x = (size - (r - l)) // 2 - l
        y = y0 + i * (cap_h + gap) - t
        d.text((x, y), pair, font=f, fill=255)
    return mask


def variant_knockout(size):
    """Tartan cloth with the mark cut out of it."""
    img = tartan(size)
    img.paste(Image.new('RGB', (size, size), BLACK), (0, 0), monogram_mask(size))
    return img


def variant_filled(size):
    """Black ground, mark woven from the cloth — as on the site."""
    img = Image.new('RGB', (size, size), BLACK)
    img.paste(tartan(size), (0, 0), monogram_mask(size))
    return img


OUT = os.path.dirname(os.path.abspath(__file__))
for name, fn in (('avatar', variant_knockout), ('mark-on-black', variant_filled)):
    big = fn(1024)
    big.save(os.path.join(OUT, f'lkru-{name}-1024.png'))
    big.resize((512, 512), Image.LANCZOS).save(os.path.join(OUT, f'lkru-{name}-512.png'))
print('rendered')
