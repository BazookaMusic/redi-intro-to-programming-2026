from pathlib import Path
import subprocess
import sys


TESTS = r'''
import contextlib
import io
import runpy

output = io.StringIO()
with contextlib.redirect_stdout(output):
    namespace = runpy.run_path("exercise.py")
print(output.getvalue(), end="")
function = namespace.get("draw_face")
assert callable(function), "Expected: draw_face(eyes, mouth). Actual: function is missing."

for eyes, mouth in [("o", "-"), ("^", "v"), ("@", "u")]:
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        result = function(eyes=eyes, mouth=mouth)
    expected = f"{eyes} {eyes}\n {mouth}\n"
    actual = captured.getvalue()
    assert actual == expected, f"Expected function output: {expected!r}. Actual: {actual!r}."
    assert result is None, f"Expected: display the face, no returned value. Actual: {result!r}."

lines = output.getvalue().splitlines()
assert len(lines) == 4, f"Expected: two two-line faces. Actual: {len(lines)} lines."
for index in (0, 2):
    eyes = lines[index].split(" ")
    assert len(eyes) == 2 and eyes[0] and eyes[0] == eyes[1], (
        f"Expected: two matching eyes separated by a space. Actual: {lines[index]!r}."
    )
    assert lines[index + 1].startswith(" ") and lines[index + 1].strip(), (
        f"Expected: a mouth preceded by a space. Actual: {lines[index + 1]!r}."
    )
assert lines[:2] != lines[2:], "Expected: two different faces. Actual: both faces are the same."
'''


def check():
    try:
        result = subprocess.run(
            [sys.executable, "-c", TESTS], cwd=Path(__file__).resolve().parent,
            capture_output=True, text=True, encoding="utf-8", timeout=3,
        )
    except subprocess.TimeoutExpired:
        print("Not quite yet.\nExpected: two faces and a program that finishes.")
        print("Actual: the program was still running after 3 seconds.")
        raise SystemExit(1)
    if result.returncode:
        print("Not quite yet.\nExpected example output:\no o\n -\n^ ^\n v")
        print("Your output:\n" + (result.stdout or "(nothing)"))
        print(result.stderr.strip().splitlines()[-1])
        raise SystemExit(1)
    print("Correct! Both faces and the function passed every test.")


if __name__ == "__main__":
    check()
