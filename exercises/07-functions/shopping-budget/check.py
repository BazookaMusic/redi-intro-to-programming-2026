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

function = namespace.get("total_price")
assert callable(function), "Expected: total_price(unit_price, quantity). Actual: function is missing."
for unit_price, quantity, expected in [(3, 4, 12), (3, 8, 24), (2, 0, 0), (5, 1, 5)]:
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        actual = function(unit_price, quantity)
    assert actual == expected, (
        f"Expected total_price({unit_price}, {quantity}) to return {expected!r}. Actual: {actual!r}."
    )
    assert not captured.getvalue(), "Expected: return the total. Actual: total_price prints."

lines = output.getvalue().split()
assert lines[:2] == ["12", "24"], f"Expected the first output lines: ['12', '24']. Actual: {lines[:2]!r}."

advanced = namespace.get("can_afford")
if advanced is None:
    print("\nAdvanced task: can_afford is not written yet.")
else:
    assert callable(advanced), "Expected: can_afford(shopping_basket, wallet_amount) to be a function."
    for basket, wallet, expected in [
        ([(3, 4), (2, 3)], 20, True),
        ([(3, 4), (2, 3)], 10, False),
        ([(3, 4), (2, 3)], 18, True),
        ([(5, 2)], 9, False),
        ([], 0, True),
    ]:
        actual = advanced(basket, wallet)
        assert actual == expected, (
            f"Expected can_afford({basket!r}, {wallet}) to return {expected!r}. Actual: {actual!r}."
        )
    print("\nAdvanced task: can_afford passed every test.")
'''


def check():
    expected = "Expected example output:\n12\n24\nTrue\nFalse"
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
    print("Correct! total_price and its output passed every test.")


if __name__ == "__main__":
    check()
