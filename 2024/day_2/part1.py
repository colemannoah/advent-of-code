from pprint import pprint
import sys


def main(input: list[list[int]]) -> None:
    def strictly_increasing(lst: list[int]) -> bool:
        return all(x < y for x, y in zip(lst, lst[1:]))

    def strictly_decreasing(lst: list[int]) -> bool:
        return all(x > y for x, y in zip(lst, lst[1:]))

    def is_valid(lst: list[int]) -> bool:
        if not strictly_increasing(lst) and not strictly_decreasing(lst):
            return False

        for i in range(1, len(lst)):
            diff = abs(lst[i] - lst[i - 1])
            valid = diff >= 1 and diff <= 3
            if not valid:
                return False
        return True

    def can_be_made_valid_by_removing_one(lst: list[int]) -> bool:
        for i in range(len(lst)):
            new_lst = lst[:i] + lst[i + 1 :]
            if is_valid(new_lst):
                return True
        return False

    safe = 0

    for report in input:
        # if (not strictly_increasing(report)) and (not strictly_decreasing(report)):
        #     continue

        if is_valid(report) or can_be_made_valid_by_removing_one(report):
            safe += 1

    pprint(safe)


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(list(map(int, line.strip().split())))

    main(input)
