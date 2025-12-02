import sys


def main(input: list[int]) -> None:
    disk_map = []
    for i, r in enumerate(input):
        if i % 2 == 0:
            for _ in range(r):
                disk_map.append(f"{i // 2}")
        else:
            for _ in range(r):
                disk_map.append(".")

    left, right = 0, len(disk_map) - 1

    while left < right:
        while disk_map[left] != ".":
            left += 1
        while disk_map[right] == ".":
            right -= 1

        disk_map[left] = disk_map[right]
        disk_map[right] = "."

        left += 1
        right -= 1

    nums = [int(x) for x in disk_map if x != "."]
    result = sum(i * c for i, c in enumerate(nums))

    print("".join(disk_map), result)


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(list(line.strip()))

    input = [int(x) for x in input[0]]

    main(input)
