from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import runpy


EXPECTED = ["<class 'str'>", "3", "4", "TypeError", "True", "<class 'float'>"]


def check():
    output = StringIO()
    with redirect_stdout(output):
        runpy.run_path(str(Path(__file__).with_name("exercise.py")), run_name="__main__")
    actual = [line.strip() for line in output.getvalue().splitlines() if line.strip()]

    if actual != EXPECTED:
        print("Not quite yet. Print the six answers in the order shown in exercise.py.")
        print("Expected output:\n" + "\n".join(EXPECTED))
        print("Your output:\n" + ("\n".join(actual) or "(nothing)"))
        raise SystemExit(1)
    print("Correct! All six answers match.")


if __name__ == "__main__":
    check()
