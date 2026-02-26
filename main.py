from models import Task, PlannerConfiguration
from allocator import naive_allocate, greedy_allocate
from risk import calculate_totalrisk, calculate_worstrisk

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
    
def run_simulation(allocator, label):
    tasks=[
        Task("EarlyExam", 2, 10, 20, 70),
        Task("MidExam", 4, 20, 30, 75),
        Task("LateExam", 5, 15, 40, 80)
    ]

    config= PlannerConfiguration(horizon_length=5, daily_limit=4)
    allocator(tasks, config)

    print(f"\n---{label}---")
    for task in tasks:
        print(task)

    print("Total Risk:", calculate_totalrisk(tasks))
    
def main():
    run_simulation(naive_allocate, "Naive")
    run_simulation(greedy_allocate, "Greedy")
    
if __name__=="__main__":
    main()