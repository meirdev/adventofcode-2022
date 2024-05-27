from .main import part1, part2


INPUT = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def test_part1():
    assert part1(INPUT) == 157


def test_part2():
    assert part2(INPUT) == 70


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 7742
    assert part2(input) == 2276
