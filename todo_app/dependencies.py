"""Shared application dependencies and service factories."""

from .services import CalendarService, NotificationService, ProgressService, ProjectService, StateManager, TaskService

state_manager = StateManager()
project_service = ProjectService(state_manager)
task_service = TaskService(state_manager)
notification_service = NotificationService(state_manager)
calendar_service = CalendarService(state_manager)
progress_service = ProgressService(state_manager)


def get_project_service() -> ProjectService:
    return project_service


def get_task_service() -> TaskService:
    return task_service


def get_notification_service() -> NotificationService:
    return notification_service


def get_calendar_service() -> CalendarService:
    return calendar_service


def get_progress_service() -> ProgressService:
    return progress_service
