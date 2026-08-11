from models.person import Person

class Student(Person):
    def __init__(self, id: str, first_name: str, last_name: str, 
                 student_number: str, major: str):
        super().__init__(id, first_name, last_name)
        self.student_number = student_number
        self.major = major
        self.selected_courses = []

    def select_course(self, course_code: str) -> None:
        if course_code not in self.selected_courses:
            self.selected_courses.append(course_code)

    def drop_course(self, course_code: str) -> None:
        if course_code in self.selected_courses:
            self.selected_courses.remove(course_code)

    def get_courses(self) -> list:
        return self.selected_courses

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "student_number": self.student_number,
            "major": self.major,
            "selected_courses": self.selected_courses
        }