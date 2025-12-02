import sys


def main(input: list[str]) -> None:
    start = 50
    count = 0

    prev_turn = "R"

    for line in input:
        direction = line[0]
        value = int(line[1:])

        if direction != prev_turn:
            start, prev_turn = 100 - start, direction

        start = (start % 100) + value

        count += start // 100

    print(count)


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(line.strip())

    main(input)
