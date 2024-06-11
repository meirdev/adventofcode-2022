import dataclasses
import re

import shapely


@dataclasses.dataclass(frozen=True)
class Position:
    x: int
    y: int


@dataclasses.dataclass(frozen=True)
class Sensor(Position):
    closest_beacon: Position


def manhattan_distance(a: Position, b: Position) -> int:
    return abs(a.x - b.x) + abs(a.y - b.y)


def sensors_coverage(input: str) -> list[shapely.Polygon]:
    sensors = parse_input(input)

    polygons = []

    for sensor in sensors:
        x, y = sensor.x, sensor.y

        md = manhattan_distance(sensor, sensor.closest_beacon)

        polygons.append(
            shapely.Polygon(((x, y - md), (x - md, y), (x, y + md), (x + md, y)))
        )

    return polygons


def parse_input(input: str) -> list[Sensor]:
    sensors = []

    for line in re.findall(
        r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)",
        input,
    ):
        sx, sy, bx, by = map(int, line)
        sensors.append(Sensor(x=sx, y=sy, closest_beacon=Position(x=bx, y=by)))

    return sensors


def part1(input: str, y: int = 2_000_000) -> int:
    polygons = sensors_coverage(input)

    poly = shapely.Polygon()

    for i in polygons:
        poly = poly.union(i)

    min_x, _, max_x, _ = poly.bounds

    row = shapely.LineString(((min_x, y + 0.5), (max_x, y + 0.5)))

    result = row.intersection(poly)

    if isinstance(result, shapely.MultiLineString):
        geoms = list(result.geoms)
    else:
        geoms = [result]

    length = 0

    for i in geoms:
        (x1, _), (x2, _) = list(i.coords)
        length += x2 - x1

    return int(length)


def part2(input: str, size: int = 4_000_000) -> int:
    polygons = sensors_coverage(input)

    poly = shapely.Polygon([(0, 0), (size, 0), (size, size), (0, size)])

    for i in polygons:
        poly = poly.difference(i)

    if isinstance(poly, shapely.MultiPolygon):
        poly = next(i for i in poly.geoms if i.area == 2)

    coords = list(poly.boundary.coords)

    return int(coords[1][0] * 4000000 + coords[0][1])


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
