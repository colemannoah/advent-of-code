import sys


def main(input: list[list[str]]) -> None:
    rows, cols = len(input), len(input[0])

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_index = 0

    for r in range(rows):
        for c in range(cols):
            if input[r][c] in "^>v<":
                guard_pos = (r, c)
                dir_index = "^>v<".index(input[r][c])
                input[r][c] = "."
                break

    visited = set()
    visited.add(guard_pos)

    while True:
        next_r = guard_pos[0] + directions[dir_index][0]
        next_c = guard_pos[1] + directions[dir_index][1]

        if not (0 <= next_r < rows and 0 <= next_c < cols):
            break

        if input[next_r][next_c] == "#":
            dir_index = (dir_index + 1) % 4
        else:
            guard_pos = (next_r, next_c)
            visited.add(guard_pos)

    print(len(visited))


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(list(line.strip()))

    main(input)
