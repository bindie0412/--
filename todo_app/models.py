"""Domain models for the to-do application."""

from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class Project(BaseModel):
    """Represents a project grouping multiple to-dos."""

    id: str
    name: str
    emoji: str = "📁"
    description: Optional[str] = None


class ToDoItem(BaseModel):
    """A single to-do item."""

    id: str
    project_id: str
    title: str
    description: Optional[str] = None
    due_date: Optional[date] = None
    completed: bool = False
    tags: List[str] = Field(default_factory=list)


class Notification(BaseModel):
    """Represents a scheduled notification."""

    id: str
    item_id: str
    scheduled_for: datetime
    message: str


class CalendarEvent(BaseModel):
    """Event projection for the calendar view."""

    date: date
    title: str
    description: Optional[str]
    project_emoji: str
    project_name: str
    completed: bool
