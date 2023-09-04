from optapy import constraint_provider
from optapy.score import HardSoftScore
from optapy.constraint import ConstraintFactory, Joiners
from datetime import datetime, date, timedelta
from models.lesson import Lesson

# Trick since timedelta only works with datetime instances
today = date.today()


def within_30_minutes(lesson1: Lesson, lesson2: Lesson):
    between = datetime.combine(today, lesson1.timeslot.end_time) - datetime.combine(
        today, lesson2.timeslot.start_time
    )
    return timedelta(minutes=0) <= between <= timedelta(minutes=30)


def within_1_hour(lesson1: Lesson, lesson2: Lesson):
    between = datetime.combine(today, lesson1.timeslot.end_time) - datetime.combine(
        today, lesson2.timeslot.start_time
    )
    return timedelta(minutes=0) <= between <= timedelta(minutes=0)


# al mismo dia, pero no tiempos consecutivos
def within_sam_day(lesson1: Lesson, lesson2: Lesson):
    between = datetime.combine(today, lesson1.timeslot.end_time) - datetime.combine(
        today, lesson2.timeslot.start_time
    )
    return between > timedelta(minutes=0)


# Type annotation not needed, but allows you to get autocompletion
@constraint_provider
def define_constraints(constraint_factory: ConstraintFactory):
    return [
        # Hard constraints
        room_conflict(constraint_factory),
        teacher_conflict(constraint_factory),
        student_group_conflict(constraint_factory),
        # Soft constraints
        # teacher_room_stability(constraint_factory),
        # teacher_time_efficiency(constraint_factory),
        # student_group_subject_variety(constraint_factory),
        # student_group_time_efficiency(constraint_factory),
        studen_group_room_stability(constraint_factory),
    ]


def room_conflict(constraint_factory: ConstraintFactory):
    # Una sala puede albergar como máximo una lección al mismo tiempo.
    return (
        constraint_factory.for_each(Lesson)
        .join(
            Lesson,
            # ... in the same timeslot ...
            Joiners.equal(lambda lesson: lesson.timeslot),
            # ... in the same room ...
            Joiners.equal(lambda lesson: lesson.room),
            # form unique pairs
            Joiners.less_than(lambda lesson: lesson.id),
        )
        .penalize("Room conflict", HardSoftScore.ONE_HARD)
    )


def teacher_conflict(constraint_factory: ConstraintFactory):
    # Un maestro puede enseñar como máximo una lección al mismo tiempo.
    return (
        constraint_factory.for_each(Lesson)
        .join(
            Lesson,
            Joiners.equal(lambda lesson: lesson.timeslot),
            Joiners.equal(lambda lesson: lesson.teacher),
            Joiners.less_than(lambda lesson: lesson.id),
        )
        .penalize("Teacher conflict", HardSoftScore.ONE_HARD)
    )


def student_group_conflict(constraint_factory: ConstraintFactory):
    # Un estudiante puede asistir como máximo a una lección al mismo tiempo.
    return (
        constraint_factory.for_each(Lesson)
        .join(
            Lesson,
            Joiners.equal(lambda lesson: lesson.timeslot),
            Joiners.equal(lambda lesson: lesson.student_group),
            Joiners.less_than(lambda lesson: lesson.id),
        )
        .penalize("Student group conflict", HardSoftScore.ONE_HARD)
    )


def studen_group_room_stability(constraint_factory: ConstraintFactory):
    # Los estudiantes prefieren permanecer en el mismo aula para clases consecutivas.
    return (
        constraint_factory.for_each(Lesson)
        .join(
            Lesson,
            Joiners.equal(lambda lesson: lesson.student_group),
            Joiners.less_than(lambda lesson: lesson.id),
        )
        .filter(lambda lesson1, lesson2: lesson1.room != lesson2.room)
        .penalize("studen_group room stability", HardSoftScore.ONE_SOFT)
    )


def teacher_time_efficiency(constraint_factory: ConstraintFactory):
    # Un maestro prefiere enseñar lecciones secuenciales y no le gustan los espacios entre lecciones.
    return (
        constraint_factory.for_each(Lesson)
        .join(
            Lesson,
            Joiners.equal(lambda lesson: lesson.teacher),
            Joiners.equal(lambda lesson: lesson.timeslot.day_of_week),
        )
        .filter(within_30_minutes)
        .reward("Teacher time efficiency", HardSoftScore.ONE_SOFT)
    )


def student_group_subject_variety(constraint_factory: ConstraintFactory):
    # A un grupo de estudiantes no le gustan las lecciones secuenciales sobre el mismo tema.
    return (
        constraint_factory.for_each(Lesson)
        .join(
            Lesson,
            Joiners.equal(lambda lesson: lesson.subject),
            Joiners.equal(lambda lesson: lesson.student_group),
            Joiners.equal(lambda lesson: lesson.timeslot.day_of_week),
        )
        .filter(within_30_minutes)
        .penalize("Student group subject variety", HardSoftScore.ONE_SOFT)
    )


def student_group_time_efficiency(constraint_factory: ConstraintFactory):
    # un grupo de estudiantes prefiere minimo 2 horas de clase del mismo tema
    return (
        constraint_factory.for_each(Lesson)
        .join(
            Lesson,
            Joiners.equal(lambda lesson: lesson.subject),
            Joiners.equal(lambda lesson: lesson.student_group),
            Joiners.equal(lambda lesson: lesson.timeslot.day_of_week),
        )
        .filter(within_sam_day)
        .penalize("Student group time efficiency", HardSoftScore.ONE_SOFT)
    )
