from pathlib import Path
import subprocess
import sys
import tempfile


# The tests run your functions inside a temporary folder, so they only use
# test files that the checker writes. Your own shopping_list.txt is never changed.
TESTS = r'''
import contextlib
import io
import os
import sys

exercise = os.path.abspath("exercise.py")
with open(exercise, "r", encoding="utf-8") as file:
    source = file.read()

os.chdir(sys.argv[1])
with open("shopping_list.txt", "w", encoding="utf-8") as file:
    file.write("bread\nmilk\neggs\n")

namespace = {"__name__": "__main__", "__file__": exercise}
output = io.StringIO()
try:
    with contextlib.redirect_stdout(output):
        exec(compile(source, exercise, "exec"), namespace)
finally:
    print(output.getvalue(), end="")


def write_test_file(name, text):
    with open(name, "w", encoding="utf-8") as file:
        file.write(text)
    return name


test_files = [
    (write_test_file("test_list.txt", "bread\nmilk\neggs\n"), ["bread", "milk", "eggs"]),
    (write_test_file("no_last_newline.txt", "cheese\nbread\ntoothbrush"),
     ["cheese", "bread", "toothbrush"]),
    (write_test_file("one_item.txt", "apples\n"), ["apples"]),
]

print_list = namespace.get("print_list")
assert callable(print_list), "Expected: print_list(filename). Actual: function is missing."
for filename, expected in test_files:
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        print_list(filename)
    actual = captured.getvalue().splitlines()
    assert actual == expected, (
        f"Expected print_list on a file with {expected!r} to print these lines: {expected!r}. "
        f"Actual lines: {actual!r}."
    )

advanced = namespace.get("has_item")
if advanced is None:
    print("\nAdvanced task: has_item is not written yet.")
else:
    assert callable(advanced), "Expected: has_item(filename, item) to be a function."
    for filename, item, expected in [
        ("test_list.txt", "milk", True),
        ("test_list.txt", "cheese", False),
        ("test_list.txt", "bread", True),
        ("test_list.txt", "eggs", True),
        ("test_list.txt", "mil", False),
        ("no_last_newline.txt", "toothbrush", True),
        ("one_item.txt", "bread", False),
    ]:
        with open(filename, "r", encoding="utf-8") as file:
            items = [line.strip() for line in file]
        actual = advanced(filename, item)
        assert actual is expected, (
            f"Expected has_item on a file with {items!r} and item {item!r} to return {expected!r}. "
            f"Actual: {actual!r}."
        )
    print("\nAdvanced task: has_item passed every test.")
print("__checks_complete__")
'''


def check():
    expected = (
        "Expected example output for a file with bread, milk and eggs:\n"
        "bread\nmilk\neggs"
    )
    folder = Path(__file__).resolve().parent
    with tempfile.TemporaryDirectory(prefix="check-temp-", dir=folder) as test_folder:
        try:
            result = subprocess.run(
                [sys.executable, "-c", TESTS, test_folder], cwd=folder,
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
    print("Correct! print_list passed every test.")


if __name__ == "__main__":
    check()
