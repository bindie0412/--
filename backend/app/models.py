from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

class UserStatus(BaseModel):
    name: str
    status: str
    is_active: bool
