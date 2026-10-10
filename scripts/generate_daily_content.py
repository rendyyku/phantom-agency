#!/usr/bin/env python3
"""
Phantom Agency — Daily Content & Propaganda Generator
Produces real human-style trader copy for:
1. TikTok 9:16 Script (Remotion)
2. Telegram Community Broadcast (t.me/phantomsmcid)
3. Owner Approval Telegram Alert
"""

import os
import sys
import json
import argparse
from datetime import datetime

def generate_campaign(
    action: str = "fly",
    pips: int = 700,
    retrace: bool = False,
    news: str = "Tensi Selat Hormuz memanas lagi, aliran tanker minyak drop 27%",
    pair: str = "XAUUSD",
    price: float = 4194.30,
    trap_zone: str = "4.198 - 4.200"
):
    retrace_str = "ada retrace santai" if retrace else "tanpa retrace sama sekali"
    
    if action.lower() == "fly":
        action_verb = f"fly {pips} pips {retrace_str}"
        pemenang = "selamat buyer yang hold dari bawah"
        pecundang = "nice try seller yang nekat counter trend"
        jebakan = f"jebakan pucuk di area {trap_zone}"
    else:
        action_verb = f"junam {pips} pips {retrace_str}"
        pemenang = "selamat seller yang sabar nunggu breakdown"
        pecundang = "nice try buyer yang nyerok pisau jatuh"
        jebakan = f"jebakan lembah di area {trap_zone}"

    # 1. TikTok Script (Format Remotion 9:16, 35-40 detik)
    tiktok_script = f"""# TIKTOK 9:16 SCRIPT — PHANTOM INTELLIGENCE
[DURASI: 38 DETIK | VISUAL: CHART {pair} + ORDERBOOK LIQUIDITY HEATMAP]

[00:00 - 00:06 | TEXT ON SCREEN: "APA YANG TERJADI HARI INI?"]
Voiceover: "Apa sih yang terjadi hari ini? Gold gimana, junam atau fly? Terus ada berita apa sih?"

[00:06 - 00:18 | VISUAL: REPLAY CHART CANDLESTICK M5 EXPANSION]
Voiceover: "Gold {action_verb} semalam langsung nyentuh {price}. Lihat tuh ada news: {news}."

[00:18 - 00:28 | VISUAL: HEATMAP LIQUIDITY RED ZONE]
Voiceover: "Hati-hati {jebakan}. {pecundang}, {pemenang}."

[00:28 - 00:38 | VISUAL: INTERFACE TERMINAL PHANTOM AI]
Voiceover: "Ingin AI agent untuk analisis realtime? Akses gratis di bio."
"""

    # 2. Telegram Group Broadcast (2.300+ Members)
    telegram_post = f"""[PHANTOM INTEL — UPDATE {pair}]

Apa sih yang terjadi hari ini? Gold {action_verb} langsung nyentuh area {price}.

Ada news apa hari ini? {news}.

Hati-hati {jebakan}. {pecundang}, {pemenang}.

Ingin AI agent untuk analisis realtime? Akses gratis di bio.

[⚡ Dapatkan Akses PRO Gratis]"""

    # 3. Owner Approval Alert
    approval_alert = f"""🔔 [KONTEN BARU SIAP REVIEW — OWNER APPROVAL]

Topik: {pair} {action_verb} ({news[:45]}...)
Format: Video TikTok 9:16 + Broadcast Grup Telegram

Preview Teks TikTok:
"Apa sih yang terjadi hari ini? Gold {action_verb}... Ingin AI agent untuk analisis realtime? Akses gratis di bio."

Pilihan:
[✅ ACC & JALANKAN]  [🔄 REVISI]"""

    return {
        "timestamp": datetime.now().isoformat(),
        "pair": pair,
        "action": action,
        "pips": pips,
        "news": news,
        "tiktok_script": tiktok_script,
        "telegram_post": telegram_post,
        "approval_alert": approval_alert
    }

def main():
    parser = argparse.ArgumentParser(description="Generate Daily Phantom Campaign")
    parser.add_argument("--action", default="fly", choices=["fly", "junam"])
    parser.add_argument("--pips", type=int, default=700)
    parser.add_argument("--retrace", action="store_true")
    parser.add_argument("--news", default="Tensi Selat Hormuz memanas lagi, aliran tanker minyak drop 27%")
    parser.add_argument("--price", type=float, default=4194.30)
    args = parser.parse_args()

    campaign = generate_campaign(
        action=args.action,
        pips=args.pips,
        retrace=args.retrace,
        news=args.news,
        price=args.price
    )

    out_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "agency", "campaigns")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "latest_campaign.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(campaign, f, indent=2)

    print("\n" + "="*60)
    print("🎬 HASIL GENERATE SCRIPT TIKTOK (REMOTION):")
    print("="*60)
    print(campaign["tiktok_script"])

    print("\n" + "="*60)
    print("📢 HASIL BROADCAST GRUP TELEGRAM (2.3K MEMBER):")
    print("="*60)
    print(campaign["telegram_post"])

    print("\n" + "="*60)
    print("📱 LAPORAN KE TELEGRAM OWNER (UNTUK ACC):")
    print("="*60)
    print(campaign["approval_alert"])
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
