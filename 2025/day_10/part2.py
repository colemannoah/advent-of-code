import re
import sys
from typing import List, Tuple
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, PULP_CBC_CMD


def main(input: List[str]) -> None:
    r_buttons = re.compile(r"\(([^)]*)\)")
    r_jolts = re.compile(r"\{([^}]*)\}")

    def _parse_machine(line: str) -> Tuple[List[List[int]], List[int]]:
        _jolts = r_jolts.search(line)
        assert _jolts is not None

        b = [int(x) for x in _jolts.group(1).split(",")]
        m = len(b)

        buttons = r_buttons.findall(line)
        n = len(buttons)

        m_A = [[0] * n for _ in range(m)]
        for j, button in enumerate(buttons):
            if button.strip():
                for t in button.split(","):
                    m_A[int(t)][j] = 1

        return m_A, b

    def _solve(m_A: List[List[int]], b: List[int]) -> int:
        m, n = len(m_A), len(m_A[0])

        model = LpProblem("joltage_factory", LpMinimize)

        x = {j: LpVariable(f"x_{j}", lowBound=0, cat="Integer") for j in range(n)}

        model += lpSum(x[j] for j in range(n))
        for i in range(m):
            model += lpSum(m_A[i][j] * x[j] for j in range(n)) == b[i]

        model.solve(PULP_CBC_CMD(msg=True))

        return sum(int(x[j].value()) for j in range(n))  # pyright: ignore[reportArgumentType]

    result = 0
    for line in input:
        if line:
            A, b = _parse_machine(line)
            result += _solve(A, b)

    print(result)


if __name__ == "__main__":
    input_data = []
    for line in sys.stdin:
        input_data.append(line.strip())
    main(input_data)
