from .main import part1, part2


INPUT = """
1
2
-3
3
-2
0
4
"""


def test_part1():
    assert part1(INPUT) == 3


def test_part2():
    assert part2(INPUT) == 1623178306


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 5904
    assert part2(input) == 8332585833851
