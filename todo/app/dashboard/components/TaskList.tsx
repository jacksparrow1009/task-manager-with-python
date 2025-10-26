import { Checkbox } from "@/components/ui/checkbox";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

const mockTasks = [
  {
    id: 1,
    title: "Finish project setup",
    description: "Set up Next.js, Tailwind, and ShadCN components",
    completed: false,
    created_at: "2025-10-25",
  },
  {
    id: 2,
    title: "Build Auth Pages",
    description: "Create login and registration UI with validation",
    completed: true,
    created_at: "2025-10-24",
  },
];

export default function TaskList() {
  return (
    <div className="grid gap-4 mt-6">
      {mockTasks.map((task) => (
        <Card key={task.id}>
          <CardHeader className="flex flex-row items-center justify-between">
            <CardTitle className="text-lg">{task.title}</CardTitle>
            <Checkbox checked={task.completed} />
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">{task.description}</p>
            <p className="text-xs text-gray-400 mt-1">
              Created at: {task.created_at}
            </p>
          </CardContent>
        </Card>
      ))}
    </div>
  );
}
