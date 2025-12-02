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
    time_steps = 100

    for _ in range(time_steps):
        for robot in input:
            robot.move()

    quadrants = [0, 0, 0, 0]
    width, height = 101, 103

    for robot in input:
        if robot.position.x == width // 2 or robot.position.y == height // 2:
            continue

        if robot.position.x < width // 2 and robot.position.y < height // 2:
            quadrants[0] += 1
        elif robot.position.x > width // 2 and robot.position.y < height // 2:
            quadrants[1] += 1
        elif robot.position.x < width // 2 and robot.position.y > height // 2:
            quadrants[2] += 1
        elif robot.position.x > width // 2 and robot.position.y > height // 2:
            quadrants[3] += 1

    print(quadrants)

    result = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
    print(result)


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        p, v = line.strip().split()
        p, v = p.replace("p=", ""), v.replace("v=", "")
        px, py, vx, vy = map(int, p.split(",") + v.split(","))

        input.append(Robot(Point(px, py), Point(vx, vy)))

    main(input)
