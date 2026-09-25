"""Tests for Exercise 4. Run them from this folder with: python -m pytest"""

PART_A_EXPECTED_OUTPUT = """\
2
4
6
8
10
"""

PART_B_EXPECTED_OUTPUT = """\
5
4
3
2
1
Liftoff!
"""


def test_part_a_prints_even_numbers_from_2_to_10(check_program):
    check_program("part_a.py", PART_A_EXPECTED_OUTPUT)


def test_part_a_uses_a_for_loop(check_uses_for_loop):
    check_uses_for_loop("part_a.py")


def test_part_b_counts_down_from_5_then_liftoff(check_program):
    check_program("part_b.py", PART_B_EXPECTED_OUTPUT)


def test_part_b_uses_a_for_loop(check_uses_for_loop):
    check_uses_for_loop("part_b.py")
