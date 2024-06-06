import functools
import itertools
import json
import math
from typing import TypeAlias


Value: TypeAlias = list["Value"] | list[int] | int


def parse_input(input: str) -> list[Value]:
    return [json.loads(line) for line in input.strip().splitlines() if line != ""]


def compare(a: Value, b: Value) -> int:
    match a, b:
        case int(), int():
            return -1 if a < b else int(a != b)
        case list(), int():
            return compare(a, [b])
        case int(), list():
            return compare([a], b)
        case list(a), list(b):
            if (
                result := next(
                    (i for ai, bi in zip(a, b) if (i := compare(ai, bi)) != 0), None
                )
            ) is None:
                return compare(len(a), len(b))
            return result
        case _:
            raise ValueError(f"invalid {a=} {b=}")


def part1(input: str) -> int:
    values = parse_input(input)

    pairs = list(itertools.batched(values, 2))

    return sum(i for i, (a, b) in enumerate(pairs, start=1) if compare(a, b) == -1)


def part2(input: str) -> int:
    values = parse_input(input)

    decoder_key: list[Value] = [[[2]], [[6]]]  # type: ignore

    return math.prod(
        i
        for i, value in enumerate(
            sorted(values + decoder_key, key=functools.cmp_to_key(compare)), start=1
        )
        if value in decoder_key
    )


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
