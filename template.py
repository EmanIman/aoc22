def loadData() -> list[str]:
    data = []
    with open("i.txt", "r") as f:
        for line in f:
            data.append(line)
    return data


def part1(data: list[str]) -> int:
    return 0


def part2(data: list[str]) -> int:
    return 0


def main() -> None:
    data = loadData()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()