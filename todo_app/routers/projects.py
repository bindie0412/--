"""Routes for managing projects and their styling."""

from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_project_service
from ..models import Project
from ..services import ProjectService

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get("/", response_model=List[Project])
def list_projects(project_service: ProjectService = Depends(get_project_service)) -> List[Project]:
    return project_service.list_projects()


@router.post("/", response_model=Project)
def create_project(
    name: str,
    emoji: str = "📁",
    description: Optional[str] = None,
    project_service: ProjectService = Depends(get_project_service),
) -> Project:
    return project_service.create_project(name=name, emoji=emoji, description=description)


@router.patch("/{project_id}", response_model=Project)
def update_project(
    project_id: str,
    name: Optional[str] = None,
    emoji: Optional[str] = None,
    description: Optional[str] = None,
    project_service: ProjectService = Depends(get_project_service),
) -> Project:
    if project_id not in project_service.state.projects:
        raise HTTPException(status_code=404, detail="Project not found")
    return project_service.update_project(
        project_id,
        name=name,
        emoji=emoji,
        description=description,
    )
