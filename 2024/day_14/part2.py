from dataclasses import dataclass
import sys


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Robot:
    position: Point
    velocity: Point
    width: int = 101
    height: int = 103

    def move(self) -> None:
        self.position.x = (self.position.x + self.velocity.x) % self.width
        self.position.y = (self.position.y + self.velocity.y) % self.height


def main(input: list[Robot]) -> None:
    def visualise_board() -> None:
        board = [["." for _ in range(101)] for _ in range(103)]

        for robot in input:
            board[robot.position.y][robot.position.x] = "#"

        for row in board:
            print("".join(row))

    i = 0
    while True:
        i += 1
        seen: set[tuple[int, int]] = set()

        for robot in input:
            robot.move()
            seen.add((robot.position.x, robot.position.y))

        if len(seen) == len(input):
            visualise_board()
            print(i)


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        p, v = line.strip().split()
        p, v = p.replace("p=", ""), v.replace("v=", "")
        px, py, vx, vy = map(int, p.split(",") + v.split(","))

        input.append(Robot(Point(px, py), Point(vx, vy)))

    main(input)
