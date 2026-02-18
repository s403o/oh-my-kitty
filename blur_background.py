#!/usr/bin/env python3
from PIL import Image, ImageFilter
import sys
import os

# Blur the background image
blur_radius = int(sys.argv[1]) if len(sys.argv) > 1 else 15

print(f"Blurring background.png with radius {blur_radius}...")

bg_path = os.path.expanduser('~/.config/kitty/background.png')
img = Image.open(bg_path)

blurred = img.filter(ImageFilter.GaussianBlur(radius=blur_radius))
blurred.save(bg_path)

print("Background image blurred successfully!")
print("Reload Kitty to see the effect.")
