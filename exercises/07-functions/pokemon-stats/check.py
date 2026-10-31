from pathlib import Path
import subprocess
import sys


TESTS = r'''
import ast
import contextlib
import io
from pathlib import Path
import runpy
import sys
from types import ModuleType, SimpleNamespace

source = Path("exercise.py").read_text(encoding="utf-8")
tree = ast.parse(source)
assert any(isinstance(node, (ast.For, ast.While)) for node in ast.walk(tree)), (
    "Expected: a loop to add the stats. Actual: no loop found."
)
assert not any(isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
               and node.func.id == "sum" for node in ast.walk(tree)), (
    "Expected: add the stats using a loop. Actual: sum() was used."
)

for numbers in [(35, 55, 40, 50, 50, 90), (10, 20, 30, 40, 50, 60)]:
    lookups = []
    library = ModuleType("pokebase")
    def pokemon(name):
        lookups.append(name)
        assert name.lower() == "pikachu", f"Expected lookup: pikachu. Actual: {name!r}."
        return SimpleNamespace(stats=[SimpleNamespace(base_stat=value) for value in numbers])
    library.pokemon = pokemon
    sys.modules["pokebase"] = library
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        runpy.run_path("exercise.py")
    actual = output.getvalue().split()
    print(output.getvalue(), end="")
    expected = [str(sum(numbers))]
    assert actual == expected, f"Expected total from sample stats: {expected!r}. Actual: {actual!r}."
    assert len(lookups) == 1, f"Expected: one Pokemon lookup. Actual: {len(lookups)}."
'''


def check():
    try:
        result = subprocess.run(
            [sys.executable, "-c", TESTS], cwd=Path(__file__).resolve().parent,
            capture_output=True, text=True, encoding="utf-8", timeout=3,
        )
    except subprocess.TimeoutExpired:
        print("Not quite yet.\nExpected output:\n320")
        print("Actual: the program was still running after 3 seconds.")
        raise SystemExit(1)
    if result.returncode:
        print("Not quite yet.\nExpected output for Pikachu:\n320")
        print("Your output:\n" + (result.stdout or "(nothing)"))
        print(result.stderr.strip().splitlines()[-1])
        raise SystemExit(1)
    print("Correct! Both sample datasets passed. No internet or packages were needed.")


if __name__ == "__main__":
    check()
