"""Tests for Exercise 1. Run them from this folder with: python -m pytest"""

EXPECTED_OUTPUT = """\
1
2
3
4
5
"""


def test_prints_numbers_from_1_to_5(check_program):
    check_program("exercise.py", EXPECTED_OUTPUT)


def test_uses_a_for_loop(check_uses_for_loop):
    check_uses_for_loop("exercise.py")
