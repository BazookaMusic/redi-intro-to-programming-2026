from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import runpy


SAMPLE = [
    "<class 'str'>", "<class 'int'>", "<class 'str'>",
    "<class 'str'>", "<class 'str'>", "<class 'bool'>",
]


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

    required = {
        "name": str, "age": int, "city": str, "favourite_food": str,
        "favourite_colour": str, "is_working": bool,
    }
    for name, expected_type in required.items():
        if type(variables.get(name)) is not expected_type:
            fail(SAMPLE, actual, f"Create {name} as a {expected_type.__name__} variable.")

    expected = [str(type(variables[name])) for name in required]
    if actual != expected:
        fail(expected, actual, "Print the type of each variable on its own line, in order.")
    print("Correct! You printed all six types.")


if __name__ == "__main__":
    check()
