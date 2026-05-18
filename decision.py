from file_handler import save_log
from utils import get_valid_input


def score_option(name, stress_factor, mode):
    print(f"\nEvaluating {name}")

    importance = get_valid_input("Importance (1-5): ", 1, 5)
    urgency = get_valid_input("Urgency (1-5): ", 1, 5)
    effort = get_valid_input("Effort (1-5): ", 1, 5)
    benefit = get_valid_input("Benefit (1-5): ", 1, 5)

    if mode == "SURVIVAL":
        score = importance * 0.3 + urgency * 0.5 + benefit * 0.1 - effort * 0.1
    elif mode == "OPTIMISED":
        score = importance * 0.3 + urgency * 0.2 + benefit * 0.5 - effort * 0.1
    else:
        score = importance * 0.4 + urgency * 0.3 + benefit * 0.3 - effort * 0.1

    score *= (1 + stress_factor * 0.05)

    return {
        "name": name,
        "score": round(score, 2),
        "importance": importance,
        "urgency": urgency,
        "effort": effort,
        "benefit": benefit
    }


def decision_helper(stress_score, mode):
    print("\n--- Decision Helper ---")
    print(f"System Mode: {mode}")
    print("Mode affects weighting of urgency vs long-term benefit\n")

    stress_factor = stress_score / 10

    n = get_valid_input("How many options? ", 1)

    options = []

    for i in range(n):
        name = input(f"Option {i+1}: ")
        options.append(score_option(name, stress_factor, mode))

    options.sort(key=lambda x: x["score"], reverse=True)

    best = options[0]

    print("\n=== RESULTS ===")
    for i, o in enumerate(options, 1):
        print(f"{i}. {o['name']} → {o['score']}")

    top_scores = [o["score"] for o in options]
    if top_scores.count(best["score"]) > 1:
        print("\n⚖️ Tie detected → selecting first ranked option")

    print(f"\nBest: {best['name']}")

    print("\nDecision Explanation:")

    if mode == "SURVIVAL":
        print("- High stress → urgency weighted heavily")
    elif mode == "BALANCED":
        print("- Moderate stress → balanced decision-making")
    else:
        print("- Low stress → long-term benefit prioritised")

    print(f"- Selected '{best['name']}' due to highest computed score")

    save_log(f"DECISION | {best['name']} | Score={best['score']} | Mode={mode}", "DECISION")

    return {
        "best": best,
        "mode": mode,
        "all_options": options
    }