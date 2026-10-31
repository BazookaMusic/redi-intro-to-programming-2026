from pathlib import Path
import subprocess
import sys


TESTS = r'''
import ast
import contextlib
import io
import math
from pathlib import Path
import runpy

output = io.StringIO()
with contextlib.redirect_stdout(output):
    namespace = runpy.run_path("exercise.py")
print(output.getvalue(), end="")
function = namespace.get("average")
assert callable(function), "Expected: average(scores). Actual: function is missing."
for scores, expected in [([12, 18, 24], 18), ([5], 5), ([1, 2], 1.5), ([0, 0], 0)]:
    original = scores[:]
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        actual = function(scores)
    assert isinstance(actual, (int, float)) and math.isclose(actual, expected), (
        f"Expected returned average: {expected!r}. Actual: {actual!r}."
    )
    assert scores == original, f"Expected input list unchanged: {original!r}. Actual: {scores!r}."
    assert not captured.getvalue(), "Expected: return the average. Actual: the function prints."
actual = output.getvalue().split()
assert actual == ["18.0", "Pass"], f"Expected output: ['18.0', 'Pass']. Actual: {actual!r}."
tree = ast.parse(Path("exercise.py").read_text(encoding="utf-8"))
definition = next(node for node in ast.walk(tree)
                  if isinstance(node, ast.FunctionDef) and node.name == "average")
assert any(isinstance(node, (ast.For, ast.While)) for node in ast.walk(definition)), (
    "Expected: a loop inside average. Actual: no loop found."
)
'''


def check():
    try:
        result = subprocess.run(
            [sys.executable, "-c", TESTS], cwd=Path(__file__).resolve().parent,
            capture_output=True, text=True, encoding="utf-8", timeout=3,
        )
    except subprocess.TimeoutExpired:
        print("Not quite yet.\nExpected output:\n18.0\nPass")
        print("Actual: the program was still running after 3 seconds.")
        raise SystemExit(1)
    if result.returncode:
        print("Not quite yet.\nExpected output:\n18.0\nPass")
        print("Your output:\n" + (result.stdout or "(nothing)"))
        print(result.stderr.strip().splitlines()[-1])
        raise SystemExit(1)
    print("Correct! Averages and the output passed every test.")


if __name__ == "__main__":
    check()
