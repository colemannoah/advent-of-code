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

    total, doubles, triples = 0, 0, 0

    for computer in connections.keys():
        if computer[0] != "t":
            continue

        for a, b in combinations(connections[computer], 2):
            if a in connections[b]:
                if a[0] == "t":
                    if b[0] == "t":
                        triples += 1
                    else:
                        doubles += 1
                else:
                    if b[0] == "t":
                        doubles += 1

                total += 1

    result = total - doubles // 2 - 2 * triples // 3
    print(result)


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(tuple(line.strip().split("-")))

    main(input)
