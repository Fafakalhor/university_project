from data.storage import load_all
from models.student import Student
from models.professor import Professor
from models.course import Course


class Database:

    def __init__(self):

        self.students = []
        self.courses = []
        self.professors = []

        data = load_all()

        for s in data["students"]:
            self.students.append(
                Student(
                    s["id"],
                    s["first_name"],
                    s["last_name"],
                    s["student_number"],
                    s["major"]
                )
            )

        for p in data["professors"]:
            self.professors.append(
                Professor(
                    p["id"],
                    p["first_name"],
                    p["last_name"],
                    p["personnel_code"],
                    p["department"]
                )
            )

        for c in data["courses"]:
            self.courses.append(
                Course(
                    c["code"],
                    c["title"],
                    c["major"],
                    c["unit"],
                    c["capacity"]
                )
            )