from .main import part1, part2


INPUT = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""


def test_part1():
    assert part1(INPUT) == 31


def test_part2():
    assert part2(INPUT) == 29


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 504
    assert part2(input) == 500
