from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Goal:

    title: str

    goal_type: str = "general"

    priority: str = "normal"

    created_at: datetime = field(default_factory=datetime.now)

    completed: bool = False

    tasks: list = field(default_factory=list)

    notes: list = field(default_factory=list)

    def add_task(self, task):

        self.tasks.append(task)

    def add_note(self, note):

        self.notes.append(note)

    def finish(self):

        self.completed = True

    def summary(self):

        return {

            "title": self.title,

            "type": self.goal_type,

            "priority": self.priority,

            "completed": self.completed,

            "tasks": self.tasks,

            "notes": self.notes,

            "created_at": str(self.created_at)

        }
