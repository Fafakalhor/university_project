from fastapi import APIRouter


router = APIRouter(
    prefix="/enrollment",
    tags=["Enrollment"]
)


from dependencies import db, enrollment_service


@router.get("/student/{student_id}/courses")
def get_student_courses(student_id: int):

    for student in db.students:
        if student.id == student_id:
            return {
                "student": student.first_name,
                "courses": enrollment_service.get_student_courses(student)
            }

    return {
        "message": "Student not found"
    }


@router.post("/student/{student_id}/course/{course_code}")
def add_course(student_id: int, course_code: str):

    student = None
    course = None

    for s in db.students:
        if s.id == student_id:
            student = s

    for c in db.courses:
        if c.code == course_code:
            course = c

    if student is None or course is None:
        return {
            "message": "Student or Course not found"
        }

    enrollment_service.add_course_to_student(student, course)

    return {
        "message": "Course added to student"
    }


@router.delete("/student/{student_id}/course/{course_code}")
def remove_course(student_id: int, course_code: str):

    student = None
    course = None

    for s in db.students:
        if s.id == student_id:
            student = s

    for c in db.courses:
        if c.code == course_code:
            course = c

    if student is None or course is None:
        return {
            "message": "Student or Course not found"
        }

    enrollment_service.remove_course_from_student(student, course)

    return {
        "message": "Course removed from student"
    }
@router.post("/professor/{professor_id}/course/{course_code}")
def assign_professor(professor_id: int, course_code: str):

    professor = None
    course = None

    for p in db.professors:
        if p.id == professor_id:
            professor = p

    for c in db.courses:
        if c.code == course_code:
            course = c

    if professor is None or course is None:
        return {
            "message": "Professor or Course not found"
        }

    enrollment_service.assign_professor_to_course(professor, course)

    return {
        "message": "Professor assigned to course"
    }