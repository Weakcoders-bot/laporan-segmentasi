# Laporan Segmentasi Citra — Thresholding

Berisi:
- `index.html` — Halaman laporan siap dipublish (GitHub Pages).
- `segmentasi.py` — Contoh kode Python (OpenCV) untuk Thresholding (Otsu & Adaptive).
- `assets/` — tempat untuk menaruh gambar hasil eksperimen (tidak disertakan).
- `README.md` — (this file) petunjuk deploy.

Sumber materi: Slide kuliah "Pengolahan Citra Digital - Segmentasi Citra - Thresholding". fileciteturn0file0

## Cara publish ke GitHub Pages (singkat)
1. Buat repository baru di GitHub (mis. `laporan-segmentasi`).
2. Clone ke lokal:
   ```
   git clone https://github.com/<your-username>/laporan-segmentasi.git
   cd laporan-segmentasi
   ```
3. Salin seluruh isi folder ini ke dalam repo lokal.
4. Commit & push:
   ```
   git add .
   git commit -m "Add laporan segmentasi thresholding"
   git push origin main
   ```
5. Aktifkan GitHub Pages:
   - Buka Settings → Pages → Source: `main` branch, folder: `/ (root)` → Save.
   - Setelah beberapa menit, situs akan tersedia di:
     `https://<your-username>.github.io/laporan-segmentasi/`
6. Ganti `<your-username>` dan nama repo pada URL di atas — itulah link yang akan mengarah langsung ke laporan.

## Cara otomatis (bash) — jika ingin:
Pastikan git sudah terkonfigurasi, lalu jalankan (ubah `<your-username>` & `<repo>`):
```bash
REPO="laporan-segmentasi"
USER="<your-username>"
git init
git remote add origin https://github.com/$USER/$REPO.git
git add .
git commit -m "Initial commit: laporan segmentasi"
git branch -M main
git push -u origin main
```

Kalau mau saya bantu generate preview atau mengubah isi laporan, bilang saja 😉