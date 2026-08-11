from pydantic import BaseModel, Field
from typing import Optional


class CourseCreate(BaseModel):
    course_name: str = Field(..., min_length=2, max_length=100)
    course_code: str = Field(..., min_length=2, max_length=20)
    units: int = Field(..., ge=1, le=4)


class CourseUpdate(BaseModel):
    course_name: Optional[str] = Field(None, min_length=2, max_length=100)
    course_code: Optional[str] = Field(None, min_length=2, max_length=20)
    units: Optional[int] = Field(None, ge=1, le=4)