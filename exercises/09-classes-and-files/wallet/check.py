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

Wallet = namespace.get("Wallet")
assert Wallet is not None, "Expected: a class called Wallet. Actual: Wallet is missing."
assert isinstance(Wallet, type), "Expected: Wallet to be a class (class Wallet:)."

for owner, money in [("Zoe", 50), ("Max", 12.5), ("Ana", 0)]:
    try:
        wallet = Wallet(owner, money)
    except TypeError as error:
        raise AssertionError(
            f"Expected: Wallet({owner!r}, {money!r}) creates a wallet. Actual: {error}."
        )
    actual_owner = getattr(wallet, "owner", "(missing)")
    assert actual_owner == owner, (
        f"Expected Wallet({owner!r}, {money!r}).owner to be {owner!r}. Actual: {actual_owner!r}."
    )
    actual_money = getattr(wallet, "money", "(missing)")
    assert actual_money == money, (
        f"Expected Wallet({owner!r}, {money!r}).money to be {money!r}. "
        f"Actual: {actual_money!r}."
    )

for name, owner, money in [("ana", "Ana", 200), ("ben", "Ben", 125)]:
    wallet = namespace.get(name)
    assert wallet is not None, (
        f"Expected: {name} = Wallet({owner!r}, {money}). Actual: {name} is missing."
    )
    assert isinstance(wallet, Wallet), (
        f"Expected: {name} = Wallet({owner!r}, {money}). Actual: {wallet!r}."
    )
    assert (wallet.owner, wallet.money) == (owner, money), (
        f"Expected: {name} has owner {owner!r} and money {money}. "
        f"Actual: owner {wallet.owner!r} and money {wallet.money!r}."
    )

lines = [line.strip() for line in output.getvalue().splitlines()]
money_lines = [["200", "200.0"], ["125", "125.0"]]
first = lines[:4]
assert (
    len(first) == 4 and first[0] == "Ana" and first[1] in money_lines[0]
    and first[2] == "Ben" and first[3] in money_lines[1]
), f"Expected the first output lines: ['Ana', '200', 'Ben', '125']. Actual: {first!r}."

loop_lines = [line for line in lines[4:] if "DKK" in line]
if not loop_lines:
    print("\nAdvanced task: the loop that prints 'Ana has 200 DKK' is not written yet.")
else:
    expected = [["Ana has 200 DKK", "Ana has 200.0 DKK"], ["Ben has 125 DKK", "Ben has 125.0 DKK"]]
    assert len(loop_lines) == 2 and all(
        line in options for line, options in zip(loop_lines, expected)
    ), (
        "Expected the loop to print: ['Ana has 200 DKK', 'Ben has 125 DKK']. "
        f"Actual: {loop_lines!r}."
    )
    print("\nAdvanced task: your loop printed every wallet correctly.")
print("__checks_complete__")
'''


def check():
    expected = (
        "Expected example output:\n"
        "Ana\n200\nBen\n125\n"
        "Advanced: Ana has 200 DKK\nAdvanced: Ben has 125 DKK"
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
    print("Correct! Wallet, ana, ben and your output passed every test.")


if __name__ == "__main__":
    check()
