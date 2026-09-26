from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import runpy


SAMPLE = ["Name length: 4", "City length: 6", "Food length: 5", "Longest: Berlin"]


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

    words = {}
    for name in ("name", "city", "food"):
        if type(variables.get(name)) is not str:
            fail(SAMPLE, actual, f"Create {name} as a text variable.")
        words[name] = variables[name]

    lengths = [len(word) for word in words.values()]
    if lengths.count(max(lengths)) != 1:
        fail(SAMPLE, actual, "Choose three words with one clear longest word.")

    longest = max(words, key=lambda name: len(words[name]))
    expected = [
        f"Name length: {len(words['name'])}",
        f"City length: {len(words['city'])}",
        f"Food length: {len(words['food'])}",
        f"Longest: {words[longest]}",
    ]
    if actual != expected:
        fail(expected, actual, "Print each length and the longest word, in order.")
    print("Correct! You found the longest word.")


if __name__ == "__main__":
    check()
