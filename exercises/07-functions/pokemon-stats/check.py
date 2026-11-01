from pathlib import Path
import subprocess
import sys


TESTS = r'''
import contextlib
import io
import runpy
import sys
from types import ModuleType, SimpleNamespace

SAMPLE = {
    "pikachu": (35, 55, 40, 50, 50, 90),
    "bulbasaur": (45, 49, 49, 65, 65, 45),
    "charmander": (39, 52, 43, 60, 50, 65),
    "mewtwo": (106, 110, 90, 154, 90, 130),
}

library = ModuleType("pokebase")
def pokemon(name):
    key = str(name).lower()
    assert key in SAMPLE, f"Sample data has no Pokemon called {name!r}."
    return SimpleNamespace(stats=[SimpleNamespace(base_stat=value) for value in SAMPLE[key]])
library.pokemon = pokemon
sys.modules["pokebase"] = library

output = io.StringIO()
with contextlib.redirect_stdout(output):
    namespace = runpy.run_path("exercise.py")
print(output.getvalue(), end="")
function = namespace.get("total_stats")
assert callable(function), "Expected: total_stats(name). Actual: function is missing."
for name, numbers in SAMPLE.items():
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        actual = function(name)
    assert not captured.getvalue(), "Expected: return the total. Actual: total_stats prints."
    expected = sum(numbers)
    assert actual == expected, (
        f"Expected total_stats({name!r}) to return {expected}. Actual: {actual!r}."
    )
actual = output.getvalue().split()
assert actual[:2] == ["320", "318"], (
    f"Expected the first output lines: ['320', '318']. Actual: {actual[:2]!r}."
)

advanced = namespace.get("strongest")
if advanced is None:
    print("\nAdvanced task: strongest is not written yet.")
else:
    assert callable(advanced), "Expected: strongest(names) to be a function."
    for names, expected in [
        (["bulbasaur", "pikachu"], "pikachu"),
        (["pikachu", "mewtwo", "charmander"], "mewtwo"),
        (["charmander", "bulbasaur"], "bulbasaur"),
        (["charmander"], "charmander"),
    ]:
        actual = advanced(names)
        assert actual == expected, (
            f"Expected strongest({names!r}) to return {expected!r}. Actual: {actual!r}."
        )
    print("\nAdvanced task: strongest passed every test.")
'''


def check():
    expected = (
        "Expected input and output:\n"
        "total_stats('pikachu') returns 320\n"
        "Your program prints:\n320\n318"
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
    if result.returncode:
        print("Not quite yet.\n" + expected)
        print("Your output:\n" + (result.stdout or "(nothing)"))
        print(result.stderr.strip().splitlines()[-1])
        raise SystemExit(1)
    print(result.stdout.strip().splitlines()[-1])
    print("Correct! total_stats passed with sample data. No internet or packages were needed.")


if __name__ == "__main__":
    check()
