Project Goal : This project allocates limited daily study time across multiple deadline-driven tasks within a fixed amount of time. THe objective of the proejct is to minimise the risk of failing to meet required preparedness thresholds while respecting hard constraints such as total available time and daily workload limits.

Definition of Success : If the final preparedness exceed the minimum required preparedness threhold on or before its due date, the task is considered to be successful.

Preparedness Update Model for v1: Preparedness increases linearly with allocated effort. If a task required Total Effort to reach 100% preparedness, then allocated effort/total effort is equal to the fractional preparedness increase. Preparedness is capped at 100%.

Risk Definition for v1: For a single task, Risk = max(0, Threshold-Final Preparedness). This represents how far below the required threshold the task remains. Total System Risk is equal to the sum of all individual task risks. Worst Task Risk is equal to the maximum individual task risk across all tasks. The project aims to minimise Total System Risk. 

Feasibility Condition: The system is not feasible if the Total Remaining Required Effort > Total Available Time. If infeasible, the project must report failure instead of generating a misleading schedule.

v1 Scope:
It includes the Task name, Due date, Estimated total effort, Current preparedness, Minimum required preparedness threshold, Duration of preparation (Horizon length), Daily workload limit, Feasibility detection, Naive allocation strategy, Greedy allocation strategy, and Risk calculation.

Monte Carlo simulation, Context-switching penalties, Cognitive fatigue modeling, Multi-objective optimization, Soft deadlines, Behavioral modifiers, and Robustness testing will be done in later versions.