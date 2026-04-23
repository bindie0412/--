from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from .models import Task, UserStatus

app = FastAPI(title="Study Sanctuary API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock data
TASKS = [
    {"id": 1, "title": "Complete Math Homework", "completed": False},
    {"id": 2, "title": "Read Research Paper", "completed": True},
]

USERS = [
    {"name": "Alex", "status": "Focusing 🧘", "is_active": True},
    {"name": "Sarah", "status": "Break ☕", "is_active": False},
    {"name": "Minji", "status": "Focusing 🧘", "is_active": True},
]

@app.get("/")
def root():
    return {"status": "Study Sanctuary API is Live"}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return TASKS

@app.get("/community", response_model=List[UserStatus])
def get_community():
    return USERS
