from dataclasses import dataclass
from typing import Dict


@dataclass
class Stone:
    val: int
    multiple: int


def group(stones: [Stone]) -> [Stone]:
    stone_map: Dict[int,Stone] = {}
    for stone in stones:
        if stone.val not in stone_map:
            stone_map[stone.val] = stone
        else:
            stone_map[stone.val].multiple += stone.multiple
    result = list(stone_map.values())
    return result


def transform(stone: Stone) -> [Stone]:
    if stone.val == 0:
        stone.val = 1
        return [stone]
    elif len(str(stone.val)) % 2 == 0:
        stone_str = str(stone.val)
        mid = len(stone_str) // 2
        return [
            Stone(val=int(stone_str[:mid]), multiple=stone.multiple),
            Stone(val=int(stone_str[mid:]), multiple=stone.multiple)
        ]
    else:
        stone.val *= 2024
        return [stone]


def blink(stones: [Stone], times: int) -> [Stone]:
    if times == 0:
        return stones
    transformed = []
    for stone in stones:
        transformed += transform(stone)
    grouped = group(transformed)
    return blink(grouped, times - 1)


def main():
    with open('resources/day11.txt', 'r') as file:
        for line in file:
            initial_stones = [Stone(val=int(x), multiple=1) for x in line.strip().split()]
            stones = blink(initial_stones, times=75)
            answer = sum([stone.multiple for stone in stones])
            print(f"answer is {answer}")


if __name__ == '__main__':
    main()