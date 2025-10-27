#!/usr/bin/env python3
"""Contoh script segmentasi sederhana.
Letakkan script ini di folder yang sama dengan input.jpg, jalankan:
    python3 segmentasi.py
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
    img_path = 'input.jpg'
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print('File input.jpg tidak ditemukan. Masukkan gambar, lalu coba lagi.')
        return

    # Preprocessing
    blurred = cv2.GaussianBlur(image, (5,5), 0)

    # Otsu's thresholding
    otsu_thresh_val, otsu = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    print('Otsu threshold:', otsu_thresh_val)

    # Adaptive Gaussian thresholding
    adaptive = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY, 11, 2)

    # Morphological cleanup
    kernel = np.ones((3,3), np.uint8)
    cleaned = cv2.morphologyEx(adaptive, cv2.MORPH_CLOSE, kernel)

    # Save outputs
    cv2.imwrite('output_otsu.png', otsu)
    cv2.imwrite('output_adaptive.png', adaptive)
    cv2.imwrite('output_cleaned.png', cleaned)
    print('Saved: output_otsu.png, output_adaptive.png, output_cleaned.png')

    # Display
    plt.figure(figsize=(10,4))
    plt.subplot(1,4,1); plt.imshow(image, cmap='gray'); plt.title('Original'); plt.axis('off')
    plt.subplot(1,4,2); plt.imshow(otsu, cmap='gray'); plt.title('Otsu'); plt.axis('off')
    plt.subplot(1,4,3); plt.imshow(adaptive, cmap='gray'); plt.title('Adaptive'); plt.axis('off')
    plt.subplot(1,4,4); plt.imshow(cleaned, cmap='gray'); plt.title('Cleaned'); plt.axis('off')
    plt.tight_layout(); plt.show()

if __name__ == '__main__':
    main()