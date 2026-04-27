import os
from PIL import Image

base_path = os.path.dirname(os.path.dirname(__file__))

input_path = os.path.join(base_path, "data/input/logo.png")
output_path = os.path.join(base_path, "data/output/logo_256.png")

img = Image.open(input_path)
img = img.resize((256, 256)).convert("RGB")

img.save(output_path)

print("LSB: Image ready and saved")