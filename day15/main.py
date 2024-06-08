import dataclasses
import re


@dataclasses.dataclass(frozen=True)
class Position:
    x: int
    y: int


@dataclasses.dataclass(frozen=True)
class Beacon(Position):
    pass


@dataclasses.dataclass(frozen=True)
class Sensor(Position):
    closest_beacon: Beacon


def manhattan_distance(a: Position, b: Position) -> int:
    return abs(a.x - b.x) + abs(a.y - b.y)


def parse_input(input: str) -> list[Sensor]:
    sensors = []

    for line in re.findall(
        r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)",
        input,
    ):
        sx, sy, bx, by = map(int, line)
        sensors.append(Sensor(x=sx, y=sy, closest_beacon=Beacon(x=bx, y=by)))

    return sensors


def part1(input: str, y: int = 2_000_000) -> int:
    sensors = parse_input(input)


def part2(input: str):
    pass


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
