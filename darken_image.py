#!/usr/bin/env python3
from PIL import Image, ImageEnhance # pillow
import sys
import os

if len(sys.argv) < 2:
    print("Usage: python3 darken_image.py <image_file> [darkness_factor]")
    print("darkness_factor: 0.0 (black) to 1.0 (original), default: 0.5")
    sys.exit(1)

image_path = os.path.expanduser(sys.argv[1])
darkness = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5

print(f"Darkening {image_path} to {darkness * 100}% brightness...")

# Open and darken the image
img = Image.open(image_path)
enhancer = ImageEnhance.Brightness(img)
darkened = enhancer.enhance(darkness)

# Save back to the same file
darkened.save(image_path)
print(f"Image darkened successfully! Brightness reduced to {darkness * 100}%")
