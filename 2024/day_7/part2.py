from itertools import product
from operator import add, mul
from dataclasses import dataclass
import sys


@dataclass
class Equation:
    result: int
    terms: list[int]


def main(input: list[Equation]) -> None:
    tot = 0

    for eq in input:
        for operator in product(
            [add, mul, lambda a, b: int(str(a) + str(b))], repeat=len(eq.terms) - 1
        ):
            result = eq.terms[0]

            for op, term in zip(operator, eq.terms[1:]):
                result = op(result, term)

            if result == eq.result:
                tot += result
                break

    print(tot)


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        split = line.strip().split()
        result = int(split[0].replace(":", ""))
        terms = list(map(int, split[1:]))
        input.append(Equation(result, terms))

    main(input)
