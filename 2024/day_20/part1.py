from itertools import product
import sys
from typing import Generator


def main(input: list[str]) -> None:
    n, m = len(input), len(input[0])
    grid = {}

    def parse() -> tuple[tuple[int, int], tuple[int, int], tuple[int, int]]:
        for x, y in product(range(n), range(m)):
            grid[(x, y)] = input[y][x]

            if input[y][x] == "S":
                start = (x, y)
            if input[y][x] == "E":
                end = (x, y)

        return grid, start, end

    def get_circle_manhattan(
        position: tuple[int, int], radius: int
    ) -> Generator[tuple[int, int]]:
        s = set()

        for i in range(radius + 1):
            x, y = (i, radius - i)
            s.update([(x, y), (-x, -y), (x, -y), (-x, y)])

        for dist in s:
            yield tuple(x + y for x, y in zip(position, dist))

    def bfs(
        grid: dict[tuple[int, int]], start: tuple[int, int], end: tuple[int, int]
    ) -> list[tuple[int, int]]:
        queue = [[start]]
        visited = set([start])

        for path in queue:
            node = path[-1]

            if node == end:
                break

            for neighbor in filter(
                lambda n: n not in visited and grid[n] != "#",
                get_circle_manhattan(node, 1),
            ):
                visited.add(neighbor)
                queue.append(list([*path, neighbor]))

        return path

    grid, start, end = parse()
    paths = bfs(grid, start, end)
    path = {pos: i for i, pos in enumerate(paths)}

    result = 0
    for i, pos in enumerate(paths):
        result += sum(
            n in path and path[n] - i - 2 >= 100 for n in get_circle_manhattan(pos, 2)
        )

    print(result)


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(line.strip())

    main(input)
