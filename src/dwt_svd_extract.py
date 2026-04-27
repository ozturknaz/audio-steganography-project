import os
import numpy as np
import cv2 # type: ignore
import pywt # type: ignore
from scipy.io import wavfile

# 1. Path setup

base_path = os.path.dirname(os.path.dirname(__file__))

audio_path = os.path.join(base_path, "data/output/stego_audio_dwt_svd.wav")

# 2. Load stego audio

rate, audio = wavfile.read(audio_path)

if len(audio.shape) > 1:
    audio = audio[:, 0]

audio = audio.astype(np.float64)

print("Stego audio loaded:", audio.shape)

# 3. DWT

coeffs = pywt.wavedec(audio, 'haar', level=1)

LL = coeffs[0]

print("DWT done")
print("LL size:", len(LL))

# 4. Extract image data
# normalize LL values
ll_norm = np.abs(LL)
ll_norm = ll_norm / np.max(ll_norm)

# take first 64x64 values
img_data = ll_norm[:64*64]
img_data = img_data * 255
img_data = img_data.reshape((64, 64)).astype(np.uint8)

# 5. Save image

out_path = os.path.join(base_path, "data/output/extracted_logo_dwt_svd.png")
cv2.imwrite(out_path, img_data)

print("DWT-SVD extraction complete")