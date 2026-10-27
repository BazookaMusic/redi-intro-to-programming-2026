# Mini project: Student report
# For each student:
# 1. Calculate their average score.
# 2. Print their name, average, and whether they passed (average >= 60).
# At the end, print the name of the student with the highest average.
#
# Example output:
# Alice  — average: 85.0 — Passed
# Bruno  — average: 61.7 — Passed
# Carla  — average: 91.3 — Passed
# Dina   — average: 46.7 — Did not pass
# Top student: Carla
#
# Write your solution below.
students = [
    ("Alice", [85, 92, 78]),
    ("Bruno", [60, 55, 70]),
    ("Carla", [95, 88, 91]),
    ("Dina",  [40, 52, 48]),
]
best_name    = ""
best_average = 0
for name, scores in students:
    total = 0
    for score in scores:
        total = total + score
    average = total / len(scores)
    result = "Passed" if average >= 60 else "Did not pass"
    print(f"{name:<6} — average: {average:.1f} — {result}")
    if average > best_average:
        best_average = average
        best_name    = name
print(f"Top student: {best_name}")
