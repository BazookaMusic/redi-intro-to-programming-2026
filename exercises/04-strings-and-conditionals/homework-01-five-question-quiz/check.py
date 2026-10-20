from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch
import runpy


CASES = (
    (("0", "snow", "rain", "100", "wind"), ("You scored 4 out of 5.",)),
    (("0", "snow", "rainbow", "100", "wind"), ("You scored 5 out of 5.",)),
    (("5", "rain", "sun", "90", "storm"), ("You scored 0 out of 5.",)),
    (("0", "hail", "rainbow", "50", "wind"), ("You scored 3 out of 5.",)),
)


def _clean(line):
    # Some emojis carry an invisible style character. Ignore it when comparing.
    return line.replace("\ufe0f", "").strip()


def _lines(text):
    return [_clean(line) for line in text.splitlines() if line.strip()]


def _fail(number, answers, expected, actual, reason=""):
    print("Not quite yet.")
    if reason:
        print(reason)
    print(f"Test {number} (input: {', '.join(repr(answer) for answer in answers)})")
    print("Expected output:\n" + "\n".join(expected))
    print("Your output:\n" + ("\n".join(actual) or "(nothing)"))
    raise SystemExit(1)


def check():
    exercise = str(Path(__file__).with_name("exercise.py"))
    for number, (answers, expected) in enumerate(CASES, start=1):
        output = StringIO()
        error = ""
        with patch("builtins.input", side_effect=answers) as requested:
            try:
                with redirect_stdout(output):
                    runpy.run_path(exercise, run_name="__main__")
            except StopIteration:
                error = f"Your program asked for more than {len(answers)} input(s)."
            except Exception as problem:
                error = f"Your program stopped with an error: {type(problem).__name__}: {problem}"

        actual = _lines(output.getvalue())
        if error:
            _fail(number, answers, expected, actual, error)
        if actual != [_clean(line) for line in expected]:
            _fail(number, answers, expected, actual)
        if requested.call_count != len(answers):
            _fail(number, answers, expected, actual,
                  f"Your program asked for {requested.call_count} input(s), "
                  f"but this test gives {len(answers)}.")

    print("Correct! Your output matches every test.")


if __name__ == "__main__":
    check()
