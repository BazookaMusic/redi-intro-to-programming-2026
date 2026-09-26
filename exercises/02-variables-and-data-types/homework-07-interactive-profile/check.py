from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch
import runpy


CASES = (("Sara", "25"), ("Kai", "18"))


def fail(expected, actual, message):
    print(f"Not quite yet. {message}")
    print("Expected output (second line is optional):\n" + "\n".join(expected))
    print("Your output:\n" + ("\n".join(actual) or "(nothing)"))
    raise SystemExit(1)


def check():
    for name, age in CASES:
        output = StringIO()
        expected = [f"Hello, {name}! You are {age} years old.", f"Name length: {len(name)}"]
        try:
            with patch("builtins.input", side_effect=(name, age)) as requested, redirect_stdout(output):
                runpy.run_path(str(Path(__file__).with_name("exercise.py")), run_name="__main__")
        except StopIteration:
            actual = [line.strip() for line in output.getvalue().splitlines() if line.strip()]
            fail(expected, actual, "Ask for the name and age once each, in that order.")

        actual = [line.strip() for line in output.getvalue().splitlines() if line.strip()]
        if requested.call_count != 2:
            fail(expected, actual, f"Ask for two answers; your program asked {requested.call_count} times.")
        if actual not in (expected[:1], expected):
            fail(expected, actual, f"Use the name and age from the input ({name}, {age}).")
    print("Correct! Your profile works with different names and ages.")


if __name__ == "__main__":
    check()
