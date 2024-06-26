from typing import NamedTuple


class Position(NamedTuple):
    x: int
    y: int
    z: int


def parse_input(input: str) -> list[Position]:
    return [Position(*map(int, line.split(","))) for line in input.strip().splitlines()]


def part1(input: str) -> int:
    pass


def part2(input: str) -> int:
    pass


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
