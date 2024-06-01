from .main import part1, part2


INPUT = """
30373
25512
65332
33549
35390
"""


def test_part1():
    assert part1(INPUT) == 21


def test_part2():
    assert part2(INPUT) == 8


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 1705
    assert part2(input) == 371200
