import os
import numpy as np
from PIL import Image
from scipy.io import wavfile

# Base path (proje kökü)
base_path = os.path.dirname(os.path.dirname(__file__))

# 1. Ses dosyasını oku
audio_path = os.path.join(base_path, "data/input/audio.wav")
rate, audio = wavfile.read(audio_path)

# stereo ise mono yap
if len(audio.shape) > 1:
    audio = audio[:, 0]

# 2. Görseli oku
img_path = os.path.join(base_path, "data/output/logo_256.png")
img = Image.open(img_path)
img = np.array(img)

# 3. Görseli bitlere çevir
flat_img = img.flatten()
bits = ''.join([format(pixel, '08b') for pixel in flat_img])

# 4. Audio kopyası
stego_audio = np.copy(audio)

# 5. LSB embedding
for i in range(len(bits)):
    stego_audio[i] = (stego_audio[i] & ~1) | int(bits[i])

# 6. Output yaz
output_path = os.path.join(base_path, "data/output/stego_audio_lsb.wav")
wavfile.write(output_path, rate, stego_audio)

print("LSB: Embedding tamamlandı")