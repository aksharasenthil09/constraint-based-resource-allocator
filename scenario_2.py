from models import Task, PlannerConfiguration

def get_scenario():
    tasks = [
        Task("EarlyExam", 2, 10, 20, 70),
        Task("MidExam", 4, 20, 30, 75),
        Task("LateExam", 5, 15, 40, 80)
    ]

    config=PlannerConfiguration(horizon_length=5, daily_limit=4)

    return tasks, config