from functools import cache
from itertools import permutations
import sys


def main(input: list[str]) -> None:
    keypad = ["789", "456", "123", "#0A"]
    moves = ["#^A", "<v>"]
    deltas = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}

    num_pad = {
        k: (x, y)
        for y, line in enumerate(keypad)
        for x, k in enumerate(line)
        if k != "#"
    }

    moves_pad = {
        k: (x, y)
        for y, line in enumerate(moves)
        for x, k in enumerate(line)
        if k != "#"
    }

    @cache
    def generate_presses(
        seq: list[tuple[int, int]],
        depth: int = 2,
        dirkey: bool = False,
        current: tuple[int, int] = None,
    ) -> int:
        keypad = moves_pad if dirkey else num_pad

        if not seq:
            return 0
        if not current:
            current = keypad["A"]

        cx, cy = current
        px, py = keypad[seq[0]]
        dx, dy = px - cx, py - cy

        buttons = ">" * dx + "<" * -dx + "v" * dy + "^" * -dy

        if depth:
            permutation_lens = []
            for perm in set(permutations(buttons)):
                cx, cy = current

                for button in perm:
                    dx, dy = deltas[button]
                    cx, cy = cx + dx, cy + dy

                    if (cx, cy) not in keypad.values():
                        break
                else:
                    permutation_lens.append(
                        generate_presses(perm + ("A",), depth - 1, True)
                    )
            min_len = min(permutation_lens)
        else:
            min_len = len(buttons) + 1

        return min_len + generate_presses(seq[1:], depth, dirkey, (px, py))

    result = 0

    for code in input:
        number = int(code[:-1])
        result += number * generate_presses(code)

    print(result)


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(line.strip())

    main(input)
