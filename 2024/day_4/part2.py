from pprint import pprint
import sys


def main(input: list[list[str]]) -> None:
    rows, cols = len(input), len(input[0])

    pprint(input)

    deltas = [
        (-1, 1),
        (1, 1),
        (-1, -1),
        (1, -1),
    ]

    def valid(x: int, y: int) -> bool:
        return 0 <= x < rows and 0 <= y < cols

    def search(x: int, y: int) -> bool:
        top_left, top_right, bot_left, bot_right = deltas

        if not valid(x + top_left[0], y + top_left[1]) or not valid(
            x + bot_right[0], y + bot_right[1]
        ):
            return False

        diag_a = f"{input[x + top_left[0]][y + top_left[1]]}A{input[x + bot_right[0]][y + bot_right[1]]}"
        diag_b = f"{input[x + top_right[0]][y + top_right[1]]}A{input[x + bot_left[0]][y + bot_left[1]]}"

        if diag_a in ["MAS", "SAM"] and diag_b in ["MAS", "SAM"]:
            return True

    count = 0

    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            if input[x][y] == "A":
                if search(x, y):
                    print(x, y)
                    count += 1

    print(count)


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(list(line.rstrip()))

    main(input)
