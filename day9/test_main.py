from .main import part1, part2


INPUT_1 = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

INPUT_2 = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""


def test_part1():
    assert part1(INPUT_1) == 13


def test_part2():
    assert part2(INPUT_1) == 1
    assert part2(INPUT_2) == 36


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 5981
    assert part2(input) == 2352
