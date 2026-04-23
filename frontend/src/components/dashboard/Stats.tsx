'use client';

import React, { useState } from 'react';
import { TrendingUp, ChevronRight, Swords } from 'lucide-react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell } from 'recharts';

const mockHistoryData = [
  { day: 'Mon', hours: 4 },
  { day: 'Tue', hours: 6 },
  { day: 'Wed', hours: 5.5 },
  { day: 'Thu', hours: 7 },
  { day: 'Fri', hours: 3 },
  { day: 'Sat', hours: 8 },
  { day: 'Sun', hours: 4.5 },
];

export default function Stats() {
  const [showDetail, setShowDetail] = useState(false);

  return (
    <div className="p-8 bg-surface-container rounded-3xl h-full flex flex-col transition-all duration-500 overflow-hidden">
      <div className="flex justify-between items-start mb-6">
        <div>
          <h3 className="text-on-surface-variant uppercase tracking-widest text-xs font-bold mb-1">Focus Stats</h3>
          <p className="text-3xl font-medium">4h 20m</p>
        </div>
        <div className="flex flex-col items-end">
          <span className="text-green-400 text-xs flex items-center gap-1 font-bold">
            <TrendingUp size={12} /> +12%
          </span>
          <span className="text-[10px] text-on-surface-variant">vs Yesterday</span>
        </div>
      </div>

      {/* Competition Mode Message */}
      <div className="bg-surface-container-highest/50 p-4 rounded-2xl mb-6 border border-primary/5 flex items-center gap-3">
        <Swords size={16} className="text-primary shrink-0" />
        <p className="text-[11px] text-on-surface-variant leading-relaxed">
           <span className="text-primary font-bold">Competition:</span> Yesterday, you were at <span className="text-foreground">3h 15m</span> by this time. You're currently <span className="text-green-400 font-bold">ahead</span> of your past self!
        </p>
      </div>

      <div className="space-y-4 flex-grow">
        <div className="flex justify-between items-center text-sm">
          <span className="text-on-surface-variant">Today's Session</span>
          <span className="font-medium text-primary">25m</span>
        </div>
        <div className="flex justify-between items-center text-sm">
          <span className="text-on-surface-variant">Yesterday's Total</span>
          <span>3h 45m</span>
        </div>
      </div>

      <button
        onClick={() => setShowDetail(!showDetail)}
        className="mt-6 flex items-center gap-2 text-primary text-sm font-medium hover:gap-3 transition-all group"
      >
        {showDetail ? 'Hide Details' : 'View Detailed Graph'}
        <ChevronRight size={16} className={`transition-transform ${showDetail ? 'rotate-90' : ''}`} />
      </button>

      {showDetail && (
        <div className="mt-6 h-48 w-full animate-in fade-in slide-in-from-top-4 duration-500">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={mockHistoryData}>
              <XAxis
                dataKey="day"
                axisLine={false}
                tickLine={false}
                tick={{ fill: '#acabaa', fontSize: 10 }}
              />
              <Tooltip
                cursor={{ fill: 'rgba(255,255,255,0.05)' }}
                contentStyle={{
                    backgroundColor: '#191a1a',
                    border: 'none',
                    borderRadius: '12px',
                    fontSize: '10px',
                    boxShadow: '0 10px 15px -3px rgba(0, 0, 0, 0.5)'
                }}
                itemStyle={{ color: '#d3bcfc' }}
              />
              <Bar
                dataKey="hours"
                radius={[4, 4, 0, 0]}
              >
                {mockHistoryData.map((entry, index) => (
                  <Cell
                    key={`cell-${index}`}
                    fill={entry.day === 'Sat' ? '#d3bcfc' : '#252626'}
                  />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>
      )}
    </div>
  );
}
