"""Tests for Exercise 2. Run them from this folder with: python -m pytest"""

EXPECTED_OUTPUT = """\
I like apple
I like banana
I like cherry
"""


def test_prints_i_like_for_each_fruit(check_program):
    check_program("exercise.py", EXPECTED_OUTPUT)


def test_uses_a_for_loop(check_uses_for_loop):
    check_uses_for_loop("exercise.py")
