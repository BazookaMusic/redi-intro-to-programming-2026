from pathlib import Path
import os
import subprocess
import sys


CASES = (
    ("milk\nbread\ndone\n", "Your list: ['milk', 'bread']"),
    ("done\n", "Your list: []"),
    ("apples\nrice\ntea\ndone\n", "Your list: ['apples', 'rice', 'tea']"),
)
TIME_LIMIT = 3


def _fail(number, answers, expected, actual, reason=""):
    print("Not quite yet.")
    if reason:
        print(reason)
    print(f"Test {number} (input: {answers!r})")
    print("Expected output:\n" + expected)
    print("Your output:\n" + (actual or "(nothing)"))
    raise SystemExit(1)


def _final_list_line(text):
    lines = (text or "").splitlines()
    if not lines:
        return ""
    line = lines[-1].rstrip()
    marker = line.rfind("Your list: ")
    return line[marker:] if marker >= 0 else line


def check():
    exercise = Path(__file__).with_name("exercise.py")
    for number, (answers, expected) in enumerate(CASES, start=1):
        try:
            result = subprocess.run(
                [sys.executable, str(exercise)],
                input=answers,
                capture_output=True,
                encoding="utf-8",
                errors="replace",
                env=dict(os.environ, PYTHONIOENCODING="utf-8"),
                timeout=TIME_LIMIT,
            )
        except subprocess.TimeoutExpired as error:
            output = (error.stdout or "")
            if isinstance(output, bytes):
                output = output.decode("utf-8", errors="replace")
            _fail(number, answers, expected, _final_list_line(output),
                  f"Your program was still running after {TIME_LIMIT} seconds. "
                  "Stop asking for items when the user types 'done'.")

        actual = _final_list_line(result.stdout)
        if result.returncode != 0:
            errors = result.stderr.strip().splitlines() or ["unknown error"]
            _fail(number, answers, expected, actual,
                  "Your program stopped with an error: " + errors[-1])
        if actual != expected:
            _fail(number, answers, expected, actual)

    print("Correct! Your output matches every test.")


if __name__ == "__main__":
    check()
