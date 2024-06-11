from .main import part1, part2


INPUT = """
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
"""


def test_part1():
    assert part1(INPUT) == 64


def test_part2():
    assert part2(INPUT) == 58


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 4348
    assert part2(input) == 2546
