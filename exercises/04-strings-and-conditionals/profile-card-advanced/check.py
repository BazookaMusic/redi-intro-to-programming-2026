from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch
import runpy


CASES = (
    (("maria", "jensen", "1996", "berlin", "hiking", "I love maps and coffee."), (
        "MARIA JENSEN",
        "============",
        "👤 @maria_jensen",
        "🎂 30 years old",
        "📍 Berlin",
        "❤️ Hiking",
        "📝 I love maps and coffee.",
    )),
    ((" ali ", "KHAN ", "2001", " hamburg", "FOOTBALL", " Learning Python! "), (
        "ALI KHAN",
        "========",
        "👤 @ali_khan",
        "🎂 25 years old",
        "📍 Hamburg",
        "❤️ Football",
        "📝 Learning Python!",
    )),
    (("anna maria", "de souza", "1990", "lisbon", "surfing", "Sun and sea."), (
        "ANNA MARIA DE SOUZA",
        "===================",
        "👤 @anna_maria_de_souza",
        "🎂 36 years old",
        "📍 Lisbon",
        "❤️ Surfing",
        "📝 Sun and sea.",
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
