class Task:
    def __init__(
            self,
            name: str,
            due_day: int,
            total_effort: float,
            current_preparedness: float,
            threshold: float
    ):
        """
        Represents a single task, which in most cases will be an exam
        """
        self.name=name
        self.due_day=due_day
        self.total_effort=total_effort
        self.current_preparedness=current_preparedness
        self.threshold=threshold

    def remaining_effort(self) -> float:
        """
        Calculates how much effort is still required to reach 100% preparedness
        """
        remaining_fraction=max(0,1-self.current_preparedness/100)
        return remaining_fraction * self.total_effort
    
    def is_successful(self) -> bool:
        """
        Returns true if task meets threshold
        """
        return self.current_preparedness >= self.threshold
    
    def __str__(self):
        return f"{self.name} | Preparedness: {self.current_preparedness}"
class PlannerConfiguration:
    def __init__(self, horizon_length: int, daily_limit: float):
        self.horizon_length=horizon_length
        self.daily_limit=daily_limit

    def total_available_time(self) -> float:
        return self.horizon_length*self.daily_limit