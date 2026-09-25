"""Tests for Exercise 10. Run them from this folder with: python -m pytest test_exercise.py"""

TILES_9_BY_9 = """\
111222333
111222333
111222333
444555666
444555666
444555666
777888999
777888999
777888999
"""

TILES_4_BY_6 = """\
112233
112233
445566
445566
"""

TILES_2_BY_3 = """\
123
456
"""


def test_fills_9_by_9_grid_with_3_by_3_tiles(check_grid):
    check_grid("exercise.py", "fill_tiles", [9, 9, 3], TILES_9_BY_9)


def test_fills_4_by_6_grid_with_2_by_2_tiles(check_grid):
    check_grid("exercise.py", "fill_tiles", [4, 6, 2], TILES_4_BY_6)


def test_fills_2_by_3_grid_with_1_by_1_tiles(check_grid):
    check_grid("exercise.py", "fill_tiles", [2, 3, 1], TILES_2_BY_3)
