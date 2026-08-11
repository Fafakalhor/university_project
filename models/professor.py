from models.person import Person

class Professor(Person):
    def __init__(self, id: str, first_name: str, last_name: str,
                 personnel_code: str, department: str):
        super().__init__(id, first_name, last_name)
        self.personnel_code = personnel_code
        self.department = department
        self.courses = []

    def assign_course(self, course_code: str) -> None:
        if course_code not in self.courses:
            self.courses.append(course_code)

    def get_courses(self) -> list:
        return self.courses

    def to_dict(self) -> dict:
     return {
        "id": self.id,
        "first_name": self.first_name,
        "last_name": self.last_name,
        "personnel_code": self.personnel_code,
        "department": self.department,
        "courses": [
            course.code for course in self.courses
        ]
    }