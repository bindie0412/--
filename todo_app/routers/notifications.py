"""Routes for managing notification schedules."""

from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_notification_service, get_task_service
from ..models import Notification
from ..services import NotificationService, TaskService

router = APIRouter(prefix="/notifications", tags=["notifications"])


@router.post("/", response_model=Notification)
def schedule_notification(
    item_id: str,
    scheduled_for: datetime,
    message: str,
    notification_service: NotificationService = Depends(get_notification_service),
    task_service: TaskService = Depends(get_task_service),
) -> Notification:
    if item_id not in task_service.state.items:
        raise HTTPException(status_code=404, detail="Task not found for notification")
    return notification_service.schedule_notification(item_id=item_id, scheduled_for=scheduled_for, message=message)


@router.get("/upcoming", response_model=List[Notification])
def list_upcoming(
    before: Optional[datetime] = None,
    notification_service: NotificationService = Depends(get_notification_service),
) -> List[Notification]:
    horizon = before or datetime.now()
    return notification_service.upcoming(before=horizon)
