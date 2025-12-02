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

        def dfs(row: int, col: int, current_height: int) -> None:
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or input[row][col] != current_height
            ):
                return

            if input[row][col] == 9:
                peaks.add((row, col))
                return
            else:
                deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in deltas:
                    next_r, next_c = row + dr, col + dc

                    if (
                        0 <= next_r < rows
                        and 0 <= next_c < cols
                        and input[next_r][next_c] == current_height + 1
                    ):
                        dfs(next_r, next_c, input[next_r][next_c])

        dfs(trailhead[0], trailhead[1], 0)

        return len(peaks)

    trailheads = find_trailheads()
    scores = [count_reachable_peaks(trailhead) for trailhead in trailheads]

    print(sum(scores))


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(list(map(int, list(line.strip()))))

    main(input)
