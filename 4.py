def loadData() -> list[tuple[str, str]]:
    data = []
    with open("4i.txt", "r") as f:
        for line in f:
            data.append(line.strip().split(","))
    return data


def part1(data: list[tuple[str, str]]) -> int:
    sum = 0
    for elf1, elf2 in data:
        elf1_start_stop = elf1.split("-")
        elf2_start_stop = elf2.split("-")
        sum += contains(elf1_start_stop, elf2_start_stop)
    return sum


def contains(elf1: tuple[str, str], elf2: tuple[str, str]) -> int:
    elf1_range = set(range(int(elf1[0]), int(elf1[1]) + 1))
    elf2_range = set(range(int(elf2[0]), int(elf2[1]) + 1))
    intersection = elf1_range & elf2_range
    if intersection == elf1_range or intersection == elf2_range:
        return 1
    return 0


def part2(data: list[tuple[str, str]]) -> int:
    sum = 0
    for elf1, elf2 in data:
        elf1_start_stop = elf1.split("-")
        elf2_start_stop = elf2.split("-")
        sum += overlap(elf1_start_stop, elf2_start_stop)
    return sum


def overlap(elf1: tuple[str, str], elf2: tuple[str, str]) -> int:
    elf1_range = set(range(int(elf1[0]), int(elf1[1]) + 1))
    elf2_range = set(range(int(elf2[0]), int(elf2[1]) + 1))
    if len(elf1_range & elf2_range) != 0:
        return 1
    return 0


def main() -> None:
    data = loadData()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()


# some code snippets 
# this was the first attempt and works fine but is maybe a bit worse then the other one
def old_contains(elf1: tuple[str, str], elf2: tuple[str, str]) -> int:
    # is elf2 contained withing elf1
    if int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):
        return 1
    # is elf1 contained within elf2
    if int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1]):
        return 1
    return 0

# this was the first attempt and works fine but is maybe a bit worse then the other one
def old_overlap(elf1: tuple[str, str], elf2: tuple[str, str]) -> int:
    elf1_range = list(range(int(elf1[0]), int(elf1[1]) + 1))
    elf2_range = list(range(int(elf2[0]), int(elf2[1]) + 1))
    if int(elf1[0]) in elf2_range or int(elf1[1]) in elf2_range:
        return 1
    if int(elf2[0]) in elf1_range or int(elf2[1]) in elf1_range:
        return 1
    return 0 
