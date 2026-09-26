from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import runpy


SAMPLE = ["The happy cat visited 3 places in Berlin."]


def fail(expected, actual, message):
    print(f"Not quite yet. {message}")
    print("Expected output:\n" + "\n".join(expected))
    print("Your output:\n" + ("\n".join(actual) or "(nothing)"))
    raise SystemExit(1)


def check():
    output = StringIO()
    with redirect_stdout(output):
        variables = runpy.run_path(str(Path(__file__).with_name("exercise.py")), run_name="__main__")
    actual = [line.strip() for line in output.getvalue().splitlines() if line.strip()]

    required = {"adjective": str, "animal": str, "place": str, "number": int}
    for name, expected_type in required.items():
        if type(variables.get(name)) is not expected_type:
            fail(SAMPLE, actual, f"Create {name} as a {expected_type.__name__} variable.")

    expected = [
        f"The {variables['adjective']} {variables['animal']} visited "
        f"{variables['number']} places in {variables['place']}."
    ]
    if actual != expected:
        fail(expected, actual, "Use all four variables in the sentence from exercise.py.")
    print("Correct! Your sentence uses all four values.")


if __name__ == "__main__":
    check()
