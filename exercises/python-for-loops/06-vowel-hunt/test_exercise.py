"""Tests for Exercise 6. Run them from this folder with: python -m pytest"""

EXPECTED_OUTPUT = """\
Number of vowels: 6
"""


def test_counts_vowels_in_text(check_program):
    check_program("exercise.py", EXPECTED_OUTPUT)


def test_uses_a_for_loop(check_uses_for_loop):
    check_uses_for_loop("exercise.py")
