The Naive Allocator has been tested and results have been obtained as follows:
Initially, Task("Math", 5, 20, 40, 75)
        Task("Physics", 4, 15, 20, 70),
        Task("Chem", 6, 10, 50, 100)
whose format is (Task Name, Due Day, Total Effort, Initial Prep, and Threshold).

Final Results are: 
        Final Preparedness:
                Math: 95%
                Physics: 73.33%
                Chemistry: 100%

        Success Status:
                Math: Successful (95>=75)
                Physics: Successful (73.33>=70)
                Chemistry: Successful(100>=80)

        Risk:
                Math: 0
                Physics: 0
                Chemistry: 0

        Aggregate Metrics:
                Total System Risk : 0
                Worst Task Risk: 0
                Feasible: Yes (Total Required hours: 29, Available: 30)  


Comparing greedy and naive allocator:
Using the parameters:
Task ["EarlyExam", due_day=2, total_effort=10, current_preparedness=20, threshold=70]
Task["MidExam", due_day=4, total_effort=20, current_preparedness=30, threhold=75]
Task["LateExam", due_day=5, total_effort=15, current_preparedness=40, threshold=80]

horizon_length=5, daily_limit=4

---Naive---
EarlyExam | Preparedness: 46.66666666666667
MidExam | Preparedness: 63.33333333333333
LateExam | Preparedness: 100
Total Risk: 35.0

---Greedy---
EarlyExam | Preparedness: 70.0
MidExam | Preparedness: 80.0
LateExam | Preparedness: 73.33333333333333
Total Risk: 6.666666666666671

As we can see, Naive offers a much higher total risk than Greedy. This is because Greedy allocates hours for each task based on a risk value that changes each hour. This allows for more efficient scheduling. However, greedy has a flaw. As we can see, MidExam has a value of preparedness above its threshold by 5%. However, Late Exam is running short of its threshold by 6.67 approximately. We may not be able to get it to 0 risk but we can certainly lower the risk. This is because the greedy rule asks the question, "Who needs the most effort per day to finish fully?" and not "Who is closest to threshold violation?" This will be attempted to solve in v2.


