from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from checking import run_check


CASES = (
    (("80", "15"), ("Final price: 68",)),
    (("19.99", "20"), ("Final price: 15.99",)),
    (("7.25", "0"), ("Final price: 7.25",)),
)

if __name__ == "__main__":
    run_check(Path(__file__).with_name("exercise.py"), CASES)
