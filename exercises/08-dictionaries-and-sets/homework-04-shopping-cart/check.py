from pathlib import Path
import subprocess
import sys


TESTS = r'''
import ast
from pathlib import Path

path = Path("exercise.py")
tree = ast.parse(path.read_text(encoding="utf-8"))
definitions = ast.Module(body=[
    node for node in tree.body
    if isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.Assign))
], type_ignores=[])
namespace = {}
exec(compile(definitions, str(path), "exec"), namespace)

prices = namespace.get("PRICES")
assert prices == {"apple": 1, "bread": 2, "cheese": 5, "milk": 1}, (
    f"Expected: keep the supplied PRICES. Actual: {prices!r}."
)

add_to_cart = namespace.get("add_to_cart")
assert callable(add_to_cart), "Expected: add_to_cart(cart, item, quantity). Actual: function is missing."
cart = {}
for item, quantity, expected, after in [
    ("apple", 3, True, {"apple": 3}),
    ("apple", 2, True, {"apple": 5}),
    ("pizza", 1, False, {"apple": 5}),
    ("cheese", 1, True, {"apple": 5, "cheese": 1}),
]:
    before = dict(cart)
    actual = add_to_cart(cart, item, quantity)
    assert actual is expected, (
        f"Expected add_to_cart({before!r}, {item!r}, {quantity}) to return {expected!r}. Actual: {actual!r}."
    )
    assert cart == after, (
        f"Expected the cart after add_to_cart({before!r}, {item!r}, {quantity}): {after!r}. Actual: {cart!r}."
    )

cart_total = namespace.get("cart_total")
assert callable(cart_total), "Expected: cart_total(cart). Actual: function is missing."
for test_cart, expected in [
    ({"apple": 5, "cheese": 1}, 10),
    ({"bread": 2, "milk": 3}, 7),
    ({}, 0),
]:
    actual = cart_total(dict(test_cart))
    assert actual == expected, (
        f"Expected cart_total({test_cart!r}) to return {expected!r}. Actual: {actual!r}."
    )

advanced = namespace.get("sale_total")
if advanced is None:
    advanced_message = "Advanced task: sale_total is not written yet."
else:
    assert callable(advanced), "Expected: sale_total(cart, sale_items) to be a function."
    for test_cart, sale_items, expected in [
        ({"apple": 5, "cheese": 1}, {"cheese"}, 7.5),
        ({"apple": 5, "cheese": 1}, set(), 10),
        ({"bread": 2, "milk": 3}, {"bread", "milk"}, 3.5),
        ({}, {"apple"}, 0),
    ]:
        actual = advanced(dict(test_cart), set(sale_items))
        assert actual == expected, (
            f"Expected sale_total({test_cart!r}, {sale_items!r}) to return {expected!r}. Actual: {actual!r}."
        )
    advanced_message = "Advanced task: sale_total passed every test."

print(advanced_message)
print("__checks_complete__")
'''

SHOP_INPUT = "apple\n3\npizza\n1\ncheese\n1\ndone\n"
SHOP_OUTPUT = """We sell:
- apple: 1 euros
- bread: 2 euros
- cheese: 5 euros
- milk: 1 euros
Item to buy (or done): How many? Added to the cart.
Item to buy (or done): How many? Sorry, we do not sell pizza
Item to buy (or done): How many? Added to the cart.
Item to buy (or done): Receipt:
apple x3 = 3 euros
cheese x1 = 5 euros
Total: 8 euros"""


def run(arguments, stdin=""):
    return subprocess.run(
        [sys.executable, *arguments], cwd=Path(__file__).resolve().parent, input=stdin,
        capture_output=True, text=True, encoding="utf-8", timeout=3,
    )


def fail(message):
    print("Not quite yet.")
    print(message)
    raise SystemExit(1)


def check():
    try:
        result = run(["-c", TESTS])
    except subprocess.TimeoutExpired:
        fail("Actual: the tests were still running after 3 seconds.")
    lines = result.stdout.strip().splitlines()
    if result.returncode or len(lines) < 2 or lines[-1] != "__checks_complete__":
        errors = result.stderr.strip().splitlines()
        if errors:
            fail(errors[-1])
        fail(
            "Expected: the functions to finish their checks.\n"
            f"Actual: the checks stopped early (exit status {result.returncode}).\n"
            "Your output:\n" + (result.stdout or "(nothing)")
        )
    advanced_message = lines[-2]

    try:
        result = run(["exercise.py"], SHOP_INPUT)
    except subprocess.TimeoutExpired:
        fail("Actual: the shop was still running after 3 seconds.")
    actual = result.stdout.strip()
    if result.returncode or actual != SHOP_OUTPUT:
        message = (
            "Buying 3 apples, 1 pizza and 1 cheese should print:\n"
            + SHOP_OUTPUT + "\n\nYour output:\n" + (actual or "(nothing)")
        )
        if result.returncode:
            errors = result.stderr.strip().splitlines()
            message += "\n" + (
                errors[-1] if errors else f"Actual: the shop exited with status {result.returncode}."
            )
        fail(message)

    print(advanced_message)
    print("Correct! add_to_cart, cart_total and the shop passed every test.")


if __name__ == "__main__":
    check()
