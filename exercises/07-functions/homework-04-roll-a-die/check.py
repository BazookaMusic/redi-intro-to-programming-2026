from pathlib import Path
import subprocess
import sys


TESTS = r'''
import contextlib
import inspect
import io
import random
import runpy
from unittest.mock import patch

calls = []
endpoint = ["low"]
def predictable_roll(low, high):
    assert low == 1 and high >= 1, f"Expected bounds: 1 through sides. Actual: {(low, high)!r}."
    calls.append((low, high))
    return low if endpoint[0] == "low" else high

output = io.StringIO()
with patch.object(random, "randint", predictable_roll):
    with contextlib.redirect_stdout(output):
        namespace = runpy.run_path("exercise.py")
    print(output.getvalue(), end="")
    function = namespace.get("roll_die")
    assert callable(function), "Expected: roll_die(sides=6). Actual: function is missing."
    assert inspect.getdoc(function), "Expected: a docstring. Actual: the docstring is missing."
    assert inspect.signature(function).parameters["sides"].default == 6, (
        "Expected default sides: 6. Actual: a different or missing default."
    )
    assert calls == [(1, 6), (1, 20)], (
        f"Expected example rolls: one six-sided and one twenty-sided die. Actual bounds: {calls!r}."
    )
    for sides in (1, 6, 20):
        for chosen_endpoint in ("low", "high"):
            endpoint[0] = chosen_endpoint
            calls.clear()
            captured = io.StringIO()
            with contextlib.redirect_stdout(captured):
                actual = function(sides=sides)
            expected = 1 if chosen_endpoint == "low" else sides
            assert calls == [(1, sides)], f"Expected bounds: {(1, sides)!r}. Actual: {calls!r}."
            assert actual == expected, f"Expected returned roll: {expected!r}. Actual: {actual!r}."
            assert not captured.getvalue(), "Expected: return the roll. Actual: the function prints."
lines = output.getvalue().split()
assert lines == ["1", "1"], f"Expected output with sample rolls: ['1', '1']. Actual: {lines!r}."
'''


def check():
    try:
        result = subprocess.run(
            [sys.executable, "-c", TESTS], cwd=Path(__file__).resolve().parent,
            capture_output=True, text=True, encoding="utf-8", timeout=3,
        )
    except subprocess.TimeoutExpired:
        print("Not quite yet.\nExpected: two rolls and a program that finishes.")
        print("Actual: the program was still running after 3 seconds.")
        raise SystemExit(1)
    if result.returncode:
        print("Not quite yet.\nExpected output with sample rolls:\n1\n1")
        print("Your output:\n" + (result.stdout or "(nothing)"))
        print(result.stderr.strip().splitlines()[-1])
        raise SystemExit(1)
    print("Correct! Defaults, docstring, output and both endpoints passed.")


if __name__ == "__main__":
    check()
