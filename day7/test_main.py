from .main import part1, part2


INPUT = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
$ cd ..
"""


def test_part1():
    assert part1(INPUT) == 95437


def test_part2():
    assert part2(INPUT) == 24933642


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 1350966
    assert part2(input) == 6296435
