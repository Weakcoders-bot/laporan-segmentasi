import cv2
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path

# Fungsi utama
def run(input_path='input.jpg', out_dir='outputs'):
    p = Path(input_path)
    if not p.exists():
        raise SystemExit(f'File tidak ditemukan: {input_path}. Pastikan file input.jpg ada di folder ini.')
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

   # 1. Baca dan ubah jadi grayscale
    img = cv2.imread(str(p), cv2.IMREAD_GRAYSCALE)
    blurred = cv2.GaussianBlur(img, (5,5), 0)

   # 2. Otsu Thresholding
    otsu_val, otsu = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    print('Nilai threshold Otsu:', otsu_val)
    cv2.imwrite(str(out / 'output_otsu.png'), otsu)

   # 3. Adaptive Thresholding
    adaptive = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite(str(out / 'output_adaptive.png'), adaptive)

   # 4. Morphology (opsional)
    kernel = np.ones((3,3), np.uint8)
    cleaned = cv2.morphologyEx(adaptive, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite(str(out / 'output_cleaned.png'), cleaned)

   # 5. Tampilkan hasil
    plt.figure(figsize=(10,4))
    plt.subplot(1,4,1); plt.imshow(img, cmap='gray'); plt.title('Original'); plt.axis('off')
    plt.subplot(1,4,2); plt.imshow(otsu, cmap='gray'); plt.title('Otsu'); plt.axis('off')
    plt.subplot(1,4,3); plt.imshow(adaptive, cmap='gray'); plt.title('Adaptive'); plt.axis('off')
    plt.subplot(1,4,4); plt.imshow(cleaned, cmap='gray'); plt.title('Cleaned'); plt.axis('off')
    plt.tight_layout()
    plt.show()

# Jalankan fungsi
run('input.jpg')
