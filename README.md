# Phantom Agency — Autonomous Marketing & Pixel Office

Sistem agensi pemasaran dan aktivasi komunitas otonom untuk **Phantom Intelligence**. Ditenagai oleh multi-agen AI dengan pengawasan manusia (Human-in-the-loop) dan divisualisasikan melalui kantor pixel interaktif.

---

## 🏢 Struktur Divisi & Peran

1. **Hermes CEO (Chief Orchestrator)**
   * Mengatur jadwal kerja, mengaudit kualitas konten, dan mengirim notifikasi persetujuan (approval) ke Telegram Owner.
2. **Divisi 1: Macro Intel & Market Researcher**
   * Memantau berita geopolitik dunia (contoh: eskalasi Selat Hormuz) dan kalender ekonomi (CPI, Fed, NFP) untuk merumuskan dampaknya ke likuiditas emas (XAUUSD).
3. **Divisi 2: Video Production (Remotion.dev + TikTok)**
   * Menghasilkan video vertikal 9:16 berbasis kode secara terprogram menggunakan Remotion (React), dan meminta ACC Owner sebelum publish ke TikTok `@phantom_intelligence`.
4. **Divisi 3: Propaganda Telegram (Komunitas 2.300+ Member)**
   * Mengirim laporan teknis dan infografis visual ke grup publik `t.me/phantomsmcid` disertai tombol `[⚡ Dapatkan Akses PRO Gratis]`.
5. **Divisi 4: Onboarding & Partner Sync**
   * Mengkonversi pengguna bot ke akun broker rekanan resmi (Exness) untuk membuka akses tak terbatas tanpa biaya langganan bulanan.

---

## 📁 Struktur Direktori

```
phantom-agency/
├── agency/
│   └── agents/
│       ├── 01_hermes_ceo.md
│       ├── 02_macro_intel.md
│       ├── 03_video_creator_remotion.md
│       ├── 04_telegram_propaganda.md
│       └── 05_onboarding_partner_sync.md
├── docs/
│   └── MASTER_PLAN_AUTONOMOUS_AGENCY.md
├── scripts/
│   └── pixel_office_controller.py
└── README.md
```

---

## 🎮 Menjalankan Kantor Pixel

Kantor pixel berjalan di atas antarmuka **Pixel Agents**:

```bash
# 1. Jalankan Pixel Agents Server
npx pixel-agents --port 3200 --host 127.0.0.1

# 2. Jalankan Controller Agen
python scripts/pixel_office_controller.py
```

Buka browser di: `http://127.0.0.1:3200`
