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
    
    def apply_effort(self, hours: float):
        """
        Applies effort and updates preparedness linearly
        """
        if self.total_effort==0:
            return
        effort_fraction=hours/self.total_effort
        self.current_preparedness+=effort_fraction*100
        self.current_preparedness=min(self.current_preparedness, 100)

    def days_remaining(self, current_day: int) -> int:
        """
        Returns how many days remain before due date.
        Always returns at least 1 to avoid division by 0
        """
        return max(1, self.due_day-current_day)
    
    def threshold_remaining_effort(self):
        """
        Reutrns how many hours are eneded to reach threshold
        Reutrns 0 if threshold already met
        """
        if self.current_preparedness >= self.threshold:
            return 0
        
        percent_gap = self.threshold - self.current_preparedness
        return (percent_gap/100) * self.total_effort


class PlannerConfiguration:
    def __init__(self, horizon_length: int, daily_limit: float):
        self.horizon_length=horizon_length
        self.daily_limit=daily_limit

    def total_available_time(self) -> float:
        return self.horizon_length*self.daily_limit