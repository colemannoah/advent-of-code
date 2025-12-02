import sys


def main(input: list[list[int]]) -> None:
    def find_trailheads() -> list[tuple[int, int]]:
        trailheads = set()
        for row in range(len(input)):
            for col in range(len(input[0])):
                if input[row][col] == 0:
                    trailheads.add((row, col))
        return trailheads

    def count_reachable_peaks(trailhead: tuple[int, int]) -> int:
        rows, cols = len(input), len(input[0])
        peaks: set[tuple[int, int]] = set()

        def dfs(row: int, col: int, current_height: int) -> int:
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or input[row][col] != current_height
            ):
                return 0

            if input[row][col] == 9:
                peaks.add((row, col))
                return 1
            else:
                return (
                    dfs(row - 1, col, current_height + 1)
                    + dfs(row + 1, col, current_height + 1)
                    + dfs(row, col - 1, current_height + 1)
                    + dfs(row, col + 1, current_height + 1)
                )

        return dfs(trailhead[0], trailhead[1], 0)

    trailheads = find_trailheads()
    result = 0

    for trailhead in trailheads:
        paths = count_reachable_peaks(trailhead)
        result += paths

    print(result)


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(list(map(int, list(line.strip()))))

    main(input)
