import sys
import re


def main(input: str) -> None:
    def multiply(term: str) -> int:
        x, y = term.replace("mul(", "").replace(")", "").split(",")
        return int(x) * int(y)

    regex = r"(?:mul\(\d+,\d+\)|don't\(\)|do\(\))"
    instructions = re.findall(regex, input)
    sum = 0

    flag = True
    for instruction in instructions:
        match instruction:
            case "don't()":
                flag = False
            case "do()":
                flag = True
            case _:
                if flag:
                    sum += multiply(instruction)

    print(sum)


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(line.rstrip())

    flatten = "".join(input)

    main(flatten)
