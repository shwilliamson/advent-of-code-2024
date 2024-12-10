from itertools import chain
from typing import Tuple, Set

matrix = []

movements = [
    lambda i, j: (i - 1, j),
    lambda i, j: (i, j + 1),
    lambda i, j: (i + 1, j),
    lambda i, j: (i, j - 1)
]

def walk_trails(position: Tuple[int, int], breadcrumbs: [Tuple[int,int]]) -> Set[Tuple[int,int]]:
    trail = breadcrumbs + [position]
    (i, j) = position
    if i not in range(len(matrix)):
        return set()
    if j not in range(len(matrix[i])):
        return set()

    elevation = matrix[i][j]
    if elevation != len(breadcrumbs):
        return set()
    if elevation == 9:
        print(f"Found valid trail: {[trail]}")
        return {position}

    all_trail_peaks = [ walk_trails(position=move(i, j), breadcrumbs=trail) for move in movements ]
    return set().union(*all_trail_peaks)


def main():
    with open('resources/day10.txt', 'r') as file:
        for line in file:
            matrix.append([int(c) for c in line.strip()])

    trail_score_sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                trails = walk_trails(position=(i, j), breadcrumbs=[])
                print(f"Trail head {(i,j)} reaches {len(trails)} distinct peaks")
                trail_score_sum += len(trails)
    print(f"answer is {trail_score_sum}")


if __name__ == '__main__':
    main()