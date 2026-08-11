class EnrollmentService:

    def add_course_to_student(self, student, course):
        if course.code in student.get_courses():
            print("Student already has this course")
            return

        if len(course.students) >= course.capacity:
            print("Course is full")
            return

        student.select_course(course.code)
        course.students.append(student)

        print("Course added to student")


    def remove_course_from_student(self, student, course):
        if course.code not in student.get_courses():
            print("Course not found for this student")
            return

        student.drop_course(course.code)

        if student in course.students:
            course.students.remove(student)

        print("Course removed from student")


    def get_student_courses(self, student):
        return student.get_courses()
    def assign_professor_to_course(self, professor, course):

     course.professor = professor

     if hasattr(professor, "assign_course"):
      professor.assign_course(course.code)

    print("Professor assigned to course")