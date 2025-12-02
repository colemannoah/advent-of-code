import sys


def main(input: list[str]) -> None:
    start = 50
    count = 0

    for line in input:
        chars = list(line)
        increasing = 1 if "R" in chars else -1
        value = int(line[1:])

        start = (start + (increasing * value)) % 100

        if start == 0:
            count += 1

    print(count)


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(line.strip())

    main(input)
