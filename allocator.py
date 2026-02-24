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