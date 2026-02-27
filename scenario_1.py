from models import Task, PlannerConfiguration
def get_scenario():
    tasks=[
        Task("Math", 5, 20, 40, 75),
        Task("Physics",4,15,20,70),
        Task("Chemistry",6,10,50,100)
    ]

    config = PlannerConfiguration(horizon_length=5,daily_limit=6)
    return tasks, config
