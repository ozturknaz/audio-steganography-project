📌 Audio Steganography Project Report
1. Introduction
This project focuses on audio steganography techniques, where a grayscale image (Kırıkkale University logo) is hidden inside an audio file using two different methods:
LSB (Least Significant Bit) method
DWT-SVD (Discrete Wavelet Transform + Singular Value Decomposition) method
2. Methods
2.1 LSB Method
The LSB method hides image data by modifying the least significant bits of audio samples. Since changes are very small, the human ear cannot easily detect them.
Advantages:
Simple implementation
Low computational cost
Disadvantages:
Very sensitive to noise
Low robustness
2.2 DWT-SVD Method
This method applies Discrete Wavelet Transform (DWT) to decompose the audio signal into frequency bands. Then Singular Value Decomposition (SVD) is used to embed image data into the LL band.
Advantages:
More robust than LSB
Works in frequency domain
Better resistance to noise
Disadvantages:
More complex
Higher computation cost
3. Implementation
The project is implemented in Python using the following libraries:
NumPy
OpenCV
PyWavelets
SciPy
Pipeline structure:
prepare_image.py → image preprocessing
embed_data.py → LSB embedding
extract_data.py → LSB extraction
dwt_svd_stego.py → DWT-SVD embedding
dwt_svd_extract.py → DWT-SVD extraction
4. Comparison
| Feature          | LSB      | DWT-SVD             |
| ---------------- | -------- | ------------------- |
| Domain           | Spatial  | Frequency           |
| Robustness       | Low      | High                |
| Complexity       | Low      | Medium              |
| Quality          | Moderate | Better preservation |
| Noise resistance | Weak     | Strong              |
5. Conclusion
LSB is suitable for simple steganography applications, while DWT-SVD provides a more robust and secure method. This project demonstrates both approaches and highlights the trade-offs between simplicity and robustness.