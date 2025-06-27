import uuid
from typing import List, Optional
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from security import get_current_user
from schema import Task, TaskBase

app = FastAPI()

# CORS Middleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# In-memory "database"
tasks_db = {}



@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskBase, user: str = Depends(get_current_user)):
    """
    Create a new task.

    - **title**: The title of the task (required).
    - **description**: An optional description of the task.
    """

    task_id = str(uuid.uuid4())
    new_task = Task(id=task_id, title=task.title, description=task.description)
    tasks_db[task_id] = new_task
    return new_task

@app.get("/tasks", response_model=list[Task])
def get_all_tasks(user: str = Depends(get_current_user)):
    """
    Retrieve a list of all tasks.
    """
    return list(tasks_db.values())

@app.get("/tasks/{task_id}", response_model=Task)
def get_task_by_id(task_id: str, user: str = Depends(get_current_user)):
    """
    Retrieve a specific task by its unique ID
    """

    task = tasks_db.get(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with ID '{task_id}' not found."
        )
    return task