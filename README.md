Laporan Praktikum Segmentasi Citra (Thresholding)

Laporan ini merupakan hasil praktikum mata kuliah Pengolahan Citra Digital dengan topik  
Segmentasi Citra Menggunakan Metode Thresholding (Otsu dan Adaptive Thresholding).
Tujuan dari praktikum ini adalah memahami konsep segmentasi citra, menerapkan dua metode thresholding yang berbeda, dan menganalisis hasilnya pada berbagai kondisi pencahayaan.

---

Struktur Folder
| Nama File | Deskripsi |
|------------|------------|
| `index.html`   | Laporan utama yang dapat dibuka langsung di browser atau dipublikasikan ke GitHub Pages. |
| `segmentasi.py`| Kode Python untuk implementasi metode Otsu dan Adaptive Thresholding menggunakan OpenCV. |
| `.nojekyll`    | File kosong agar GitHub Pages dapat menampilkan file HTML tanpa diproses oleh Jekyll. |
| `README.md`    | Petunjuk lengkap penggunaan dan publikasi laporan ini. |

---

Segmentasi citraadalah proses pemisahan citra menjadi beberapa bagian (region) berdasarkan karakteristik tertentu seperti intensitas atau warna.  
Thresholding merupakan teknik segmentasi paling sederhana, di mana piksel citra dibandingkan dengan nilai ambang tertentu untuk menentukan apakah piksel termasuk objek atau latar belakang.

Metode Otsu
Menentukan nilai ambang otomatis dengan memaksimalkan variansi antar-kelas (antara objek dan latar). Cocok untuk citra dengan histogram bimodal dan pencahayaan seragam.

Metode Adaptive Thresholding
Menentukan ambang secara lokal berdasarkan area kecil di sekitar tiap piksel (menggunakan rata-rata atau Gaussian). Lebih efektif pada citra dengan pencahayaan tidak merata.

---

Cara Menjalankan Program di Jupyter Notebook
Persiapan Awal
Pastikan Python dan Jupyter Notebook sudah terpasang di perangkat kamu.  
Instal library yang dibutuhkan dengan menjalankan perintah berikut di **cell Jupyter Notebook**:

```python
pip install opencv-python-headless numpy matplotlib
