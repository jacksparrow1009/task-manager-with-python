"use client";

import Link from "next/link";
import { Button } from "@/components/ui/button";

export default function Navbar() {
  return (
    <nav className="flex items-center justify-between bg-white shadow-sm px-6 py-3">
      <Link href="/dashboard" className="text-lg font-semibold">
        Task Manager
      </Link>
      <Button asChild>
        <Link href="/add-task">+ Add Task</Link>
      </Button>
    </nav>
  );
}
