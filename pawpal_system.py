from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List, Optional, Literal

Frequency = Literal["once", "daily", "weekly"]


@dataclass
class Task:
    description: str
    time: str  # HH:MM
    frequency: Frequency
    is_complete: bool = False
    due_date: Optional[date] = None

    def mark_complete(self) -> Optional[Task]:
        self.is_complete = True
        if self.frequency == "daily":
            next_due = date.today() + timedelta(days=1)
            return Task(self.description, self.time, self.frequency, False, next_due)
        if self.frequency == "weekly":
            next_due = date.today() + timedelta(days=7)
            return Task(self.description, self.time, self.frequency, False, next_due)
        return None


@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        return self.tasks


@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        all_tasks: List[Task] = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


@dataclass
class Scheduler:
    owner: Owner

    def get_schedule(self) -> List[Task]:
        return self.owner.get_all_tasks()

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        return sorted(tasks, key=lambda t: t.time)

    def detect_conflicts(self, tasks: List[Task]) -> List[str]:
        conflicts: List[str] = []
        time_map: dict[str, List[Task]] = {}
        for t in tasks:
            time_map.setdefault(t.time, []).append(t)
        for time_str, task_list in time_map.items():
            if len(task_list) > 1:
                descriptions = ", ".join(
                    f"'{t.description}'" for t in task_list)
                conflicts.append(f"Conflict at {time_str}: {descriptions}")
        return conflicts
