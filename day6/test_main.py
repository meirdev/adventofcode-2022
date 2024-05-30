from .main import part1, part2


INPUT_EXPECT = (
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7, 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5, 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6, 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10, 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11, 26),
)


def test_part1():
    for input, expect, _ in INPUT_EXPECT:
        assert part1(input) == expect


def test_part2():
    for input, _, expect in INPUT_EXPECT:
        assert part2(input) == expect


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 1909
    assert part2(input) == 3380
