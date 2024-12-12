import itertools


def blink(stone: int, remaining: int) -> [int]:
    if remaining == 0:
        return [stone]

    if stone == 0:
        stones = [1]
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        mid = len(stone_str) // 2
        stones = [int(stone_str[:mid]), int(stone_str[mid:])]
    else:
        stones = [stone * 2024]

    stones = [blink(stone, remaining - 1) for stone in stones]
    return list(itertools.chain(*stones))


def main():
    with open('resources/day11.txt', 'r') as file:
        for line in file:
            stones = [blink(int(stone), 25) for stone in line.strip().split()]
            answer = len(list(itertools.chain(*stones)))
            print(f"answer is {answer}")


if __name__ == '__main__':
    main()