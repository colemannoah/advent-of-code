import sys


def main(input: list[int]) -> None:
    id_map: dict[int, tuple[int, int]] = {}
    spaces_map: dict[int, int] = {}

    i, j, id = 0, 0, 0

    while i < len(input):
        a, b = i, i + 1

        if a < len(input):
            id_map[id] = (input[a], j)
            j += input[a]

        if b < len(input):
            if input[b] > 0:
                spaces_map[j] = input[b]

            j += input[b]

        id += 1
        i += 2

    for k, v in reversed(id_map.items()):
        size = v[0]

        for position, space in sorted(spaces_map.items()):
            if position >= v[1]:
                break

            if space >= size:
                id_map[k] = (id_map[k][0], position)

                if space - size > 0:
                    spaces_map[position + size] = space - size

                spaces_map.pop(position)
                break

    result = 0

    for k, v in id_map.items():
        n, pos = v[0], v[1]
        result += k * (n * pos + n * (n - 1) // 2)

    print(result)


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(list(line.strip()))

    input = [int(x) for x in input[0]]

    main(input)
