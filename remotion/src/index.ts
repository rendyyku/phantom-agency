import { registerRoot } from 'remotion';
import React from 'react';
import { Composition } from 'remotion';
import { XAUUSDRadar } from './XAUUSD_Radar';

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="XAUUSD_Daily_Radar"
      component={XAUUSDRadar}
      durationInFrames={38 * 30}
      fps={30}
      width={1080}
      height={1920}
      defaultProps={{
        pair: 'XAUUSD',
        actionText: 'fly 700 pips tanpa retrace',
        pips: 700,
        newsText: 'Tensi Selat Hormuz memanas lagi, aliran tanker minyak drop 27%',
        price: '$4,194.30',
        trapZone: '4.198 - 4.200',
      }}
    />
  );
};

registerRoot(RemotionRoot);
