from file_handler import save_log
from utils import get_valid_input


def get_mode(score):
    if score >= 8:
        return "SURVIVAL"
    elif score >= 5 and score<8:
        return "BALANCED"
    return "OPTIMISED"


def stress_checker():
    print("\n--- Mental Load Checker ---")

    stress = get_valid_input("Stress (1-10): ", 1, 10)
    sleep = get_valid_input("Sleep hours (0-12): ", 0, 12)
    workload = get_valid_input("Workload (1-10): ", 1, 10)

    sleep_impact = 10 - sleep

    score = stress * 0.5 + workload * 0.3 + sleep_impact * 0.2
    score = round(score, 2)

    state = get_mode(score)

    print("\n=== ANALYSIS ===")
    print(f"State: {state}")
    print(f"Score: {score}")

    print("\n System Interpretation:")

    if state == "SURVIVAL":
        print("High stress → system prioritises urgent survival tasks")
        print("Recommendation: Reduce workload immediately")
    elif state == "BALANCED":
        print("Moderate stress → balanced decision-making mode active")
        print("Recommendation: Maintain structure, avoid overload")
    else:
        print("Low stress → system optimises for long-term productivity")
        print("Recommendation: Focus on efficiency and planning")

    print("\nSystem Role:")
    print(f"- Stress Score drives mode selection → {state}")
    print("- Mode influences task prioritisation + decision scoring")

    save_log(f"MENTAL | {state} | {score}", "MENTAL")

    return {
        "stress_score": score,
        "state": state
    }