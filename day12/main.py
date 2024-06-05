from typing import NamedTuple


class Position(NamedTuple):
    y: int
    x: int


class HeightMap(NamedTuple):
    map: dict[Position, int]
    start: Position
    end: Position


def parse_input(input: str) -> HeightMap:
    map: dict[Position, int] = {}

    start: Position | None = None
    end: Position | None = None

    for y, line in enumerate(input.strip().splitlines()):
        for x, square in enumerate(line):
            position = Position(y, x)

            if square == "S":
                start = position
                value = 0
            elif square == "E":
                end = position
                value = 25
            else:
                value = ord(square) - ord("a")

            map[position] = value

    assert start is not None and end is not None

    return HeightMap(map, start, end)


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
