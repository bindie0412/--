import { Calendar as CalendarIcon, ChevronRight } from 'lucide-react';

export default function Calendar() {
  const events = [
    { time: '14:00', title: 'Deep Work Session', color: 'bg-primary' },
    { time: '16:30', title: 'Weekly Review', color: 'bg-surface-container-highest' },
  ];

  return (
    <div className="p-8 bg-surface-container rounded-3xl h-full flex flex-col">
      <div className="flex justify-between items-center mb-6">
        <h3 className="text-on-surface-variant uppercase tracking-widest text-xs font-bold">Upcoming</h3>
        <CalendarIcon size={18} className="text-on-surface-variant" />
      </div>

      <div className="space-y-6">
        {events.map((event, i) => (
          <div key={i} className="flex gap-4 items-start">
            <span className="text-xs text-on-surface-variant w-10 mt-1">{event.time}</span>
            <div className="flex-grow">
              <div className="flex items-center gap-2">
                <div className={`w-1 h-4 rounded-full ${event.color}`} />
                <span className="text-sm font-medium">{event.title}</span>
              </div>
            </div>
          </div>
        ))}
      </div>

      <button className="mt-auto flex items-center gap-2 text-on-surface-variant text-xs hover:text-foreground transition-colors pt-4">
        Go to Calendar <ChevronRight size={14} />
      </button>
    </div>
  );
}
