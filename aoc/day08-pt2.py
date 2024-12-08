from typing import Tuple, Optional
from itertools import combinations


def compute_antinodes(x: Tuple[int, int], d: Tuple[int, int], bounds: Tuple[int, int])-> [Tuple[int, int]]:
    n = (x[0] + d[0], x[1] + d[1])
    if n[0] in range(bounds[0]) and n[1] in range(bounds[1]):
        return [n] + compute_antinodes(n, d, bounds)
    else:
        return []


def main():
    antinodes = set()
    antenna_map = {}
    bounds = (0, 0)
    with open('resources/day08.txt', 'r') as file:
        for i, line in enumerate(file):
            for j, char in enumerate(line.strip()):
                bounds = (i+1, j+1)
                if char != '.':
                    antenna_map[char] = antenna_map.get(char, []) + [(i,j)]

    for nodes in antenna_map.values():
        for x, y in combinations(nodes, 2):
            d = y[0] - x[0], y[1] - x[1] # distance
            antinodes.update([x, y])
            antinodes.update(compute_antinodes(x, (-d[0], -d[1]), bounds))
            antinodes.update(compute_antinodes(y, d, bounds))

    print(antinodes)
    print(f"answer is {len(antinodes)}")

if __name__ == '__main__':
    main()