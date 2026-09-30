from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import runpy


EXPECTED = ["<class 'int'>", "<class 'float'>", "<class 'str'>"]


def check():
    output = StringIO()
    with redirect_stdout(output):
        variables = runpy.run_path(str(Path(__file__).with_name("exercise.py")), run_name="__main__")
    actual = [line.strip() for line in output.getvalue().splitlines() if line.strip()]

    if "age_text" not in variables or actual != EXPECTED:
        print("Not quite yet. Start with age_text = \"28\" and print each new type.")
        print("Expected output:\n" + "\n".join(EXPECTED))
        print("Your output:\n" + ("\n".join(actual) or "(nothing)"))
        raise SystemExit(1)
    print("Correct! The types change from int to float to str.")


if __name__ == "__main__":
    check()
