from pathlib import Path
import subprocess
import sys


TESTS = r'''
import ast
import builtins
import contextlib
import inspect
import io
from pathlib import Path
import random
import runpy
import sys
from types import ModuleType, SimpleNamespace
from unittest.mock import patch

health = {"pikachu": 35, "bulbasaur": 45, "charmander": 39, "eevee": 55, "mewtwo": 106}
lookups = []
library = ModuleType("pokebase")
def pokemon(name):
    lookups.append(name)
    if name == "offline":
        raise OSError("connection unavailable")
    if name not in health:
        error = OSError("Pokemon not found")
        error.response = SimpleNamespace(status_code=404)
        raise error
    values = (health[name], 55, 40, 50, 50, 90)
    return SimpleNamespace(stats=[SimpleNamespace(base_stat=value) for value in values])
library.pokemon = pokemon
def resource_list(endpoint):
    assert endpoint == "pokemon", f"Expected resource: pokemon. Actual: {endpoint!r}."
    return SimpleNamespace(names=list(health) + ["offline"])
library.APIResourceList = resource_list
sys.modules["pokebase"] = library

# Check function bodies without starting the incomplete battle loop.
tree = ast.parse(Path("exercise.py").read_text(encoding="utf-8"))
definitions = [node for node in tree.body
               if isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef))]
namespace = {}
exec(compile(ast.Module(body=definitions, type_ignores=[]), "exercise.py", "exec"), namespace)
for name in ("get_hp", "attack"):
    assert callable(namespace.get(name)), f"Expected: function {name}. Actual: it is missing."
    assert inspect.getdoc(namespace[name]), f"Expected: a docstring on {name}. Actual: none."

for name in ("pikachu", "eevee", "mewtwo"):
    lookups.clear()
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        actual = namespace["get_hp"](name)
    expected = health[name]
    assert actual == expected, f"Expected returned health for {name}: {expected}. Actual: {actual!r}."
    assert lookups == [name], f"Expected: look up {name!r} once. Actual: {lookups!r}."
    assert not output.getvalue(), "Expected: get_hp returns health. Actual: it prints."

for hp, damage, expected in [(35, 5, 30), (35, 15, 20), (10, 15, 0), (1, 1, 0), (0, 5, 0)]:
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        actual = namespace["attack"](hp, damage)
    assert actual == expected, f"Expected returned health for attack({hp}, {damage}): {expected}. Actual: {actual!r}."
    assert not output.getvalue(), "Expected: attack returns health. Actual: it prints."

def play(inputs, damage_values, expected_end, expected_player, expected_exit=0,
         fail_opponent=False, fail_names=False):
    lookups.clear()
    values = iter(inputs)
    damages = iter(damage_values)
    prompts = []
    rolls = []

    def read_input(prompt=""):
        prompts.append(prompt)
        try:
            answer = next(values)
        except StopIteration:
            raise AssertionError("Expected: battle ends or asks for a valid name. Actual: too many input calls.")
        print(prompt + answer)
        return answer

    def choose_opponent(names):
        assert "bulbasaur" in names, f"Expected: a valid opponent list. Actual: {names!r}."
        return "bulbasaur"

    def roll(low, high):
        assert (low, high) == (5, 15), f"Expected damage bounds: (5, 15). Actual: {(low, high)!r}."
        try:
            value = next(damages)
        except StopIteration:
            raise AssertionError("Expected: no more attacks after defeat. Actual: an extra damage roll.")
        rolls.append(value)
        return value

    def lookup(name):
        if fail_opponent and name == "bulbasaur":
            lookups.append(name)
            raise OSError("opponent connection unavailable")
        return pokemon(name)

    def names(endpoint):
        if fail_names:
            raise OSError("name list connection unavailable")
        return resource_list(endpoint)

    output = io.StringIO()
    exit_code = 0
    with patch.object(builtins, "input", read_input), \
         patch.object(random, "choice", choose_opponent), \
         patch.object(random, "randint", roll), \
         patch.object(library, "pokemon", lookup), \
         patch.object(library, "APIResourceList", names), \
         contextlib.redirect_stdout(output):
        try:
            runpy.run_path("exercise.py", run_name="__main__")
        except SystemExit as error:
            exit_code = error.code or 0
    actual = output.getvalue()
    assert exit_code == expected_exit, f"Expected exit code: {expected_exit}. Actual: {exit_code!r}. Output: {actual!r}."
    assert expected_end in actual, f"Expected message: {expected_end!r}. Actual output: {actual!r}."
    assert len(rolls) == len(damage_values), (
        f"Expected: {len(damage_values)} attacks. Actual: {len(rolls)}. Output: {actual!r}."
    )
    if expected_exit == 0:
        assert f"You: {expected_player} ({health[expected_player]} HP)" in actual, (
            f"Expected: use the chosen Pokemon's real health. Actual output: {actual!r}."
        )
        assert lookups.count(expected_player) == 1 and lookups.count("bulbasaur") == 1, (
            f"Expected: fetch each fighter once, not per turn. Actual lookups: {lookups!r}."
        )
        assert "has -" not in actual, f"Expected: health never below zero. Actual output: {actual!r}."
    return actual, prompts

win, prompts = play(["pikachu", "", "", ""], [15, 15, 15, 15, 15], "You win!", "pikachu")
assert win.count("pikachu has") == 2, f"Expected: two counterattacks. Actual output: {win!r}."
assert "bulbasaur has 0 HP." in win, f"Expected: opponent reaches zero. Actual output: {win!r}."
loss, prompts = play(["pikachu", "", "", ""], [5, 15, 5, 15, 5, 15], "You lose!", "pikachu")
assert "pikachu has 0 HP." in loss, f"Expected: player reaches zero. Actual output: {loss!r}."
play(["eevee", "", "", ""], [15, 15, 15, 15, 15], "You win!", "eevee")
retry, prompts = play(["not-a-pokemon", " PIKACHU ", "", "", ""],
                      [15, 15, 15, 15, 15], "You win!", "pikachu")
assert "Pokemon not found" in retry, f"Expected: explain the invalid name. Actual output: {retry!r}."
play(["", "pikachu", "", "", ""], [15, 15, 15, 15, 15], "You win!", "pikachu")
play(["offline"], [], "Could not load Pokemon data", "pikachu", expected_exit=1)
play(["pikachu"], [], "Could not load opponent data", "pikachu", expected_exit=1, fail_opponent=True)
play([], [], "Could not load Pokemon data", "pikachu", expected_exit=1, fail_names=True)
'''


def check():
    try:
        result = subprocess.run(
            [sys.executable, "-c", TESTS], cwd=Path(__file__).resolve().parent,
            capture_output=True, text=True, encoding="utf-8", timeout=5,
        )
    except subprocess.TimeoutExpired:
        print("Not quite yet.\nExpected: a battle that ends when health reaches zero.")
        print("Actual: the program was still running after 5 seconds. Did you fill both loop gaps?")
        raise SystemExit(1)
    if result.returncode:
        print("Not quite yet.\nExpected: implemented functions, docstrings, and a finishing battle.")
        print("Your output:\n" + (result.stdout or "(nothing; see the function or battle error below)"))
        print(result.stderr.strip().splitlines()[-1])
        raise SystemExit(1)
    print("Correct! Functions, wins, losses, random bounds and lookup errors all passed offline.")


if __name__ == "__main__":
    check()
