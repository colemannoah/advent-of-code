from dataclasses import dataclass
import re
import sys

from sympy import Eq, Integer, solve, symbols


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Config:
    a_pos: Point
    b_pos: Point
    prize_pos: Point


def main(input: list[Config]) -> None:
    total = 0

    # It's a system of linear equations!
    for config in input:
        x, y = symbols("x y")
        eq1 = Eq(config.a_pos.x * x + config.b_pos.x * y, config.prize_pos.x)
        eq2 = Eq(config.a_pos.y * x + config.b_pos.y * y, config.prize_pos.y)
        soln = solve((eq1, eq2), (x, y))

        if isinstance(soln[x], Integer) and isinstance(soln[y], Integer):
            x, y = soln[x], soln[y]
            total += int(x * 3 + y)

    print(total)


if __name__ == "__main__":
    input = sys.stdin.read()
    blocks = input.strip().split("\n\n")

    configs: list[Config] = []
    for block in blocks:
        lines = block.split("\n")

        a_match = re.match(r"Button A: X\+(\d+), Y\+(\d+)", lines[0])
        a_x, a_y = map(int, a_match.groups())

        b_match = re.match(r"Button B: X\+(\d+), Y\+(\d+)", lines[1])
        b_x, b_y = map(int, b_match.groups())

        prize_match = re.match(r"Prize: X=(\d+), Y=(\d+)", lines[2])
        prize_x, prize_y = map(int, prize_match.groups())

        configs.append(
            Config(
                a_pos=Point(a_x, a_y),
                b_pos=Point(b_x, b_y),
                prize_pos=Point(prize_x, prize_y),
            )
        )

    main(configs)
