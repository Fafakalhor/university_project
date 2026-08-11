class DatabaseService:

    def __init__(self, database):
        self.database = database


    def save_student(self, student):
        self.database.students.append(student)
        print("Student saved")


    def save_course(self, course):
        self.database.courses.append(course)
        print("Course saved")


    def get_students(self):
        return self.database.students


    def get_courses(self):
        return self.database.courses


    def delete_student(self, student):
        if student in self.database.students:
            self.database.students.remove(student)
            print("Student deleted")


    def delete_course(self, course):
        if course in self.database.courses:
            self.database.courses.remove(course)
            print("Course deleted")