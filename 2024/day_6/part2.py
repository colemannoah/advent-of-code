import sys

WALL, GUARD, VOID = "#", "^", "."
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def main(input: list[list[str]]) -> None:
    def get_guard_coords(input: list[str]) -> tuple[int, int]:
        for i, row in enumerate(input):
            for j, val in enumerate(row):
                if val == GUARD:
                    return i, j

        return -1, -1

    def check_loop(curr_dir: int, obstacle: tuple[int, int], input: list[str]) -> bool:
        n, m = len(input), len(input[0])

        oi, oj = obstacle
        di, dj = DIR[curr_dir]
        i, j = oi - di, oj - dj

        input[oi][oj] = WALL
        visited = set()

        while 0 <= i < n and 0 <= j < m:
            if (i, j, curr_dir) in visited:
                input[oi][oj] = VOID
                return True

            visited.add((i, j, curr_dir))

            ni, nj = i + di, j + dj
            if not (0 <= ni < n and 0 <= nj < m):
                break

            while input[ni][nj] == WALL:
                curr_dir = (curr_dir + 1) % len(DIR)
                di, dj = DIR[curr_dir]
                ni, nj = i + di, j + dj

            i, j = ni, nj

        input[oi][oj] = VOID
        return False

    rows, cols = len(input), len(input[0])
    i, j = get_guard_coords(input)

    curr_dir = 0
    di, dj = DIR[0]
    visited = set()
    obstacles_that_make_loops = 0
    while 0 <= i < rows and 0 <= j < cols:
        visited.add((i, j))

        ni, nj = i + di, j + dj
        if not (0 <= ni < rows and 0 <= nj < cols):
            break

        while input[ni][nj] == WALL:
            curr_dir = (curr_dir + 1) % len(DIR)
            di, dj = DIR[curr_dir]
            ni, nj = i + di, j + dj

        if (ni, nj) not in visited and check_loop(curr_dir, (ni, nj), input):
            obstacles_that_make_loops += 1

        i, j = ni, nj

    print(obstacles_that_make_loops)


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(list(line.strip()))

    main(input)
