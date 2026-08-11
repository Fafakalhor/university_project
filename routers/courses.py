from fastapi import APIRouter

from services.course_service import CourseService
from models.course import Course
from schemas.course_schema import CourseCreate, CourseUpdate


router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


from dependencies import db, course_service

@router.post("/")
def create_course(course_data: CourseCreate):

    course = Course(
        len(db.courses) + 1,
        course_data.title,
        course_data.code,
        course_data.unit,
        course_data.capacity
    )

    course_service.add_course(course)

    return {
        "message": "Course created successfully",
        "course": {
            "title": course.title,
            "code": course.code,
            "unit": course.unit,
            "capacity": course.capacity
        }
    }


@router.get("/")
def get_courses():

    courses = course_service.get_courses()

    return [
        {
            "title": c.title,
            "code": c.code,
            "unit": c.unit,
            "capacity": c.capacity
        }
        for c in courses
    ]


@router.get("/{course_code}")
def get_course(course_code: str):

    course = course_service.find_course(course_code)

    if course:
        return {
            "title": course.title,
            "code": course.code,
            "unit": course.unit,
            "capacity": course.capacity
        }

    return {
        "message": "Course not found"
    }


@router.delete("/{course_code}")
def delete_course(course_code: str):

    course_service.delete_course(course_code)

    return {
        "message": "Course delete request completed"
    }
@router.put("/{course_code}")
def update_course(course_code: str, course_data: CourseUpdate):

    course = course_service.find_course(course_code)

    if not course:
        return {
            "message": "Course not found"
        }

    if course_data.title is not None:
        course.title = course_data.title

    if course_data.code is not None:
        course.code = course_data.code

    if course_data.unit is not None:
        course.unit = course_data.unit

    if course_data.capacity is not None:
        course.capacity = course_data.capacity

    return {
        "message": "Course updated successfully",
        "course": {
            "title": course.title,
            "code": course.code,
            "unit": course.unit,
            "capacity": course.capacity
        }
    }