import React from 'react';
import {
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
  Sequence,
} from 'remotion';

export interface VideoProps {
  pair: string;
  actionText: string;
  pips: number;
  newsText: string;
  price: string;
  trapZone: string;
}

export const XAUUSDRadar: React.FC<VideoProps> = ({
  pair = 'XAUUSD',
  actionText = 'fly 700 pips tanpa retrace',
  pips = 700,
  newsText = 'Tensi Selat Hormuz memanas lagi, aliran tanker minyak drop 27%',
  price = '$4,194.30',
  trapZone = '4.198 - 4.200',
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  return (
    <div
      style={{
        flex: 1,
        backgroundColor: '#090c10',
        color: '#ffffff',
        fontFamily: 'sans-serif',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'space-between',
        padding: '80px 60px',
        position: 'relative',
        overflow: 'hidden',
      }}
    >
      {/* Top Header */}
      <div
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          borderBottom: '2px solid #30363d',
          paddingBottom: '30px',
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '15px' }}>
          <div
            style={{
              width: '20px',
              height: '20px',
              borderRadius: '50%',
              backgroundColor: '#f85149',
            }}
          />
          <span style={{ fontSize: '32px', fontWeight: 800, color: '#8b949e' }}>
            PHANTOM AI TERMINAL
          </span>
        </div>
        <div
          style={{
            backgroundColor: '#f0883e',
            color: '#000000',
            padding: '10px 24px',
            borderRadius: '12px',
            fontSize: '32px',
            fontWeight: 900,
          }}
        >
          {pair} M5
        </div>
      </div>

      {/* Sequence 1: Hook (0s - 6s) */}
      <Sequence from={0} durationInFrames={fps * 6}>
        <div style={{ textAlign: 'center', margin: 'auto 0' }}>
          <h1
            style={{
              fontSize: '84px',
              fontWeight: 900,
              lineHeight: 1.1,
              textTransform: 'uppercase',
            }}
          >
            APA SIH YANG TERJADI <span style={{ color: '#d29922' }}>HARI INI?</span>
          </h1>
          <p
            style={{
              fontSize: '44px',
              color: '#8b949e',
              marginTop: '40px',
              lineHeight: 1.4,
            }}
          >
            "Gold gimana, junam atau fly? Terus ada berita apa sih?"
          </p>
        </div>
      </Sequence>

      {/* Sequence 2: Fakta Pips & News (6s - 18s) */}
      <Sequence from={fps * 6} durationInFrames={fps * 12}>
        <div style={{ textAlign: 'center', margin: 'auto 0' }}>
          <div
            style={{
              fontSize: '40px',
              color: '#3fb950',
              fontWeight: 800,
              marginBottom: '20px',
            }}
          >
            EXPANSION ALERT
          </div>
          <h1
            style={{
              fontSize: '76px',
              fontWeight: 900,
              lineHeight: 1.1,
              color: '#3fb950',
            }}
          >
            GOLD FLY {pips} PIPS
          </h1>
          <div
            style={{
              backgroundColor: '#161b22',
              border: '2px solid #30363d',
              borderRadius: '24px',
              padding: '40px',
              margin: '40px 0',
            }}
          >
            <div style={{ fontSize: '32px', color: '#8b949e' }}>CATATAN NEWS:</div>
            <div style={{ fontSize: '42px', fontWeight: 800, marginTop: '15px' }}>
              {newsText}
            </div>
            <div
              style={{
                fontSize: '56px',
                fontWeight: 900,
                color: '#58a6ff',
                marginTop: '25px',
              }}
            >
              {price}
            </div>
          </div>
        </div>
      </Sequence>

      {/* Sequence 3: Sentimen & Trap Zone (18s - 28s) */}
      <Sequence from={fps * 18} durationInFrames={fps * 10}>
        <div style={{ textAlign: 'center', margin: 'auto 0' }}>
          <h1
            style={{
              fontSize: '74px',
              fontWeight: 900,
              color: '#f85149',
              lineHeight: 1.1,
            }}
          >
            AWAS JEBAKAN PUCUK!
          </h1>
          <div
            style={{
              backgroundColor: 'rgba(248, 81, 73, 0.15)',
              border: '2px solid #f85149',
              borderRadius: '24px',
              padding: '40px',
              margin: '40px 0',
            }}
          >
            <div style={{ fontSize: '36px', color: '#f85149', fontWeight: 800 }}>
              AREA RESISTENSI: {trapZone}
            </div>
            <p style={{ fontSize: '44px', fontWeight: 800, marginTop: '20px' }}>
              Nice try seller counter trend. Selamat buyer yang udah hold dari bawah.
            </p>
          </div>
        </div>
      </Sequence>

      {/* Sequence 4: Soft-Sell CTA (28s - 38s) */}
      <Sequence from={fps * 28} durationInFrames={fps * 10}>
        <div style={{ textAlign: 'center', margin: 'auto 0' }}>
          <div style={{ fontSize: '36px', color: '#58a6ff', fontWeight: 800 }}>
            PHANTOM INTELLIGENCE
          </div>
          <h1 style={{ fontSize: '72px', fontWeight: 900, margin: '20px 0' }}>
            INGIN AI AGENT UNTUK ANALISIS REALTIME?
          </h1>
          <div
            style={{
              backgroundColor: '#238636',
              padding: '30px',
              borderRadius: '24px',
              fontSize: '48px',
              fontWeight: 900,
              marginTop: '40px',
            }}
          >
            AKSES GRATIS DI BIO
          </div>
        </div>
      </Sequence>

      {/* Bottom Footer Bar */}
      <div
        style={{
          borderTop: '2px solid #30363d',
          paddingTop: '30px',
          display: 'flex',
          justifyContent: 'space-between',
          fontSize: '28px',
          color: '#8b949e',
        }}
      >
        <div>INSTITUTIONAL LIQUIDITY TRACKER</div>
        <div>t.me/phantomsmcid</div>
      </div>
    </div>
  );
};
