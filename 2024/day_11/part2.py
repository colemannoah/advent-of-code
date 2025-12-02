import sys


def main(input: list[int]) -> None:
    table: dict[tuple[int, int], int] = {}

    def solve(v: int, blinks: int) -> int:
        if (v, blinks) in table:
            return table[(v, blinks)]

        if blinks == 0:
            sol = 1
        elif v == 0:
            sol = solve(1, blinks - 1)
        elif len(str(v)) % 2 == 0:
            d = str(v)
            left, right = int(d[: len(d) // 2]), int(d[len(d) // 2 :])

            sol = solve(left, blinks - 1) + solve(right, blinks - 1)
        else:
            sol = solve(v * 2024, blinks - 1)

        table[(v, blinks)] = sol
        return sol

    blinks = 75
    solution = sum(solve(v, blinks) for v in input)
    print(solution)


if __name__ == "__main__":
    input_data = []
    for line in sys.stdin:
        input_data.extend(map(int, line.strip().split()))

    main(input_data)
