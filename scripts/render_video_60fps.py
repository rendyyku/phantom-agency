#!/usr/bin/env python3
"""
Phantom Agency — Ultra Smooth 60FPS Video Renderer (TikTok 9:16)
Renders high-definition vertical MP4 video with real TTS audio voiceover,
animated candlestick charts, liquidity heatmap, kinetic typography, and CTA.
"""

import os
import sys
import math
import subprocess
import time
from PIL import Image, ImageDraw, ImageFont

WIDTH = 1080
HEIGHT = 1920
FPS = 60

CWD = "C:/Users/phantom/Desktop/PHANTOM/phantom-agency"
AUDIO_PATH = os.path.join(CWD, "remotion", "voiceover.mp3")
OUT_DIR = os.path.join(CWD, "remotion", "out")
os.makedirs(OUT_DIR, exist_ok=True)
OUT_PATH = os.path.join(OUT_DIR, "xauusd_viral_60fps.mp4")

# Fonts
FONT_HEADING = ImageFont.truetype("C:/Windows/Fonts/bahnschrift.ttf", 74)
FONT_SUBHEADING = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 46)
FONT_BODY = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 36)
FONT_MONO = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 32)
FONT_MONO_BIG = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 52)
FONT_CAPTION = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 34)
FONT_CTA = ImageFont.truetype("C:/Windows/Fonts/bahnschrift.ttf", 56)

def get_audio_duration(path: str) -> float:
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    try:
        return float(res.stdout.strip())
    except:
        return 41.38

def draw_header(draw, frame: int):
    # Top header bar
    # Red Live Blinking Dot
    blink = (frame // 25) % 2 == 0
    dot_color = (248, 81, 73) if blink else (130, 40, 36)
    draw.ellipse([60, 75, 80, 95], fill=dot_color)
    draw.text((95, 70), "LIVE TERMINAL • PHANTOM AI SWARM", font=FONT_MONO, fill=(139, 148, 158))
    
    # Pair Badge
    draw.rounded_rectangle([820, 62, 1020, 108], radius=10, fill=(240, 136, 62))
    draw.text((845, 66), "XAUUSD M5", font=ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 26), fill=(0, 0, 0))
    
    # Dividing line
    draw.line([(60, 125), (1020, 125)], fill=(48, 54, 61), width=2)

def draw_caption_box(draw, text: str):
    # Fixed subtitle box near the bottom
    box_y1 = 1580
    box_y2 = 1760
    draw.rounded_rectangle([60, box_y1, 1020, box_y2], radius=18, fill=(13, 17, 23), outline=(88, 166, 255), width=3)
    
    # Word wrap or 2 lines
    words = text.split(" ")
    line1 = []
    line2 = []
    for w in words:
        if len(" ".join(line1 + [w])) < 42:
            line1.append(w)
        else:
            line2.append(w)
    
    txt1 = " ".join(line1)
    txt2 = " ".join(line2)
    
    bbox1 = draw.textbbox((0, 0), txt1, font=FONT_CAPTION)
    w1 = bbox1[2] - bbox1[0]
    draw.text(((WIDTH - w1) // 2, box_y1 + 35), txt1, font=FONT_CAPTION, fill=(255, 255, 255))
    
    if txt2:
        bbox2 = draw.textbbox((0, 0), txt2, font=FONT_CAPTION)
        w2 = bbox2[2] - bbox2[0]
        draw.text(((WIDTH - w2) // 2, box_y1 + 88), txt2, font=FONT_CAPTION, fill=(201, 209, 217))

# Pre-render static background grid
BG_STATIC = Image.new("RGB", (WIDTH, HEIGHT), color=(8, 11, 17))
_bg_draw = ImageDraw.Draw(BG_STATIC)
for y in range(0, HEIGHT, 60):
    _bg_draw.line([(0, y), (WIDTH, y)], fill=(20, 26, 36), width=1)
for x in range(0, WIDTH, 60):
    _bg_draw.line([(x, 0), (x, HEIGHT)], fill=(20, 26, 36), width=1)

def render_frame(frame: int, total_frames: int) -> bytes:
    img = BG_STATIC.copy()
    draw = ImageDraw.Draw(img)
        
    draw_header(draw, frame)
    
    sec = frame / FPS
    
    # SCENE 1: HOOK (0s - 6s)
    if sec < 6.0:
        # Radar circle in center
        radar_rad = 180 + int(30 * math.sin(frame * 0.1))
        cx, cy = WIDTH // 2, 850
        draw.ellipse([cx - radar_rad, cy - radar_rad, cx + radar_rad, cy + radar_rad], outline=(35, 134, 54), width=3)
        draw.ellipse([cx - 80, cy - 80, cx + 80, cy + 80], outline=(88, 166, 255), width=2)
        # Radar scanline
        angle = (frame * 0.08)
        sweep_x = cx + int(radar_rad * math.cos(angle))
        sweep_y = cy + int(radar_rad * math.sin(angle))
        draw.line([(cx, cy), (sweep_x, sweep_y)], fill=(63, 185, 80), width=4)
        
        # Kinetic Titles
        draw.text((100, 320), "APA SIH YANG TERJADI", font=FONT_HEADING, fill=(240, 246, 252))
        draw.text((100, 420), "HARI INI?", font=FONT_HEADING, fill=(210, 153, 34))
        
        draw.text((100, 560), "GOLD GIMANA, JUNAM ATAU FLY?", font=FONT_SUBHEADING, fill=(139, 148, 158))
        draw.text((100, 630), "TERUS ADA BERITA APA SIH?", font=FONT_SUBHEADING, fill=(88, 166, 255))
        
        draw_caption_box(draw, "Apa sih yang terjadi hari ini? Gold gimana, junam atau fly? Terus ada berita apa sih?")

    # SCENE 2: FLY 700 PIPS & NEWS (6s - 18s)
    elif sec < 18.0:
        draw.text((80, 220), "EXPANSION ALERT", font=FONT_SUBHEADING, fill=(63, 185, 80))
        draw.text((80, 300), "GOLD FLY 700 PIPS", font=FONT_HEADING, fill=(63, 185, 80))
        draw.text((80, 400), "TANPA RETRACE SAMA SEKALI", font=FONT_SUBHEADING, fill=(240, 246, 252))
        
        # Live Price Box
        draw.rounded_rectangle([80, 480, 1000, 600], radius=16, fill=(13, 17, 23), outline=(63, 185, 80), width=3)
        draw.text((120, 510), "SPOT XAUUSD:", font=FONT_MONO, fill=(139, 148, 158))
        draw.text((450, 500), "$4,194.30", font=FONT_MONO_BIG, fill=(63, 185, 80))
        
        # Candlestick Chart Animation
        chart_top = 660
        chart_bot = 1120
        draw.rounded_rectangle([80, chart_top, 1000, chart_bot], radius=16, fill=(13, 17, 23), outline=(48, 54, 61), width=2)
        
        # Candles
        candles = [
            (140, 950, 990, False),
            (210, 920, 960, True),
            (280, 930, 970, False),
            (350, 900, 940, True),
            (420, 880, 920, True),
            (490, 860, 900, True),
            (560, 840, 880, True),
            (630, 820, 860, True),
            (700, 800, 840, True),
            (770, 780, 820, True),
        ]
        for cx, top, bot, is_green in candles:
            col = (63, 185, 80) if is_green else (248, 81, 73)
            # Wick
            draw.line([(cx, top - 20), (cx, bot + 20)], fill=col, width=3)
            # Body
            draw.rectangle([cx - 18, top, cx + 18, bot], fill=col)
            
        # The Giant Pumping Candle (Grows with frame!)
        progress_s2 = min(1.0, (sec - 6.0) / 4.0)
        lead_x = 880
        lead_bot = 820
        lead_top = int(lead_bot - (420 * progress_s2))
        # Wick
        draw.line([(lead_x, lead_top - 30), (lead_x, lead_bot + 10)], fill=(63, 185, 80), width=6)
        # Body
        draw.rectangle([lead_x - 30, lead_top, lead_x + 30, lead_bot], fill=(63, 185, 80))
        
        # News Notification Banner
        draw.rounded_rectangle([80, 1170, 1000, 1480], radius=16, fill=(22, 27, 34), outline=(248, 81, 73), width=3)
        draw.text((120, 1205), "🚨 NEWS GEOPOLITIK TERBARU:", font=FONT_BODY, fill=(248, 81, 73))
        draw.text((120, 1270), "Tensi Selat Hormuz Memanas!", font=FONT_SUBHEADING, fill=(240, 246, 252))
        draw.text((120, 1345), "Aliran tanker minyak turun drastis 27%.", font=FONT_BODY, fill=(201, 209, 217))
        draw.text((120, 1405), "Safe-haven volume tersedot ke Gold.", font=FONT_BODY, fill=(88, 166, 255))
        
        draw_caption_box(draw, "Gold fly 700 pips tanpa retrace semalam, langsung nyentuh 4194. Lihat tuh ada news: Tensi Selat Hormuz memanas lagi, aliran tanker minyak drop 27%.")

    # SCENE 3: JEBAKAN PUCUK (18s - 29s)
    elif sec < 29.0:
        draw.text((80, 220), "PERINGATAN INSTITUSI", font=FONT_SUBHEADING, fill=(248, 81, 73))
        draw.text((80, 300), "AWAS JEBAKAN PUCUK!", font=FONT_HEADING, fill=(248, 81, 73))
        draw.text((80, 400), "LIQUIDITY SWEEP ZONE", font=FONT_SUBHEADING, fill=(240, 246, 252))
        
        # Resistance Pool Box
        draw.rounded_rectangle([80, 500, 1000, 780], radius=16, fill=(43, 16, 22), outline=(248, 81, 73), width=4)
        draw.text((120, 530), "AREA TARGET JEBAKAN:", font=FONT_BODY, fill=(248, 81, 73))
        draw.text((120, 600), "RESISTENSI 4.198 - 4.200", font=FONT_HEADING, fill=(255, 255, 255))
        draw.text((120, 700), "Likuiditas Stop Loss Seller Menggunung di Sini", font=FONT_BODY, fill=(201, 209, 217))
        
        # Sentiment Cards
        # Seller Card (Red)
        draw.rounded_rectangle([80, 840, 1000, 1060], radius=16, fill=(22, 27, 34), outline=(248, 81, 73), width=2)
        draw.text((120, 875), "❌ TEAM SELLER (RETAIL COUNTER TREND)", font=FONT_BODY, fill=(248, 81, 73))
        draw.text((120, 940), "NICE TRY SELLER! Kena sapu ekspansi.", font=FONT_SUBHEADING, fill=(240, 246, 252))
        
        # Buyer Card (Green)
        draw.rounded_rectangle([80, 1120, 1000, 1340], radius=16, fill=(15, 43, 34), outline=(63, 185, 80), width=2)
        draw.text((120, 1155), "✅ TEAM BUYER (SMART MONEY DISCIPLINE)", font=FONT_BODY, fill=(63, 185, 80))
        draw.text((120, 1220), "SELAMAT BUYER yang hold dari bawah!", font=FONT_SUBHEADING, fill=(240, 246, 252))
        
        draw_caption_box(draw, "Hati-hati jebakan pucuk di area 4198 sampai 4200. Nice try seller yang nekat counter trend, selamat buyer yang hold dari bawah.")

    # SCENE 4: CTA FINAL & REALTIME AI AGENT (29s - END)
    else:
        # Pulsing Glow Frame
        pulse_val = int(20 * math.sin(frame * 0.15))
        draw.rounded_rectangle([60, 320, 1020, 1450], radius=24, fill=(13, 17, 23), outline=(31, 111, 235), width=5)
        
        draw.text((100, 400), "PHANTOM INTELLIGENCE", font=FONT_MONO, fill=(88, 166, 255))
        draw.text((100, 480), "INGIN AI AGENT", font=FONT_HEADING, fill=(255, 255, 255))
        draw.text((100, 580), "UNTUK ANALISIS", font=FONT_HEADING, fill=(255, 255, 255))
        draw.text((100, 680), "REALTIME?", font=FONT_HEADING, fill=(63, 185, 80))
        
        draw.text((100, 840), "• Pantau ekspansi & likuiditas 24/7", font=FONT_SUBHEADING, fill=(201, 209, 217))
        draw.text((100, 920), "• Radar deteksi news global instan", font=FONT_SUBHEADING, fill=(201, 209, 217))
        draw.text((100, 1000), "• Tanpa sinyal sampah, full data", font=FONT_SUBHEADING, fill=(201, 209, 217))
        
        # MEGA CTA BUTTON
        btn_y = 1150
        draw.rounded_rectangle([100, btn_y, 980, btn_y + 160], radius=20, fill=(35, 134, 54), outline=(63, 185, 80), width=4)
        draw.text((140, btn_y + 45), "⚡ AKSES GRATIS DI BIO", font=FONT_CTA, fill=(255, 255, 255))
        
        draw_caption_box(draw, "Ingin AI agent untuk analisis realtime? Akses gratis di bio.")
        
    return img.tobytes()

def main():
    print(f"🎬 RENDERING 60FPS VIRAL TIKTOK VIDEO (9:16)...")
    dur = get_audio_duration(AUDIO_PATH)
    total_frames = int(dur * FPS)
    print(f"• Audio Duration: {dur:.2f}s ({total_frames} frames @ 60fps)")
    print(f"• Target Resolution: {WIDTH}x{HEIGHT} (1080x1920)")
    print(f"• Audio Source: {AUDIO_PATH}")
    print(f"• Output File: {OUT_PATH}\n")
    
    cmd = [
        "ffmpeg", "-y",
        "-loglevel", "error",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{WIDTH}x{HEIGHT}",
        "-pix_fmt", "rgb24",
        "-r", str(FPS),
        "-i", "-",
        "-i", AUDIO_PATH,
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-crf", "20",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        OUT_PATH
    ]
    
    t0 = time.time()
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
    assert proc.stdin is not None
    
    for f in range(total_frames):
        raw = render_frame(f, total_frames)
        proc.stdin.write(raw)
        if f % 300 == 0 or f == total_frames - 1:
            elapsed = time.time() - t0
            speed = (f + 1) / max(0.001, elapsed)
            pct = ((f + 1) / total_frames) * 100
            print(f"  Rendering: {pct:.1f}% ({f}/{total_frames} frames) - {speed:.1f} fps")
            
    proc.stdin.close()
    proc.wait()
    dt = time.time() - t0
    
    size_mb = os.path.getsize(OUT_PATH) / (1024 * 1024)
    print(f"\n\n✅ SELESAI! Video 60fps berhasil dirender!")
    print(f"• Total Waktu Render: {dt:.1f}s")
    print(f"• Ukuran File: {size_mb:.2f} MB")
    print(f"• Path Video MP4: {OUT_PATH}")

if __name__ == "__main__":
    main()
