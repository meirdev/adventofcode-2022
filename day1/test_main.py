from .main import part1, part2


INPUT = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def test_part1():
    assert part1(INPUT) == 24000


def test_part2():
    assert part2(INPUT) == 45000


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 70374
    assert part2(input) == 204610
