import re
import sys


def main(input: str) -> None:
    pairs = [(a, b) for a, b in [p.split("-") for p in input.split(",")]]
    regex = re.compile(r"^(\d+)\1+$")

    result = 0

    for pair in pairs:
        a, b = pair

        for j in range(int(a), int(b) + 1):
            if regex.findall(str(j)):
                result += j

    print(result)


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(line.strip())

    main(input[0])
