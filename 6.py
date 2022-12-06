def loadData() -> str:
    with open("6i.txt", "r") as f:
        return f.readline()


def part1(data: str) -> int:
    for i in range(len(data) - 3):
        s = set(data[i:i+4])
        if len(s) == 4:
            # i is index of the first character in the four character sequence and we want index of the last character
            return i + 4


def part2(data: str) -> int:
    for i in range(len(data) - 13):
        s = set(data[i:i+14])
        if len(s) == 14:
            # same thing but sequence is 14 long
            return i + 14


def main() -> None:
    data = loadData()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()