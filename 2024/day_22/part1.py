import sys


def main(input: list[int]) -> None:
    def calculate(num: int) -> int:
        num = ((num << 6) ^ num) % 16777216
        num = ((num >> 5) ^ num) % 16777216
        num = ((num << 11) ^ num) % 16777216

        return num

    result = 0

    for number in input:
        secret = number

        for _ in range(2_000):
            secret = calculate(secret)

        print(secret)
        result += secret

    print(f"\n{result}")


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(int(line.strip()))

    main(input)
