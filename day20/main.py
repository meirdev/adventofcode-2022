import itertools


def parse_input(input: str) -> list[int]:
    return list(map(int, input.strip().splitlines()))


def solution(numbers: list[int], rounds: int) -> int:
    last_index = len(numbers) - 1

    mixed = list(enumerate(numbers))

    for _, current in zip(range(rounds * len(numbers)), itertools.cycle(mixed[:])):
        old = mixed.index(current)
        mixed.remove(current)

        new = (old + current[1] + last_index) % last_index
        mixed.insert(new, current)

    return sum(
        mixed[(mixed.index((numbers.index(0), 0)) + i) % len(numbers)][1]
        for i in (1000, 2000, 3000)
    )


def part1(input: str) -> int:
    numbers = parse_input(input)

    return solution(numbers, 1)


def part2(input: str) -> int:
    numbers = parse_input(input)

    return solution([i * 811589153 for i in numbers], 10)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
