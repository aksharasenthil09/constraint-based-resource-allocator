def calculate_taskrisk(task):
    """
    Risk is how far below the threshold the task remains.
    If preparedness>=threshold, risk=0
    """
    return max(0, task.threshold-task.current_preparedness)

def calculate_totalrisk(tasks):
    return sum(calculate_taskrisk(task) for task in tasks)

def calculate_worstrisk(tasks):
    return max(calculate_taskrisk(task) for task in tasks)