from typing import NamedTuple

import networkx as nx


class Position(NamedTuple):
    y: int
    x: int


class HeightMap(NamedTuple):
    map: dict[Position, int]
    start: Position
    end: Position


def parse_input(input: str) -> HeightMap:
    map: dict[Position, int] = {}

    start: Position | None = None
    end: Position | None = None

    for y, line in enumerate(input.strip().splitlines()):
        for x, square in enumerate(line):
            position = Position(y, x)

            if square == "S":
                start = position
                value = 0
            elif square == "E":
                end = position
                value = 25
            else:
                value = ord(square) - ord("a")

            map[position] = value

    assert start is not None and end is not None

    return HeightMap(map, start, end)


def solution(input: str, all_nodes: bool) -> int:
    height_map = parse_input(input)

    G: nx.DiGraph[Position] = nx.DiGraph()

    for pos in height_map.map:
        for y, x in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            pos_ = Position(pos[0] + y, pos[1] + x)

            if (
                pos_ in height_map.map
                and height_map.map[pos] + 1 >= height_map.map[pos_]
            ):
                G.add_edge(pos, pos_)

    if all_nodes:
        nodes = [pos for pos, value in height_map.map.items() if value == 0]
    else:
        nodes = [height_map.start]

    def get_path_length(position: Position) -> int | float:
        try:
            return nx.dijkstra_path_length(G, position, height_map.end)
        except nx.exception.NetworkXNoPath:
            return float("inf")

    return min(get_path_length(i) for i in nodes)


def part1(input: str) -> int:
    return solution(input, all_nodes=False)


def part2(input: str) -> int:
    return solution(input, all_nodes=True)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
