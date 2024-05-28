from .main import part1, part2


INPUT = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def test_part1():
    assert part1(INPUT) == 2


def test_part2():
    assert part2(INPUT) == 4


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 556
    assert part2(input) == 876
