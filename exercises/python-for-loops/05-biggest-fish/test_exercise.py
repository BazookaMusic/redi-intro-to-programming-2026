"""Tests for Exercise 5. Run them from this folder with: python -m pytest"""

EXPECTED_OUTPUT = """\
The largest number is 89
"""


def test_prints_largest_number(check_program):
    check_program("exercise.py", EXPECTED_OUTPUT)


def test_uses_a_for_loop(check_uses_for_loop):
    check_uses_for_loop("exercise.py")


def test_does_not_use_max_sorted_or_sort(check_does_not_use):
    check_does_not_use("exercise.py", ["max", "sorted", "sort"])
