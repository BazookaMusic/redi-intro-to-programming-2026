from pathlib import Path
import subprocess
import sys


TESTS = r'''
import ast
import contextlib
import io
import runpy

output = io.StringIO()
try:
    with contextlib.redirect_stdout(output):
        namespace = runpy.run_path("exercise.py")
finally:
    print(output.getvalue(), end="")

function = namespace.get("count_words")
assert callable(function), "Expected: count_words(sentence). Actual: function is missing."
for sentence, expected in [
    ("the cat and the dog", {"the": 2, "cat": 1, "and": 1, "dog": 1}),
    ("the cat and the dog and the bird", {"the": 3, "cat": 1, "and": 2, "dog": 1, "bird": 1}),
    ("hello", {"hello": 1}),
    ("", {}),
]:
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        actual = function(sentence)
    assert actual == expected, (
        f"Expected count_words({sentence!r}) to return {expected!r}. Actual: {actual!r}."
    )
    assert not captured.getvalue(), "Expected: return the dictionary. Actual: count_words prints."

lines = output.getvalue().splitlines()
expected_output = {"the": 3, "cat": 1, "and": 2, "dog": 1, "bird": 1}
try:
    printed = ast.literal_eval(lines[0].strip())
except (IndexError, SyntaxError, ValueError):
    printed = None
assert isinstance(printed, dict) and printed == expected_output, (
    f"Expected the first output line to be {expected_output!r}. Actual: {lines[:1]!r}."
)

advanced = namespace.get("repeated_words")
if advanced is None:
    print("\nAdvanced task: repeated_words is not written yet.")
else:
    assert callable(advanced), "Expected: repeated_words(sentence) to be a function."
    for sentence, expected in [
        ("the cat and the dog and the bird", {"the", "and"}),
        ("one two three", set()),
        ("go go go", {"go"}),
    ]:
        actual = advanced(sentence)
        assert actual == expected and isinstance(actual, set), (
            f"Expected repeated_words({sentence!r}) to return the set {expected!r}. Actual: {actual!r}."
        )
    print("\nAdvanced task: repeated_words passed every test.")
print("__checks_complete__")
'''


def check():
    expected = "Expected example output:\n{'the': 3, 'cat': 1, 'and': 2, 'dog': 1, 'bird': 1}"
    try:
        result = subprocess.run(
            [sys.executable, "-c", TESTS], cwd=Path(__file__).resolve().parent,
            capture_output=True, text=True, encoding="utf-8", timeout=3,
        )
    except subprocess.TimeoutExpired:
        print("Not quite yet.\n" + expected)
        print("Actual: the program was still running after 3 seconds.")
        raise SystemExit(1)
    lines = result.stdout.strip().splitlines()
    if result.returncode or len(lines) < 2 or lines[-1] != "__checks_complete__":
        print("Not quite yet.\n" + expected)
        print("Your output:\n" + (result.stdout or "(nothing)"))
        errors = result.stderr.strip().splitlines()
        if errors:
            print(errors[-1])
        else:
            print(f"Actual: exercise.py stopped the checks early (exit status {result.returncode}).")
        raise SystemExit(1)
    print(lines[-2])
    print("Correct! count_words and your output passed every test.")


if __name__ == "__main__":
    check()
