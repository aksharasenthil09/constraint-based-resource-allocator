from models import Task, PlannerConfiguration
from allocator import naive_allocate, greedy_allocate
from risk import calculate_totalrisk, calculate_worstrisk
import scenario_1
import scenario_2

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
    
def run_simulation(get_scenario, allocator, label):
    tasks, config = get_scenario()
    allocator(tasks, config)
    
    print(f"\n--- {label} ---")
    for task in tasks:
        print(task)

    print("Total Risk:", calculate_totalrisk(tasks))
    
def main():
    run_simulation(scenario_1.get_scenario, naive_allocate, "Scenario 1 - Naive")
    run_simulation(scenario_1.get_scenario, greedy_allocate, "Scenario 1 - Greedy")
    run_simulation(scenario_2.get_scenario, naive_allocate, "Scenario 2 - Naive")
    run_simulation(scenario_2.get_scenario, greedy_allocate, "Scenario 2 - Greedy")
    
if __name__=="__main__":
    main()