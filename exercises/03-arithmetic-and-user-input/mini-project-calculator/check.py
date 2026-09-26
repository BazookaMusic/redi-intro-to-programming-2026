from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from checking import run_check


CASES = (
    (
        ("10", "3"),
        (
            "Sum: 13",
            "Difference: 7",
            "Product: 30",
            "Quotient: 3.33",
            "Remainder: 1",
            "Power: 1000",
        ),
    ),
    (
        ("2.5", "2"),
        (
            "Sum: 4.5",
            "Difference: 0.5",
            "Product: 5",
            "Quotient: 1.25",
            "Remainder: 0.5",
            "Power: 6.25",
        ),
    ),
)

if __name__ == "__main__":
    run_check(Path(__file__).with_name("exercise.py"), CASES)
