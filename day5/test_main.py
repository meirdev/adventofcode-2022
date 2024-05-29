from .main import part1, part2


INPUT = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


def test_part1():
    assert part1(INPUT) == "CMZ"


def test_part2():
    assert part2(INPUT) == "MCD"


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == "ZWHVFWQWW"
    assert part2(input) == "HZFZCCWWV"
