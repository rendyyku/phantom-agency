#!/usr/bin/env python3
"""
Agent 01: Hermes CEO — Autonomous Task Execution
Simulates and executes the CEO's morning orchestration workflow,
streaming live visual state to Pixel Agents HQ (http://127.0.0.1:3200).
"""
import os
import sys
import time
import json
import urllib.request
import urllib.error

TOKEN = "40f05fe0-7bde-4ea9-8ef1-e82dd8bb8b58"
PORT = 3200
BASE_URL = f"http://127.0.0.1:{PORT}"
CWD = "C:/Users/phantom/Desktop/PHANTOM/phantom-agency"

def send_hook(event_name: str, **kwargs):
    payload = {
        "session_id": "01-hermes-ceo",
        "hook_event_name": event_name,
        "cwd": CWD,
        **kwargs
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{BASE_URL}/api/hooks/claude",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {TOKEN}"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=3) as resp:
            return resp.read().decode("utf-8")
    except Exception as e:
        return f"Hook Err: {e}"

def log_step(step_num: int, title: str, details: str):
    print(f"\n========================================================")
    print(f"💼 [HERMES CEO - STEP {step_num}] {title}")
    print(f"========================================================")
    print(details)

def run():
    print("👔 HERMES CEO: Mengambil kendali kantor Phantom Agency...\n")
    
    # 0. Start Session in Pixel Office
    send_hook("SessionStart")
    time.sleep(1)

    # 1. Macro Scan
    log_step(1, "SCAN BERITA GLOBAL & GEOPOLITIK", 
             "• Membuka feed berita geopolitik dan kalender ekonomi.\n"
             "• Menemukan isu panas: Tensi Selat Hormuz, trafik tanker turun 27%.\n"
             "• Harga emas (XAUUSD) tertahan di zona supply $4.194 / oz.")
    
    send_hook("PreToolUse", tool_name="WebSearch", tool_input={"query": "XAUUSD Strait of Hormuz tanker disruption & liquidity"})
    time.sleep(2.5)
    send_hook("PostToolUse", tool_name="WebSearch", tool_output="Ditemukan: Safe-haven demand menguat, zona likuiditas atas di $4.198 - $4.215.")
    time.sleep(1)

    # 2. Market Structure Audit
    log_step(2, "AUDIT STRUKTUR LIKUIDITAS EMAS (XAUUSD)",
             "• Analisis: Konflik bukan sekadar kenaikan harga, tapi jebakan likuiditas.\n"
             "• Retail trader panik buy di pucuk resistance $4.195.\n"
             "• Institusi mengincar stop loss di bawah $4.178 sebelum ekspansi berlanjut.")
    
    send_hook("PreToolUse", tool_name="Read", tool_input={"file_path": "agency/agents/02_macro_intel.md"})
    time.sleep(2.5)
    send_hook("PostToolUse", tool_name="Read", tool_output="Framework Macro Intel terverifikasi.")
    time.sleep(1)

    # 3. Create Strategic Directive
    directive_dir = os.path.join(CWD, "agency", "directives")
    os.makedirs(directive_dir, exist_ok=True)
    directive_file = os.path.join(directive_dir, "2026-10-11_macro_brief.json")

    directive_data = {
        "timestamp": "2026-10-11T02:50:00Z",
        "market": "XAUUSD",
        "current_price": 4194.32,
        "key_event": "Gangguan navigasi tanker Selat Hormuz (-27% traffic)",
        "thesis": "Kenaikan premi risiko safe-haven tertahan resistensi 4.198. Potensi sweep likuiditas bawah di 4.180 sebelum dorongan tren naik.",
        "video_hook": "Jangan FOMO buy emas di $4.194 gara-gara berita Selat Hormuz semalam. Ini yang sebenarnya diincar institusi.",
        "telegram_focus": "Peta Likuiditas Sesi London: Bahas spread melebar dan jebakan pending order mepet.",
        "conversion_cta": "Akses Peta Likuiditas Real-time & Bot MT5: 100% Gratis via Partner Broker."
    }

    with open(directive_file, "w", encoding="utf-8") as f:
        json.dump(directive_data, f, indent=2)

    log_step(3, "MENERBITKAN BRIEF STRATEGIS DIVISI",
             f"• Berkas arahan disimpan ke: agency/directives/2026-10-11_macro_brief.json\n"
             "• Menetapkan Angle Konten: Bongkar jebakan buy FOMO berita Selat Hormuz.")

    send_hook("PreToolUse", tool_name="Write", tool_input={"file_path": "agency/directives/2026-10-11_macro_brief.json"})
    time.sleep(2.5)
    send_hook("PostToolUse", tool_name="Write", tool_output="Brief tersimpan.")
    time.sleep(1)

    # 4. Delegate to Video Creator (Remotion)
    log_step(4, "MENUGASKAN DIVISI VIDEO (REMOTION.DEV)",
             "• Perintah ke Agent 03 (Video Creator):\n"
             "  - Render video 9:16 durasi 40 detik.\n"
             "  - Visual: Animasi orderbook XAUUSD + garis sweep likuiditas 4.180.\n"
             "  - Status video: Menunggu render & siap untuk review Owner.")
    
    send_hook("PreToolUse", tool_name="SendMessage", tool_input={"recipient": "Agent 03 (Video Creator): Render video Hormuz_Gold_Sweep_9x16"})
    time.sleep(2.5)
    send_hook("PostToolUse", tool_name="SendMessage", tool_output="Agent 03 menerima tugas.")
    time.sleep(1)

    # 5. Delegate to Telegram Propaganda
    log_step(5, "MENUGASKAN DIVISI TELEGRAM (2.3K MEMBER)",
             "• Perintah ke Agent 04 (Tele Propaganda):\n"
             "  - Siapkan infografis rute tanker Hormuz vs grafik harga emas.\n"
             "  - Jadwalkan rilis pukul 14.00 WIB (Sesi London).\n"
             "  - Lampirkan inline button: [⚡ Dapatkan Akses PRO Gratis].")

    send_hook("PreToolUse", tool_name="SendMessage", tool_input={"recipient": "Agent 04 (Tele Propaganda): Schedule London Brief + Free PRO Button"})
    time.sleep(2.5)
    send_hook("PostToolUse", tool_name="SendMessage", tool_output="Agent 04 menjadwalkan broadcast.")
    time.sleep(1)

    # 6. Compose Owner Approval Report
    log_step(6, "MENYUSUN LAPORAN APPROVAL KE TELEGRAM OWNER",
             "• Hermes CEO menyelesaikan seluruh delegasi kerja.\n"
             "• Menyusun draft pesan preview untuk Owner:\n"
             "--------------------------------------------------\n"
             "🔔 [REVIEW KONTEN MARKETING - SIAP APPROVAL]\n"
             "Topik: Selat Hormuz & Jebakan Buy Pucuk Emas $4.194\n"
             "Format: Video TikTok 9:16 + Poster Infografis Tele\n"
             "Target: Publikasi TikTok @phantom_intelligence & Grup 2.3k Member\n"
             "Tindakan Diperlukan: Klik [ACC] untuk langsung publish otomatis.\n"
             "--------------------------------------------------")

    send_hook("PreToolUse", tool_name="SendMessage", tool_input={"recipient": "Telegram Owner: Approval Notification Sent"})
    time.sleep(2)
    send_hook("PostToolUse", tool_name="SendMessage", tool_output="Notifikasi terkirim.")
    
    print("\n✅ Selesai. Hermes CEO telah mengkoordinasikan seluruh tim secara otonom.")
    print("👉 Cek tampilan animasinya di browser: http://127.0.0.1:3200\n")

if __name__ == "__main__":
    run()
