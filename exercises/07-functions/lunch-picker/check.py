from pathlib import Path
import subprocess
import sys


TESTS = r'''
import contextlib
import io
import runpy

output = io.StringIO()
with contextlib.redirect_stdout(output):
    namespace = runpy.run_path("exercise.py")
print(output.getvalue(), end="")
function = namespace.get("pick_lunch")
assert callable(function), "Expected: pick_lunch(options). Actual: function is missing."

options = ["pizza", "sushi", "falafel"]
seen = set()
for _ in range(200):
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        actual = function(options)
    assert not captured.getvalue(), "Expected: return the food. Actual: pick_lunch prints."
    assert actual in options, (
        f"Expected pick_lunch({options!r}) to return one of {options!r}. Actual: {actual!r}."
    )
    seen.add(actual)
assert len(seen) > 1, (
    f"Expected: a random food each time. Actual: always {actual!r}."
)
assert function(["soup"]) == "soup", "Expected pick_lunch(['soup']) to return 'soup'."

foods = namespace.get("foods")
assert isinstance(foods, list) and len(foods) >= 3, (
    f"Expected: a list called foods with at least three foods. Actual: {foods!r}."
)
lines = output.getvalue().splitlines()
assert lines and lines[0].strip() in [str(food) for food in foods], (
    f"Expected the first output line: one food from {foods!r}. Actual: {lines[:1]!r}."
)

advanced = namespace.get("plan_week")
if advanced is None:
    print("\nAdvanced task: plan_week is not written yet.")
else:
    assert callable(advanced), "Expected: plan_week(options, days) to be a function."
    for days in (3, 5, 0):
        actual = advanced(options, days)
        assert isinstance(actual, list) and len(actual) == days, (
            f"Expected plan_week(options, {days}) to return a list of {days} foods. "
            f"Actual: {actual!r}."
        )
        assert all(food in options for food in actual), (
            f"Expected every lunch to come from {options!r}. Actual: {actual!r}."
        )
    plans = {tuple(advanced(options, 5)) for _ in range(20)}
    assert len(plans) > 1, "Expected: random lunches. Actual: the same plan every time."
    print("\nAdvanced task: plan_week passed every test.")
'''


def check():
    expected = (
        "Expected input and output:\n"
        "pick_lunch(['pizza', 'sushi', 'falafel']) returns one of the three foods\n"
        "Your program prints one food from your foods list, for example:\nsushi"
    )
    try:
        result = subprocess.run(
            [sys.executable, "-c", TESTS], cwd=Path(__file__).resolve().parent,
            capture_output=True, text=True, encoding="utf-8", timeout=3,
        )
    except subprocess.TimeoutExpired:
        print("Not quite yet.\n" + expected)
        print("Actual: the program was still running after 3 seconds.")
        raise SystemExit(1)
    if result.returncode:
        print("Not quite yet.\n" + expected)
        print("Your output:\n" + (result.stdout or "(nothing)"))
        print(result.stderr.strip().splitlines()[-1])
        raise SystemExit(1)
    print(result.stdout.strip().splitlines()[-1])
    print("Correct! pick_lunch and its output passed every test.")


if __name__ == "__main__":
    check()
