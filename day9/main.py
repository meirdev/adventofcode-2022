from typing import NamedTuple


class Point(NamedTuple):
    y: int
    x: int

    def add(self, other: "Point") -> "Point":
        return Point(self.y + other.y, self.x + other.x)

    def distance(self, other: "Point") -> int:
        return abs(self.y - other.y) + abs(self.x - other.x)


DIRECTIONS = {
    "U": Point(-1, 0),
    "D": Point(1, 0),
    "L": Point(0, -1),
    "R": Point(0, 1),
}

DIRECTLY = [
    Point(-1, 0),
    Point(1, 0),
    Point(0, -1),
    Point(0, 1),
]

DIAGONALLY = [
    Point(1, 1),
    Point(1, -1),
    Point(-1, 1),
    Point(-1, -1),
]

DIRS = [Point(0, 0)] + DIRECTLY + DIAGONALLY


def parse_input(input: str) -> list[tuple[Point, int]]:
    moves = []

    for line in input.strip().splitlines():
        dir, steps = line.split(" ")

        moves.append((DIRECTIONS[dir], int(steps)))

    return moves


def solution(input: str, tail_length: int) -> int:
    moves = parse_input(input)

    head = Point(0, 0)
    tails = [Point(0, 0) for _ in range(tail_length)]

    visited = set()

    for dir, steps in moves:
        for _ in range(steps):
            head = head.add(dir)

            current_head = head

            for k in range(len(tails)):
                distance, closest = min(
                    (
                        (tails[k].add(i).distance(current_head), tails[k].add(i))
                        for i in DIRS
                    ),
                    key=lambda i: i[0],
                )

                if distance > 0:
                    tails[k] = closest

                if tails[k] is tails[-1]:
                    visited.add(tails[k])

                current_head = tails[k]

    return len(visited)


def part1(input: str) -> int:
    return solution(input, 1)


def part2(input: str) -> int:
    return solution(input, 9)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
