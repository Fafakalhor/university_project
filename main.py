from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from contextlib import asynccontextmanager

from routers import students
from routers import professors
from routers import courses
from routers import enrollment

from data.storage import save_all

from exceptions.custom_exceptions import (
    CourseSelectionException,
)

# برای ساخت سرویس‌ها و دیتابیس در زمان اجرای برنامه
from dependencies import (
    db,
    student_service,
    course_service,
    professor_service,
    enrollment_service,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

    save_all(
        db.students,
        db.professors,
        db.courses
    )


app = FastAPI(
    title="University System API",
    description="University Management System",
    version="1.0.0",
    lifespan=lifespan
)


# =========================
# Routers
# =========================

app.include_router(students.router)
app.include_router(professors.router)
app.include_router(courses.router)
app.include_router(enrollment.router)


# =========================
# Home Page
# =========================

@app.get("/", include_in_schema=False)
def home():
    return FileResponse("static/index.html")


# =========================
# Exception Handling
# =========================

@app.exception_handler(CourseSelectionException)
async def course_selection_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "message": str(exc)
        }
    )


# =========================
# Summary / Statistics
# =========================

@app.get("/summary")
@app.get("/stats")
def summary():
    return {
        "students_count": len(db.students),
        "professors_count": len(db.professors),
        "courses_count": len(db.courses)
    }


# =========================
# All Data
# =========================

@app.get("/all-data")
def all_data():
    return {
        "students": [
            student.to_dict()
            for student in db.students
        ],

        "professors": [
            professor.to_dict()
            for professor in db.professors
        ],

        "courses": [
            course.to_dict()
            for course in db.courses
        ]
    }


print("University System Started")