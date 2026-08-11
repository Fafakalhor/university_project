from fastapi import APIRouter

from services.Professor_Service import ProfessorService
from models.professor import Professor
from schemas.professor_schema import ProfessorCreate, ProfessorUpdate


router = APIRouter(
    prefix="/professors",
    tags=["Professors"]
)


from dependencies import db, professor_service


@router.post("/")
def create_professor(professor_data: ProfessorCreate):

    professor = Professor(
        len(db.professors) + 1,
        professor_data.first_name,
        professor_data.last_name,
        professor_data.personnel_code,
        professor_data.department
    )

    professor_service.add_professor(professor)

    return {
        "message": "Professor created successfully",
        "professor": {
            "id": professor.id,
            "first_name": professor.first_name,
            "last_name": professor.last_name,
            "personnel_code": professor.personnel_code,
            "department": professor.department
        }
    }


@router.get("/")
def get_professors():

    professors = professor_service.get_professors()

    return [
        {
            "id": p.id,
            "first_name": p.first_name,
            "last_name": p.last_name,
            "personnel_code": p.personnel_code,
            "department": p.department
        }
        for p in professors
    ]


@router.get("/{professor_id}")
def get_professor(professor_id: int):

    professor = professor_service.find_professor(professor_id)

    if professor:
        return {
            "id": professor.id,
            "first_name": professor.first_name,
            "last_name": professor.last_name,
            "personnel_code": professor.personnel_code,
            "department": professor.department
        }

    return {
        "message": "Professor not found"
    }


@router.delete("/{professor_id}")
def delete_professor(professor_id: int):

    professor_service.delete_professor(professor_id)

    return {
        "message": "Professor delete request completed"
    }
@router.put("/{professor_id}")
def update_professor(professor_id: int, professor_data: ProfessorUpdate):

    professor = professor_service.find_professor(professor_id)

    if not professor:
        return {
            "message": "Professor not found"
        }

    if professor_data.first_name is not None:
        professor.first_name = professor_data.first_name

    if professor_data.last_name is not None:
        professor.last_name = professor_data.last_name

    if professor_data.personnel_code is not None:
        professor.personnel_code = professor_data.personnel_code

    if professor_data.department is not None:
        professor.department = professor_data.department

    return {
        "message": "Professor updated successfully",
        "professor": {
            "id": professor.id,
            "first_name": professor.first_name,
            "last_name": professor.last_name,
            "personnel_code": professor.personnel_code,
            "department": professor.department
        }
    }
