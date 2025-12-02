import sys


def main(input: list[list[str]]) -> None:
    n, m = len(input), len(input[0])

    graph: dict[complex, str] = {
        i + j * 1j: c for i, r in enumerate(input) for j, c in enumerate(r)
    }

    for i in range(-1, n + 1):
        graph[i - 1 * 1j] = graph[i + m * 1j] = "#"

    for j in range(-1, m + 1):
        graph[-1 + j * 1j] = graph[n + j * 1j] = "#"

    visited = set()

    def dfs(node: complex, color: str, dir: complex) -> tuple[int, int]:
        if graph[node] != color:
            if graph[node + dir * 1j] == color or graph[node - dir + dir * 1j] != color:
                return 0, 1
            else:
                return 0, 1

        if node in visited:
            return 0, 0
        visited.add(node)

        area, perim = 1, 0
        for d in (1, -1, 1j, -1j):
            a, p = dfs(node + d, color, d)
            area, perim = area + a, perim + p

        return area, perim

    result_part1 = 0
    for node in graph:
        if node not in visited and graph[node] != "#":
            area, perimeter = dfs(node, graph[node], 1)
            result_part1 += area * perimeter

    print(result_part1)


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(list(line.strip()))

    main(input)
