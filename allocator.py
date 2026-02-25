def greedy_allocate(tasks, config):
    """
    Allocates time based on urgency.
    Urgency = remaining_effort/days_remaining
    """

    for day in range(config.horizon_length):

        active_tasks = [task for task in tasks if task.due_day>day]

        if not active_tasks:
            continue
        
        remaining_hours=config.daily_limit

        while remaining_hours>0 and active_tasks:
            active_tasks.sort(
                key=lambda t: t.remaining_effort()/t.days_remaining(day),
                reverse=True
            )

            most_urgent = active_tasks[0]

            allocation = min(1, remaining_hours)

            most_urgent.apply_effort(allocation)

            remaining_hours=remaining_hours-allocation

            if most_urgent.remaining_effort() == 0:
                active_tasks.remove(most_urgent)

def naive_allocate(tasks, config):
    """
    Distributes daily available hours euqally among tasks.
    Simulates day-by-day allocation.
    """
    for day in range(config.horizon_length):
        active_tasks = [task for task in tasks if task.due_day > day]
        if not active_tasks:
            continue

        daily_share=config.daily_limit/len(active_tasks)

        for task in active_tasks:
            task.apply_effort(daily_share)