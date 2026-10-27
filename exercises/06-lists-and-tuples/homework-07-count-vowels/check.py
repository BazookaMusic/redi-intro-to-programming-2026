from pathlib import Path
import os
import subprocess
import sys


CASES = (
    ("programming", ("a: 1", "e: 0", "i: 1", "o: 1", "u: 0")),
    ("banana", ("a: 3", "e: 0", "i: 0", "o: 0", "u: 0")),
    ("education", ("a: 1", "e: 1", "i: 1", "o: 1", "u: 1")),
    ("rhythm", ("a: 0", "e: 0", "i: 0", "o: 0", "u: 0")),
)
TIME_LIMIT = 3


def _fail(number, word, expected, actual, reason=""):
    print("Not quite yet.")
    if reason:
        print(reason)
    print(f"Test {number} (input: {word!r})")
    print("Expected output:\n" + "\n".join(expected))
    print("Your output:\n" + ("\n".join(actual) or "(nothing)"))
    raise SystemExit(1)


def _last_five_lines(text):
    if isinstance(text, bytes):
        text = text.decode("utf-8", errors="replace")
    lines = (text or "").splitlines()
    if len(lines) < 5:
        return [line.rstrip() for line in lines]
    lines = [line.rstrip() for line in lines[-5:]]
    first_vowel_line = lines[0].find("a: ")
    if first_vowel_line >= 0:
        lines[0] = lines[0][first_vowel_line:]
    return lines


def check():
    exercise = Path(__file__).with_name("exercise.py")
    for number, (word, expected) in enumerate(CASES, start=1):
        try:
            result = subprocess.run(
                [sys.executable, str(exercise)],
                input=word + "\n",
                capture_output=True,
                encoding="utf-8",
                errors="replace",
                env=dict(os.environ, PYTHONIOENCODING="utf-8"),
                timeout=TIME_LIMIT,
            )
        except subprocess.TimeoutExpired as error:
            _fail(number, word, expected, _last_five_lines(error.stdout) + ["..."],
                  f"Your program was still running after {TIME_LIMIT} seconds.")

        actual = _last_five_lines(result.stdout)
        if result.returncode != 0:
            errors = result.stderr.strip().splitlines() or ["unknown error"]
            _fail(number, word, expected, actual,
                  "Your program stopped with an error: " + errors[-1])
        if actual != list(expected):
            _fail(number, word, expected, actual)

    print("Correct! Your output matches every test.")


if __name__ == "__main__":
    check()
