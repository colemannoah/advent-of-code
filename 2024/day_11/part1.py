import sys


def main(input: list[int]) -> None:
    def split_number(num: int) -> tuple[int, int]:
        str_num = str(num)
        mid = len(str_num) // 2
        left = int(str_num[:mid]) if mid > 0 else 0
        right = int(str_num[mid:]) if mid > 0 else num

        return left, right

    def transform(input: list[int]) -> list[int]:
        stones = []

        for original in input:
            if original == 0:
                stones.append(1)
            elif len(str(original)) % 2 == 0:
                l, r = split_number(original)
                stones.extend([l, r])
            else:
                stones.append(original * 2024)

        return stones

    result = input.copy()

    for _ in range(25):
        result = transform(result)

    print(result, len(result))


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(line.strip().split())

    input = [int(x) for x in input[0]]

    main(input)
