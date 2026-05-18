import os
from datetime import datetime

FILE_PATH = "data/logs.txt"


def save_log(entry, log_type="GENERAL"):

    try:
        os.makedirs("data", exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        formatted = f"[{timestamp}] | {log_type} | {entry}"

        with open(FILE_PATH, "a", encoding="utf-8") as file:
            file.write(formatted + "\n")

    except Exception as e:
        print(f"Logging failed: {e}")


def view_logs(filter_type=None):
    """
    Display logs with optional filtering by type.
    """

    print("\n=== LOG HISTORY ===")

    try:
        if not os.path.exists(FILE_PATH):
            print("No logs found.")
            return []

        with open(FILE_PATH, "r", encoding="utf-8") as file:
            logs = file.readlines()

        if not logs:
            print("Log file is empty.")
            return []

        filtered_logs = []

        for log in logs:
            log = log.strip()

            if filter_type:
                if f"| {filter_type} |" in log:
                    filtered_logs.append(log)
            else:
                filtered_logs.append(log)

        for log in filtered_logs:
            print("•", log)

        return filtered_logs

    except Exception as e:
        print(f"Error reading logs: {e}")
        return []