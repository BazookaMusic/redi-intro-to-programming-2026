from pathlib import Path
import subprocess
import sys


TESTS = r'''
import contextlib
import io
import runpy

output = io.StringIO()
try:
    with contextlib.redirect_stdout(output):
        namespace = runpy.run_path("exercise.py")
finally:
    print(output.getvalue(), end="")

function = namespace.get("unique_visitors")
assert callable(function), "Expected: unique_visitors(names). Actual: function is missing."
for names, expected in [
    (["Ana", "Ben", "Ana", "Cleo", "Ben"], 3),
    (["Ana", "Ana", "Ana"], 1),
    (["Dan", "Eva"], 2),
    ([], 0),
]:
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        actual = function(list(names))
    assert actual == expected, (
        f"Expected unique_visitors({names!r}) to return {expected!r}. Actual: {actual!r}."
    )
    assert not captured.getvalue(), "Expected: return the number. Actual: unique_visitors prints."

lines = [line.strip() for line in output.getvalue().splitlines()]
assert lines[:1] == ["3"], f"Expected the first output line: '3'. Actual: {lines[:1]!r}."

advanced = namespace.get("first_visits")
if advanced is None:
    print("\nAdvanced task: first_visits is not written yet.")
else:
    assert callable(advanced), "Expected: first_visits(names) to be a function."
    for names, expected in [
        (["Ana", "Ben", "Ana", "Cleo", "Ben"], ["Ana", "Ben", "Cleo"]),
        (["Cleo", "Ana", "Cleo"], ["Cleo", "Ana"]),
        ([], []),
    ]:
        actual = advanced(list(names))
        assert actual == expected, (
            f"Expected first_visits({names!r}) to return {expected!r}. Actual: {actual!r}."
        )
    print("\nAdvanced task: first_visits passed every test.")
print("__checks_complete__")
'''


def check():
    expected = "Expected example output:\n3"
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
    print("Correct! unique_visitors and your output passed every test.")


if __name__ == "__main__":
    check()
