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

restock = namespace.get("restock")
assert callable(restock), "Expected: restock(stock, item, amount). Actual: function is missing."
for stock, item, amount, expected in [
    ({"apples": 5}, "apples", 3, {"apples": 8}),
    ({"apples": 5}, "eggs", 6, {"apples": 5, "eggs": 6}),
    ({}, "milk", 2, {"milk": 2}),
]:
    before = dict(stock)
    actual = restock(stock, item, amount)
    assert stock == expected, (
        f"Expected restock({before!r}, {item!r}, {amount}) to change stock to {expected!r}. "
        f"Actual: {stock!r}."
    )
    assert actual is None, f"Expected: restock returns nothing. Actual: it returns {actual!r}."

sell = namespace.get("sell")
assert callable(sell), "Expected: sell(stock, item). Actual: function is missing."
stock = {"apples": 5, "bread": 1, "milk": 0}
for item, expected, after in [
    ("bread", True, {"apples": 5, "bread": 0, "milk": 0}),
    ("bread", False, {"apples": 5, "bread": 0, "milk": 0}),
    ("milk", False, {"apples": 5, "bread": 0, "milk": 0}),
    ("apples", True, {"apples": 4, "bread": 0, "milk": 0}),
    ("cheese", False, {"apples": 4, "bread": 0, "milk": 0}),
]:
    before = dict(stock)
    actual = sell(stock, item)
    assert actual is expected, (
        f"Expected sell({before!r}, {item!r}) to return {expected!r}. Actual: {actual!r}."
    )
    assert stock == after, (
        f"Expected stock after sell({before!r}, {item!r}): {after!r}. Actual: {stock!r}."
    )

advanced = namespace.get("out_of_stock")
if advanced is None:
    print("\nAdvanced task: out_of_stock is not written yet.")
else:
    assert callable(advanced), "Expected: out_of_stock(stock) to be a function."
    for stock, expected in [
        ({"apples": 5, "bread": 0, "milk": 0, "eggs": 6}, ["bread", "milk"]),
        ({"apples": 5}, []),
        ({"tea": 0}, ["tea"]),
    ]:
        actual = advanced(dict(stock))
        assert isinstance(actual, list) and len(actual) == len(expected) and all(
            item in actual for item in expected
        ), (
            f"Expected out_of_stock({stock!r}) to return the list {expected!r} in any order. "
            f"Actual: {actual!r}."
        )
    print("\nAdvanced task: out_of_stock passed every test.")
print("__checks_complete__")
'''


def check():
    expected = (
        "Expected example results:\n"
        "sell(stock, 'bread') returns True, then False\n"
        "after restock(stock, 'eggs', 6): {'apples': 5, 'bread': 0, 'milk': 0, 'eggs': 6}"
    )
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
    print("Correct! restock and sell passed every test.")


if __name__ == "__main__":
    check()
