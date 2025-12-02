from dataclasses import dataclass
import sys


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def to_tuple(self) -> tuple[int, int]:
        return self.x, self.y


def main(grid: list[list[str]], moves: list[list[str]]) -> None:
    def find_start() -> Point:
        for i, row in enumerate(grid):
            if "@" in row:
                return Point(i, row.index("@"))

    def move(sx: int, sy: int, dx: int, dy: int) -> tuple[int, int]:
        stack, path, visited = [], [(sx, sy)], set()

        while path:
            x, y = path.pop()
            if (x, y) in visited or grid[x][y] == ".":
                continue

            visited.add((x, y))
            if grid[x][y] == "#":
                return Point(sx, sy).to_tuple()

            stack.append(((grid[x][y], x, y)))
            path.append((x + dx, y + dy))

            if grid[x][y] == "[":
                path.append((x, y + 1))
            if grid[x][y] == "]":
                path.append((x, y - 1))

        if dx > 0:
            stack.sort(key=lambda path: path[1])
        if dx < 0:
            stack.sort(key=lambda path: -path[1])

        if dy > 0:
            stack.sort(key=lambda path: path[2])
        if dy < 0:
            stack.sort(key=lambda path: -path[2])

        while stack:
            c, x, y = stack.pop()
            grid[x + dx][y + dy] = c
            grid[x][y] = "."

        return Point(sx + dx, sy + dy).to_tuple()

    deltas = {"v": (1, 0), "^": (-1, 0), ">": (0, 1), "<": (0, -1)}
    x, y = find_start().to_tuple()

    for move_l in moves:
        for m in move_l:
            dx, dy = deltas[m]
            x, y = move(x, y, dx, dy)

    coord_sum = 0
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            if col in {"[", "O"}:
                coord_sum += 100 * x + y

    print("\n".join("".join(cell for cell in row) for row in grid))
    print(coord_sum)


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(line.strip())

    grid, moves = input[: input.index("")], input[input.index("") + 1 :]
    grid, moves = [list(row) for row in grid], [list(move) for move in moves]

    main(grid, moves)
