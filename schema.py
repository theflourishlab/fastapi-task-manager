from typing import List, Optional
from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    """Request Model"""
    title: str = Field(..., min_length=1, description="Title of the task must not be an empty string.")
    description: Optional[str] = None

class Task(TaskBase):
    """Output model"""
    id: str