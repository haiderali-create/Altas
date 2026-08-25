from typing import Any, Literal
from pydantic import BaseModel, Field

class Step(BaseModel):
    action: str
    arguments: dict[str, Any] = Field(default_factory=dict)
    reason: str = ''
    requires_confirmation: bool = False

class Plan(BaseModel):
    goal: str
    steps: list[Step]

class StepResult(BaseModel):
    action: str
    success: bool
    message: str
    data: dict[str, Any] = Field(default_factory=dict)

class TaskResult(BaseModel):
    success: bool
    message: str
    steps: list[StepResult]
