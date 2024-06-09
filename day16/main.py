import re
from typing import NamedTuple

import networkx as nx


class Valve(NamedTuple):
    id: str
    flow_rate: int
    tunnels: list[str]


def parse_input(input: str) -> dict[str, Valve]:
    valves = {}

    for id, flow_rate, tunnels in re.findall(
        r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)", input
    ):
        valves[id] = Valve(id, int(flow_rate), tunnels.split(", "))

    return valves


def part1(input: str) -> int:
    pass


def part2(input: str) -> int:
    pass


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
