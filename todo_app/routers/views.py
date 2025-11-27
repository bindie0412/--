"""Read-only views combining multiple services."""

from typing import Dict, List, Optional

from fastapi import APIRouter, Depends

from ..dependencies import get_calendar_service, get_progress_service
from ..models import CalendarEvent
from ..services import CalendarService, ProgressService

router = APIRouter(prefix="/views", tags=["views"])


@router.get("/calendar", response_model=List[CalendarEvent])
def calendar_view(
    project_id: Optional[str] = None,
    calendar_service: CalendarService = Depends(get_calendar_service),
) -> List[CalendarEvent]:
    return calendar_service.events(project_id=project_id)


@router.get("/progress", response_model=Dict[str, Dict[str, Dict[str, int]]])
def weekly_progress(
    project_id: Optional[str] = None,
    progress_service: ProgressService = Depends(get_progress_service),
) -> Dict[str, Dict[str, Dict[str, int]]]:
    return progress_service.weekly_map(project_id=project_id)
