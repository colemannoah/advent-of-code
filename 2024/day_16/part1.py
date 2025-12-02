from queue import PriorityQueue
import sys
from typing import Any
import numpy as np


def main(grid: np.ndarray[Any], start: tuple[int, int], end: tuple[int, int]) -> None:
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    q = PriorityQueue()
    q.put((0, start, 0))

    visited = set()

    while True:
        pos = q.get()
        score, p, d = pos
        visited.add((p, d))

        for i in [0, -1, 1, 2]:
            d_new = (d + i) % 4
            dr, dc = deltas[d_new]

            r, c = p
            r_n, c_n = r + dr, c + dc

            if grid[r_n][c_n] == 1:
                continue

            if ((r_n, c_n), d_new) in visited:
                continue

            score_new = score + abs(i) * 1000 + 1
            if (r_n, c_n) == end:
                print(score_new)
                return
            else:
                q.put((score_new, (r_n, c_n), d_new))


if __name__ == "__main__":
    lines = []
    for line in sys.stdin:
        lines.append(line)

    grid = np.zeros((len(lines), len(lines[0]) - 1), dtype=int)
    for row, line in enumerate(lines):
        for col, c in enumerate(line.strip()):
            if c == "#":
                grid[row][col] = 1
            if c == "S":
                start = (row, col)
            if c == "E":
                end = (row, col)

    main(grid, start, end)
