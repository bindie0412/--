"""Entrypoint for the modular to-do backend."""

from fastapi import FastAPI

from todo_app.dependencies import (
    calendar_service,
    notification_service,
    progress_service,
    project_service,
    state_manager,
    task_service,
)
from todo_app.routers import notifications, projects, tasks, views

app = FastAPI(
    title="Modular To-Do Cloud API",
    description=(
        "Project-aware to-do manager with cloud-friendly storage, "
        "emoji customization, calendar views, weekly progress mapping, and notifications."
    ),
    version="0.1.0",
)

app.include_router(projects.router)
app.include_router(tasks.router)
app.include_router(notifications.router)
app.include_router(views.router)


@app.get("/health")
def healthcheck() -> dict:
    return {
        "status": "ok",
        "projects": len(project_service.state.projects),
        "tasks": len(task_service.state.items),
        "notifications": len(notification_service.state.notifications),
        "calendar_ready": len(calendar_service.events()),
        "progress_maps": len(progress_service.weekly_map()),
    }


@app.get("/modules")
def modules() -> dict:
    return {
        "storage": state_manager.storage.__class__.__name__,
        "features": [
            "projects",
            "tasks",
            "notifications",
            "calendar",
            "progress",
        ],
    }
