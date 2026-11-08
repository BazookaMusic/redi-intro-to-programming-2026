from pathlib import Path
import subprocess
import sys


TESTS = r'''
import contextlib
import io
import runpy

output = io.StringIO()
try:
    with contextlib.redirect_stdout(output):
        namespace = runpy.run_path("exercise.py")
finally:
    print(output.getvalue(), end="")

functions = {}
for name in ["add_contact", "find_number", "remove_contact"]:
    function = namespace.get(name)
    assert callable(function), f"Expected: {name}. Actual: function is missing."
    functions[name] = function

book = {"Ana": "0151 111", "Ben": "0152 222"}
actual = functions["find_number"](book, "Ana")
assert actual == "0151 111", f"Expected find_number(book, 'Ana') to return '0151 111'. Actual: {actual!r}."
actual = functions["find_number"](book, "Zoe")
assert actual == "Unknown", f"Expected find_number(book, 'Zoe') to return 'Unknown'. Actual: {actual!r}."

actual = functions["add_contact"](book, "Zoe", "0153 333")
assert actual is None, f"Expected: add_contact returns nothing. Actual: it returns {actual!r}."
expected = {"Ana": "0151 111", "Ben": "0152 222", "Zoe": "0153 333"}
assert book == expected, f"Expected the book after add_contact: {expected!r}. Actual: {book!r}."
functions["add_contact"](book, "Ana", "0159 999")
actual = book.get("Ana")
assert actual == "0159 999", (
    f"Expected add_contact(book, 'Ana', '0159 999') to update Ana's number. Actual: {actual!r}."
)
actual = functions["find_number"](book, "Zoe")
assert actual == "0153 333", f"Expected find_number(book, 'Zoe') to return '0153 333'. Actual: {actual!r}."

actual = functions["remove_contact"](book, "Ben")
assert actual is True, f"Expected remove_contact(book, 'Ben') to return True. Actual: {actual!r}."
assert "Ben" not in book, f"Expected Ben to be removed. Actual book: {book!r}."
actual = functions["remove_contact"](book, "Ben")
assert actual is False, f"Expected a second remove_contact(book, 'Ben') to return False. Actual: {actual!r}."
assert book == {"Ana": "0159 999", "Zoe": "0153 333"}, f"Expected: the other contacts stay. Actual: {book!r}."

advanced = namespace.get("names_starting_with")
if advanced is None:
    print("\nAdvanced task: names_starting_with is not written yet.")
else:
    assert callable(advanced), "Expected: names_starting_with(book, letter) to be a function."
    book = {"Ana": "1", "Ben": "2", "Zoe": "3", "Alex": "4"}
    for letter, expected in [("Z", ["Zoe"]), ("A", ["Ana", "Alex"]), ("Q", [])]:
        actual = advanced(dict(book), letter)
        assert isinstance(actual, list) and len(actual) == len(expected) and all(
            name in actual for name in expected
        ), (
            f"Expected names_starting_with({book!r}, {letter!r}) to return the list "
            f"{expected!r} in any order. Actual: {actual!r}."
        )
    print("\nAdvanced task: names_starting_with passed every test.")
print("__checks_complete__")
'''


def check():
    expected = (
        "Expected example results:\n"
        "find_number(book, 'Zoe') returns 'Unknown', then '0153 333' after add_contact\n"
        "remove_contact(book, 'Ben') returns True, then False"
    )
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
    print("Correct! add_contact, find_number and remove_contact passed every test.")


if __name__ == "__main__":
    check()
