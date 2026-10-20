from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch
import runpy


CASES = (
    (("0", "rain", "snow", "rainbow"), (
        "+2 points",
        "Hint: it's white and cold.",
        "+1 point",
        "+2 points",
        "You scored 5 out of 6.",
    )),
    (("0", "snow", "rainbow", "7"), (
        "+2 points",
        "+2 points",
        "+2 points",
        "You scored 6 out of 6.",
        "Bonus question unlocked!",
        "Bonus point! Final score: 7",
    )),
    (("0", " SNOW ", "Rainbow", "5"), (
        "+2 points",
        "+2 points",
        "+2 points",
        "You scored 6 out of 6.",
        "Bonus question unlocked!",
        "No bonus this time.",
    )),
    (("3", "0", "hail", "sleet", "sun", "rainbow"), (
        "Hint: it's between -1 and 1.",
        "+1 point",
        "Hint: it's white and cold.",
        "No points. The answer was snow.",
        "Hint: it has seven colours.",
        "+1 point",
        "You scored 2 out of 6.",
    )),
    (("5", "-2", "snow", "cloud", "rain"), (
        "Hint: it's between -1 and 1.",
        "No points. The answer was 0.",
        "+2 points",
        "Hint: it has seven colours.",
        "No points. The answer was rainbow.",
        "You scored 2 out of 6.",
    )),
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
