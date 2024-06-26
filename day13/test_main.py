from .main import part1, part2


INPUT = """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""


def test_part1():
    assert part1(INPUT) == 13


def test_part2():
    assert part2(INPUT) == 140


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 4894
    assert part2(input) == 24180
