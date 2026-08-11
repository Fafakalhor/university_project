class Course:
    def __init__(self, code: str, title: str, major: str, 
                 unit: int, capacity: int):
        self.code = code
        self.title = title
        self.major = major
        self.unit = unit
        self.capacity = capacity
        self.students = []
        self.professor = None

    def is_full(self) -> bool:
        return len(self.students) >= self.capacity

    def add_student(self, student_number: str) -> bool:
        if self.is_full():
            return False
        if student_number not in self.students:
            self.students.append(student_number)
            return True
        return False

    def remove_student(self, student_number: str) -> bool:
        if student_number in self.students:
            self.students.remove(student_number)
            return True
        return False

    def assign_professor(self, professor_id: str) -> None:
        self.professor = professor_id

    def to_dict(self) -> dict:
     return {
        "code": self.code,
        "title": self.title,
        "major": self.major,
        "unit": self.unit,
        "capacity": self.capacity,
        "students": [
            student.id for student in self.students
        ],
        "professor": self.professor.id if self.professor else None
    }