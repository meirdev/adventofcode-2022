from .main import part1, part2


INPUT = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""


def test_part1():
    assert part1(INPUT) == 3068


def test_part2():
    assert part2(INPUT) == 1514285714288


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 3235
    assert part2(input) == 1591860465110
