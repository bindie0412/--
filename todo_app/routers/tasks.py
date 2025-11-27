"""Routes for to-do item management."""

from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_project_service, get_task_service
from ..models import ToDoItem
from ..services import ProjectService, TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])


def _validate_project(project_service: ProjectService, project_id: str) -> None:
    if project_id not in project_service.state.projects:
        raise HTTPException(status_code=404, detail="Project not found")


@router.get("/", response_model=List[ToDoItem])
def list_tasks(
    project_id: Optional[str] = None,
    task_service: TaskService = Depends(get_task_service),
) -> List[ToDoItem]:
    return task_service.list_items(project_id=project_id)


@router.post("/", response_model=ToDoItem)
def create_task(
    *,
    project_id: str,
    title: str,
    description: Optional[str] = None,
    due_date: Optional[datetime] = None,
    tags: Optional[List[str]] = None,
    task_service: TaskService = Depends(get_task_service),
    project_service: ProjectService = Depends(get_project_service),
) -> ToDoItem:
    _validate_project(project_service, project_id)
    return task_service.create_item(
        project_id=project_id,
        title=title,
        description=description,
        due_date=due_date,
        tags=tags,
    )


@router.patch("/{item_id}", response_model=ToDoItem)
def update_task(
    item_id: str,
    title: Optional[str] = None,
    description: Optional[str] = None,
    due_date: Optional[datetime] = None,
    tags: Optional[List[str]] = None,
    completed: Optional[bool] = None,
    task_service: TaskService = Depends(get_task_service),
) -> ToDoItem:
    if item_id not in task_service.state.items:
        raise HTTPException(status_code=404, detail="Task not found")
    if completed is not None:
        task_service.toggle_complete(item_id, completed)
    return task_service.update_item(
        item_id,
        title=title,
        description=description,
        due_date=due_date,
        tags=tags,
    )


@router.delete("/{item_id}")
def delete_task(item_id: str, task_service: TaskService = Depends(get_task_service)) -> dict:
    if item_id not in task_service.state.items:
        raise HTTPException(status_code=404, detail="Task not found")
    task_service.delete_item(item_id)
    return {"status": "deleted", "item_id": item_id}
