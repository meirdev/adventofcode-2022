import enum
import re
from typing import NamedTuple, TypeAlias


class Resource(enum.IntEnum):
    ORE = 0
    CLAY = 1
    OBSIDIAN = 2
    GEODE = 3


Cost: TypeAlias = dict[Resource, int]


class Blueprint(NamedTuple):
    id: int
    ore: Cost
    clay: Cost
    obsidian: Cost
    geode: Cost


def parse_input(input: str) -> list[Blueprint]:
    blueprints = []

    for i in re.findall(
        r"Blueprint (\d+): "
        r"Each ore robot costs (\d+) ore. "
        r"Each clay robot costs (\d+) ore. "
        r"Each obsidian robot costs (\d+) ore and (\d+) clay. "
        r"Each geode robot costs (\d+) ore and (\d+) obsidian.",
        input,
    ):
        i = list(map(int, i))

        blueprints.append(
            Blueprint(
                id=i[0],
                ore={Resource.ORE: i[1]},
                clay={Resource.ORE: i[2]},
                obsidian={Resource.ORE: i[3], Resource.CLAY: i[4]},
                geode={Resource.ORE: i[5], Resource.OBSIDIAN: i[6]},
            )
        )

    return blueprints


def part1(input: str) -> int:
    blueprints = parse_input(input)


def part2(input: str) -> int:
    pass


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
