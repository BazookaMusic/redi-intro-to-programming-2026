"""Tests for Exercise 9. Run them from this folder with: python -m pytest"""

BOARD_10 = """\
#.#.#.#.#.
.#.#.#.#.#
#.#.#.#.#.
.#.#.#.#.#
#.#.#.#.#.
.#.#.#.#.#
#.#.#.#.#.
.#.#.#.#.#
#.#.#.#.#.
.#.#.#.#.#
"""

BOARD_5 = """\
#.#.#
.#.#.
#.#.#
.#.#.
#.#.#
"""

BOARD_2 = """\
#.
.#
"""


def test_makes_10_by_10_board(check_grid):
    check_grid("exercise.py", "make_checkerboard", [10], BOARD_10)


def test_makes_5_by_5_board(check_grid):
    check_grid("exercise.py", "make_checkerboard", [5], BOARD_5)


def test_makes_2_by_2_board(check_grid):
    check_grid("exercise.py", "make_checkerboard", [2], BOARD_2)
