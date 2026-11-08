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

menu = namespace.get("menu")
assert menu is not None, "Expected: menu = {'tea': 2, 'coffee': 3, 'cake': 4}. Actual: menu is missing."
assert menu == {"tea": 2, "coffee": 3, "cake": 4}, (
    "Expected: menu = {'tea': 2, 'coffee': 3, 'cake': 4}. "
    f"Actual: {menu!r}."
)

function = namespace.get("price_of")
assert callable(function), "Expected: price_of(menu, item). Actual: function is missing."
other_menu = {"juice": 5, "bagel": 1}
for test_menu, item, expected in [
    (menu, "coffee", 3), (menu, "tea", 2), (menu, "pizza", 0),
    (other_menu, "juice", 5), (other_menu, "tea", 0), ({}, "tea", 0),
]:
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        actual = function(dict(test_menu), item)
    assert actual == expected, (
        f"Expected price_of({test_menu!r}, {item!r}) to return {expected!r}. Actual: {actual!r}."
    )
    assert not captured.getvalue(), "Expected: return the price. Actual: price_of prints."

lines = [line.strip() for line in output.getvalue().splitlines()]
assert lines[:2] == ["3", "0"], f"Expected the first output lines: ['3', '0']. Actual: {lines[:2]!r}."

advanced = namespace.get("order_total")
if advanced is None:
    print("\nAdvanced task: order_total is not written yet.")
else:
    assert callable(advanced), "Expected: order_total(menu, items) to be a function."
    for test_menu, items, expected in [
        (menu, ["tea", "cake", "tea"], 8),
        (menu, ["coffee"], 3),
        (menu, ["pizza", "tea"], 2),
        (menu, [], 0),
        ({"juice": 5, "bagel": 1}, ["juice", "bagel", "tea"], 6),
    ]:
        actual = advanced(dict(test_menu), items)
        assert actual == expected, (
            f"Expected order_total({test_menu!r}, {items!r}) to return {expected!r}. Actual: {actual!r}."
        )
    print("\nAdvanced task: order_total passed every test.")
print("__checks_complete__")
'''


def check():
    expected = "Expected example output:\n3\n0"
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
    print("Correct! menu, price_of and your output passed every test.")


if __name__ == "__main__":
    check()
