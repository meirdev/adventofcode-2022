import re
from typing import Callable, Iterator, NamedTuple


class Move(NamedTuple):
    quantity: int
    src: int
    dst: int


def parse_input(input: str) -> tuple[dict[int, list[str]], list[Move]]:
    input_a, input_b = input.strip("\n").split("\n\n")

    columns = list(
        zip(
            *(
                [line[i : i + 3] for i in range(0, len(line), 4)]
                for line in reversed(input_a.splitlines())
            )
        )
    )

    stacks = {int(col[0][1]): [i[1] for i in col[1:] if i[1] != " "] for col in columns}

    moves = [
        Move(*map(int, i))
        for i in re.findall(r"move (\d+) from (\d+) to (\d+)", input_b)
    ]

    return stacks, moves


def solution(input: str, reverse: bool = False) -> str:
    stacks, moves = parse_input(input)

    pick: Callable[..., Iterator[str]]

    if reverse:
        pick = reversed
    else:
        pick = iter

    for move in moves:
        stacks[move.dst] += pick([stacks[move.src].pop() for _ in range(move.quantity)])

    return "".join(i[-1] for i in stacks.values())


def part1(input: str) -> str:
    return solution(input)


def part2(input: str) -> str:
    return solution(input, reverse=True)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
