from pathlib import Path
import subprocess
import sys
import tempfile


# The tests run your functions inside a temporary folder, so they only use
# test files that the checker writes. Your own shopping.txt is never changed.
TESTS = r'''
import contextlib
import io
import os
import sys

exercise = os.path.abspath("exercise.py")
with open(exercise, "r", encoding="utf-8") as file:
    source = file.read()

os.chdir(sys.argv[1])
for name in ["shopping.txt", "shopping_list.txt"]:
    with open(name, "w", encoding="utf-8") as file:
        file.write("bread\nmilk\neggs\n")

namespace = {"__name__": "__main__", "__file__": exercise}
output = io.StringIO()
try:
    with contextlib.redirect_stdout(output):
        exec(compile(source, exercise, "exec"), namespace)
finally:
    print(output.getvalue(), end="")


def read_lines(filename):
    assert os.path.exists(filename), f"Expected: the file {filename!r} exists. Actual: it was not created."
    with open(filename, "r", encoding="utf-8") as file:
        return file.read().splitlines()


def check_file(call, filename, expected):
    actual = read_lines(filename)
    assert actual == expected, (
        f"Expected after {call}: {filename} contains the lines {expected!r}. "
        f"Actual lines: {actual!r}."
    )


save_list = namespace.get("save_list")
assert callable(save_list), "Expected: save_list(filename, items). Actual: function is missing."
save_list("test.txt", ["bread", "milk"])
check_file("save_list('test.txt', ['bread', 'milk'])", "test.txt", ["bread", "milk"])
save_list("test.txt", ["tea"])
check_file("save_list('test.txt', ['tea'])", "test.txt", ["tea"])
with open("old.txt", "w", encoding="utf-8") as file:
    file.write("old\nthings\n")
save_list("old.txt", ["rice", "beans", "salt"])
check_file(
    "save_list('old.txt', ['rice', 'beans', 'salt']) on a file with old and things",
    "old.txt", ["rice", "beans", "salt"],
)

add_item = namespace.get("add_item")
assert callable(add_item), "Expected: add_item(filename, item). Actual: function is missing."
save_list("list.txt", ["bread", "milk"])
add_item("list.txt", "eggs")
check_file("save_list(['bread', 'milk']) and add_item('eggs')", "list.txt", ["bread", "milk", "eggs"])
add_item("list.txt", "cheese")
check_file("add_item('cheese')", "list.txt", ["bread", "milk", "eggs", "cheese"])
save_list("list.txt", ["tea"])
check_file("save_list(['tea'])", "list.txt", ["tea"])
add_item("list.txt", "honey")
check_file("save_list(['tea']) and add_item('honey')", "list.txt", ["tea", "honey"])

advanced = namespace.get("add_items")
if advanced is None:
    print("\nAdvanced task: add_items is not written yet.")
else:
    assert callable(advanced), "Expected: add_items(filename, items) to be a function."
    calls = []

    def counting_add_item(filename, item):
        calls.append(item)
        add_item(filename, item)

    namespace["add_item"] = counting_add_item
    try:
        save_list("more.txt", ["bread", "milk", "eggs"])
        advanced("more.txt", ["cheese", "apples"])
    finally:
        namespace["add_item"] = add_item
    check_file(
        "save_list(['bread', 'milk', 'eggs']) and add_items(['cheese', 'apples'])",
        "more.txt", ["bread", "milk", "eggs", "cheese", "apples"],
    )
    assert calls == ["cheese", "apples"], (
        "Expected: add_items calls add_item once for each item: ['cheese', 'apples']. "
        f"Actual add_item calls: {calls!r}."
    )
    advanced("more.txt", [])
    check_file("add_items([])", "more.txt", ["bread", "milk", "eggs", "cheese", "apples"])
    print("\nAdvanced task: add_items passed every test.")
print("__checks_complete__")
'''


def check():
    expected = (
        "Expected example results:\n"
        "after save_list('shopping.txt', ['bread', 'milk']): bread, milk\n"
        "after add_item('shopping.txt', 'eggs'): bread, milk, eggs"
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
    print("Correct! save_list and add_item passed every test.")


if __name__ == "__main__":
    check()
