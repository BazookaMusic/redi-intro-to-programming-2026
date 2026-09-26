from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import runpy


SAMPLE = ["Bread — quantity: 2 — price: 1.5"]


def fail(expected, actual, message):
    print(f"Not quite yet. {message}")
    print("Expected output:\n" + "\n".join(expected))
    print("Your output:\n" + ("\n".join(actual) or "(nothing)"))
    raise SystemExit(1)


def check():
    output = StringIO()
    with redirect_stdout(output):
        variables = runpy.run_path(str(Path(__file__).with_name("exercise.py")), run_name="__main__")
    actual = [line.strip() for line in output.getvalue().splitlines() if line.strip()]

    required = {"item": str, "price": float, "quantity": int}
    for name, expected_type in required.items():
        if type(variables.get(name)) is not expected_type:
            fail(SAMPLE, actual, f"Create {name} as a {expected_type.__name__} variable.")

    expected = [
        f"{variables['item']} — quantity: {variables['quantity']} — price: {variables['price']}"
    ]
    if actual != expected:
        fail(expected, actual, "Print the item, quantity, and price on one line.")
    print("Correct! Your receipt matches your variables.")


if __name__ == "__main__":
    check()
