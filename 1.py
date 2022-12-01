def loadData() -> list[int]:
    data = []
    with open("i.txt", "r") as f:
        calories = 0
        for line in f:
            if line != '\n':
                calories += int(line.strip())
            else:
                data.append(calories)
                calories = 0
    return data


def part1(data: list[int]) -> int:
    return max(data)


def part2(data: list[int]) -> int:
    sum = 0
    for i in range(3):
        m = max(data)
        sum += m
        data.remove(m)
    return sum


def main() -> None:
    data = loadData()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()




# using a maxheap instead heapq implementation is a minheap so we multiply a num with -1 to make it so 500 -> -500 so it counts as the max as -500 < -400 while 400 < 500
from heapq import heappop, heappush, heapify

def loadDataOther() -> list[int]:
    data = []
    heapify(data)
    with open("i.txt", "r") as f:
        calories = 0
        for line in f:
            if line != '\n':
                calories += int(line.strip())
            else:
                heappush(data, -1 * calories)
                calories = 0
    return data


def part1Other(data: list[int]) -> int:
    # poping means we lose the max for the next part, to fix reread the data or just look using index to not lose it
    # return -1 * heappop(data)
    return -1 * data[0]


def part2Other(data: list[int]) -> int:
    sum = 0
    for i in range(3):
        sum += heappop(data)
    return -1 * sum


def mainOther() -> None:
    data = loadDataOther()
    print(part1Other(data))
    print(part2Other(data))

