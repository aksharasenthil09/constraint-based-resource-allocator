The Naive Allocator has been tested and results have been obtained as follows:
Initially, Task("Math", 5, 20, 40, 75),
        Task("Physics", 4, 15, 20, 70),
        Task("Chem", 6, 10, 50, 100)
of the format (Task Name, Due Date, Total Effort (in hours), Initial Prep (in %), Threshold (in %))

The results are as followed:
Final Preparedness:
        Math: 95%
        Physics: 73.33%
        Chemistry: 100%

Success Status:
        Math: Successful (95>=75)
        Physics: Successful (73.33>=70)
        Chemistry: Successful (100>=80)

Risk Values:
        Math: 0
        Physics: 0
        Chemistry: 0

Aggregate Metrics:
        Total System Risk: 0
        Worst Task Risk: 0
        Feasible: Yes (Total required hours: 29, Available hours: 30)