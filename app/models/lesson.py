from optapy import planning_id, planning_entity, planning_variable
from models.timeslot import Timeslot
from models.classroom import classroom
from models.timeslot import Timeslot


@planning_entity
class Lesson:
    def __init__(self, id, subject, teacher, student_group, timeslot=None, room=None):
        self.id = id
        self.subject = subject
        self.teacher = teacher
        self.student_group = student_group
        self.timeslot = timeslot
        self.room = room
        self.color = None

    @planning_id
    def get_id(self):
        return self.id

    @planning_variable(Timeslot, ["timeslotRange"])
    def get_timeslot(self):
        return self.timeslot

    def set_timeslot(self, new_timeslot):
        self.timeslot = new_timeslot

    @planning_variable(classroom, ["roomRange"])
    def get_room(self):
        return self.room

    def set_room(self, new_room):
        self.room = new_room

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color

    def __str__(self):
        return (
            f"Lesson("
            f"id={self.id}, "
            f"timeslot={self.timeslot}, "
            f"room={self.room}, "
            f"teacher={self.teacher}, "
            f"subject={self.subject}, "
            f"student_group={self.student_group}"
            f"color={self.color}"
            f")"
        )
