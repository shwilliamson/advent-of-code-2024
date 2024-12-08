from typing import Tuple
from itertools import combinations


def compute_antinodes(x: Tuple[int, int], y: Tuple[int, int])-> [Tuple[int, int]]:
    d = y[0] - x[0], y[1] - x[1] # distance between nodes
    return [
        (x[0] - d[0], x[1] - d[1]),
        (y[0] + d[0], y[1] + d[1])
    ]


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
        for pair in combinations(nodes, 2):
            for an in compute_antinodes(pair[0], pair[1]):
                if an[0] in range(bounds[0]) and an[1] in range(bounds[1]):
                    antinodes.add(an)

    print(f"answer is {len(antinodes)}")

if __name__ == '__main__':
    main()