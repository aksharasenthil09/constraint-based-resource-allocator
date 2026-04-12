from allocator import naive_allocate, greedy_allocate, threshold_greedyallocate
from risk import print_evaluation
import scenario_1
import scenario_2


def check_feasibility(tasks, config):
    total_required = sum(task.remaining_effort() for task in tasks)
    total_available = config.total_available_time()

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

    print(f"\n--- {label} ---")

    feasible = check_feasibility(tasks, config)
    if not feasible:
        print("Skipping allocation because the schedule is infeasible.")
        return

    allocator(tasks, config)
    print_evaluation(tasks)


def main():
    run_simulation(scenario_1.get_scenario, naive_allocate, "Scenario 1 - Naive")
    run_simulation(scenario_1.get_scenario, greedy_allocate, "Scenario 1 - Greedy")
    run_simulation(scenario_2.get_scenario, naive_allocate, "Scenario 2 - Naive")
    run_simulation(scenario_2.get_scenario, greedy_allocate, "Scenario 2 - Greedy")
    run_simulation(scenario_1.get_scenario, threshold_greedyallocate, "Scenario 1 - Threshold Greedy")
    run_simulation(scenario_2.get_scenario, threshold_greedyallocate, "Scenario 2 - Threshold Greedy")


if __name__ == "_main_":
    main()