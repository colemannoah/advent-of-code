import sys


def main(input: list[list[str]]) -> None:
    word = "XMAS"
    rows, cols = len(input), len(input[0])
    word_len = len(word)

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ]

    first_letter_positions = [
        (x, y) for x in range(rows) for y in range(cols) if input[x][y] == word[0]
    ]

    def can_fit(x, y, dx, dy):
        end_x = x + dx * (word_len - 1)
        end_y = y + dy * (word_len - 1)
        return 0 <= end_x < rows and 0 <= end_y < cols

    occurrences = 0

    for x, y in first_letter_positions:
        for dx, dy in directions:
            if can_fit(x, y, dx, dy):
                match = True

                for i in range(1, word_len):
                    nx, ny = x + i * dx, y + i * dy

                    if input[nx][ny] != word[i]:
                        match = False
                        break

                if match:
                    occurrences += 1

    print(occurrences)


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(list(line.rstrip()))

    main(input)
