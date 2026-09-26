from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from checking import run_check


CASES = (
    (("125",), ("Minutes: 2", "Seconds: 5")),
    (("59",), ("Minutes: 0", "Seconds: 59")),
    (("3600",), ("Minutes: 60", "Seconds: 0")),
)

if __name__ == "__main__":
    run_check(Path(__file__).with_name("exercise.py"), CASES)
