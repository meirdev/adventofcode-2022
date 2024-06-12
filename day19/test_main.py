from .main import part1, part2


INPUT = """
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
"""


def test_part1():
    assert part1(INPUT) == 33


def test_part2():
    assert part2(INPUT) == 62


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 960
    assert part2(input) == 2040
