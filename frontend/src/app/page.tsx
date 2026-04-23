'use client';

import React, { useState } from 'react';
import Quote from '@/components/dashboard/Quote';
import Pomodoro from '@/components/dashboard/Pomodoro';
import Stats from '@/components/dashboard/Stats';
import TaskList from '@/components/dashboard/TaskList';
import Calendar from '@/components/dashboard/Calendar';
import WhiteNoise from '@/components/dashboard/WhiteNoise';
import Community from '@/components/dashboard/Community';
import FocusMode from '@/components/dashboard/FocusMode';

export default function Home() {
  const [isFocusMode, setIsFocusMode] = useState(false);

  if (isFocusMode) {
    return <FocusMode onExit={() => setIsFocusMode(false)} />;
  }

  return (
    <main className="min-h-screen bg-background text-foreground p-4 md:p-8 lg:p-12 font-sans">
      <div className="max-w-7xl mx-auto">
        <Quote />

        <div className="grid grid-cols-1 md:grid-cols-12 gap-6">
          {/* Main Focus Area */}
          <div className="md:col-span-8 grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="md:col-span-1">
              <Pomodoro onFocusModeToggle={() => setIsFocusMode(true)} />
            </div>
            <div className="md:col-span-1">
              <Stats />
            </div>

            <div className="md:col-span-1 h-64">
              <TaskList />
            </div>
            <div className="md:col-span-1 h-64">
              <Calendar />
            </div>
          </div>

          {/* Sidebar Area */}
          <div className="md:col-span-4 flex flex-col gap-6">
            <div className="flex-grow">
              <WhiteNoise />
            </div>
            <div className="h-64">
              <Community />
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
