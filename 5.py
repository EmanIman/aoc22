from collections import deque
from re import findall

def loadData(crates: dict[str, deque]) -> list[list[str]]:
    data = []
    with open("5i.txt", "r") as f:
        reading_crates = True
        for line in f:
            if reading_crates:
                add_crates(crates, line.strip())
                if line == "\n":
                    reading_crates = False
            else:
                # finds all the numbers in a string
                data.append(findall('[0-9]+', line))
    return data


def add_crates(crates: dict[str, deque], line: str) -> None:
    i = 1
    crate_number = 1
    lenght = len(line)
    while i < lenght:
        key = f"{crate_number}"
        crate = line[i]
        # check so crate is a character an not something else like a number or blank space
        if crate.isalpha():
            crates[key] = push(crates.get(key, deque()), crate)
        crate_number += 1
        i += 4


# append returns None so we do it in a function to return the stack back into the dict
def push(queue: deque, crate: str) -> list[str]:
    queue.appendleft(crate)
    return queue


def part1() -> str:
    crates: dict[str, deque] = {}
    data = loadData(crates)
    for move_amount, from_key, to_key in data:
        from_stack = crates[from_key]
        to_stack = crates[to_key]
        for _ in range(int(move_amount)):
            to_stack.append(from_stack.pop())

    res = ""
    for i in range(9):
        # get the top crate in each stack aka item the fruthest to the right
        res += crates[f"{i + 1}"][-1]
    return res


def part2() -> str:
    crates: dict[str, deque] = {}
    data = loadData(crates)
    for move_amount, from_key, to_key in data:
        from_stack = crates[from_key]
        to_stack = crates[to_key]
        crates_to_move = deque()
        for _ in range(int(move_amount)):
            crates_to_move.appendleft(from_stack.pop())
        to_stack.extend(crates_to_move)

    res = ""
    for i in range(9):
        res += crates[f"{i + 1}"][-1]
    return res


def main() -> None:
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()