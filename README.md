# Steganography Project

## Description
This project demonstrates audio steganography techniques by hiding a grayscale image inside an audio file using two different methods:

- LSB (Least Significant Bit) method
- DWT-SVD (Discrete Wavelet Transform + Singular Value Decomposition) method

The goal is to compare spatial-domain and frequency-domain steganography approaches.

---

## Methods

### 1. LSB Method
Hides image data by modifying the least significant bits of audio samples.

### 2. DWT-SVD Method
Decomposes audio using wavelet transform and embeds data in the frequency domain using SVD.

---

## Project Structure

- `src/prepare_image.py` → image preprocessing
- `src/embed_data.py` → LSB embedding
- `src/extract_data.py` → LSB extraction
- `src/dwt_svd_stego.py` → DWT-SVD embedding
- `src/dwt_svd_extract.py` → DWT-SVD extraction

---

## Run LSB Pipeline | Run DWT-SVD Pipeline

```bash
python3 src/prepare_image.py
python3 src/embed_data.py
python3 src/extract_data.py

python3 src/dwt_svd_stego.py
python3 src/dwt_svd_extract.py