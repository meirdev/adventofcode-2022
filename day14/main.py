import itertools
from typing import TypeAlias


Point: TypeAlias = tuple[int, int]


def parse_input(input: str) -> set[Point]:
    rocks = set()

    def get_points(part: str) -> Point:
        a, b = map(int, part.split(","))
        return a, b

    for line in input.strip().splitlines():
        for (ax, ay), (bx, by) in itertools.pairwise(
            map(get_points, line.split(" -> "))
        ):
            for y in range(min(ay, by), max(ay, by) + 1):
                for x in range(min(ax, bx), max(ax, bx) + 1):
                    rocks.add((x, y))

    return rocks


def solution(input: str, part: int) -> int:
    rocks_and_sands = parse_input(input)

    floor = max(rocks_and_sands, key=lambda i: i[1])[1] + (2 if part == 2 else 0)

    for i in itertools.count():
        x, y = (500, 0)

        while True:
            for x_, y_ in ((x, y + 1), (x - 1, y + 1), (x + 1, y + 1)):
                if part == 1 and floor < y_:
                    return i
                elif part == 2 and floor == y_:
                    continue

                if (x_, y_) not in rocks_and_sands:
                    x, y = x_, y_
                    break
            else:
                if ((x, y)) in rocks_and_sands:
                    return i

                rocks_and_sands.add((x, y))
                break

    return -1


def part1(input: str) -> int:
    return solution(input, part=1)


def part2(input: str) -> int:
    return solution(input, part=2)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
