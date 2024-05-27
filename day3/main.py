import functools
import itertools
import string
from typing import Callable, Iterator


def parse_input(input: str) -> list[str]:
    return input.strip().splitlines()


def priority(char: str) -> int:
    if char in string.ascii_lowercase:
        return ord(char) - ord("a") + 1
    return ord(char) - ord("A") + 27


def solution(
    input: str, group_by: Callable[[list[str]], Iterator[tuple[str, ...]]]
) -> int:
    rucksacks = parse_input(input)

    return sum(map(lambda i: priority(next(iter(functools.reduce(lambda a, b: set(a) & set(b), i)))), group_by(rucksacks)))  # type: ignore


def part1(input: str) -> int:
    return solution(input, lambda rucksacks: itertools.chain(itertools.batched(i, len(i) // 2) for i in rucksacks))  # type: ignore


def part2(input: str) -> int:
    return solution(input, lambda rucksacks: itertools.batched(rucksacks, 3))


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
