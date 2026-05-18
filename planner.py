from file_handler import save_log
from utils import get_valid_input


def calculate_priority(importance, days_left, stress_factor):
    if days_left == 0:
        urgency = 5
    elif days_left <= 2:
        urgency = 4
    elif days_left <= 5:
        urgency = 3
    elif days_left <= 10:
        urgency = 2
    else:
        urgency = 1

    urgency = urgency * (1 + stress_factor)

    priority = importance * 0.6 + urgency * 0.4
    return round(priority, 2), urgency


def task_prioritiser(stress_score, mode):
    print("\n--- Task Prioritiser ---")

    stress_factor = stress_score / 10

    print(f"System Mode: {mode}")

    n = get_valid_input("How many tasks? ", 1)

    tasks = []

    for i in range(n):
        print(f"\nTask {i+1}")
        name = input("Task name: ")
        days = get_valid_input("Days until due: ", 0)
        importance = get_valid_input("Importance (1-5): ", 1, 5)

        priority, urgency = calculate_priority(
            importance,
            days,
            stress_factor
        )

        tasks.append({
            "name": name,
            "priority": priority,
            "days": days,
            "urgency": urgency
        })

    if mode == "SURVIVAL":
        tasks = [t for t in tasks if t["days"] <= 3]

    if not tasks:
        print("\nNo tasks available after applying system filtering.")
        print("Try adding tasks with closer deadlines or switch mode.")

        save_log("TASK | No valid tasks after filtering", "TASK")

        return {
            "top_task": None,
            "mode": mode,
            "all_tasks": []
        }

    tasks.sort(key=lambda x: x["priority"], reverse=True)

    print("\n=== PRIORITY ORDER ===")

    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t['name']} → {t['priority']}")

    top = tasks[0]

    save_log(f"TASK | {top['name']} | {top['priority']}", "TASK")

    return {
        "top_task": top,
        "mode": mode,
        "all_tasks": tasks
    }