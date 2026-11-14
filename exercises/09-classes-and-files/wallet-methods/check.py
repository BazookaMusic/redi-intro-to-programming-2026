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

wallet = Wallet("Ana", 200)
assert (wallet.owner, wallet.money) == ("Ana", 200), (
    "Expected: Wallet('Ana', 200) has owner 'Ana' and money 200. "
    f"Actual: owner {wallet.owner!r} and money {wallet.money!r}."
)

for method in ["receive", "has_enough_money", "pay"]:
    assert callable(getattr(Wallet, method, None)), (
        f"Expected: a method {method} in the Wallet class. Actual: {method} is missing."
    )


def run_call(wallet, text, method, argument, expected, after):
    with contextlib.redirect_stdout(io.StringIO()):
        actual = getattr(wallet, method)(argument)
    if expected is None:
        assert actual is None, f"Expected {text} to return nothing (None). Actual: {actual!r}."
    else:
        assert actual == expected and type(actual) == type(expected), (
            f"Expected {text} to return {expected!r}. Actual: {actual!r}."
        )
    assert wallet.money == after, (
        f"Expected money after {text}: {after!r}. Actual: {wallet.money!r}."
    )


wallet = Wallet("Ana", 200)
for text, method, argument, expected, after in [
    ("wallet.receive(50)", "receive", 50, None, 250),
    ("wallet.has_enough_money(300)", "has_enough_money", 300, False, 250),
    ("wallet.has_enough_money(250)", "has_enough_money", 250, True, 250),
    ("wallet.pay(100)", "pay", 100, True, 150),
    ("wallet.pay(400)", "pay", 400, False, 150),
    ("wallet.pay(150)", "pay", 150, True, 0),
    ("wallet.receive(30)", "receive", 30, None, 30),
    ("wallet.pay(31)", "pay", 31, False, 30),
]:
    run_call(wallet, text, method, argument, expected, after)

if getattr(Wallet, "pay_all", None) is None:
    print("\nAdvanced task: pay_all is not written yet.")
else:
    assert callable(Wallet.pay_all), "Expected: pay_all(prices) to be a method."
    for start, prices, expected, after in [
        (200, [50, 200, 30], 2, 120),
        (70, [50, 200, 30], 1, 20),
        (100, [], 0, 100),
        (10, [20, 30], 0, 10),
        (100, [40, 60], 2, 0),
    ]:
        wallet = Wallet("Ana", start)
        run_call(
            wallet, f"Wallet('Ana', {start}).pay_all({prices!r})",
            "pay_all", list(prices), expected, after,
        )

    wallet = Wallet("Ana", 100)
    calls = []
    original_pay = wallet.pay

    def counting_pay(price):
        calls.append(price)
        return original_pay(price)

    wallet.pay = counting_pay
    with contextlib.redirect_stdout(io.StringIO()):
        wallet.pay_all([10, 500, 20])
    assert calls == [10, 500, 20], (
        "Expected: pay_all calls self.pay(price) once for each price, in order. "
        f"Actual: self.pay was called with {calls!r}."
    )
    print("\nAdvanced task: pay_all passed every test.")
print("__checks_complete__")
'''


def check():
    expected = (
        "Expected example results, starting from wallet = Wallet('Ana', 200):\n"
        "wallet.receive(50) returns None, money 250\n"
        "wallet.has_enough_money(300) returns False, money 250\n"
        "wallet.pay(100) returns True, money 150\n"
        "wallet.pay(400) returns False, money 150\n"
        "Advanced: wallet.pay_all([50, 200, 30]) returns 2, money 70"
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
    print("Correct! receive, has_enough_money and pay passed every test.")


if __name__ == "__main__":
    check()
