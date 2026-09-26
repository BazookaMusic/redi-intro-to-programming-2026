from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from checking import run_check


CASES = (
    (("70", "1.75"), ("BMI: 22.9",)),
    (("54", "1.5"), ("BMI: 24.0",)),
    (("80", "1.8"), ("BMI: 24.7",)),
)

if __name__ == "__main__":
    run_check(Path(__file__).with_name("exercise.py"), CASES)
