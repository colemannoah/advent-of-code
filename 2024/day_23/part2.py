from collections import defaultdict
from itertools import combinations
from pprint import pprint
import sys


def main(input: list[list[str]]) -> None:
    connections: dict[str, list[str]] = defaultdict(list)

    for s, e in input:
        connections[s].append(e)
        connections[e].append(s)

    pprint(connections)

    weighted: list[tuple[str, int]] = []

    for computer in connections.keys():
        total = 0

        for a, b in combinations(connections[computer], 2):
            if b in connections[a]:
                total += 1

        weighted.append((computer, total))

    output: list[str] = []
    for computer in weighted:
        c, total = computer

        if total == 66:
            output.append(c)

    output.sort()

    print(",".join(output))


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(tuple(line.strip().split("-")))

    main(input)
