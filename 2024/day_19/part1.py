import sys


def main(patterns: list[str], designs: list[str]) -> None:
    def possibilities(target: str) -> int:
        n = len(target)
        lengths = {len(p) for p in patterns}

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            for lengt in lengths:
                if i >= lengt and target[i - lengt : i] in patterns:
                    dp[i] += dp[i - lengt]

        return dp[n]

    possible = 0
    for design in designs:
        poss = possibilities(design)
        possible += 1 if poss != 0 else 0

    print(possible)


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(line.strip())

    split = input.index("")
    patterns, designs = input[:split][0].split(", "), input[split + 1 :]

    main(patterns, designs)
