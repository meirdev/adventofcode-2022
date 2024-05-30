import more_itertools


def parse_input(input: str) -> str:
    return input.strip()


def solution(input: str, length: int) -> int:
    data_stream = parse_input(input)

    return next(
        marker + length
        for marker, characters in zip(
            range(len(data_stream)), more_itertools.windowed(data_stream, length)
        )
        if more_itertools.all_unique(characters)
    )


def part1(input: str) -> int:
    return solution(input, 4)


def part2(input: str) -> int:
    return solution(input, 14)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
