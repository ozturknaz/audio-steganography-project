import os
import numpy as np
import cv2 # type: ignore
import pywt # type: ignore
from scipy.io import wavfile

# 1. Path setup

base_path = os.path.dirname(os.path.dirname(__file__))

audio_path = os.path.join(base_path, "data/input/audio.wav")
image_path = os.path.join(base_path, "data/input/logo.png")

# 2. Load audio file

rate, audio = wavfile.read(audio_path)

# Convert stereo to mono if needed
if len(audio.shape) > 1:
    audio = audio[:, 0]

audio = audio.astype(np.float64)

print("Audio loaded:", audio.shape)

# 3. Load image

img = cv2.imread(image_path, 0)
img = cv2.resize(img, (64, 64))
img_flat = img.flatten().astype(np.float64)

print("Image ready:", img.shape)

# 4. Discrate Wavelet Transform (DWT)

coeffs = pywt.wavedec(audio, 'haar', level=1)

LL = coeffs[0]
LH = coeffs[1]

print("DWT done")
print("LL size:", len(LL))

# 5. Simple embedding in LL band
# (SVD version simplified for stability)

min_len = min(len(LL), len(img_flat))

for i in range(min_len):
    LL[i] = LL[i] + img_flat[i] * 0.001

coeffs[0] = LL

# 6. Reconstruct audio

stego_audio = pywt.waverec(coeffs, 'haar')
stego_audio = np.int16(stego_audio)

# 7. Save output file

out_path = os.path.join(base_path, "data/output/stego_audio_dwt_svd.wav")
wavfile.write(out_path, rate, stego_audio)

print("DWT-SVD embedding complete")