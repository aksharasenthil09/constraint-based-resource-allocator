from models import Task

def main():
    math=Task(
        name="Math",
        due_day=5,
        total_effort=20,
        current_preparedness=40,
        threshold=75
    )

    print("Task:", math)
    print("Remaining effort: ", math.remaining_effort())
    print("Is successful:", math.is_successful())

if __name__ == "__main__":
    main()