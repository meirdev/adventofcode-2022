import re
from typing import TypeAlias

Section: TypeAlias = tuple[int, int]
Pair: TypeAlias = tuple[Section, Section]


def parse_input(input: str) -> list[Pair]:
    pairs = []

    for line in input.strip().splitlines():
        a1, a2, b1, b2 = map(int, re.findall(r"\d+", line))
        pairs.append(((a1, a2), (b1, b2)))

    return pairs


def part1(input: str) -> int:
    pairs = parse_input(input)

    return sum(
        (a[0] <= b[0] and b[1] <= a[1]) or (b[0] <= a[0] and a[1] <= b[1])
        for a, b in pairs
    )


def part2(input: str) -> int:
    pairs = parse_input(input)

    return sum(a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1] for a, b in pairs)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
