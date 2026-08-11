from data.storage import save_all
from exceptions.custom_exceptions import (
    DuplicateProfessorException,
    ProfessorNotFoundException
)

class ProfessorService:

    def __init__(self, database):
        self.database = database

    def add_professor(self, professor):
     if self.find_professor(professor.id):
        raise DuplicateProfessorException("Professor already exists")

     self.database.professors.append(professor)

     save_all(
        self.database.students,
        self.database.professors,
        self.database.courses
    )

    print("Professor added successfully")

    def get_professors(self):
        return self.database.professors

    def find_professor(self, professor_id):
        for professor in self.database.professors:
            if professor.id == professor_id:
                return professor
        return None

    def delete_professor(self, professor_id):
     professor = self.find_professor(professor_id)

     if professor:
        self.database.professors.remove(professor)

        save_all(
            self.database.students,
            self.database.professors,
            self.database.courses
        )

        print("Professor deleted")
     else:
        raise ProfessorNotFoundException("Professor not found")