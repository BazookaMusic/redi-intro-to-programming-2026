from pathlib import Path
import subprocess
import sys


TESTS = r'''
import contextlib
import io
import math
import runpy

output = io.StringIO()
with contextlib.redirect_stdout(output):
    namespace = runpy.run_path("exercise.py")
print(output.getvalue(), end="")
function = namespace.get("circle_area")
assert callable(function), "Expected: circle_area(radius). Actual: function is missing."
for radius in (0, 1, 2, 2.5, 10):
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        actual = function(radius)
    expected = math.pi * radius * radius
    assert isinstance(actual, (int, float)) and math.isclose(
        actual, expected, rel_tol=1e-12, abs_tol=1e-12
    ), f"Expected unrounded area: {expected!r}. Actual: {actual!r}."
    assert not captured.getvalue(), "Expected: return the area. Actual: the function prints."
actual = output.getvalue().split()
assert actual == ["12.57"], f"Expected output: ['12.57']. Actual: {actual!r}."
'''


def check():
    try:
        result = subprocess.run(
            [sys.executable, "-c", TESTS], cwd=Path(__file__).resolve().parent,
            capture_output=True, text=True, encoding="utf-8", timeout=3,
        )
    except subprocess.TimeoutExpired:
        print("Not quite yet.\nExpected output:\n12.57")
        print("Actual: the program was still running after 3 seconds.")
        raise SystemExit(1)
    if result.returncode:
        print("Not quite yet.\nExpected output:\n12.57")
        print("Your output:\n" + (result.stdout or "(nothing)"))
        print(result.stderr.strip().splitlines()[-1])
        raise SystemExit(1)
    print("Correct! The area function and output passed every test.")


if __name__ == "__main__":
    check()
