from contextlib import redirect_stdout
from io import StringIO
from math import isclose
from pathlib import Path
from unittest.mock import patch
import runpy


CASES = (
    (
        ("10", "3"),
        (
            "Sum: 13",
            "Difference: 7",
            "Product: 30",
            "Quotient: 3.33",
            "Remainder: 1",
            "Power: 1000",
        ),
    ),
    (
        ("2.5", "2"),
        (
            "Sum: 4.5",
            "Difference: 0.5",
            "Product: 5",
            "Quotient: 1.25",
            "Remainder: 0.5",
            "Power: 6.25",
        ),
    ),
)

def _matches(expected, actual):
    expected_label, _, expected_value = expected.partition(":")
    actual_label, separator, actual_value = actual.partition(":")
    if not separator or actual_label.strip().casefold() != expected_label.strip().casefold():
        return False
    try:
        return isclose(float(actual_value), float(expected_value), rel_tol=0, abs_tol=1e-9)
    except ValueError:
        return False


def _fail(number, answers, expected, actual, reason=""):
    print("Not quite yet.")
    if reason:
        print(reason)
    print(f"Test {number} (input: {', '.join(answers) or '(none)'})")
    print("Expected output:\n" + "\n".join(expected))
    print("Your output:\n" + ("\n".join(actual) or "(nothing)"))
    raise SystemExit(1)


def check():
    for number, (answers, expected) in enumerate(CASES, start=1):
        output = StringIO()
        try:
            with patch("builtins.input", side_effect=answers) as requested, redirect_stdout(output):
                runpy.run_path(str(Path(__file__).with_name("exercise.py")), run_name="__main__")
        except StopIteration:
            actual = [line.strip() for line in output.getvalue().splitlines() if line.strip()]
            _fail(number, answers, expected, actual,
                  f"Your program asked for more than {len(answers)} input(s).")

        actual = [line.strip() for line in output.getvalue().splitlines() if line.strip()]
        if requested.call_count != len(answers):
            _fail(number, answers, expected, actual,
                  f"Your program asked for {requested.call_count} input(s), "
                  f"but this task needs {len(answers)}.")
        if len(actual) != len(expected) or any(
            not _matches(want, got) for want, got in zip(expected, actual)
        ):
            _fail(number, answers, expected, actual)

    print("Correct! Your output matches every test.")


if __name__ == "__main__":
    check()
