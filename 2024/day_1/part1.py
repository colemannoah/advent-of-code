import sys


def main(left: list[int], right: list[int]) -> None:
    left.sort()
    right.sort()

    distance = 0

    for l_n, r_n in zip(left, right):
        distance += abs(l_n - r_n)

    print(distance)


if __name__ == "__main__":
    left: list[int] = []
    right: list[int] = []

    for line in sys.stdin:
        row = tuple(map(int, line.strip().split()))
        left.append(row[0])
        right.append(row[1])

    main(left, right)
