import math
from typing import Iterable


def parse_input(input: str) -> list[list[int]]:
    return [[int(i) for i in row] for row in input.strip().splitlines()]


def part1(input: str) -> int:
    grid = parse_input(input)

    visible = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            height = grid[y][x]

            visible += any(
                [
                    all(grid[i][x] < height for i in range(0, y)),
                    all(grid[i][x] < height for i in range(y + 1, len(grid))),
                    all(grid[y][i] < height for i in range(0, x)),
                    all(grid[y][i] < height for i in range(x + 1, len(grid[y]))),
                ]
            )

    return visible


def part2(input: str) -> int:
    grid = parse_input(input)

    max_scenic_score = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            height = grid[y][x]

            def take_while(iterable: Iterable[int]) -> int:
                k = 0
                for i in iterable:
                    k += 1
                    if i >= height:
                        break
                return k

            max_scenic_score = max(
                max_scenic_score,
                math.prod(
                    [
                        take_while(grid[i][x] for i in range(y - 1, -1, -1)),
                        take_while(grid[i][x] for i in range(y + 1, len(grid))),
                        take_while(grid[y][i] for i in range(x - 1, -1, -1)),
                        take_while(grid[y][i] for i in range(x + 1, len(grid[y]))),
                    ]
                ),
            )

    return max_scenic_score


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
