import { User } from 'lucide-react';

export default function Community() {
  const users = [
    { name: 'Alex', status: 'Focusing 🧘', active: true },
    { name: 'Sarah', status: 'Break ☕', active: false },
    { name: 'Minji', status: 'Focusing 🧘', active: true },
  ];

  return (
    <div className="p-8 bg-surface-container rounded-3xl h-full flex flex-col">
      <h3 className="text-on-surface-variant uppercase tracking-widest text-xs font-bold mb-6">Community</h3>
      <div className="space-y-6">
        {users.map((user, i) => (
          <div key={i} className="flex items-center gap-4">
            <div className="relative">
              <div className="w-10 h-10 rounded-full bg-surface-container-highest flex items-center justify-center">
                <User size={20} className="text-on-surface-variant" />
              </div>
              {user.active && (
                <div className="absolute bottom-0 right-0 w-3 h-3 bg-green-500 rounded-full border-2 border-surface-container" />
              )}
            </div>
            <div className="flex flex-col">
              <span className="text-sm font-medium">{user.name}</span>
              <span className="text-[10px] text-on-surface-variant">{user.status}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
