from pathlib import Path
import subprocess
import sys


TESTS = r'''
import ast
import contextlib
import io
import runpy

output = io.StringIO()
try:
    with contextlib.redirect_stdout(output):
        namespace = runpy.run_path("exercise.py")
finally:
    print(output.getvalue(), end="")

examples = [
    {"name": "apple", "category": "fruit"},
    {"name": "bread", "category": "bakery"},
    {"name": "banana", "category": "fruit"},
    {"name": "cake", "category": "bakery"},
    {"name": "milk", "category": "dairy"},
]
expected_example = {
    "fruit": ["apple", "banana"],
    "bakery": ["bread", "cake"],
    "dairy": ["milk"],
}
assert "PRODUCTS" in namespace, "Expected: the supplied PRODUCTS list. Actual: it is missing."

function = namespace.get("products_by_category")
assert callable(function), (
    "Expected: products_by_category(products). Actual: function is missing."
)
tests = [
    (examples, expected_example),
    ([], {}),
    (
        [{"name": "pear", "category": "fruit"}, {"name": "pear", "category": "fruit"}],
        {"fruit": ["pear", "pear"]},
    ),
    (
        [
            {"name": "tea", "category": "drinks"},
            {"name": "milk", "category": "Dairy"},
            {"name": "coffee", "category": "drinks"},
            {"name": "water", "category": "drinks"},
        ],
        {"drinks": ["tea", "coffee", "water"], "Dairy": ["milk"]},
    ),
]
for products, expected in tests:
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        actual = function([product.copy() for product in products])
    assert isinstance(actual, dict) and actual == expected, (
        f"Expected products_by_category({products!r}) to return {expected!r}. Actual: {actual!r}."
    )

printed = []
for line in output.getvalue().splitlines():
    try:
        printed.append(ast.literal_eval(line.strip()))
    except (SyntaxError, ValueError):
        continue
assert expected_example in printed, (
    f"Expected the program to print {expected_example!r}. Actual: {output.getvalue()!r}."
)

advanced = namespace.get("categories_with_multiple")
if advanced is None:
    print("\nAdvanced task: categories_with_multiple is not written yet.")
else:
    assert callable(advanced), (
        "Expected: categories_with_multiple(products) to be a function. "
        f"Actual: {advanced!r}."
    )
    function_globals = advanced.__globals__
    original = function_globals.get("products_by_category")
    calls = []

    def tracked_products_by_category(products):
        calls.append(True)
        return function(products)

    function_globals["products_by_category"] = tracked_products_by_category
    try:
        for products, expected in [
            (examples, {"fruit", "bakery"}),
            ([], set()),
            ([{"name": "pear", "category": "fruit"}], set()),
            (
                [{"name": "pear", "category": "fruit"}, {"name": "pear", "category": "fruit"}],
                {"fruit"},
            ),
        ]:
            calls.clear()
            captured = io.StringIO()
            with contextlib.redirect_stdout(captured):
                actual = advanced([product.copy() for product in products])
            assert isinstance(actual, set) and actual == expected, (
                f"Expected categories_with_multiple({products!r}) to return the set {expected!r}. "
                f"Actual: {actual!r}."
            )
            assert calls, (
                "Expected: categories_with_multiple calls products_by_category. "
                "Actual: products_by_category was not called."
            )
    finally:
        function_globals["products_by_category"] = original
    print("\nAdvanced task: categories_with_multiple passed every test.")
print("__checks_complete__")
'''


def check():
    expected = (
        "Expected example output:\n"
        "{'fruit': ['apple', 'banana'], 'bakery': ['bread', 'cake'], 'dairy': ['milk']}"
    )
    try:
        result = subprocess.run(
            [sys.executable, "-c", TESTS], cwd=Path(__file__).resolve().parent,
            input="", capture_output=True, text=True, encoding="utf-8", timeout=3,
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
    print("Correct! products_by_category and your output passed every test.")


if __name__ == "__main__":
    check()
