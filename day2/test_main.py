from .main import part1, part2


INPUT = """
A Y
B X
C Z
"""


def test_part1():
    assert part1(INPUT) == 15


def test_part2():
    assert part2(INPUT) == 12


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 13484
    assert part2(input) == 13433
