from models.timeslot import Timeslot
from models.classroom import classroom
from models.lesson import Lesson
from models.timetable import TimeTable
from datetime import time
from services.api import Api

DAYS_OF_WEEK = ["LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES"]
HOURLY_RANGE = [h for h in range(7, 13) if h != 13]


def generate_problem():
    api = Api()
    # Timeslot
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

    # Classroom
    rooms = api.get_rooms()
    room_list = []
    for idx, room in enumerate(rooms):
        room_list.append(classroom(idx, room["ambiente"]))

    # Lesson
    lessons = api.get_lessons()
    lesson_list = []
    for idx, lesson in enumerate(lessons):
        lesson_list.append(
            Lesson(
                idx,
                lesson["curso"],
                lesson["docente"],
                lesson["grupo"]
            )
        )

    l=lesson_list[0]
    l.set_timeslot(timeslot_list[0])
    l.set_room(room_list[0])

    return TimeTable(timeslot_list, room_list, lesson_list)
    
