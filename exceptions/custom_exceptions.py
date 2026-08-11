class CourseSelectionException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class StudentNotFoundException(CourseSelectionException):
    pass


class ProfessorNotFoundException(CourseSelectionException):
    pass


class CourseNotFoundException(CourseSelectionException):
    pass


class DuplicateStudentException(CourseSelectionException):
    pass


class DuplicateProfessorException(CourseSelectionException):
    pass


class DuplicateCourseException(CourseSelectionException):
    pass


class CourseCapacityFullException(CourseSelectionException):
    pass