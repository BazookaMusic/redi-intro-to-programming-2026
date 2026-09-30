from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import runpy


SAMPLE = [
    "Sara", "25", "Berlin", "Arabic", "True",
    "<class 'str'>", "<class 'int'>", "<class 'str'>",
    "<class 'str'>", "<class 'bool'>", "26", "4",
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

    required = {"name": str, "age": int, "city": str, "language": str, "is_student": bool}
    for name, expected_type in required.items():
        if type(variables.get(name)) is not expected_type:
            fail(SAMPLE, actual, f"Create {name} as a {expected_type.__name__} variable.")

    if len(actual) != 12:
        fail(SAMPLE, actual, "Print five values, five types, the new age, and the name length.")
    try:
        starting_age = int(actual[1])
    except ValueError:
        fail(SAMPLE, actual, "Print your starting age as a whole number on line 2.")

    expected = [
        variables["name"], str(starting_age), variables["city"], variables["language"],
        str(variables["is_student"]), str(type(variables["name"])),
        str(type(variables["age"])), str(type(variables["city"])),
        str(type(variables["language"])), str(type(variables["is_student"])),
        str(starting_age + 1), str(len(variables["name"])),
    ]
    if variables["age"] != starting_age + 1 or actual != expected:
        fail(expected, actual, "Print your values and types, then increase age by 1.")
    print("Correct! Your About Me program matches your variables.")


if __name__ == "__main__":
    check()
