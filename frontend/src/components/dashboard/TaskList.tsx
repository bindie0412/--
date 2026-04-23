'use client';

import React, { useState } from 'react';
import { CheckCircle2, Circle, Plus, X } from 'lucide-react';

interface Task {
  id: number;
  title: string;
  completed: boolean;
}

const initialTasks: Task[] = [
  { id: 1, title: 'Complete Math Homework', completed: false },
  { id: 2, title: 'Read Research Paper', completed: true },
  { id: 3, title: 'Review Japanese Kanji', completed: false },
];

export default function TaskList() {
  const [tasks, setTasks] = useState<Task[]>(initialTasks);
  const [isAdding, setIsAdding] = useState(false);
  const [newTaskTitle, setNewTaskTitle] = useState('');

  const toggleTask = (id: number) => {
    setTasks(tasks.map(t => t.id === id ? { ...t, completed: !t.completed } : t));
  };

  const addTask = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newTaskTitle.trim()) return;
    const newTask = {
      id: Date.now(),
      title: newTaskTitle,
      completed: false,
    };
    setTasks([newTask, ...tasks]);
    setNewTaskTitle('');
    setIsAdding(false);
  };

  const deleteTask = (id: number) => {
    setTasks(tasks.filter(t => t.id !== id));
  };

  return (
    <div className="p-8 bg-surface-container rounded-3xl h-full flex flex-col transition-all duration-300">
      <div className="flex justify-between items-center mb-6">
        <h3 className="text-on-surface-variant uppercase tracking-widest text-xs font-bold">To-Do</h3>
        <button
          onClick={() => setIsAdding(!isAdding)}
          className="text-primary hover:scale-110 transition-transform p-1"
        >
          {isAdding ? <X size={20} /> : <Plus size={20} />}
        </button>
      </div>

      {isAdding && (
        <form onSubmit={addTask} className="mb-6 animate-in fade-in slide-in-from-top-2 duration-300">
          <input
            autoFocus
            type="text"
            placeholder="What needs to be done?"
            value={newTaskTitle}
            onChange={(e) => setNewTaskTitle(e.target.value)}
            className="w-full bg-surface-container-highest text-sm p-3 rounded-xl focus:outline-none focus:ring-1 focus:ring-primary/40 transition-all"
          />
        </form>
      )}

      <div className="space-y-4 overflow-y-auto custom-scrollbar flex-grow pr-2">
        {tasks.map(task => (
          <div
            key={task.id}
            className="flex items-center justify-between group"
          >
            <div
              onClick={() => toggleTask(task.id)}
              className="flex items-center gap-4 cursor-pointer flex-grow"
            >
              {task.completed ? (
                <CheckCircle2 size={20} className="text-primary shrink-0" />
              ) : (
                <Circle size={20} className="text-on-surface-variant group-hover:text-primary shrink-0 transition-colors" />
              )}
              <span className={`text-sm transition-all ${task.completed ? 'text-on-surface-variant line-through opacity-50' : 'text-foreground'}`}>
                {task.title}
              </span>
            </div>
            <button
              onClick={() => deleteTask(task.id)}
              className="opacity-0 group-hover:opacity-100 p-1 text-on-surface-variant hover:text-red-400 transition-all"
            >
              <X size={14} />
            </button>
          </div>
        ))}
        {tasks.length === 0 && !isAdding && (
          <p className="text-xs text-on-surface-variant italic text-center mt-10">No tasks for today. Rest or add new ones.</p>
        )}
      </div>
    </div>
  );
}
