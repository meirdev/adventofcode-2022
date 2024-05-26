import enum


class Choice(enum.IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(enum.IntEnum):
    LOST = 0
    DRAW = 3
    WON = 6


OPPONENT = {
    "A": Choice.ROCK,
    "B": Choice.PAPER,
    "C": Choice.SCISSORS,
}

YOU = {
    "X": Choice.ROCK,
    "Y": Choice.PAPER,
    "Z": Choice.SCISSORS,
}

OUTCOME = {
    "X": Outcome.LOST,
    "Y": Outcome.DRAW,
    "Z": Outcome.WON,
}


def play(opponent: Choice, you: Choice) -> Outcome:
    match (opponent, you):
        case Choice.ROCK, Choice.SCISSORS:
            return Outcome.LOST
        case Choice.PAPER, Choice.ROCK:
            return Outcome.LOST
        case Choice.SCISSORS, Choice.PAPER:
            return Outcome.LOST
        case Choice.SCISSORS, Choice.ROCK:
            return Outcome.WON
        case Choice.ROCK, Choice.PAPER:
            return Outcome.WON
        case Choice.PAPER, Choice.SCISSORS:
            return Outcome.WON
        case _:
            return Outcome.DRAW


def parse_input(input: str) -> list[tuple[str, str]]:
    games = []

    for line in input.strip().splitlines():
        a, b = line.split(" ")

        games.append((a, b))

    return games


def part1(input: str) -> int:
    score = 0

    for a, b in parse_input(input):
        match (OPPONENT[a], YOU[b]):
            case (
                (Choice.ROCK, Choice.SCISSORS)
                | (Choice.PAPER, Choice.ROCK)
                | (Choice.SCISSORS, Choice.PAPER)
            ):
                score += Outcome.LOST
            case (
                (Choice.SCISSORS, Choice.ROCK)
                | (Choice.ROCK, Choice.PAPER)
                | (Choice.PAPER, Choice.SCISSORS)
            ):
                score += Outcome.WON
            case _:
                score += Outcome.DRAW

        score += YOU[b]

    return score


def part2(input: str) -> int:
    score = 0

    for a, b in parse_input(input):
        match (OPPONENT[a], OUTCOME[b]):
            case (Choice.ROCK, Outcome.LOST) | (Choice.PAPER, Outcome.WON):
                score += Choice.SCISSORS
            case (Choice.PAPER, Outcome.LOST) | (Choice.SCISSORS, Outcome.WON):
                score += Choice.ROCK
            case (Choice.SCISSORS, Outcome.LOST) | (Choice.ROCK, Outcome.WON):
                score += Choice.PAPER
            case _:
                score += OPPONENT[a]

        score += OUTCOME[b]

    return score


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
