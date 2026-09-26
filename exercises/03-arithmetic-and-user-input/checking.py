from contextlib import redirect_stdout
from io import StringIO
from math import isclose
from unittest.mock import patch
import runpy


class CheckFailed(AssertionError):
    pass


def _matches(expected, actual):
    expected_label, separator, expected_number = expected.partition(":")
    if separator:
        actual_label, actual_separator, actual_number = actual.partition(":")
        if not actual_separator or actual_label.strip().casefold() != expected_label.strip().casefold():
            return False
    else:
        expected_number = expected
        actual_number = actual

    try:
        return isclose(float(actual_number), float(expected_number), rel_tol=0, abs_tol=1e-9)
    except ValueError:
        return False


def _details(number, answers, expected, actual):
    supplied = ", ".join(answers) if answers else "(none)"
    expected_text = "\n".join(expected)
    actual_text = "\n".join(actual) or "(nothing)"
    return (
        f"Test {number} (input: {supplied})\n"
        f"Expected output:\n{expected_text}\n"
        f"Your output:\n{actual_text}"
    )


def check_output(exercise_file, cases):
    for number, (answers, expected) in enumerate(cases, start=1):
        output = StringIO()
        try:
            with patch("builtins.input", side_effect=answers) as requested, redirect_stdout(output):
                runpy.run_path(str(exercise_file), run_name="__main__")
        except StopIteration as error:
            actual = [line.strip() for line in output.getvalue().splitlines() if line.strip()]
            raise CheckFailed(
                f"Your program asked for more than {len(answers)} input(s).\n"
                + _details(number, answers, expected, actual)
            ) from error

        actual = [line.strip() for line in output.getvalue().splitlines() if line.strip()]
        if requested.call_count != len(answers):
            raise CheckFailed(
                f"Your program asked for {requested.call_count} input(s), "
                f"but this task needs {len(answers)}.\n"
                + _details(number, answers, expected, actual)
            )
        if len(actual) != len(expected) or any(
            not _matches(want, got) for want, got in zip(expected, actual)
        ):
            raise CheckFailed(_details(number, answers, expected, actual))

    print("Correct! Your output matches every test.")


def run_check(exercise_file, cases):
    try:
        check_output(exercise_file, cases)
    except CheckFailed as error:
        print(f"Not quite yet.\n{error}")
        raise SystemExit(1) from None
