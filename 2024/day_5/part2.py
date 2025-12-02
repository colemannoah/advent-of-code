from functools import cmp_to_key
import sys


def main(rules: list[tuple[int]], updates: list[list[int]]) -> None:
    def in_order(update: list[int]):
        relevant_rules = [(a, b) for a, b in rules if a in update and b in update]

        for a, b in relevant_rules:
            a_i = update.index(a)
            b_i = update.index(b)

            if b_i < a_i:
                return False
        return True

    def sort_incorrect(update: list[int]):
        corrected = update.copy()

        def comparator(a: int, b: int):
            for before, after in rules:
                if before == a and after == b:
                    return -1
                elif before == b and after == a:
                    return 1
            return 0

        corrected.sort(key=cmp_to_key(comparator))

        return corrected

    middles = []

    for update in updates:
        if not in_order(update):
            corrected = sort_incorrect(update)

            middle = len(corrected) // 2
            middles.append(corrected[middle])

    print(sum(middles))


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(line.rstrip())

    s_rules, s_updates = input[: input.index("")], input[input.index("") + 1 :]
    rules = [tuple(map(int, rule.split("|"))) for rule in s_rules]
    updates = [list(map(int, update.split(","))) for update in s_updates]

    main(rules, updates)
