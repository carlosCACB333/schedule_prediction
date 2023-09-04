from models.timeslot import Timeslot
from models.classroom import classroom
from models.lesson import Lesson
from models.timetable import TimeTable
from datetime import time

DAYS_OF_WEEK = ["LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES"][0:1]
HOURLY_RANGE = [h for h in range(7, 22) if h != 13]


def generate_problem():
    counter = 0
    timeslot_list = []
    for day in DAYS_OF_WEEK:
        for h in HOURLY_RANGE:
            timeslot_list.append(
                Timeslot(
                    counter,
                    day,
                    time(hour=h, minute=0),
                    time(hour=h + 1, minute=0),
                )
            )
            counter += 1

    room_list = [classroom(0, "G401"), classroom(1, "G402"), classroom(2, "G4003")]
    lesson_list = [
        Lesson(0, "MatematicaI", "Alejando Pacheco", "ciclo1"),
        Lesson(1, "MatematicaII", "Alejando Pacheco", "ciclo2"),
        Lesson(2, "MatematicaIII", "Alejando Pacheco", "ciclo3"),
        Lesson(3, "MatematicaIV", "Alejando Pacheco", "ciclo4"),
        Lesson(4, "MatematicaV", "Alejando Pacheco", "ciclo5"),
        Lesson(5, "MatematicaVI", "Alejando Pacheco", "ciclo6"),
        Lesson(6, "MatematicaVII", "Alejando Pacheco", "ciclo7"),
        Lesson(7, "MatematicaVIII", "Alejando Pacheco", "ciclo8"),
        Lesson(8, "MatematicaI", "Alejando Pacheco", "ciclo1"),
    ]
    lesson = lesson_list[0]
    lesson.set_timeslot(timeslot_list[0])
    lesson.set_room(room_list[0])

    return TimeTable(timeslot_list, room_list, lesson_list)


def getResponseExample():
    data = {
        "timeslot_list": [
            {
                "id": 1,
                "day_of_week": "MONDAY",
                "start_time": "08:30:00",
                "end_time": "09:30:00",
            },
            {
                "id": 2,
                "day_of_week": "MONDAY",
                "start_time": "09:30:00",
                "end_time": "10:30:00",
            },
            {
                "id": 3,
                "day_of_week": "MONDAY",
                "start_time": "10:30:00",
                "end_time": "11:30:00",
            },
            {
                "id": 4,
                "day_of_week": "MONDAY",
                "start_time": "13:30:00",
                "end_time": "14:30:00",
            },
            {
                "id": 5,
                "day_of_week": "MONDAY",
                "start_time": "14:30:00",
                "end_time": "15:30:00",
            },
            {
                "id": 6,
                "day_of_week": "TUESDAY",
                "start_time": "08:30:00",
                "end_time": "09:30:00",
            },
            {
                "id": 7,
                "day_of_week": "TUESDAY",
                "start_time": "09:30:00",
                "end_time": "10:30:00",
            },
            {
                "id": 8,
                "day_of_week": "TUESDAY",
                "start_time": "10:30:00",
                "end_time": "11:30:00",
            },
            {
                "id": 9,
                "day_of_week": "TUESDAY",
                "start_time": "13:30:00",
                "end_time": "14:30:00",
            },
            {
                "id": 10,
                "day_of_week": "TUESDAY",
                "start_time": "14:30:00",
                "end_time": "15:30:00",
            },
        ],
        "room_list": [
            {"id": 1, "name": "Room A"},
            {"id": 2, "name": "Room B"},
            {"id": 3, "name": "Room C"},
        ],
        "lesson_list": [
            {
                "id": 1,
                "subject": "Math",
                "teacher": "A. Turing",
                "student_group": "9th grade",
                "timeslot": {
                    "id": 1,
                    "day_of_week": "MONDAY",
                    "start_time": "08:30:00",
                    "end_time": "09:30:00",
                },
                "room": {"id": 1, "name": "Room A"},
            },
            {
                "id": 2,
                "subject": "Math",
                "teacher": "A. Turing",
                "student_group": "9th grade",
                "timeslot": {
                    "id": 2,
                    "day_of_week": "MONDAY",
                    "start_time": "09:30:00",
                    "end_time": "10:30:00",
                },
                "room": {"id": 2, "name": "Room B"},
            },
            {
                "id": 3,
                "subject": "Physics",
                "teacher": "M. Curie",
                "student_group": "9th grade",
                "timeslot": {
                    "id": 10,
                    "day_of_week": "TUESDAY",
                    "start_time": "14:30:00",
                    "end_time": "15:30:00",
                },
                "room": {"id": 1, "name": "Room A"},
            },
            {
                "id": 4,
                "subject": "Chemistry",
                "teacher": "M. Curie",
                "student_group": "9th grade",
                "timeslot": {
                    "id": 4,
                    "day_of_week": "MONDAY",
                    "start_time": "13:30:00",
                    "end_time": "14:30:00",
                },
                "room": {"id": 1, "name": "Room A"},
            },
            {
                "id": 5,
                "subject": "Biology",
                "teacher": "C. Darwin",
                "student_group": "9th grade",
                "timeslot": {
                    "id": 5,
                    "day_of_week": "MONDAY",
                    "start_time": "14:30:00",
                    "end_time": "15:30:00",
                },
                "room": {"id": 1, "name": "Room A"},
            },
            {
                "id": 6,
                "subject": "History",
                "teacher": "I. Jones",
                "student_group": "9th grade",
                "timeslot": {
                    "id": 6,
                    "day_of_week": "TUESDAY",
                    "start_time": "08:30:00",
                    "end_time": "09:30:00",
                },
                "room": {"id": 1, "name": "Room A"},
            },
            {
                "id": 7,
                "subject": "English",
                "teacher": "I. Jones",
                "student_group": "9th grade",
                "timeslot": {
                    "id": 7,
                    "day_of_week": "TUESDAY",
                    "start_time": "09:30:00",
                    "end_time": "10:30:00",
                },
                "room": {"id": 1, "name": "Room A"},
            },
            {
                "id": 8,
                "subject": "English",
                "teacher": "I. Jones",
                "student_group": "9th grade",
                "timeslot": {
                    "id": 8,
                    "day_of_week": "TUESDAY",
                    "start_time": "10:30:00",
                    "end_time": "11:30:00",
                },
                "room": {"id": 1, "name": "Room A"},
            },
            {
                "id": 9,
                "subject": "Spanish",
                "teacher": "P. Cruz",
                "student_group": "9th grade",
                "timeslot": {
                    "id": 9,
                    "day_of_week": "TUESDAY",
                    "start_time": "13:30:00",
                    "end_time": "14:30:00",
                },
                "room": {"id": 2, "name": "Room B"},
            },
            {
                "id": 10,
                "subject": "Spanish",
                "teacher": "P. Cruz",
                "student_group": "9th grade",
                "timeslot": {
                    "id": 3,
                    "day_of_week": "MONDAY",
                    "start_time": "10:30:00",
                    "end_time": "11:30:00",
                },
                "room": {"id": 1, "name": "Room A"},
            },
            {
                "id": 11,
                "subject": "Math",
                "teacher": "A. Turing",
                "student_group": "10th grade",
                "timeslot": {
                    "id": 3,
                    "day_of_week": "MONDAY",
                    "start_time": "10:30:00",
                    "end_time": "11:30:00",
                },
                "room": {"id": 2, "name": "Room B"},
            },
            {
                "id": 12,
                "subject": "Math",
                "teacher": "A. Turing",
                "student_group": "10th grade",
                "timeslot": {
                    "id": 9,
                    "day_of_week": "TUESDAY",
                    "start_time": "13:30:00",
                    "end_time": "14:30:00",
                },
                "room": {"id": 3, "name": "Room C"},
            },
            {
                "id": 13,
                "subject": "Math",
                "teacher": "A. Turing",
                "student_group": "10th grade",
                "timeslot": {
                    "id": 6,
                    "day_of_week": "TUESDAY",
                    "start_time": "08:30:00",
                    "end_time": "09:30:00",
                },
                "room": {"id": 2, "name": "Room B"},
            },
            {
                "id": 14,
                "subject": "Physics",
                "teacher": "M. Curie",
                "student_group": "10th grade",
                "timeslot": {
                    "id": 5,
                    "day_of_week": "MONDAY",
                    "start_time": "14:30:00",
                    "end_time": "15:30:00",
                },
                "room": {"id": 3, "name": "Room C"},
            },
            {
                "id": 15,
                "subject": "Chemistry",
                "teacher": "M. Curie",
                "student_group": "10th grade",
                "timeslot": {
                    "id": 2,
                    "day_of_week": "MONDAY",
                    "start_time": "09:30:00",
                    "end_time": "10:30:00",
                },
                "room": {"id": 3, "name": "Room C"},
            },
            {
                "id": 16,
                "subject": "French",
                "teacher": "M. Curie",
                "student_group": "10th grade",
                "timeslot": {
                    "id": 1,
                    "day_of_week": "MONDAY",
                    "start_time": "08:30:00",
                    "end_time": "09:30:00",
                },
                "room": {"id": 2, "name": "Room B"},
            },
            {
                "id": 17,
                "subject": "Geography",
                "teacher": "C. Darwin",
                "student_group": "10th grade",
                "timeslot": {
                    "id": 8,
                    "day_of_week": "TUESDAY",
                    "start_time": "10:30:00",
                    "end_time": "11:30:00",
                },
                "room": {"id": 2, "name": "Room B"},
            },
            {
                "id": 18,
                "subject": "History",
                "teacher": "I. Jones",
                "student_group": "10th grade",
                "timeslot": {
                    "id": 4,
                    "day_of_week": "MONDAY",
                    "start_time": "13:30:00",
                    "end_time": "14:30:00",
                },
                "room": {"id": 2, "name": "Room B"},
            },
            {
                "id": 19,
                "subject": "English",
                "teacher": "P. Cruz",
                "student_group": "10th grade",
                "timeslot": {
                    "id": 7,
                    "day_of_week": "TUESDAY",
                    "start_time": "09:30:00",
                    "end_time": "10:30:00",
                },
                "room": {"id": 2, "name": "Room B"},
            },
            {
                "id": 20,
                "subject": "Spanish",
                "teacher": "P. Cruz",
                "student_group": "10th grade",
                "timeslot": {
                    "id": 10,
                    "day_of_week": "TUESDAY",
                    "start_time": "14:30:00",
                    "end_time": "15:30:00",
                },
                "room": {"id": 2, "name": "Room B"},
            },
        ],
        "score": {},
        "_optapy_solver_run_id": [
            139928606931168,
            139928607098112,
            "213dcfec-4127-11ee-a728-0242ac1a0002",
        ],
    }
    return data
