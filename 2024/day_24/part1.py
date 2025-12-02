from dataclasses import dataclass
import sys


@dataclass
class Instruction:
    id: int
    op_a: str
    op_b: str
    action: callable
    result: str


def main(wire_values: dict[str, int], instructions: list[Instruction]) -> None:
    seen: set[int] = set()

    while len(seen) < len(instructions):
        for instruction in instructions:
            if instruction.id in seen:
                continue

            try:
                a = (
                    instruction.op_a
                    if instruction.op_a.isnumeric()
                    else wire_values[instruction.op_a]
                )
                b = (
                    instruction.op_b
                    if instruction.op_b.isnumeric()
                    else wire_values[instruction.op_b]
                )
            except KeyError:
                continue

            wire_values[instruction.result] = instruction.action(a, b)
            seen.add(instruction.id)

    result = [(int(k[1:]), str(v)) for k, v in wire_values.items() if k.startswith("z")]
    result.sort(reverse=True)

    print(int("".join([x[1] for x in result]), 2))


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(line.strip())

    split = input.index("")
    left, right = input[:split], input[split + 1 :]

    wire_values: dict[str, int] = {}
    for line in left:
        k, v = line.split(": ")
        wire_values[k] = int(v)

    actions = {
        "AND": lambda a, b: a & b,
        "OR": lambda a, b: a | b,
        "XOR": lambda a, b: a ^ b,
    }

    instructions: list[Instruction] = []
    for i, line in enumerate(right):
        s1, s2 = line.split(" -> ")
        op_a, action, op_b = s1.split(" ")

        instruction = Instruction(i, op_a, op_b, actions[action], s2)
        instructions.append(instruction)

    main(wire_values, instructions)
