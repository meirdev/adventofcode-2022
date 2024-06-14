import collections
import itertools
import re
from typing import DefaultDict, NamedTuple

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


def solution(input: str, minutes: int) -> dict[frozenset[str], int]:
    valves = parse_input(input)

    G = nx.Graph(
        (valve.id, tunnel) for valve in valves.values() for tunnel in valve.tunnels
    )

    shortest_path: DefaultDict[tuple[str, str], int] = collections.defaultdict(int)

    for a, b in itertools.permutations(G.nodes, r=2):
        shortest_path[a, b] = nx.shortest_path_length(G, a, b)

    options = {i.id for i in valves.values() if i.flow_rate != 0}

    def visit(
        valve: str,
        minutes: int,
        pressure: int,
        state: frozenset[str],
        answer: dict[frozenset[str], int],
    ):
        answer[state] = max(answer.get(state, 0), pressure)

        for i in options - state:
            new_minutes = minutes - shortest_path[valve, i] - 1

            if new_minutes > 0:
                visit(
                    i,
                    new_minutes,
                    pressure + new_minutes * valves[i].flow_rate,
                    state | {i},
                    answer,
                )

        return answer

    return visit(
        "AA",
        minutes,
        0,
        frozenset(),
        {},
    )


def part1(input: str) -> int:
    visited = solution(input, 30)

    return max(visited.values())


def part2(input: str) -> int:
    visited = solution(input, 26)

    return max(
        visited[a] + visited[b]
        for a, b in itertools.permutations(visited, r=2)
        if not a & b
    )


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
