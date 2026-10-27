from pathlib import Path
import os
import subprocess
import sys


EXPECTED = ("Bruno", "Dina")
TIME_LIMIT = 3


def _fail(expected, actual, reason=""):
    print("Not quite yet.")
    if reason:
        print(reason)
    print("Expected output:\n" + "\n".join(expected))
    print("Your output:\n" + ("\n".join(actual) or "(nothing)"))
    raise SystemExit(1)


def _lines(text):
    if isinstance(text, bytes):
        text = text.decode("utf-8", errors="replace")
    return [line.strip() for line in (text or "").splitlines() if line.strip()]


def check():
    exercise = Path(__file__).with_name("exercise.py")
    try:
        result = subprocess.run(
            [sys.executable, str(exercise)],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            stdin=subprocess.DEVNULL,
            env=dict(os.environ, PYTHONIOENCODING="utf-8"),
            timeout=TIME_LIMIT,
        )
    except subprocess.TimeoutExpired as error:
        _fail(EXPECTED, _lines(error.stdout)[:20] + ["..."],
              f"Your program was still running after {TIME_LIMIT} seconds.")

    actual = _lines(result.stdout)
    if result.returncode != 0:
        errors = result.stderr.strip().splitlines() or ["unknown error"]
        _fail(EXPECTED, actual, "Your program stopped with an error: " + errors[-1])
    if actual != list(EXPECTED):
        _fail(EXPECTED, actual)

    print("Correct! Your output matches the expected result.")


if __name__ == "__main__":
    check()
