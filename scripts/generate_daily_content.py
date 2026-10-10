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

def generate_post_market_campaign(
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
        pemenang = "selamat buyer yang udah hold dari bawah"
        pecundang = "nice try seller yang nekat counter trend"
        jebakan = f"jebakan pucuk di area {trap_zone}"
    else:
        action_verb = f"junam {pips} pips {retrace_str}"
        pemenang = "selamat seller yang sabar nunggu breakdown"
        pecundang = "nice try buyer yang nyerok pisau jatuh"
        jebakan = f"jebakan lembah di area {trap_zone}"

    tiktok_script = f"""# TIKTOK 9:16 SCRIPT — PHANTOM INTELLIGENCE (POST-MARKET REPLAY)
[DURASI: 38 DETIK | VISUAL: CHART {pair} + HEATMAP LIQUIDITY]

[00:00 - 00:06 | TEXT ON SCREEN: "APA YANG TERJADI HARI INI?"]
Voiceover: "Apa sih yang terjadi hari ini? Gold gimana, junam atau fly? Terus ada berita apa sih?"

[00:06 - 00:18 | VISUAL: REPLAY CANDLESTICK EXPANSION]
Voiceover: "Gold {action_verb} semalam langsung nyentuh {price}. Lihat tuh ada news: {news}."

[00:18 - 00:28 | VISUAL: HEATMAP LIQUIDITY RED ZONE]
Voiceover: "Hati-hati {jebakan}. {pecundang}, {pemenang}."

[00:28 - 00:38 | VISUAL: TERMINAL PHANTOM AI]
Voiceover: "Ingin AI agent untuk analisis realtime? Akses gratis di bio."
"""

    telegram_post = f"""[PHANTOM INTEL — UPDATE {pair}]

Apa sih yang terjadi hari ini? Gold {action_verb} langsung nyentuh area {price}.

Ada news apa hari ini? {news}.

Hati-hati {jebakan}. {pecundang}, {pemenang}.

Ingin AI agent untuk analisis realtime? Akses gratis di bio.

[⚡ Dapatkan Akses PRO Gratis]"""

    approval_alert = f"""🔔 [KONTEN POST-MARKET SIAP REVIEW — OWNER APPROVAL]

Topik: {pair} {action_verb}
News: {news}
Format: Video TikTok 9:16 + Broadcast Grup Telegram

Preview Teks:
"Apa sih yang terjadi hari ini? Gold {action_verb}... Ingin AI agent untuk analisis realtime? Akses gratis di bio."

Pilihan:
[✅ ACC & JALANKAN]  [🔄 REVISI]"""

    return {
        "type": "post_market",
        "timestamp": datetime.now().isoformat(),
        "pair": pair,
        "tiktok_script": tiktok_script,
        "telegram_post": telegram_post,
        "approval_alert": approval_alert
    }

def generate_pre_news_campaign(
    news_name: str = "FOMC Rate Decision",
    release_time: str = "01:00 WIB dini hari",
    pair: str = "XAUUSD",
    price: float = 4194.30,
    macro_context: str = "The Fed diprediksi tahan suku bunga, tapi inflasi masih kencang",
    status_chart: str = "nahan di zona resistensi 4.190 - 4.195",
):
    tiktok_script = f"""# TIKTOK 9:16 SCRIPT — PHANTOM INTELLIGENCE (PRE-NEWS RADAR)
[DURASI: 38 DETIK | VISUAL: RADAR KALENDER EKONOMI + CHART {pair}]

[00:00 - 00:06 | TEXT ON SCREEN: "NEWS BESAR MALAM INI!"]
Voiceover: "Nanti malam jam {release_time} ada rilis news besar: {news_name}."

[00:06 - 00:18 | VISUAL: DATA MAKRO THE FED & INFLASI]
Voiceover: "Kondisi makro gimana? {macro_context}. Posisi {pair} sekarang lagi {status_chart}."

[00:18 - 00:28 | VISUAL: VOTING POLLING BUYER VS SELLER]
Voiceover: "Kalian tim seller atau buyer malam ini? Hati-hati spread melebar dan slippage liar pas detik-detik rilis."

[00:28 - 00:38 | VISUAL: PHANTOM AI LIVE RADAR]
Voiceover: "Ingin AI agent untuk analisis realtime? Akses gratis di bio."
"""

    telegram_post = f"""[WAR ROOM — ANTISIPASI HIGH IMPACT NEWS]

Nanti malam jam {release_time} ada rilis news: {news_name}.

Kondisi makro gimana?
{macro_context}. Emas ({pair}) sekarang lagi {status_chart}.

Kalian masuk tim mana malam ini?
🔴 Team Seller
🟢 Team Buyer

Jangan nekat pasang pending order terlalu mepet ke harga aktif kalau gak mau kena slippage.

Ingin AI agent untuk analisis realtime? Akses gratis di bio.

[⚡ Dapatkan Akses PRO Gratis]"""

    approval_alert = f"""🔔 [KONTEN PRE-NEWS SIAP REVIEW — OWNER APPROVAL]

Topik: Antisipasi {news_name} ({release_time})
Konteks: {macro_context}
Format: Video TikTok 9:16 + Polling Grup Telegram

Preview Teks:
"Nanti malam jam {release_time} ada rilis {news_name}... Kalian tim seller atau buyer? Ingin AI agent untuk analisis realtime? Akses gratis di bio."

Pilihan:
[✅ ACC & JALANKAN]  [🔄 REVISI]"""

    return {
        "type": "pre_news",
        "timestamp": datetime.now().isoformat(),
        "pair": pair,
        "tiktok_script": tiktok_script,
        "telegram_post": telegram_post,
        "approval_alert": approval_alert
    }

def main():
    parser = argparse.ArgumentParser(description="Generate Daily Phantom Campaign")
    parser.add_argument("--mode", default="pre_news", choices=["post_market", "pre_news"])
    parser.add_argument("--action", default="fly", choices=["fly", "junam"])
    parser.add_argument("--pips", type=int, default=700)
    parser.add_argument("--retrace", action="store_true")
    parser.add_argument("--news", default="Tensi Selat Hormuz memanas lagi, aliran tanker minyak drop 27%")
    parser.add_argument("--news-name", default="FOMC Rate Decision")
    parser.add_argument("--time", default="01:00 WIB dini hari")
    parser.add_argument("--macro", default="The Fed diprediksi tahan suku bunga, tapi inflasi masih kencang")
    parser.add_argument("--price", type=float, default=4194.30)
    args = parser.parse_args()

    if args.mode == "pre_news":
        campaign = generate_pre_news_campaign(
            news_name=args.news_name,
            release_time=args.time,
            macro_context=args.macro,
            price=args.price
        )
    else:
        campaign = generate_post_market_campaign(
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
    print(f"🎬 HASIL GENERATE SCRIPT TIKTOK ({args.mode.upper()}):")
    print("="*60)
    print(campaign["tiktok_script"])

    print("\n" + "="*60)
    print(f"📢 HASIL BROADCAST GRUP TELEGRAM ({args.mode.upper()}):")
    print("="*60)
    print(campaign["telegram_post"])

    print("\n" + "="*60)
    print("📱 LAPORAN KE TELEGRAM OWNER (UNTUK ACC):")
    print("="*60)
    print(campaign["approval_alert"])
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
