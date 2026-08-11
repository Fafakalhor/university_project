from database import Database

from services.student_service import StudentService
from services.course_service import CourseService
from services.Professor_Service import ProfessorService
from services.enrollment_service import EnrollmentService


db = Database()

student_service = StudentService(db)
course_service = CourseService(db)
professor_service = ProfessorService(db)
enrollment_service = EnrollmentService()