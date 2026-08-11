from data.storage import save_all
from exceptions.custom_exceptions import (
    DuplicateCourseException,
    CourseNotFoundException
)

class CourseService:

    def __init__(self, database):
        self.database = database


    def add_course(self, course):
     if self.find_course(course.code):
        raise DuplicateCourseException("Course already exists")

     self.database.courses.append(course)

     save_all(
        self.database.students,
        self.database.professors,
        self.database.courses
    )

    print("Course added successfully")
    def assign_professor(self, course_code, professor):
        course = self.get_courses_by_code(course_code)
        if course is None:
            print("course not found!")
            return
        course.professor = professor
        print("professor assigned successfully. ")
    
    def get_courses(self):
        return self.database.courses


    def find_course(self, course_code):
        for course in self.database.courses:
            if course.code == course_code:
                return course

        return None


    def delete_course(self, course_code):
     course = self.find_course(course_code)

     if course:
        self.database.courses.remove(course)

        save_all(
            self.database.students,
            self.database.professors,
            self.database.courses
        )

        print("Course deleted")
     else:
        raise CourseNotFoundException("Course not found")