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
function = namespace.get("slices_left")
assert callable(function), "Expected: slices_left(slices, eaten). Actual: function is missing."
for slices, eaten, expected in [(8, 3, 5), (5, 2, 3), (4, 4, 0), (7, 0, 7)]:
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        actual = function(slices, eaten)
    assert actual == expected, f"Expected returned value: {expected!r}. Actual: {actual!r}."
    assert not captured.getvalue(), "Expected: return the value. Actual: the function prints."
actual = output.getvalue().split()
assert actual == ["5", "3"], f"Expected output: ['5', '3']. Actual: {actual!r}."
tree = ast.parse(Path("exercise.py").read_text(encoding="utf-8"))
calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)
         and isinstance(node.func, ast.Name) and node.func.id == "slices_left"]
assert len(calls) >= 2, "Expected: call slices_left twice. Actual: fewer than two calls."
'''


def check():
    try:
        result = subprocess.run(
            [sys.executable, "-c", TESTS], cwd=Path(__file__).resolve().parent,
            capture_output=True, text=True, encoding="utf-8", timeout=3,
        )
    except subprocess.TimeoutExpired:
        print("Not quite yet.\nExpected output:\n5\n3")
        print("Actual: the program was still running after 3 seconds.")
        raise SystemExit(1)
    if result.returncode:
        print("Not quite yet.\nExpected output:\n5\n3")
        print("Your output:\n" + (result.stdout or "(nothing)"))
        print(result.stderr.strip().splitlines()[-1])
        raise SystemExit(1)
    print("Correct! The returned values and output passed every test.")


if __name__ == "__main__":
    check()
