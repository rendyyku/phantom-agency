# Master Plan: Autonomous Marketing & Community Agency (Phantom Intelligence)

Dokumen ini adalah cetak biru operasional untuk menjalankan pemasaran, produksi konten video, dan aktivasi komunitas Telegram secara otonom menggunakan multi-agen AI dengan pengawasan satu pintu (Human-in-the-loop).

---

## 1. Model Bisnis & Target Akhir

* **Tujuan Utama:** Akuisisi pengguna aktif broker rekanan (Exness IB) sebanyak mungkin.
* **Strategi Penjualan:** Soft-selling berbasis utilitas gratis (*free institutional utility*). Kami tidak menjual langganan sinyal berbayar dan tidak memungut biaya bulanan.
* **Proposisi Nilai:** Pengguna mendapatkan akses penuh ke mesin analisis AI dan integrasi auto-trade MT5 secara gratis. Syaratnya adalah menghubungkan akun trading broker mitra resmi agar sistem terhubung langsung ke likuiditas. Komisi didapatkan secara berkelanjutan dari rabat spread lot transaksi pengguna.

---

## 2. Struktur Tim & Pembagian Tugas Agen

Sistem digerakkan oleh 4 divisi agen otonom di bawah koordinasi CEO.

```
                         ┌───────────────────────────────────┐
                         │      CEO / ORCHESTRATOR           │
                         │    (Hermes AI - Pengawas Utama)   │
                         └─────────────────┬─────────────────┘
                                           │
            ┌──────────────────────────────┼──────────────────────────────┐
            │                              │                              │
┌───────────▼────────────┐    ┌────────────▼─────────────┐   ┌────────────▼────────────┐
│   DIVISI 1: INTEL      │    │    DIVISI 2: KONTEN      │   │   DIVISI 3: TELEGRAM    │
│   MAKRO & RISET PASAR  │    │  VIDEO (REMOTION.DEV)    │   │  PROPAGANDA & EDUKASI   │
├────────────────────────┤    ├──────────────────────────┤   ├─────────────────────────┤
│ • Pantau news global   │    │ • Terima brief dari D1   │   │ • Bot aktif di grup     │
│ • Kalender ekonomi     │    │ • Render video 9:16 code │   │   2.300+ member         │
│ • Korelasi ke XAUUSD   │    │ • Kirim link review ke   │   │ • Bedah teknikal/news   │
│ • Susun angle konten   │    │   Telegram Owner (ACC)   │   │ • Generate grafis data  │
│                        │    │ • Auto-upload ke TikTok  │   │ • Tombol Akses PRO Free │
└────────────────────────┘    └──────────────────────────┘   └─────────────────────────┘
                                                                          │
                                                              ┌───────────▼────────────┐
                                                              │   DIVISI 4: ONBOARDING │
                                                              │  (BOT MT5 PARTNER SYNC)│
                                                              ├────────────────────────┤
                                                              │ • Verifikasi nomor MT5 │
                                                              │ • Buka akses unlimited │
                                                              └────────────────────────┘
```

### A. CEO & Orchestrator (Hermes)
* Mengatur jadwal kerja tiap agen.
* Melakukan validasi kualitas sebelum pesan atau brief diteruskan ke tahap berikutnya.
* Mengirimkan notifikasi ringkas dan permohonan persetujuan (approval) ke Telegram Owner.

### B. Divisi 1: Intel Makro & Riset Pasar
* **Sumber Data:** Kalender ekonomi harian, rilis data inflasi (CPI, PPI), keputusan suku bunga bank sentral (Fed, ECB), tensi geopolitik (contoh: eskalasi Selat Hormuz, konflik energi).
* **Tugas Spesifik:**
  1. Menghitung dampak langsung terhadap volatilitas dan likuiditas emas (XAUUSD).
  2. Menyusun ringkasan fakta tanpa bumbu narasi berlebihan.
  3. Menyerahkan satu brief harian ke Divisi Konten Video dan tiga brief harian ke Divisi Telegram.

### C. Divisi 2: Video Production (Remotion.dev + TikTok)
* **Teknologi:** Framework Remotion (React/TypeScript) untuk render video 9:16 beresolusi 1080x1920.
* **Gaya Visual:** Data-driven, rekaman replay chart TradingView, visualisasi order book/likuiditas, teks tebal yang mudah dibaca di ponsel.
* **Alur Persetujuan:**
  1. Render video selesai secara lokal/cloud.
  2. Agen mengirim pesan ke Telegram Owner berisi: link preview video dan dua tombol interaktif (`[Setujui & Publikasikan]` / `[Revisi]`).
  3. Video hanya diunggah ke akun TikTok `@phantom_intelligence` setelah Owner menekan tombol setuju.

### D. Divisi 3: Propaganda Telegram (Komunitas 2.300 Member)
* **Wadah:** Grup publik Telegram `t.me/phantomsmcid`.
* **Identitas Akun:** Bot resmi terverifikasi dengan persona analis institusi yang objektif dan tenang.
* **Jadwal & Frekuensi Posting:**
  * **Pukul 08.00 WIB (Sesi Asia):** Peta likuiditas harian dan zona harga penting.
  * **Pukul 14.00 WIB (Sesi London):** Konfirmasi reaksi harga dan volume transaksi.
  * **Pukul 19.00 WIB (Sesi New York):** Peringatan volatilitas berita penting dan analisis geopolitik beserta visual infografis data.
* **Komponen Pesan Wajib:** Setiap pesan menyertakan tombol inline:
  `[⚡ Buka Akses PRO Gratis]` yang langsung mengarahkan pengguna ke bot onboarding.

### E. Divisi 4: Onboarding & Konversi Broker
* Menyediakan 3 kali percobaan gratis analisis instan per hari bagi pengguna baru.
* Memberikan opsi aktivasi akun tak terbatas tanpa biaya dengan cara memasukkan nomor akun MT5 di bawah broker mitra resmi.
* Memvalidasi akun secara otomatis untuk mengaktifkan akses fitur webhook dan auto-execute.

---

## 3. Kantor Pixel (Pixel Agents HQ Interface)

Untuk memantau operasional agen secara transparan, seluruh agen dipetakan ke dalam antarmuka kantor pixel 16-bit (*Pixel Agents*):

1. **Meja CEO (Hermes):** Menampilkan status orkestrasi, log persetujuan dari Owner, dan ringkasan metrik harian.
2. **Meja Riset Makro:** Menampilkan terminal data pasar live dan status kalender ekonomi.
3. **Studio Remotion:** Menampilkan status render video (Idle, Rendering, Waiting Approval, Uploaded).
4. **Meja Komunitas Telegram:** Menampilkan riwayat broadcast dan tingkat interaksi member grup.
5. **Meja Verifikasi Onboarding:** Menampilkan jumlah pengguna aktif yang menghubungkan akun MT5.

Setiap workstation dapat diklik untuk membaca aktivitas terbaru agen yang bersangkutan.

---

## 4. Tahapan Implementasi

* **Fase 1: Fondasi & Dokumentasi**
  * Finalisasi master plan dan sinkronisasi ke repositori GitHub.
* **Fase 2: Pembuatan Kantor Pixel**
  * Setup workspace Pixel Agents dengan denah ruangan khusus tim marketing dan riset.
* **Fase 3: Pipeline Konten Remotion**
  * Pembuatan template video React 9:16 untuk analisis pasar dan setup skrip render otomatis.
* **Fase 4: Integrasi Bot Telegram & Sistem Approval**
  * Pemasangan handler persetujuan ke chat pribadi Owner dan automasi broadcast ke grup publik.
* **Fase 5: Peluncuran Penuh**
  * Uji coba siklus harian dari deteksi berita, produksi video, approval, hingga konversi member.
