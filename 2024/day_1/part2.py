import sys


def main(left: list[int], right: list[int]) -> None:
    similarity = 0

    for n in left:
        count = right.count(n)
        similarity += n * count

    print(similarity)


if __name__ == "__main__":
    left: list[int] = []
    right: list[int] = []

    for line in sys.stdin:
        row = tuple(map(int, line.strip().split()))
        left.append(row[0])
        right.append(row[1])

    main(left, right)
