import numpy as np
from scipy.io import wavfile
from PIL import Image
import os

# Get the main project folder path
base = os.path.dirname(os.path.dirname(__file__))

# 1. Load stego audio file

audio_path = os.path.join(base, "data/output/stego_audio_lsb.wav")
rate, audio = wavfile.read(audio_path)

# Convert stereo to mono if needed
if len(audio.shape) > 1:
    audio = audio[:, 0]

# 2. Define total number of bits to extract
# (256x256 image, 3 channels, 8 bits per pixel)

total_bits = 256 * 256 * 3 * 8

# 3. Extract LSB bits from audio

bits = [str(audio[i] & 1) for i in range(total_bits)]
bits = ''.join(bits)

# 4. Convert bits back to bytes

bytes_list = [bits[i:i+8] for i in range(0, len(bits), 8)]

# 5. Convert bytes to image array

img_data = np.array([int(b, 2) for b in bytes_list], dtype=np.uint8)
img_data = img_data.reshape((256, 256, 3))

# 6. Save extracted image

img = Image.fromarray(img_data)
output_path = os.path.join(base, "data/output/extracted_logo_lsb.png")
img.save(output_path)

# Print message when done
print("LSB: Extraction completed")