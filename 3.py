def loadData() -> list[str]:
    data = []
    with open("3i.txt", "r") as f:
        for line in f:
            data.append(line.strip())
    return data


def prioritie(char: str) -> int:
    if char.isupper():
        return 27 + ord(char) - 65
    return ord(char) - 96


def part1(data: list[str]) -> int:
    sum = 0
    for rucksack in data:
        compartment1 = rucksack[:len(rucksack) // 2]
        compartment2 = rucksack[len(rucksack) // 2:]
        # & is intersection operator for sets 
        sameChar = set(compartment1) & set(compartment2)
        # loop or just call prioritie(*sameChar) to unpack, but this breaks if there are multiple characters in sameChars I do believe
        sum += prioritie(*sameChar)
    return sum


def part2(data: list[str]) -> int:
    sum = 0
    for i in range(0, len(data) - 2, 3):
        sack1, sack2, sack3 = data[i], data[i + 1], data[i + 2]
        sameChar = set(sack1) & set(sack2) & set(sack3)
        sum += prioritie(*sameChar)
    return sum


def main() -> None:
    data = loadData()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()