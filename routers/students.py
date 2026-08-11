from fastapi import APIRouter

from services.student_service import StudentService
from models.student import Student
from schemas.student_schema import StudentCreate, StudentUpdate


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


from dependencies import db, student_service


@router.post("/")
def create_student(student_data: StudentCreate):
    student = Student(
        len(db.students) + 1,
        student_data.name_first,
        student_data.name_last,
        student_data.number_student,
        student_data.major
    )

    student_service.add_student(student)

    return {
        "message": "Student created successfully",
        "student": {
            "id": student.id,
            "first_name": student.first_name,
            "last_name": student.last_name,
            "student_number": student.student_number,
            "major": student.major
        }
    }


@router.get("/")
def get_students():
    students = student_service.get_students()

    return [
        {
            "id": s.id,
            "first_name": s.first_name,
            "last_name": s.last_name,
            "student_number": s.student_number,
            "major": s.major
        }
        for s in students
    ]


@router.get("/{student_id}")
def get_student(student_id: int):
    student = student_service.find_student(student_id)

    if student:
        return {
            "id": student.id,
            "first_name": student.first_name,
            "last_name": student.last_name,
            "student_number": student.student_number,
            "major": student.major
        }

    return {
        "message": "Student not found"
    }


@router.delete("/{student_id}")
def delete_student(student_id: int):
    student_service.delete_student(student_id)

    return {
        "message": "Student delete request completed"
    }
@router.put("/{student_id}")
def update_student(student_id: int, student_data: StudentUpdate):

    student = student_service.update_student(
        student_id,
        student_data
    )

    return {
        "message": "Student updated successfully",
        "student": student.to_dict()
    }