"""Tests for Exercise 3. Run them from this folder with: python -m pytest"""

EXPECTED_OUTPUT = """\
Total so far: 4
Total so far: 14
Total so far: 17
Total so far: 24
Final total: 24
"""


def test_prints_running_total_and_final_total(check_program):
    check_program("exercise.py", EXPECTED_OUTPUT)


def test_uses_a_for_loop(check_uses_for_loop):
    check_uses_for_loop("exercise.py")
