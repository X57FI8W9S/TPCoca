from pathlib import Path
from PIL import Image
import numpy as np

# Load the template image
img_path = Path(__file__).with_name('pattern.png')
img = Image.open(img_path)
arr = np.array(img)

# Detect non-white pixels to determine the area of interest
mask = arr.mean(axis=2) < 250
coords = np.argwhere(mask)
if coords.size == 0:
    raise ValueError('No foreground pixels found to crop.')

y0, x0 = coords.min(axis=0)
y1, x1 = coords.max(axis=0) + 1

cropped = img.crop((x0, y0, x1, y1))
out_path = img_path.with_name('pattern_cropped.png')
cropped.save(out_path)

print(f'Cropped image saved to {out_path}')
