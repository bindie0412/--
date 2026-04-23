'use client';

import React, { useState, useEffect } from 'react';
import { Minimize2, Clock } from 'lucide-react';

interface FocusModeProps {
  onExit: () => void;
}

export default function FocusMode({ onExit }: FocusModeProps) {
  const [time, setTime] = useState(new Date());

  useEffect(() => {
    const timer = setInterval(() => setTime(new Date()), 1000);
    return () => clearInterval(timer);
  }, []);

  const formatTime = (date: Date) => {
    return date.toLocaleTimeString('en-US', {
      hour12: false,
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  return (
    <div className="fixed inset-0 bg-[#000000] z-[100] flex flex-col items-center justify-center select-none cursor-none overflow-hidden">
      {/* Ghost exit button - only visible on hover near corner */}
      <button
        onClick={onExit}
        className="absolute top-12 right-12 p-4 text-neutral-900 hover:text-neutral-600 transition-all cursor-auto duration-500 opacity-20 hover:opacity-100"
        title="Exit Focus Mode"
      >
        <Minimize2 size={40} strokeWidth={1} />
      </button>

      <div className="flex flex-col items-center">
        <Clock size={60} strokeWidth={1} className="text-neutral-800 mb-12" />

        <div className="flex items-center gap-4">
           <span className="text-[18rem] font-extralight tracking-tight text-neutral-300 leading-none">
            {formatTime(time)}
          </span>
        </div>

        <div className="mt-20 flex flex-col items-center gap-4">
            <div className="flex items-center gap-6">
                <div className="w-1.5 h-1.5 rounded-full bg-primary animate-pulse shadow-[0_0_15px_rgba(211,188,252,0.5)]" />
                <span className="text-neutral-700 tracking-[0.5em] uppercase text-xs font-light">Deep Work in Progress</span>
            </div>
            <p className="text-neutral-800 text-[10px] mt-4 tracking-widest uppercase">
               Silence is the canvas of greatness
            </p>
        </div>
      </div>

      {/* Very subtle ambient movement */}
      <div className="absolute inset-0 pointer-events-none overflow-hidden">
         <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-primary opacity-[0.02] blur-[150px] animate-pulse" />
         <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-primary opacity-[0.01] blur-[150px] animate-pulse" style={{ animationDelay: '2s' }} />
      </div>
    </div>
  );
}
