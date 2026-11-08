from pathlib import Path
import subprocess
import sys


TESTS = r'''
import ast
import contextlib
import io
import runpy

output = io.StringIO()
try:
    with contextlib.redirect_stdout(output):
        namespace = runpy.run_path("exercise.py")
finally:
    print(output.getvalue(), end="")

function = namespace.get("count_votes")
assert callable(function), "Expected: count_votes(votes). Actual: function is missing."
for votes, expected in [
    (["zoo", "museum", "zoo", "park", "zoo", "park"], {"zoo": 3, "museum": 1, "park": 2}),
    (["beach"], {"beach": 1}),
    (["a", "a", "a"], {"a": 3}),
    ([], {}),
]:
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        actual = function(list(votes))
    assert actual == expected, (
        f"Expected count_votes({votes!r}) to return {expected!r}. Actual: {actual!r}."
    )
    assert not captured.getvalue(), "Expected: return the dictionary. Actual: count_votes prints."

lines = output.getvalue().splitlines()
expected_output = {"zoo": 3, "museum": 1, "park": 2}
try:
    printed = ast.literal_eval(lines[0].strip())
except (IndexError, SyntaxError, ValueError):
    printed = None
assert isinstance(printed, dict) and printed == expected_output, (
    f"Expected the first output line to be {expected_output!r}. Actual: {lines[:1]!r}."
)

advanced = namespace.get("winner")
if advanced is None:
    print("\nAdvanced task: winner is not written yet.")
else:
    assert callable(advanced), "Expected: winner(counts) to be a function."
    for counts, expected in [
        ({"zoo": 3, "museum": 1, "park": 2}, "zoo"),
        ({"zoo": 1, "museum": 4, "park": 2}, "museum"),
        ({"beach": 1}, "beach"),
    ]:
        actual = advanced(dict(counts))
        assert actual == expected, (
            f"Expected winner({counts!r}) to return {expected!r}. Actual: {actual!r}."
        )
    print("\nAdvanced task: winner passed every test.")
print("__checks_complete__")
'''


def check():
    expected = "Expected example output:\n{'zoo': 3, 'museum': 1, 'park': 2}"
    try:
        result = subprocess.run(
            [sys.executable, "-c", TESTS], cwd=Path(__file__).resolve().parent,
            capture_output=True, text=True, encoding="utf-8", timeout=3,
        )
    except subprocess.TimeoutExpired:
        print("Not quite yet.\n" + expected)
        print("Actual: the program was still running after 3 seconds.")
        raise SystemExit(1)
    lines = result.stdout.strip().splitlines()
    if result.returncode or len(lines) < 2 or lines[-1] != "__checks_complete__":
        print("Not quite yet.\n" + expected)
        print("Your output:\n" + (result.stdout or "(nothing)"))
        errors = result.stderr.strip().splitlines()
        if errors:
            print(errors[-1])
        else:
            print(f"Actual: exercise.py stopped the checks early (exit status {result.returncode}).")
        raise SystemExit(1)
    print(lines[-2])
    print("Correct! count_votes and your output passed every test.")


if __name__ == "__main__":
    check()
