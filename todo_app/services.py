"""Core services implementing application logic."""

from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Optional
from uuid import uuid4

from .models import CalendarEvent, Notification, Project, ToDoItem
from .storage import CloudStorage, LocalJSONStorage, to_serializable


class StateManager:
    """Orchestrates loading and saving state through a storage backend."""

    def __init__(self, storage: Optional[CloudStorage] = None):
        self.storage = storage or LocalJSONStorage()
        self.projects: Dict[str, Project] = {}
        self.items: Dict[str, ToDoItem] = {}
        self.notifications: Dict[str, Notification] = {}
        self._load()

    def _load(self) -> None:
        state = self.storage.load_state()
        for project in state.get("projects", []):
            obj = Project(**project)
            self.projects[obj.id] = obj
        for item in state.get("items", []):
            obj = ToDoItem(**item)
            self.items[obj.id] = obj
        for notification in state.get("notifications", []):
            obj = Notification(**notification)
            self.notifications[obj.id] = obj

    def _persist(self) -> None:
        self.storage.save_state(
            {
                "projects": to_serializable(list(self.projects.values())),
                "items": to_serializable(list(self.items.values())),
                "notifications": to_serializable(list(self.notifications.values())),
            }
        )


class ProjectService:
    """Handles CRUD operations for projects."""

    def __init__(self, state: StateManager):
        self.state = state

    def create_project(self, name: str, emoji: str = "📁", description: Optional[str] = None) -> Project:
        project = Project(id=str(uuid4()), name=name, emoji=emoji, description=description)
        self.state.projects[project.id] = project
        self.state._persist()
        return project

    def update_project(self, project_id: str, *, name: Optional[str] = None, emoji: Optional[str] = None,
                       description: Optional[str] = None) -> Project:
        project = self.state.projects[project_id]
        if name is not None:
            project.name = name
        if emoji is not None:
            project.emoji = emoji
        if description is not None:
            project.description = description
        self.state._persist()
        return project

    def list_projects(self) -> List[Project]:
        return list(self.state.projects.values())


class TaskService:
    """Manages to-do items."""

    def __init__(self, state: StateManager):
        self.state = state

    def create_item(
        self,
        project_id: str,
        title: str,
        description: Optional[str] = None,
        due_date: Optional[datetime] = None,
        tags: Optional[List[str]] = None,
    ) -> ToDoItem:
        item = ToDoItem(
            id=str(uuid4()),
            project_id=project_id,
            title=title,
            description=description,
            due_date=due_date.date() if isinstance(due_date, datetime) else due_date,
            tags=tags or [],
        )
        self.state.items[item.id] = item
        self.state._persist()
        return item

    def toggle_complete(self, item_id: str, completed: Optional[bool] = None) -> ToDoItem:
        item = self.state.items[item_id]
        item.completed = not item.completed if completed is None else completed
        self.state._persist()
        return item

    def update_item(
        self,
        item_id: str,
        *,
        title: Optional[str] = None,
        description: Optional[str] = None,
        due_date: Optional[datetime] = None,
        tags: Optional[List[str]] = None,
    ) -> ToDoItem:
        item = self.state.items[item_id]
        if title is not None:
            item.title = title
        if description is not None:
            item.description = description
        if due_date is not None:
            item.due_date = due_date.date() if isinstance(due_date, datetime) else due_date
        if tags is not None:
            item.tags = tags
        self.state._persist()
        return item

    def delete_item(self, item_id: str) -> None:
        self.state.items.pop(item_id, None)
        self.state.notifications = {
            nid: notif for nid, notif in self.state.notifications.items() if notif.item_id != item_id
        }
        self.state._persist()

    def list_items(self, project_id: Optional[str] = None) -> List[ToDoItem]:
        if project_id:
            return [item for item in self.state.items.values() if item.project_id == project_id]
        return list(self.state.items.values())


class NotificationService:
    """Stub notification dispatcher; can be extended for real providers."""

    def __init__(self, state: StateManager):
        self.state = state

    def schedule_notification(self, item_id: str, scheduled_for: datetime, message: str) -> Notification:
        notification = Notification(id=str(uuid4()), item_id=item_id, scheduled_for=scheduled_for, message=message)
        self.state.notifications[notification.id] = notification
        self.state._persist()
        return notification

    def upcoming(self, *, before: Optional[datetime] = None) -> List[Notification]:
        now = datetime.now()
        horizon = before or datetime.max
        return [n for n in self.state.notifications.values() if now <= n.scheduled_for <= horizon]


class CalendarService:
    """Projects calendar-ready entries from to-dos."""

    def __init__(self, state: StateManager):
        self.state = state

    def events(self, project_id: Optional[str] = None) -> List[CalendarEvent]:
        items = list(self.state.items.values())
        if project_id:
            items = [item for item in items if item.project_id == project_id]
        events: List[CalendarEvent] = []
        for item in items:
            if item.due_date is None:
                continue
            project = self.state.projects[item.project_id]
            events.append(
                CalendarEvent(
                    date=item.due_date,
                    title=item.title,
                    description=item.description,
                    project_emoji=project.emoji,
                    project_name=project.name,
                    completed=item.completed,
                )
            )
        return sorted(events, key=lambda event: event.date)


class ProgressService:
    """Generates weekly progress maps for projects."""

    def __init__(self, state: StateManager):
        self.state = state

    def weekly_map(self, project_id: Optional[str] = None) -> Dict[str, Dict[str, Dict[str, int]]]:
        summary: Dict[str, Dict[str, Dict[str, int]]] = defaultdict(lambda: defaultdict(lambda: {"completed": 0, "total": 0}))
        for item in self.state.items.values():
            if project_id and item.project_id != project_id:
                continue
            week_key = item.due_date.isocalendar() if item.due_date else datetime.now().isocalendar()
            week_label = f"{week_key.year}-W{week_key.week:02d}"
            project = self.state.projects[item.project_id]
            counts = summary[week_label][project.id]
            counts["total"] += 1
            if item.completed:
                counts["completed"] += 1
        return summary
