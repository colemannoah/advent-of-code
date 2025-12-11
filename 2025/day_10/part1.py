import re
import sys
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, PULP_CBC_CMD


def main(input: list[str]) -> None:
    r_lights = re.compile(r"\[([.#]+)\]")
    r_buttons = re.compile(r"\(([^)]*)\)")

    def _parse_machine(line: str) -> tuple[list[list[int]], list[int]]:
        _lights = r_lights.search(line)
        assert _lights is not None

        lights = _lights.group(1)

        b = [1 if c == "#" else 0 for c in lights]
        m = len(b)

        buttons = r_buttons.findall(line)
        n = len(buttons)

        m_A = [[0] * n for _ in range(m)]

        for j, button in enumerate(buttons):
            if button.strip():
                for t in button.split(","):
                    m_A[int(t)][j] = 1

        return m_A, b

    def _solve(m_A: list[list[int]], b: list[int]) -> int:
        m, n = len(m_A), len(m_A[0])

        model = LpProblem("le_factory", LpMinimize)

        x = {
            j: LpVariable(f"x_{j}", cat="Binary", lowBound=0, upBound=1)
            for j in range(n)
        }

        y = {i: LpVariable(f"y_{i}", cat="Integer") for i in range(m)}

        model += lpSum(x[j] for j in range(n))
        for i in range(m):
            model += lpSum(m_A[i][j] * x[j] for j in range(n)) - 2 * y[i] == b[i]

        model.solve(PULP_CBC_CMD(msg=True))

        return sum(int(x[j].value()) for j in range(n))  # pyright: ignore[reportArgumentType]

    result = 0

    for line in input:
        A, b = _parse_machine(line)
        result += _solve(A, b)

    print(result)


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(line.strip())

    main(input)
