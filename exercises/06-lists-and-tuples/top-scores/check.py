from pathlib import Path
import ast
import io
import os
import subprocess
import sys
import tokenize


EXPECTED = ("Top 3: [91, 89, 76]", "Lowest: 11", "Scores above 50: 5")
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
    return [line.rstrip() for line in (text or "").splitlines()]


def _source_features(source):
    try:
        words = {
            token.string
            for token in tokenize.generate_tokens(io.StringIO(source).readline)
            if token.type == tokenize.NAME
        }
        tree = ast.parse(source)
    except (tokenize.TokenError, SyntaxError):
        return True, True, True
    uses_loop = "for" in words or "while" in words
    uses_sort = "sort" in words or "sorted" in words
    uses_slice = any(isinstance(node, ast.Slice) for node in ast.walk(tree))
    return uses_loop, uses_sort, uses_slice


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
        _fail(
            EXPECTED,
            _lines((error.stdout or "")[:2000])[:20] + ["..."],
            f"Your program was still running after {TIME_LIMIT} seconds. Does your loop ever stop?",
        )

    actual = _lines(result.stdout)
    if result.returncode != 0:
        _fail(EXPECTED, actual, "Your program stopped with an error. Check your code and try again.")
    if actual != list(EXPECTED):
        _fail(EXPECTED, actual)
    uses_loop, uses_sort, uses_slice = _source_features(exercise.read_text(encoding="utf-8"))
    if not uses_sort:
        _fail(EXPECTED, actual, "Sort the scores from highest to lowest.")
    if not uses_slice:
        _fail(EXPECTED, actual, "Use slicing to print the top 3 scores.")
    if not uses_loop:
        _fail(EXPECTED, actual, "Use a loop to count the scores above 50.")

    print("Correct! Your output matches every test.")


if __name__ == "__main__":
    check()
