from pathlib import Path
import io
import os
import subprocess
import sys
import tokenize


EXPECTED = ("1. pizza", "2. sushi", "3. pasta", "4. tacos", "5. soup")
LOOP_WORDS = ("for", "while")
LOOP_HINT = "Use a loop to go through the foods list."
TIME_LIMIT = 3


def _fail(expected, actual, reason=""):
    print("Not quite yet.")
    if reason:
        print(reason)
    print("Expected output:\n" + "\n".join(expected))
    print("Your output:\n" + ("\n".join(actual) or "(nothing)"))
    raise SystemExit(1)


def _uses_loop(source):
    try:
        words = {
            token.string
            for token in tokenize.generate_tokens(io.StringIO(source).readline)
            if token.type == tokenize.NAME
        }
    except (tokenize.TokenError, SyntaxError):
        return True
    return any(word in words for word in LOOP_WORDS)


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
        output = error.stdout or ""
        if isinstance(output, bytes):
            output = output.decode("utf-8", errors="replace")
        _fail(EXPECTED, output.splitlines()[:20] + ["..."],
              f"Your program was still running after {TIME_LIMIT} seconds. Does your loop ever stop?")

    actual = result.stdout.splitlines()
    if result.returncode != 0:
        errors = result.stderr.strip().splitlines() or ["unknown error"]
        _fail(EXPECTED, actual, "Your program stopped with an error: " + errors[-1])

    valid_lines = len(actual) == 5
    if valid_lines:
        for position, line in enumerate(actual, start=1):
            prefix = f"{position}. "
            if not line.startswith(prefix) or not line[len(prefix):].strip():
                valid_lines = False
                break
    if not valid_lines:
        _fail(
            EXPECTED,
            actual,
            "Print exactly five lines. Number them from 1 to 5, followed by a period, a space, and a non-empty food name.",
        )

    if not _uses_loop(exercise.read_text(encoding="utf-8")):
        _fail(EXPECTED, actual, LOOP_HINT)

    print("Correct! Your output has five numbered foods.")


if __name__ == "__main__":
    check()
