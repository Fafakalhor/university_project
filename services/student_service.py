from data.storage import save_all
from exceptions.custom_exceptions import (
    StudentNotFoundException,
    DuplicateStudentException
)
class StudentService:

    def __init__(self, database):
        self.database = database


    def add_student(self, student):
     if self.find_student(student.id):
        raise DuplicateStudentException("Student already exists")

     self.database.students.append(student)

     save_all(
        self.database.students,
        self.database.professors,
        self.database.courses
    )

    print("Student added successfully") 

    def get_students(self):
        return self.database.students


    def find_student(self, student_id):
        for student in self.database.students:
            if student.id == student_id:
                return student

        return None


    def delete_student(self, student_id):
     student = self.find_student(student_id)

     if student:
        self.database.students.remove(student)

        save_all(
            self.database.students,
            self.database.professors,
            self.database.courses
        )

        print("Student deleted")
     else:
        raise StudentNotFoundException("Student not found")