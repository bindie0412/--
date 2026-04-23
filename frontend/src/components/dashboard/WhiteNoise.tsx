'use client';

import React, { useState, useEffect, useRef } from 'react';
import { Volume2, CloudRain, Coffee, Zap } from 'lucide-react';

interface Sound {
  name: string;
  icon: React.ReactNode;
  volume: number;
  file: string;
}

export default function WhiteNoise() {
  const [sounds, setSounds] = useState<Sound[]>([
    { name: 'Rain', icon: <CloudRain size={18} />, volume: 50, file: '/audio/rain.mp3' },
    { name: 'Cafe', icon: <Coffee size={18} />, volume: 0, file: '/audio/cafe.mp3' },
    { name: 'Focus (Alpha)', icon: <Zap size={18} />, volume: 20, file: '/audio/alpha.mp3' },
  ]);

  const audioRefs = useRef<(HTMLAudioElement | null)[]>([]);

  useEffect(() => {
    audioRefs.current = sounds.map((sound, i) => {
      if (typeof window !== 'undefined') {
        const audio = new Audio(sound.file);
        audio.loop = true;
        audio.volume = sound.volume / 100;
        return audio;
      }
      return null;
    });

    return () => {
      audioRefs.current.forEach(audio => {
        if (audio) {
          audio.pause();
          audio.src = '';
        }
      });
    };
  }, []);

  const handleVolumeChange = (index: number, value: number) => {
    const newSounds = [...sounds];
    newSounds[index].volume = value;
    setSounds(newSounds);

    const audio = audioRefs.current[index];
    if (audio) {
      audio.volume = value / 100;
      if (value > 0 && audio.paused) {
        audio.play().catch(e => console.log("Audio play deferred until user interaction"));
      } else if (value === 0 && !audio.paused) {
        audio.pause();
      }
    }
  };

  return (
    <div className="p-8 bg-surface-container rounded-3xl h-full flex flex-col">
      <div className="flex justify-between items-center mb-8">
        <h3 className="text-on-surface-variant uppercase tracking-widest text-xs font-bold">Atmosphere</h3>
        <Volume2 size={18} className="text-on-surface-variant" />
      </div>

      <div className="space-y-8">
        {sounds.map((sound, i) => (
          <div key={sound.name} className="flex flex-col gap-3">
            <div className="flex justify-between items-center">
              <div className="flex items-center gap-2 text-on-surface-variant">
                {sound.icon}
                <span className="text-sm font-medium">{sound.name}</span>
              </div>
              <span className="text-[10px] font-bold text-on-surface-variant">{sound.volume}%</span>
            </div>
            <input
              type="range"
              min="0"
              max="100"
              value={sound.volume}
              onChange={(e) => handleVolumeChange(i, parseInt(e.target.value))}
              className="w-full h-1 bg-surface-container-highest rounded-full appearance-none cursor-pointer accent-primary"
            />
          </div>
        ))}
      </div>
      <p className="mt-6 text-[10px] text-on-surface-variant italic">
        * Mix sounds to create your perfect study environment.
      </p>
      <div className="mt-auto p-4 bg-surface-container-highest/30 rounded-2xl border border-primary/5">
        <p className="text-[9px] text-on-surface-variant/60 uppercase tracking-tighter text-center">
            Experimental: Neural Flow Mixing Enabled
        </p>
      </div>
    </div>
  );
}
