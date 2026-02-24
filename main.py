from models import Task, PlannerConfiguration
from allocator import naive_allocate

def check_feasibility(tasks, config):
    total_required=sum(task.remaining_effort() for task in tasks)
    total_available=config.total_available_time()

    print("Total required effort:", total_required)
    print("Total available time:", total_available)

    if total_required > total_available:
        print("Schedule is infeasible")
        return False
    else:
        print("Schedule is feasible")
        return True
    
def main():
    tasks=[
        Task("Math", 5, 20, 40, 75),
        Task("Physics", 4, 15, 20, 70),
        Task("Chem", 6, 10, 50, 100)
    ]    

    config=PlannerConfiguration(horizon_length=5, daily_limit=6)
    naive_allocate(tasks,config)

    for task in tasks:
        print(task)
        print("Succesful:", task.is_successful())
        print("---")


if __name__=="__main__":
    main()