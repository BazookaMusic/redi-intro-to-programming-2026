from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import runpy


EXPECTED = ["First: 9", "Second: 5"]


def check():
    output = StringIO()
    with redirect_stdout(output):
        variables = runpy.run_path(str(Path(__file__).with_name("exercise.py")), run_name="__main__")
    actual = [line.strip() for line in output.getvalue().splitlines() if line.strip()]

    if variables.get("first") != 9 or variables.get("second") != 5 or actual != EXPECTED:
        print("Not quite yet. Swap the values so first is 9 and second is 5.")
        print("Expected output:\n" + "\n".join(EXPECTED))
        print("Your output:\n" + ("\n".join(actual) or "(nothing)"))
        raise SystemExit(1)
    print("Correct! The two values are swapped.")


if __name__ == "__main__":
    check()
