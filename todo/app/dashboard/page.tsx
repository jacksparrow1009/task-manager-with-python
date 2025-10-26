import TaskList from "./components/TaskList";

export default function Dashboard() {
  return (
    <div>
      <main className="max-w-2xl mx-auto p-6">
        <h1 className="text-2xl font-semibold mb-4">Your Tasks</h1>
        <TaskList />
      </main>
    </div>
  );
}
