def calculate_taskrisk(task):
    """
    Risk is how far below the threshold the task remains.
    If preparedness >= threshold, risk = 0.
    """
    return max(0, task.threshold - task.current_preparedness)


def calculate_totalrisk(tasks):
    return sum(calculate_taskrisk(task) for task in tasks)


def calculate_worstrisk(tasks):
    if not tasks:
        return 0
    return max(calculate_taskrisk(task) for task in tasks)


def calculate_tasksurplus(task):
    """
    Surplus is how far above threshold the task is.
    If preparedness <= threshold, surplus = 0.
    """
    return max(0, task.current_preparedness - task.threshold)


def calculate_totalsurplus(tasks):
    return sum(calculate_tasksurplus(task) for task in tasks)


def calculate_successcount(tasks):
    """
    Counts how many tasks meet or exceed threshold.
    """
    return sum(1 for task in tasks if calculate_taskrisk(task) == 0)


def evaluate_tasks(tasks):
    """
    Returns a dictionary of overall metrics.
    """
    return {
        "total_risk": calculate_totalrisk(tasks),
        "worst_risk": calculate_worstrisk(tasks),
        "total_surplus": calculate_totalsurplus(tasks),
        "success_count": calculate_successcount(tasks),
        "total_tasks": len(tasks),
    }


def print_evaluation(tasks):
    """
    Prints per-task and overall evaluation metrics.
    """
    print("\n--- Task Results ---")
    for task in tasks:
        risk = calculate_taskrisk(task)
        surplus = calculate_tasksurplus(task)
        status = "OK" if risk == 0 else "AT RISK"

        print(f"{task.name}:")
        print(f"  Preparedness: {task.current_preparedness:.2f}")
        print(f"  Threshold: {task.threshold}")
        print(f"  Risk: {risk:.2f}")
        print(f"  Surplus: {surplus:.2f}")
        print(f"  Status: {status}")

    metrics = evaluate_tasks(tasks)

    print("\n--- Summary ---")
    print(f"Total Risk: {metrics['total_risk']:.2f}")
    print(f"Worst Task Risk: {metrics['worst_risk']:.2f}")
    print(f"Total Surplus: {metrics['total_surplus']:.2f}")
    print(f"Tasks Meeting Threshold: {metrics['success_count']}/{metrics['total_tasks']}")