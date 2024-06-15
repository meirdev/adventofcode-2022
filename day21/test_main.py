from .main import part1, part2


INPUT = """
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
"""


def test_part1():
    assert part1(INPUT) == 152


def test_part2():
    assert part2(INPUT) == 301


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 78342931359552
    assert part2(input) == 3296135418820
