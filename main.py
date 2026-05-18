from decision import decision_helper
from planner import task_prioritiser
from stress import stress_checker, get_mode
from file_handler import view_logs


system_state = {
    "stress": None,
    "mode": None,
    "last_result": None
}


def display_menu():
    print("\n===================================")
    print("     LIFE ADMIN ASSISTANT")
    print("===================================")

    print("SYSTEM INSIGHT: Decisions adapt dynamically based on stress level")

    print("-----------------------------------")
    print("1. Decision Helper")
    print("2. Task Prioritiser")
    print("3. Mental Load Checker")
    print("4. View Logs")
    print("5. Exit")


def update_state(result):
    system_state["last_result"] = result


def main():
    print("Welcome to your Personal Productivity Assistant")

    while True:
        display_menu()
        choice = input("Enter choice (1-5): ").strip()

        if choice == "3":
            result = stress_checker()

            system_state["stress"] = result["stress_score"]
            system_state["mode"] = get_mode(result["stress_score"])

            print("\nSYSTEM PROPAGATION ACTIVE")
            print(f"Stress Score → {system_state['stress']}")
            print(f"Mapped Mode → {system_state['mode']}")
            print("→ This mode will influence ALL downstream decisions\n")

            update_state(result)

        elif choice == "2":
            if system_state["stress"] is None:
                print("Please run Stress Checker first.")
                continue

            result = task_prioritiser(
                system_state["stress"],
                system_state["mode"]
            )
            update_state(result)

        elif choice == "1":
            if system_state["stress"] is None:
                print("Please run Stress Checker first.")
                continue

            result = decision_helper(
                system_state["stress"],
                system_state["mode"]
            )
            update_state(result)

        elif choice == "4":
            view_logs()

        elif choice == "5":
            print("\nSession ended.")

            print("\nSESSION SUMMARY")

            if system_state["stress"] is not None:
                print(f"- Final Stress Score: {system_state['stress']}")
                print(f"- System Mode: {system_state['mode']}")

            if system_state["last_result"]:
                print("- Last operation executed successfully")

            print("\nInsight: System adapted decisions dynamically based on stress-driven mode.")

            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()