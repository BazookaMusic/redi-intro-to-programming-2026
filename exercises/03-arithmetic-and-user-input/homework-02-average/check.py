from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from checking import run_check


CASES = (((), ("Average: 81.7",)),)

if __name__ == "__main__":
    run_check(Path(__file__).with_name("exercise.py"), CASES)
