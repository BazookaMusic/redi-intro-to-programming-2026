from pathlib import Path
import subprocess
import sys


TESTS = r'''
import ast
import contextlib
import io
from pathlib import Path
import runpy

output = io.StringIO()
with contextlib.redirect_stdout(output):
    namespace = runpy.run_path("exercise.py")
print(output.getvalue(), end="")
function = namespace.get("count_high_scores")
assert callable(function), "Expected: count_high_scores(scores, minimum). Actual: function is missing."
cases = [([12, 45, 7, 30], 20, 2), ([20, 19, 20], 20, 2),
         ([], 10, 0), ([1, 2], 10, 0), ([5, 6], 5, 2)]
for scores, minimum, expected in cases:
    original = scores[:]
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        actual = function(scores, minimum)
    assert actual == expected, f"Expected returned count: {expected!r}. Actual: {actual!r}."
    assert scores == original, f"Expected input list unchanged: {original!r}. Actual: {scores!r}."
    assert not captured.getvalue(), "Expected: return the count. Actual: the function prints."
actual = output.getvalue().split()
assert actual == ["2"], f"Expected output: ['2']. Actual: {actual!r}."
tree = ast.parse(Path("exercise.py").read_text(encoding="utf-8"))
definition = next(node for node in ast.walk(tree)
                  if isinstance(node, ast.FunctionDef) and node.name == "count_high_scores")
assert any(isinstance(node, (ast.For, ast.While)) for node in ast.walk(definition)), (
    "Expected: a loop inside count_high_scores. Actual: no loop found."
)
'''


def check():
    try:
        result = subprocess.run(
            [sys.executable, "-c", TESTS], cwd=Path(__file__).resolve().parent,
            capture_output=True, text=True, encoding="utf-8", timeout=3,
        )
    except subprocess.TimeoutExpired:
        print("Not quite yet.\nExpected output:\n2")
        print("Actual: the program was still running after 3 seconds.")
        raise SystemExit(1)
    if result.returncode:
        print("Not quite yet.\nExpected output:\n2")
        print("Your output:\n" + (result.stdout or "(nothing)"))
        print(result.stderr.strip().splitlines()[-1])
        raise SystemExit(1)
    print("Correct! High-score counts and the output passed every test.")


if __name__ == "__main__":
    check()
