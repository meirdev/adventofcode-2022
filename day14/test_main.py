from .main import part1, part2


INPUT = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""


def test_part1():
    assert part1(INPUT) == 24


def test_part2():
    assert part2(INPUT) == 93


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 892
    assert part2(input) == 27155
