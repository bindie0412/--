export default function Quote() {
  return (
    <div className="p-6 bg-surface-container rounded-3xl mb-8 flex flex-col items-center text-center">
      <p className="text-xl font-medium italic text-on-surface-variant max-w-2xl">
        "The only way to do great work is to love what you do."
      </p>
      <span className="mt-2 text-sm text-primary uppercase tracking-widest">— Steve Jobs</span>
    </div>
  );
}
