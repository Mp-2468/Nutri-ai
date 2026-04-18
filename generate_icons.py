#!/usr/bin/env python3
"""
NutriAI Icon Generator
Generates PWA icons in all required sizes using PIL/Pillow.
Run: pip install Pillow && python generate_icons.py
"""

import os
import math

try:
    from PIL import Image, ImageDraw, ImageFont
    HAS_PILLOW = True
except ImportError:
    HAS_PILLOW = False

SIZES = [72, 96, 128, 144, 152, 192, 384, 512]
ICON_DIR = "icons"

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_icon_svg(size):
    """Create an SVG icon — works without Pillow."""
    bg      = "#060610"
    accent  = "#C1FF47"
    teal    = "#00E5C0"
    r       = size // 2
    pad     = size * 0.12
    inner_r = r - pad

    # Leaf icon paths scaled to size
    scale   = size / 512
    cx, cy  = size / 2, size / 2

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 {size} {size}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0E0E22"/>
      <stop offset="100%" stop-color="#060610"/>
    </linearGradient>
    <linearGradient id="leaf" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{accent}"/>
      <stop offset="100%" stop-color="{teal}"/>
    </linearGradient>
  </defs>
  <!-- Background -->
  <rect width="{size}" height="{size}" rx="{size*0.22}" fill="url(#bg)"/>
  <!-- Outer ring -->
  <circle cx="{cx}" cy="{cy}" r="{inner_r}" fill="none" stroke="{accent}22" stroke-width="{size*0.025}"/>
  <!-- Leaf / fork icon -->
  <g transform="translate({cx},{cy}) scale({scale*0.55})">
    <!-- Plate circle -->
    <circle cx="0" cy="30" r="160" fill="none" stroke="url(#leaf)" stroke-width="28" opacity="0.9"/>
    <!-- Fork tines -->
    <rect x="-80" y="-200" width="22" height="160" rx="11" fill="url(#leaf)"/>
    <rect x="-30" y="-200" width="22" height="160" rx="11" fill="url(#leaf)"/>
    <rect x="20" y="-200" width="22" height="160" rx="11" fill="url(#leaf)"/>
    <!-- Fork handle -->
    <rect x="-44" y="-40" width="100" height="22" rx="11" fill="url(#leaf)"/>
    <rect x="-22" y="-40" width="56" height="180" rx="11" fill="url(#leaf)"/>
    <!-- Sparkle -->
    <circle cx="120" cy="-160" r="20" fill="{accent}"/>
    <circle cx="100" cy="-110" r="12" fill="{accent}" opacity="0.6"/>
  </g>
  <!-- "N" lettermark -->
  <text x="{size*0.5}" y="{size*0.62}" text-anchor="middle" font-family="Arial Black, Arial" font-weight="900" font-size="{size*0.18}" fill="{accent}" opacity="0.15">N</text>
</svg>'''
    return svg

def generate_all_icons():
    os.makedirs(ICON_DIR, exist_ok=True)

    if HAS_PILLOW:
        print("✅ Pillow found — generating PNG icons...")
        for size in SIZES:
            # Create SVG first, then convert
            svg_path = os.path.join(ICON_DIR, f"icon_{size}_temp.svg")
            png_path = os.path.join(ICON_DIR, f"icon-{size}.png")

            svg = create_icon_svg(size)
            with open(svg_path, "w") as f:
                f.write(svg)

            # Simple PIL icon (gradient circle with "N")
            img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)

            # Rounded rect background
            corner = int(size * 0.22)
            draw.rounded_rectangle([0, 0, size-1, size-1], radius=corner, fill=(14, 14, 34, 255))

            # Accent circle outline
            pad = int(size * 0.1)
            draw.ellipse([pad, pad, size-pad, size-pad], outline=(193, 255, 71, 80), width=max(2, size//60))

            # Leaf green ring (plate)
            mid = size // 2
            rr = int(size * 0.25)
            draw.ellipse([mid-rr, mid-rr+size//12, mid+rr, mid+rr+size//12],
                        outline=(0, 229, 192, 230), width=max(3, size//50))

            # Center dot
            dot = size // 16
            draw.ellipse([mid-dot, mid-dot, mid+dot, mid+dot], fill=(193, 255, 71, 255))

            img.save(png_path, "PNG")
            os.remove(svg_path)
            print(f"  ✓ icon-{size}.png")
    else:
        print("⚠️  Pillow not installed — generating SVG icons instead.")
        print("   Install Pillow for PNG icons: pip install Pillow")
        print("   Or use https://realfavicongenerator.net to convert SVGs to PNGs.\n")

        for size in SIZES:
            svg_path = os.path.join(ICON_DIR, f"icon-{size}.svg")
            svg = create_icon_svg(size)
            with open(svg_path, "w") as f:
                f.write(svg)
            print(f"  ✓ icon-{size}.svg")

    print(f"\n✅ Icons generated in ./{ICON_DIR}/")
    print("   Next: convert any SVGs to PNGs using an online converter or Pillow.")

if __name__ == "__main__":
    generate_all_icons()
