from collections import defaultdict
from itertools import combinations
import sys


def main(input: list[list[str]]) -> None:
    width, height = len(input[0]), len(input)

    antennas = defaultdict(list)
    antinodes: set[complex] = set()

    for y, row in enumerate(input):
        for x, cell in enumerate(row):
            if cell != ".":
                antennas[cell].append(complex(x, y))

    for coord in antennas.values():
        for a, b in combinations(coord, 2):
            v = a - b
            u = b - a

            antinodes.add(a + u * 2)
            antinodes.add(b + v * 2)

    print(sum(0 <= x.real < width and 0 <= x.imag < height for x in antinodes))


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(list(line.strip()))

    main(input)
