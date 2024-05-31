import dataclasses
import itertools
import re
from typing import cast


@dataclasses.dataclass
class Command:
    program: str
    arg: str | None = None


@dataclasses.dataclass
class Entry:
    name: str


@dataclasses.dataclass
class File(Entry):
    size: int = 0


@dataclasses.dataclass
class Dir(Entry):
    pass


def parse_input(input: str) -> list[tuple[Command, list[Entry] | None]]:
    command_output: list[tuple[Command, list[Entry] | None]] = []

    regex = re.compile(r"\$ (.+?)\n")

    for cmd, out in itertools.batched(regex.split(input)[1:], 2):
        command = Command(*cmd.split(" "))

        entries: list[Entry] | None

        if command.program == "ls":
            entries = []

            for i in out.strip().splitlines():
                size_type, name = i.split(" ")

                if size_type == "dir":
                    entries.append(Dir(name))
                else:
                    entries.append(File(name, int(size_type)))
        else:
            entries = None

        command_output.append((command, entries))

    return command_output


def solution(input: str) -> dict[tuple[str, ...], int]:
    command_output = parse_input(input)

    path: list[str] = []

    tree: dict[tuple[str, ...], list[Entry]] = {}

    for command, output in command_output:
        match command:
            case Command("ls"):
                tree[tuple(path)] = cast(list[Entry], output)
            case Command("cd", ".."):
                path.pop()
            case Command("cd", dir):
                path.append(cast(str, dir))

    def dir_size(dir: tuple[str, ...]) -> int:
        total_size = 0

        for entry in tree[dir]:
            match entry:
                case Dir(name):
                    total_size += dir_size(dir + (name,))
                case File(_, size):
                    total_size += size

        return total_size

    return {i: dir_size(i) for i in tree}


def part1(input: str) -> int:
    return sum(i for i in solution(input).values() if i <= 100000)


def part2(input: str) -> int:
    tree = solution(input)

    return min(i for i in tree.values() if 70000000 - tree[("/",)] + i >= 30000000)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
