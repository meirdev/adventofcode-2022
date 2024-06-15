from sympy import Eq, Symbol, nsimplify, solve


def parse_input(input: str) -> dict[str, int | list[str]]:
    labels: dict[str, int | list[str]] = {}

    for line in input.strip().splitlines():
        label, line = line.split(": ")

        if line.isnumeric():
            labels[label] = int(line)
        else:
            labels[label] = line.split(" ")

    return labels


def solution(input: str, part: int) -> int:
    labels = parse_input(input)

    def calculate(key: str) -> float:
        value = labels[key]

        if not isinstance(value, list):
            return value

        match value[1]:
            case "+":
                return calculate(value[0]) + calculate(value[2])
            case "-":
                return calculate(value[0]) - calculate(value[2])
            case "*":
                return calculate(value[0]) * calculate(value[2])
            case "/":
                return calculate(value[0]) / calculate(value[2])
            case _:
                raise ValueError("invalid operator")

    root = labels["root"]

    if part == 2:
        labels["humn"] = Symbol("x")  # type: ignore

    a = calculate(root[0])  # type: ignore
    b = calculate(root[2])  # type: ignore

    if part == 1:
        return int(a + b)

    return nsimplify(solve(Eq(a, b))[0])


def part1(input: str) -> int:
    return solution(input, 1)


def part2(input: str) -> int:
    return solution(input, 2)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
