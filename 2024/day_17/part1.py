from dataclasses import dataclass
from enum import Enum
import sys


@dataclass
class Register:
    value: int


@dataclass
class Program:
    instructions: list["Instruction"]


class OPCode(Enum):
    ADV = 0
    BXL = 1
    BST = 2
    JNZ = 3
    BXC = 4
    OUT = 5
    BDV = 6
    CDV = 7


@dataclass
class Instruction:
    opcode: int
    operand: int

    def combo(self, registers: list[Register]) -> int:
        match self.operand:
            case 0 | 1 | 2 | 3:
                return self.operand
            case 4:
                return registers[0].value
            case 5:
                return registers[1].value
            case 6:
                return registers[2].value
            case _:
                raise ValueError(f"Invalid operand: {self.operand}")


def main(registers: list[Register], program: Program) -> None:
    out = []
    pointer = 0

    while pointer < len(program.instructions):
        instruction = program.instructions[pointer]

        match OPCode(instruction.opcode):
            case OPCode.ADV | OPCode.BDV | OPCode.CDV:
                target = None

                match OPCode(instruction.opcode):
                    case OPCode.ADV:
                        target = 0
                    case OPCode.BDV:
                        target = 1
                    case OPCode.CDV:
                        target = 2

                registers[target].value = registers[0].value >> instruction.combo(
                    registers
                )

            case OPCode.BXL:
                registers[1].value = registers[1].value ^ instruction.operand

            case OPCode.BST:
                registers[1].value = instruction.combo(registers) % 8

            case OPCode.JNZ:
                if registers[0].value != 0:
                    pointer = instruction.operand
                    continue

            case OPCode.BXC:
                registers[1].value = registers[1].value ^ registers[2].value

            case OPCode.OUT:
                out.append(instruction.combo(registers) % 8)

            case _:
                raise ValueError(f"Invalid opcode: {instruction.opcode}")

        pointer += 1

    print(registers, program)
    print(",".join(map(str, out)))


if __name__ == "__main__":
    registers: list[Register] = []
    program: Program = None

    for line in sys.stdin:
        if line.startswith("Register"):
            parts = line.split(": ")
            register_name = parts[0].split(" ")[1]
            register_value = int(parts[1])
            registers.append(Register(value=register_value))
        elif line.startswith("Program"):
            parts = line.split(": ")

            instructions = list(map(int, parts[1].split(",")))
            instructions = [
                Instruction(opcode=instructions[i], operand=instructions[i + 1])
                for i in range(0, len(instructions), 2)
            ]

            program = Program(instructions=instructions)

    main(registers, program)
