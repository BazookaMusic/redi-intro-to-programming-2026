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
function = namespace.get("ticket_price")
assert callable(function), "Expected: ticket_price(age). Actual: function is missing."
for age, expected in [(0, 5), (8, 5), (11, 5), (12, 10), (16, 10), (80, 10)]:
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        actual = function(age)
    assert actual == expected, f"Expected price for age {age}: {expected!r}. Actual: {actual!r}."
    assert not captured.getvalue(), "Expected: return the price. Actual: the function prints."
actual = output.getvalue().split()
assert actual == ["5", "10", "15"], f"Expected output: ['5', '10', '15']. Actual: {actual!r}."
'''


def check():
    try:
        result = subprocess.run(
            [sys.executable, "-c", TESTS], cwd=Path(__file__).resolve().parent,
            capture_output=True, text=True, encoding="utf-8", timeout=3,
        )
    except subprocess.TimeoutExpired:
        print("Not quite yet.\nExpected output:\n5\n10\n15")
        print("Actual: the program was still running after 3 seconds.")
        raise SystemExit(1)
    if result.returncode:
        print("Not quite yet.\nExpected output:\n5\n10\n15")
        print("Your output:\n" + (result.stdout or "(nothing)"))
        print(result.stderr.strip().splitlines()[-1])
        raise SystemExit(1)
    print("Correct! Ticket prices and the output passed every test.")


if __name__ == "__main__":
    check()
