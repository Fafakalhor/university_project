from pydantic import BaseModel, Field
from typing import Optional


class StudentCreate(BaseModel):
    name_first: str = Field(..., min_length=2, max_length=50)
    name_last: str = Field(..., min_length=2, max_length=50)
    number_student: str = Field(..., min_length=3, max_length=20)
    major: str = Field(..., min_length=2, max_length=80)


class StudentUpdate(BaseModel):
    name_first: Optional[str] = Field(None, min_length=2, max_length=50)
    name_last: Optional[str] = Field(None, min_length=2, max_length=50)
    number_student: Optional[str] = Field(None, min_length=3, max_length=20)
    major: Optional[str] = Field(None, min_length=2, max_length=80)