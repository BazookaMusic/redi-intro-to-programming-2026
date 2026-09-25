"""Tests for Exercise 8. Run them from this folder with: python -m pytest"""

EXPECTED_OUTPUT = """\
*
**
***
****
*****
"""


def test_prints_star_triangle_5_rows_tall(check_program):
    check_program("exercise.py", EXPECTED_OUTPUT)


def test_uses_a_for_loop(check_uses_for_loop):
    check_uses_for_loop("exercise.py")
