import dataclasses
import itertools
from typing import Iterator


@dataclasses.dataclass
class Instruction:
    pass


@dataclasses.dataclass
class addx(Instruction):
    value: int


@dataclasses.dataclass
class noop(Instruction):
    pass


def parse_input(input: str) -> list[Instruction]:
    instructions: list[Instruction] = []

    for line in input.strip().splitlines():
        parts = line.split(" ")

        match parts:
            case ["noop"]:
                instructions.append(noop())
            case ["addx", value]:
                instructions.append(addx(int(value)))

    return instructions


def run(input: str) -> Iterator[tuple[int, int]]:
    instructions = parse_input(input)

    cycles, x = 0, 1

    for i in instructions:
        match i:
            case noop():
                cycles += 1
                yield cycles, x
            case addx(value):
                cycles += 1
                yield cycles, x
                cycles += 1
                yield cycles, x
                x += value


def part1(input: str) -> int:
    ticks = itertools.chain([20], itertools.count(60, 40))

    sum_signal_strength, tick = 0, next(ticks)

    for cycles, x in run(input):
        if cycles == tick:
            sum_signal_strength += cycles * x
            tick = next(ticks)

    return sum_signal_strength


def part2(input: str) -> str:
    output, column = "", 0

    for cycles, x in run(input):
        output += "#" if x - 1 <= column <= x + 1 else "."
        column += 1

        if cycles % 40 == 0:
            output += "\n"
            column = 0

    return output.strip()


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:")
    print(part2(input))


if __name__ == "__main__":
    main()
