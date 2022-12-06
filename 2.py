points = {"W": 6, "T": 3, "L": 0, "X": 1, "Y": 2, "Z": 3}

def loadData() -> list[tuple[str, str]]:
    data = []
    with open("2i.txt", "r") as f:
        for line in f:
            data.append((line[:1], line[2:3]))
    return data


def part1(data: list[tuple[str, str]]) -> int:
    sum = 0
    # A, X Rock, B, Y Paper, C,Z Scissor
    convert = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}
    for round in data:
        elf_choice = round[0]
        my_choice = round[1]
        result = winner(convert[elf_choice], convert[my_choice])
        sum += points[result] + points[my_choice]
    return sum 


def winner(elf: int, me: int) -> str:
    if (elf + 1) % 3 == me:
        return "W"
    elif elf == me:
        return "T"
    else:
        return "L"


def part2(data: list[tuple[str, str]]) -> int:
    sum = 0
    # what we should pick dependion on if we should lose, tie or win and what the elf picks
    choice = {"X": {"A": "Z", "B": "X", "C": "Y"}
            , "Y": {"A": "X", "B": "Y", "C": "Z"}
            , "Z": {"A": "Y", "B": "Z", "C": "X"}}
    outcomes = {"X": "L", "Y": "T", "Z": "W"}
    for round in data:
        elf_choice = round[0]
        my_choice = choice[round[1]][elf_choice]
        sum += points[outcomes[round[1]]] + points[my_choice]
    return sum


def main() -> None:
    data = loadData()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()