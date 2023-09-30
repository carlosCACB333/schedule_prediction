from optapy import solver_factory_create
from optapy import config
from fastapi import APIRouter
from optapy.types import Duration
from models.lesson import Lesson
from models.timetable import TimeTable
from libs.constraints import define_constraints
from utils.problem import generate_problem
from services.api import Api
from utils.color import pick_color

main_router = APIRouter(prefix="/api", tags=["api"])


@main_router.get("/timetable")
async def get_timetable():
    solver_config = (
        config.solver.SolverConfig()
        .withEntityClasses(Lesson)
        .withSolutionClass(TimeTable)
        .withConstraintProviderClass(define_constraints)
        .withTerminationSpentLimit(Duration.ofSeconds(120))
    )   

    solution: TimeTable = (
        solver_factory_create(solver_config).buildSolver().solve(generate_problem())
    )
    print(solution)
    timeslot_list = solution.timeslot_list
    lesson_list = solution.lesson_list
    room_list = solution.room_list

    lesson_matriz = [
        [[] for _ in range(len(room_list))] for _ in range(len(timeslot_list))
    ]

    for lesson in lesson_list:
        lesson_timeslot_id = lesson.timeslot.id
        lesson_room_id = lesson.room.id
        c = pick_color(lesson.subject)
        lesson.set_color(c)
        lesson_matriz[lesson_timeslot_id][lesson_room_id].append(lesson)
    return {
        "timeslot_list": timeslot_list,
        "room_list": room_list,
        "lesson_matriz": lesson_matriz,
    }


@main_router.get("/test")
async def test():
    api = Api()
    return {
        "lessons": api.get_lessons(),
        "rooms": api.get_rooms(),
    }
