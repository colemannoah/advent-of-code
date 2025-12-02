from collections import deque
import sys


class Grid:
    def __init__(self, n: int, walls: list[tuple[int, int]]) -> None:
        self.n = n
        self.walls = walls
        self.start = (0, 0)
        self.end = (n - 1, n - 1)
        self.grid = [["." for _ in range(n)] for _ in range(n)]

    def bfs(self, bytes: int) -> int:
        queue = deque([self.start])
        visited = {self.start} | set(self.walls[:bytes])
        result = 0

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()

                if (x, y) == self.end:
                    return result

                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if (
                        0 <= nx < self.n
                        and 0 <= ny < self.n
                        and (nx, ny) not in visited
                    ):
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            result += 1

        return -1

    def add_walls(self, walls: list[tuple[int, int]]) -> None:
        for x, y in walls:
            self.grid[y][x] = "#"

    def _draw(self) -> str:
        s = ""
        for i in range(self.n):
            for j in range(self.n):
                if (i, j) == self.start:
                    s += "S"
                elif (i, j) == self.end:
                    s += "E"
                else:
                    s += self.grid[i][j]
            s += "\n"
        return s


def main(input: list[tuple[int, int]]) -> None:
    n = 71

    grid = Grid(n, input)
    grid.add_walls(input)
    print(grid._draw())

    for i in range(len(input) - 1):
        bfs = grid.bfs(i)

        if bfs == -1:
            print(f"No path found, {i}, {input[:i][-1]}")
            break


if __name__ == "__main__":
    input = []
    n = 6

    for line in sys.stdin:
        input.append(tuple(map(int, line.strip().split(","))))

    main(input)
