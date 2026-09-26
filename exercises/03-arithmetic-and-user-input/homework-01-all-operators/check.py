from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from checking import run_check


CASES = (
    (
        (),
        (
            "Sum: 22",
            "Difference: 12",
            "Product: 85",
            "Quotient: 3.4",
            "Whole number division: 3",
            "Remainder: 2",
            "Power: 1419857",
        ),
    ),
)

if __name__ == "__main__":
    run_check(Path(__file__).with_name("exercise.py"), CASES)
