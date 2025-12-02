from collections import deque
from rich.live import Live
import sys


class Grid:
    def __init__(self, n: int, bytes: int, walls: list[tuple[int, int]]) -> None:
        self.n = n
        self.bytes = bytes
        self.walls = walls
        self.start = (0, 0)
        self.end = (n, n)
        self.grid = [["." for _ in range(n + 1)] for _ in range(n + 1)]

    def animate(self) -> None:
        with Live("", refresh_per_second=120) as live:
            queue = deque([self.start])
            visited = {self.start} | set(self.walls[: self.bytes])
            result = 0

            while queue:
                for _ in range(len(queue)):
                    x, y = queue.popleft()

                    self.grid[x][y] = "X"
                    live.update(self._draw())

                    if (x, y) == self.end:
                        print(f"Found the end! {result}\n")
                        break

                    for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                        if (
                            0 <= nx < self.n + 1
                            and 0 <= ny < self.n + 1
                            and (nx, ny) not in visited
                        ):
                            visited.add((nx, ny))
                            queue.append((nx, ny))

                result += 1

    def add_walls(self, walls: list[tuple[int, int]]) -> None:
        for x, y in walls[: self.bytes]:
            self.grid[y][x] = "#"

    def _draw(self) -> str:
        s = ""
        for i in range(self.n + 1):
            for j in range(self.n + 1):
                if (i, j) == self.start:
                    s += "S"
                elif (i, j) == self.end:
                    s += "E"
                else:
                    s += self.grid[i][j]
            s += "\n"
        return s


def main(input: list[tuple[int, int]]) -> None:
    n = 70
    bytes = 1024 + 1

    grid = Grid(n, bytes, input)
    grid.add_walls(input)
    grid.animate()


if __name__ == "__main__":
    input = []
    n = 6

    for line in sys.stdin:
        input.append(tuple(map(int, line.strip().split(","))))

    main(input)
