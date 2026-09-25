"""Shared pytest setup for the exercise tests.

Students do not need to read or change this file. pytest loads it
automatically for every test in the exercises folder.
"""

import ast
import json
import subprocess
import sys

import pytest

TIME_LIMIT_SECONDS = 10

# Stop pytest from adding __pycache__ folders next to the students' files.
sys.dont_write_bytecode = True

# Runs a student's file in a separate Python, calls one function and prints
# the returned grid as JSON. Anything the student's code prints is hidden.
_CALL_FUNCTION = """
import contextlib, io, json, runpy, sys, traceback

path, name, arguments = sys.argv[1], sys.argv[2], json.loads(sys.argv[3])
try:
    with contextlib.redirect_stdout(io.StringIO()):
        function = runpy.run_path(path, run_name="student_program").get(name)
        result = function(*arguments) if callable(function) else None
except Exception as error:
    # Show only the lines from the student's file, not from this helper.
    frames = [frame for frame in traceback.extract_tb(error.__traceback__) if frame.filename == path]
    print("Traceback (most recent call last):", file=sys.stderr)
    print("".join(traceback.format_list(frames)) + "".join(traceback.format_exception_only(error)), end="", file=sys.stderr)
    sys.exit(1)

if not callable(function):
    outcome = {"problem": "missing"}
elif result is None:
    outcome = {"problem": "none"}
elif isinstance(result, list) and all(isinstance(row, (list, tuple, str)) for row in result):
    outcome = {"rows": ["".join(str(cell) for cell in row) for row in result]}
else:
    outcome = {"problem": "type", "type": type(result).__name__}
print(json.dumps(outcome))
"""


def pytest_addoption(parser):
    parser.addoption(
        "--solutions",
        action="store_true",
        help="Test the files in the topic's solutions folder instead of the students' files.",
    )


def _program_folder(request):
    """Return the folder with the files to test.

    Normally this is the exercise folder. With --solutions, it is the
    matching folder in solutions/, for example solutions/01-counting-sheep.
    """
    folder = request.path.parent
    if request.config.getoption("solutions"):
        return folder.parent / "solutions" / folder.name
    return folder


def _clean_lines(text):
    lines = [line.rstrip() for line in text.splitlines()]
    while lines and lines[-1] == "":
        lines.pop()
    return lines


def _read_program(path):
    """Read a student's file and return its syntax tree, or fail with a clear message."""
    try:
        return ast.parse(path.read_text(encoding="utf-8"), filename=path.name)
    except SyntaxError as error:
        problem = error
    pytest.fail(
        f"{path.name} has a mistake on line {problem.lineno}: {problem.msg}\n"
        f"Run {path.name} to see where it is.",
        pytrace=False,
    )


def _indented(lines):
    if not lines:
        return "    (nothing)"
    return "\n".join(f"    {line}" for line in lines)


def _output_problem(name, expected, actual):
    if not actual:
        return f"{name} did not print anything."
    return _first_difference(expected, actual, "Line", "Your output", "lines")


def _first_difference(expected, actual, label, yours, plural):
    for number, (want, got) in enumerate(zip(expected, actual), start=1):
        if want != got:
            return (
                f"{label} {number} is different.\n"
                f"    Expected:    {want}\n"
                f"    {yours + ':':<12} {got}"
            )
    return f"{yours} has {len(actual)} {plural}, but {len(expected)} {plural} were expected."


def _run(filename, arguments, folder):
    try:
        result = subprocess.run(
            [sys.executable, *arguments],
            cwd=folder,
            capture_output=True,
            text=True,
            timeout=TIME_LIMIT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        result = None
    if result is None:
        pytest.fail(
            f"{filename} took longer than {TIME_LIMIT_SECONDS} seconds.\n"
            "Does it wait for input() or have a loop that never ends?",
            pytrace=False,
        )
    if result.returncode != 0:
        pytest.fail(f"{filename} stopped with an error:\n\n{result.stderr.rstrip()}", pytrace=False)
    return result.stdout


@pytest.fixture
def check_program(request):
    """Run a program in the test's folder and compare what it prints."""
    folder = _program_folder(request)

    def check(filename, expected_output):
        expected = _clean_lines(expected_output)
        actual = _clean_lines(_run(filename, [filename], folder))
        if actual != expected:
            pytest.fail(
                f"{_output_problem(filename, expected, actual)}\n\n"
                f"Expected output:\n{_indented(expected)}\n\n"
                f"Your output:\n{_indented(actual)}",
                pytrace=False,
            )

    return check


@pytest.fixture
def check_grid(request):
    """Call a function in a program and compare the grid it returns.

    A grid is a list of rows. Each row can be a list of cells or a string.
    For example, check_grid("exercise.py", "make_checkerboard", [2], "#.\\n.#")
    checks that make_checkerboard(2) returns [["#", "."], [".", "#"]].
    Pass call="zoom(INVADER, 2)" to show a short call in messages when the
    arguments are long.
    """
    folder = _program_folder(request)

    def check(filename, function_name, arguments, expected_grid, call=None):
        _read_program(folder / filename)
        if call is None:
            call = f"{function_name}({', '.join(repr(argument) for argument in arguments)})"
        output = _run(filename, ["-c", _CALL_FUNCTION, filename, function_name, json.dumps(arguments)], folder)
        outcome = json.loads(output.splitlines()[-1])

        problem = outcome.get("problem")
        if problem == "missing":
            pytest.fail(f"{filename} must have a function called {function_name}. Do not rename it.", pytrace=False)
        if problem == "none":
            pytest.fail(
                f"{call} returned None.\nMake sure the function still ends with its return line.",
                pytrace=False,
            )
        if problem == "type":
            pytest.fail(f"{call} must return a grid, but it returned a {outcome['type']}.", pytrace=False)

        expected = expected_grid.strip().splitlines()
        actual = outcome["rows"]
        if actual != expected:
            pytest.fail(
                f"{call} returned a different grid.\n"
                f"{_first_difference(expected, actual, 'Row', 'Your grid', 'rows')}\n\n"
                f"Expected grid:\n{_indented(expected)}\n\n"
                f"Your grid:\n{_indented(actual)}",
                pytrace=False,
            )

    return check


@pytest.fixture
def check_uses_for_loop(request):
    """Read a program and check that it contains a for loop.

    A for loop statement or a list comprehension both count.
    Comments and text inside strings do not.
    """
    folder = _program_folder(request)

    def check(filename):
        tree = _read_program(folder / filename)
        for node in ast.walk(tree):
            if isinstance(node, (ast.For, ast.comprehension)):
                return
        pytest.fail(f"{filename} must use a for loop.", pytrace=False)

    return check


@pytest.fixture
def check_does_not_use(request):
    """Read a program and check that it does not use any of the given names.

    For example, check_does_not_use("exercise.py", ["max"]) fails for
    max(numbers), and ["sort"] fails for numbers.sort().
    """
    folder = _program_folder(request)

    def check(filename, names):
        tree = _read_program(folder / filename)
        used = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                used.add(node.id)
            elif isinstance(node, ast.Attribute):
                used.add(node.attr)
        for name in names:
            if name in used:
                pytest.fail(f"{filename} must not use `{name}`. Try to solve it without it.", pytrace=False)

    return check
