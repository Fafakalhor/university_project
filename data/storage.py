import json
import os

BASE_DIR = os.path.dirname(__file__)

STUDENTS_FILE = os.path.join(BASE_DIR, "students.json")
PROFESSORS_FILE = os.path.join(BASE_DIR, "professors.json")
COURSES_FILE = os.path.join(BASE_DIR, "courses.json")


def _read_json(path):
    if not os.path.exists(path):
        return []

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _write_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def save_all(students, professors, courses):

    students_data = [
        student.to_dict()
        for student in students
    ]

    professors_data = [
        professor.to_dict()
        for professor in professors
    ]

    courses_data = [
        course.to_dict()
        for course in courses
    ]

    _write_json(STUDENTS_FILE, students_data)
    _write_json(PROFESSORS_FILE, professors_data)
    _write_json(COURSES_FILE, courses_data)


def load_all():
    return {
        "students": _read_json(STUDENTS_FILE),
        "professors": _read_json(PROFESSORS_FILE),
        "courses": _read_json(COURSES_FILE)
    }


def reset_storage():
    _write_json(STUDENTS_FILE, [])
    _write_json(PROFESSORS_FILE, [])
    _write_json(COURSES_FILE, [])