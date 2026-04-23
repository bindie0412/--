'use client';

import React, { useState, useEffect } from 'react';
import { Play, Pause, RotateCcw, Maximize2 } from 'lucide-react';

interface PomodoroProps {
  onFocusModeToggle: () => void;
}

export default function Pomodoro({ onFocusModeToggle }: PomodoroProps) {
  const [timeLeft, setTimeLeft] = useState(25 * 60);
  const [isActive, setIsActive] = useState(false);

  useEffect(() => {
    let interval: NodeJS.Timeout;
    if (isActive && timeLeft > 0) {
      interval = setInterval(() => {
        setTimeLeft((prev) => prev - 1);
      }, 1000);
    } else if (timeLeft === 0) {
      setIsActive(false);
    }
    return () => clearInterval(interval);
  }, [isActive, timeLeft]);

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  const toggleTimer = () => setIsActive(!isActive);
  const resetTimer = () => {
    setIsActive(false);
    setTimeLeft(25 * 60);
  };

  const progress = ((25 * 60 - timeLeft) / (25 * 60)) * 100;

  return (
    <div className="flex flex-col items-center justify-center p-8 bg-surface-container rounded-3xl relative group">
      <button
        onClick={onFocusModeToggle}
        className="absolute top-4 right-4 p-2 text-on-surface-variant hover:text-primary transition-colors"
        title="Enter Focus Mode"
      >
        <Maximize2 size={20} />
      </button>

      <div className="relative w-64 h-64 flex items-center justify-center">
        <svg className="w-full h-full transform -rotate-90">
          <circle
            cx="128"
            cy="128"
            r="120"
            stroke="currentColor"
            strokeWidth="8"
            fill="transparent"
            className="text-surface-container-highest"
          />
          <circle
            cx="128"
            cy="128"
            r="120"
            stroke="currentColor"
            strokeWidth="8"
            fill="transparent"
            strokeDasharray={2 * Math.PI * 120}
            strokeDashoffset={2 * Math.PI * 120 * (1 - progress / 100)}
            strokeLinecap="round"
            className="text-primary transition-all duration-1000"
          />
        </svg>
        <span className="absolute text-6xl font-medium tracking-tighter">
          {formatTime(timeLeft)}
        </span>
      </div>

      <div className="flex gap-4 mt-8">
        <button
          onClick={toggleTimer}
          className="w-14 h-14 flex items-center justify-center bg-primary text-primary-container rounded-full hover:scale-105 transition-transform"
        >
          {isActive ? <Pause fill="currentColor" /> : <Play fill="currentColor" className="ml-1" />}
        </button>
        <button
          onClick={resetTimer}
          className="w-14 h-14 flex items-center justify-center bg-surface-container-highest text-on-surface-variant rounded-full hover:scale-105 transition-transform"
        >
          <RotateCcw size={24} />
        </button>
      </div>
    </div>
  );
}
