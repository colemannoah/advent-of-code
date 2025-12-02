from collections import defaultdict
import sys


def main(input: list[int]) -> None:
    def calculate(num: int) -> int:
        num = ((num << 6) ^ num) % 16777216
        num = ((num >> 5) ^ num) % 16777216
        num = ((num << 11) ^ num) % 16777216

        return num

    ranges: dict[str, list[int]] = defaultdict(list)

    for num in input:
        secret, visited, diffs = num, set(), []

        for _ in range(2_000):
            next_s = calculate(secret)
            diffs.append((next_s % 10) - (secret % 10))
            secret = next_s

            if len(diffs) == 4:
                key = ",".join(map(str, diffs))

                if key not in visited:
                    ranges[key].append(next_s % 10)
                    visited.add(key)

                diffs.pop(0)

    result = max(sum(vals) for vals in ranges.values())

    print(result)


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(int(line.strip()))

    main(input)
