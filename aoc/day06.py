from typing import Tuple, Callable
from enum import Enum

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

movements = {
    Direction.NORTH.value : lambda i, j: (i - 1, j),
    Direction.EAST.value : lambda i, j: (i, j + 1),
    Direction.SOUTH.value : lambda i, j: (i + 1, j),
    Direction.WEST.value : lambda i, j: (i, j - 1),
}


def patrol(matrix: [str], position: Tuple[int, int], direction: int) -> int:
    visited_positions = set()
    while True:
        visited_positions.add(position)
        new_position = movements[direction](*position)
        (i, j) = new_position
        if i not in range(len(matrix)) or j not in range(len(matrix[i])):
            return len(visited_positions)
        if matrix[i][j] == '#':
            direction = (direction + 1) % 4
        else:
            position = new_position


def main():
    matrix = []
    starting_position = (0, 0)
    with open('resources/day06.txt', 'r') as file:
        for idx, line in enumerate(file):
            matrix.append(line.strip())
            if '^' in line:
                starting_position = (idx, line.index('^'))
    movement_count = patrol(matrix, starting_position, Direction.NORTH.value)
    print(f"The answer is {movement_count}.")


if __name__ == '__main__':
    main()