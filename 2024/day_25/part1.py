from dataclasses import dataclass
from enum import Enum
import sys


class SchematicType(Enum):
    KEY = "key"
    LOCK = "lock"


@dataclass
class Schematic:
    val: list[str]
    heights: list[int] = None
    type: SchematicType = None

    def __post_init__(self) -> None:
        if self.val[0] == ".....":
            self.type = SchematicType.KEY
        else:
            self.type = SchematicType.LOCK

    def __str__(self) -> str:
        return "\n".join(self.val)

    @property
    def columns(self) -> list[str]:
        return [
            "".join([self.val[i][j] for i in range(len(self.val))])
            for j in range(len(self.val[0]))
        ]

    @property
    def rows(self) -> list[str]:
        return self.val


def main(input: list[Schematic]) -> None:
    for schematic in input:
        height = []
        for col in schematic.columns:
            count = col.count("#") - 1
            height.append(count)
        schematic.heights = height

    keys, locks = (
        [sch for sch in input if sch.type == SchematicType.KEY],
        [sch for sch in input if sch.type == SchematicType.LOCK],
    )

    fits = 0

    for key in keys:
        for lock in locks:
            added = [sum(x) for x in zip(key.heights, lock.heights)]
            does_fit = all([x < 6 for x in added])

            if does_fit:
                fits += 1

            print(added, does_fit)

    print(fits)


if __name__ == "__main__":
    schematics: list[Schematic] = []

    val = []
    for line in sys.stdin:
        if line == "\n":
            schematics.append(Schematic(val))
            val = []
        else:
            val.append(line.strip())

    main(schematics)
