import dataclasses
import math
import re
from typing import Callable

RE = re.compile(
    r"""Monkey (\d+):
  Starting items: (.*?)
  Operation: new = (.*?)
  Test: divisible by (\d+)
    If true: throw to monkey (\d+)
    If false: throw to monkey (\d+)"""
)


@dataclasses.dataclass
class Monkey:
    id: int
    starting_items: list[int]
    operation: str
    test: int
    test_result: dict[bool, int]

    inspected_items: int = 0


def parse_input(input: str) -> dict[int, Monkey]:
    monkeys: dict[int, Monkey] = {}

    for id, starting_items, operation, test, true, false in RE.findall(input):
        monkeys[int(id)] = Monkey(
            id=int(id),
            starting_items=list(map(int, starting_items.split(", "))),
            operation=operation,
            test=int(test),
            test_result={True: int(true), False: int(false)},
        )

    return monkeys


def solution(
    input: str,
    rounds: int,
    worry_level_divided_fn: Callable[[list[Monkey]], Callable[[int], int]],
) -> int:
    monkeys = parse_input(input)

    sorted_monkeys = sorted(monkeys.values(), key=lambda i: i.id)

    worry_level_divided = worry_level_divided_fn(sorted_monkeys)

    for _ in range(rounds):
        for monkey in sorted_monkeys:
            while monkey.starting_items:
                old = monkey.starting_items.pop(0)
                worry_level = worry_level_divided(eval(monkey.operation))

                monkeys[
                    monkey.test_result[worry_level % monkey.test == 0]
                ].starting_items.append(worry_level)

                monkey.inspected_items += 1

    return math.prod(
        sorted([i.inspected_items for i in sorted_monkeys], reverse=True)[:2]
    )


def part1(input: str) -> int:
    def fn(_: list[Monkey]) -> Callable[[int], int]:
        return lambda i: i // 3

    return solution(input, 20, fn)


def part2(input: str) -> int:
    def fn(monkeys: list[Monkey]) -> Callable[[int], int]:
        lcm = math.lcm(*(i.test for i in monkeys))
        return lambda i: i % lcm

    return solution(input, 10_000, fn)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
