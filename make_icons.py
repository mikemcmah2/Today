from PIL import Image, ImageDraw
import math

# Palette (matches the app UI)
INK = (25, 28, 34, 255)        # background
SAGE = (107, 143, 113, 255)    # positive / green half
TERRACOTTA = (181, 83, 60, 255)  # negative / red half
CREAM = (232, 223, 206, 255)   # ring + hairline

def make_icon(size, corner_radius_ratio=0.22, padding_ratio=0.09):
    scale = 4
    S = size * scale
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # Rounded-square ink background (app-icon style)
    r = int(S * corner_radius_ratio)
    d.rounded_rectangle([0, 0, S - 1, S - 1], radius=r, fill=INK)

    # Circle split into two halves along a soft diagonal,
    # evoking two crescents meeting -- a moon-phase read for a nightly ritual.
    pad = int(S * padding_ratio)
    bbox = [pad, pad, S - pad, S - pad]
    cx, cy = S / 2, S / 2
    radius = (S - 2 * pad) / 2

    # Full circle base in sage, then terracotta pie for the right/lower half,
    # split along a diagonal for a dynamic, non-static feel.
    d.ellipse(bbox, fill=SAGE)
    d.pieslice(bbox, start=-35, end=145, fill=TERRACOTTA)

    # Thin cream ring outline
    ring_w = max(2, int(S * 0.012))
    d.ellipse(bbox, outline=CREAM, width=ring_w)

    # Fine dividing hairline along the split for definition
    ang1 = math.radians(-35)
    ang2 = math.radians(145)
    x1, y1 = cx + radius * math.cos(ang1), cy + radius * math.sin(ang1)
    x2, y2 = cx + radius * math.cos(ang2), cy + radius * math.sin(ang2)
    d.line([x1, y1, cx, cy], fill=CREAM, width=ring_w)
    d.line([x2, y2, cx, cy], fill=CREAM, width=ring_w)

    img = img.resize((size, size), Image.LANCZOS)
    return img

sizes = {
    "icon-512.png": 512,
    "icon-192.png": 192,
    "apple-touch-icon.png": 180,
    "favicon-32.png": 32,
    "favicon-16.png": 16,
}

for name, sz in sizes.items():
    make_icon(sz).save(name)
    print("saved", name)
