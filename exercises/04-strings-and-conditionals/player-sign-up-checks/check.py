from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import re


VARIABLES = ("age", "password", "city", "points")
CASES = (
    ((20, "secret", "Copenhagen", 10), ("True", "True", "True", "True")),
    ((17, "Secret", "Berlin", 0), ("False", "False", "False", "False")),
    ((18, "secret", "Lagos", -5), ("True", "True", "False", "True")),
    ((30, "hunter2", "Copenhagen", 0), ("True", "False", "True", "False")),
)


def _describe(values):
    return ", ".join(f"{name} = {value!r}" for name, value in zip(VARIABLES, values))


def _fail(number, values, expected, actual, reason=""):
    print("Not quite yet.")
    if reason:
        print(reason)
    print(f"Test {number} ({_describe(values)})")
    print("Expected output:\n" + "\n".join(expected))
    print("Your output:\n" + ("\n".join(actual) or "(nothing)"))
    raise SystemExit(1)


def _with_values(source, values):
    for name, value in zip(VARIABLES, values):
        pattern = rf"^{name}\s*=.*$"
        if not re.search(pattern, source, flags=re.MULTILINE):
            return None, name
        source = re.sub(pattern, f"{name} = {value!r}", source, count=1, flags=re.MULTILINE)
    return source, ""


def check():
    exercise = Path(__file__).with_name("exercise.py")
    original = exercise.read_text(encoding="utf-8")
    for number, (values, expected) in enumerate(CASES, start=1):
        source, missing = _with_values(original, values)
        if source is None:
            _fail(number, values, expected, [],
                  f"Keep the line that creates the variable {missing} at the start of a line.")

        output = StringIO()
        error = ""
        try:
            with redirect_stdout(output):
                exec(compile(source, str(exercise), "exec"), {"__name__": "__main__"})
        except Exception as problem:
            error = f"Your program stopped with an error: {type(problem).__name__}: {problem}"

        actual = [line.strip() for line in output.getvalue().splitlines() if line.strip()]
        if error:
            _fail(number, values, expected, actual, error)
        if actual != list(expected):
            reason = ""
            if number > 1:
                reason = ("The checker changed the values of the variables. "
                          "Use comparisons, so your answers change with them.")
            _fail(number, values, expected, actual, reason)

    print("Correct! Your output matches every test.")


if __name__ == "__main__":
    check()
