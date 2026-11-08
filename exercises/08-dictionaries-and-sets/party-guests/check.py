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

ana_friends = {"Ben", "Cleo", "Dan"}
max_friends = {"Cleo", "Dan", "Eva"}
for name, cases in [
    ("common_friends", [
        ((ana_friends, max_friends), {"Cleo", "Dan"}),
        (({"Ben"}, {"Eva"}), set()),
        (({1, 2, 3}, {2, 3, 4}), {2, 3}),
    ]),
    ("all_guests", [
        ((ana_friends, max_friends), {"Ben", "Cleo", "Dan", "Eva"}),
        (({"Ben"}, set()), {"Ben"}),
        (({1, 2, 3}, {2, 3, 4}), {1, 2, 3, 4}),
    ]),
]:
    function = namespace.get(name)
    assert callable(function), f"Expected: {name}(friends1, friends2). Actual: function is missing."
    for (first, second), expected in cases:
        first_copy, second_copy = set(first), set(second)
        actual = function(first_copy, second_copy)
        assert actual == expected, (
            f"Expected {name}({first!r}, {second!r}) to return {expected!r}. Actual: {actual!r}."
        )
        assert isinstance(actual, set), f"Expected: {name} returns a set. Actual: {type(actual).__name__}."
        assert first_copy == first and second_copy == second, (
            f"Expected: {name} does not change the sets it is given. "
            f"Actual: {first_copy!r} and {second_copy!r}."
        )

lines = [line.strip() for line in output.getvalue().splitlines()]
assert lines[:1] == ["4"], f"Expected the first output line: '4'. Actual: {lines[:1]!r}."

advanced = namespace.get("everyone")
if advanced is None:
    print("\nAdvanced task: everyone is not written yet.")
else:
    assert callable(advanced), "Expected: everyone(groups) to be a function."
    for groups, expected in [
        ([{"Ben"}, {"Ben", "Cleo"}, {"Eva"}], {"Ben", "Cleo", "Eva"}),
        ([ana_friends, max_friends], {"Ben", "Cleo", "Dan", "Eva"}),
        ([{"Ana"}], {"Ana"}),
        ([], set()),
    ]:
        actual = advanced([set(group) for group in groups])
        assert isinstance(actual, set) and actual == expected, (
            f"Expected everyone({groups!r}) to return the set {expected!r}. Actual: {actual!r}."
        )
    print("\nAdvanced task: everyone passed every test.")
print("__checks_complete__")
'''


def check():
    expected = "Expected example output:\n4"
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
    print("Correct! common_friends, all_guests and your output passed every test.")


if __name__ == "__main__":
    check()
