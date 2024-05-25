def parse_input(input: str) -> list[list[int]]:
    return [list(map(int, i.splitlines())) for i in input.strip().split("\n\n")]


def solution(input: str, top: int) -> int:
    elf_calories = parse_input(input)

    return sum(sorted(map(sum, elf_calories), reverse=True)[:top])


def part1(input: str) -> int:
    return solution(input, 1)


def part2(input: str) -> int:
    return solution(input, 3)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
